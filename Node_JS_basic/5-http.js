const http = require('http');
const fs = require('fs').promises;

async function countStudents(dbPath) {
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

  let result = `Number of students: ${total}`;
  for (const [field, names] of Object.entries(students)) {
    result += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
  }

  return result;
}

const PORT = 1245;
const HOST = 'localhost';
const app = http.createServer();

app.on('request', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');

    const dbPath = process.argv[2];

    try {
      const report = await countStudents(dbPath);
      res.end(report);
    } catch (err) {
      res.end('Cannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(PORT, HOST, () => {
  process.stdout.write(`Server listening at -> http://${HOST}:${PORT}\n`);
});

module.exports = app;
