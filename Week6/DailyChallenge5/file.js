const express = require('express');
const fs = require('fs');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const FILE = 'users.json';

function readUsers() {
    return JSON.parse(fs.readFileSync(FILE));
}

function writeUsers(data) {
    fs.writeFileSync(FILE, JSON.stringify(data));
}

app.post('/register', async (req, res) => {
    const users = readUsers();

    const { username, password, email, first_name, last_name } = req.body;

    if (users.find(u => u.username === username)) {
        return res.send('Username already exists');
    }

    const hash = await bcrypt.hash(password, 10);

    users.push({
        id: users.length + 1,
        username,
        password: hash,
        email,
        first_name,
        last_name
    });

    writeUsers(users);

    res.send('Hello Your account is now created!');
});

app.post('/login', async (req, res) => {
    const users = readUsers();
    const { username, password } = req.body;

    const user = users.find(u => u.username === username);
    if (!user) return res.send('Username is not registered');

    const valid = await bcrypt.compare(password, user.password);
    if (!valid) return res.send('Wrong password');

    res.send(`Hi ${username} welcome back again!`);
});

app.get('/users', (req, res) => {
    res.json(readUsers());
});

app.get('/users/:id', (req, res) => {
    const user = readUsers().find(u => u.id == req.params.id);
    res.json(user || { message: 'not found' });
});

app.put('/users/:id', (req, res) => {
    let users = readUsers();
    let user = users.find(u => u.id == req.params.id);

    if (!user) return res.json({ message: 'not found' });

    user.username = req.body.username || user.username;
    user.email = req.body.email || user.email;

    writeUsers(users);
    res.json(user);
});

app.listen(3000);
