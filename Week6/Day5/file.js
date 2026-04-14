const express = require('express');
const fs = require('fs');

const app = express();
app.use(express.json());

const file = 'tasks.json';

app.get('/tasks', (req, res) => {
    const data = fs.readFileSync(file);
    res.json(JSON.parse(data));
});

app.get('/tasks/:id', (req, res) => {
    const tasks = JSON.parse(fs.readFileSync(file));
    const task = tasks.find(t => t.id == req.params.id);
    res.json(task || { message: 'not found' });
});

app.post('/tasks', (req, res) => {
    const tasks = JSON.parse(fs.readFileSync(file));

    const newTask = {
        id: tasks.length + 1,
        title: req.body.title
    };

    tasks.push(newTask);
    fs.writeFileSync(file, JSON.stringify(tasks));

    res.json(newTask);
});

app.put('/tasks/:id', (req, res) => {
    const tasks = JSON.parse(fs.readFileSync(file));
    const task = tasks.find(t => t.id == req.params.id);

    if (task) {
        task.title = req.body.title;
        fs.writeFileSync(file, JSON.stringify(tasks));
        res.json(task);
    } else {
        res.json({ message: 'not found' });
    }
});

app.delete('/tasks/:id', (req, res) => {
    let tasks = JSON.parse(fs.readFileSync(file));
    tasks = tasks.filter(t => t.id != req.params.id);

    fs.writeFileSync(file, JSON.stringify(tasks));
    res.json({ message: 'deleted' });
});

app.listen(3000);
