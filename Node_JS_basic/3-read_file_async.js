const fs = require('fs').promises;

async function countStudents(dbPath) {
  try {
    const data = await fs.readFile(dbPath, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const headers = lines[0].split(',');
    const fieldIndex = headers.indexOf('field');

    const students = {};

    for (let i = 1; i < lines.length; i += 1) {
      const columns = lines[i].split(',');
      const field = columns[fieldIndex].trim();
      const firstname = columns[0].trim();

      if (field && firstname) {
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }
    }

    process.stdout.write(`Number of students: ${lines.length - 1}\n`);

    for (const [field, names] of Object.entries(students)) {
      process.stdout.write(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
