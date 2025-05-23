const express = require('express');
const fs = require('fs').promises;

const app = express();
const PORT = 1245;

async function countStudents(dbPath) {
  try {
    const data = await fs.readFile(dbPath, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const headers = lines[0].split(',');
    const fieldIndex = headers.indexOf('field');

    const students = {};
    let total = 0;

    for (let i = 1; i < lines.length; i += 1) {
      const columns = lines[i].split(',');
      const field = columns[fieldIndex].trim();
      const firstname = columns[0].trim();

      if (field && firstname) {
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
        total += 1;
      }
    }

    let output = `Number of students: ${total}`;
    for (const [field, names] of Object.entries(students)) {
      output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
    }

    return output;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  const dbPath = process.argv[2];

  let response = 'This is the list of our students\n';

  try {
    const report = await countStudents(dbPath);
    response += report;
    res.status(200).send(response);
  } catch (err) {
    res.status(200).send(response + err.message);
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});

module.exports = app;
