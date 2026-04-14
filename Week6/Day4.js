//EX1

const express = require('express');
const app = express();
app.use(express.json());

let posts = [];

app.get('/posts', (req, res) => {
    res.json(posts);
});

app.get('/posts/:id', (req, res) => {
    const post = posts.find(p => p.id == req.params.id);
    if (!post) return res.status(404).json({ message: 'Not found' });
    res.json(post);
});

app.post('/posts', (req, res) => {
    const newPost = {
        id: posts.length + 1,
        title: req.body.title,
        content: req.body.content
    };
    posts.push(newPost);
    res.json(newPost);
});

app.put('/posts/:id', (req, res) => {
    const post = posts.find(p => p.id == req.params.id);
    if (!post) return res.status(404).json({ message: 'Not found' });

    post.title = req.body.title;
    post.content = req.body.content;

    res.json(post);
});

app.delete('/posts/:id', (req, res) => {
    posts = posts.filter(p => p.id != req.params.id);
    res.json({ message: 'Deleted' });
});

app.listen(3000);


//EX2

const app2 = express();
app2.use(express.json());

let books = [];

app2.get('/api/books', (req, res) => {
    res.json(books);
});

app2.get('/api/books/:bookId', (req, res) => {
    const book = books.find(b => b.id == req.params.bookId);
    if (!book) return res.status(404).json({ message: 'Book not found' });
    res.json(book);
});

app2.post('/api/books', (req, res) => {
    const newBook = {
        id: books.length + 1,
        title: req.body.title,
        author: req.body.author,
        publishedYear: req.body.publishedYear
    };
    books.push(newBook);
    res.json(newBook);
});

app2.listen(5000);
