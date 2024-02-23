// conertStyles.js
const { execSync } = require('child_process');

// Run npm commands
console.log('Running npm make-styles');
execSync('npm run make-styles');

// Run Python script
console.log('Running Python script...');
execSync('python3 transferVariables.py');

// More npm commands if needed
console.log('Running npm css-compile...');
execSync('npm run css-compile');

console.log('All commands executed successfully.');
