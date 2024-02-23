import shutil


def update_file_b(file_a_path, file_b_path, duplicate_file_path):
    with open(file_a_path, 'r') as file_a:
        content_a = file_a.read()

    with open(file_b_path, 'r') as file_b:
        content_b = file_b.read()

    shutil.copyfile(file_b_path, duplicate_file_path)

    variables_a = {}
    for line in content_a.split('\n'):
        line = line.strip()
        if line.startswith('--theme'):
            line = line.split("--theme-")[1]
            variable, value = map(str.strip, line.split(':', 1))
            variables_a[variable] = value.rstrip(';')

    for variable, value in variables_a.items():
        search_pattern = f"${variable}:"
        if search_pattern in content_b:
            print(variable, value)
            content_b = content_b.replace(
                next(line for line in content_b.split(
                    '\n') if search_pattern in line),
                f"${variable}:       {value} !default;")

    with open(file_b_path, 'w') as output_file:
        output_file.write(content_b)


if __name__ == "__main__":
    # File a is the file that we generate from npm run make-styles
    file_a_path = "_variables.css"

    # File b is the variables file that we want to overwrite
    file_b_path = "../scss/_variables.scss"

    # Backup of modified variables file
    duplicate_file_path = "BACKUP_variables.scss"

    update_file_b(file_a_path, file_b_path, duplicate_file_path)
