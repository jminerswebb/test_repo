# Components Completed

- [] Accordion
- [x] Alerts
- [] Badge
- [] Breadcrumb
- [] Buttons
- [] Button group
- [] Card
- [] Carousel
- [] Close button
- [] Collapse
- [] Dropdowns
- [] List group
- [] Modal
- [] Navs & tabs
- [] Navbar
- [] Offcanvas
- [] Pagination
- [] Popovers
- [] Progress
- [] Scrollspy
- [] Spinners
- [] Toasts
- [] Tooltips

# Done

- Can serve docs server with formatted styles
- Stripped down docs to only be the parts we need, removed most of the Bootstrap Affiliate terminology and links
- Initial style override done
- Custom Component example
- 'npm publish' command to repo

# In Progress

- Override more components
- Add more Core components
- Overide theme colors

# To-Do

- GitHub actions package publication

# Notes

1. Variables.scss file, figure out way to automate the conversion of tokens -> this file
   - Source file that is compiled into css
   - Process: From tokens.json -> ? -> \_variables.scss (Try and change Primary from Blue to Green) -> bootstrap.css (generated)
   - Changes should be cascaded from primary/secondary/etc themes
   - Parameter for which style we are generating, defaultTheme_tokens.json -> pipe into generation
2. GitHub automation when uploading tokens.json
3. Getting the component stylings
4. Custom components
5. Changing values in \_variables.scss and then running npm run css rebuilds themes and colors

# Next steps

1. GitHub Pages
2. Object Object, sd-transforms reference
3. Get inter font

# Exploration

- How to include multiple themes

# Node commands for building tokens/css

- npm run make-styles
