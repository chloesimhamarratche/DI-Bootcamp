const express = require('express');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());

let users = [];
let passwords = [];

app.post('/register', async (req, res) => {
    const { username, password, email, first_name, last_name } = req.body;

    const hash = await bcrypt.hash(password, 10);

    const user = {
        id: users.length + 1,
        email,
        username,
        first_name,
        last_name
    };

    users.push(user);

    passwords.push({
        username,
        password: hash
    });

    res.json({ message: 'User registered' });
});

app.post('/login', async (req, res) => {
    const { username, password } = req.body;

    const userPass = passwords.find(u => u.username === username);
    if (!userPass) return res.status(404).json({ message: 'User not found' });

    const valid = await bcrypt.compare(password, userPass.password);
    if (!valid) return res.status(401).json({ message: 'Wrong password' });

    res.json({ message: 'Login success' });
});

app.get('/users', (req, res) => {
    res.json(users);
});

app.get('/users/:id', (req, res) => {
    const user = users.find(u => u.id == req.params.id);
    if (!user) return res.status(404).json({ message: 'Not found' });
    res.json(user);
});

app.put('/users/:id', (req, res) => {
    const user = users.find(u => u.id == req.params.id);
    if (!user) return res.status(404).json({ message: 'Not found' });

    user.email = req.body.email || user.email;
    user.username = req.body.username || user.username;
    user.first_name = req.body.first_name || user.first_name;
    user.last_name = req.body.last_name || user.last_name;

    res.json(user);
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
