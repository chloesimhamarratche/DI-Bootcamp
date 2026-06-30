const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const booksContainer = document.getElementById("books");
const sortSelect = document.getElementById("sortSelect");
const loader = document.getElementById("loader");
const message = document.getElementById("message");

let books = [];

async function getBooks(query = "javascript") {

    loader.classList.remove("hidden");
    booksContainer.innerHTML = "";
    message.innerHTML = "";

    try {

        const response = await fetch(
            `https://www.googleapis.com/books/v1/volumes?q=${query}&maxResults=40`
        );

        const data = await response.json();

        books = data.items || [];

        sortBooks();

    } catch (error) {

        message.innerHTML = "❌ Error while loading books.";

    }

    loader.classList.add("hidden");

}

function sortBooks() {

    if (sortSelect.value === "newest") {

        books.sort((a, b) => {

            const yearA = parseInt(a.volumeInfo.publishedDate) || 0;
            const yearB = parseInt(b.volumeInfo.publishedDate) || 0;

            return yearB - yearA;

        });

    } else {

        books.sort((a, b) => {

            const yearA = parseInt(a.volumeInfo.publishedDate) || 0;
            const yearB = parseInt(b.volumeInfo.publishedDate) || 0;

            return yearA - yearB;

        });

    }

    displayBooks();

}

function displayBooks() {

    booksContainer.innerHTML = "";

    if (books.length === 0) {

        message.innerHTML = "No books found.";

        return;

    }

    books.forEach(book => {

        const info = book.volumeInfo;

        const image = info.imageLinks
            ? info.imageLinks.thumbnail
            : "https://via.placeholder.com/200x300?text=No+Image";

        const title = info.title || "Unknown title";

        const author = info.authors
            ? info.authors.join(", ")
            : "Unknown";

        const year = info.publishedDate || "Unknown";

        booksContainer.innerHTML += `

            <div class="card">

                <img src="${image}" alt="${title}">

                <div class="info">

                    <h3>${title}</h3>

                    <p><strong>Author:</strong> ${author}</p>

                    <p><strong>Published:</strong> ${year}</p>

                </div>

            </div>

        `;

    });

}

searchBtn.addEventListener("click", () => {

    const query = searchInput.value.trim();

    if (query === "") {

        getBooks();

    } else {

        getBooks(query);

    }

});

searchInput.addEventListener("keypress", e => {

    if (e.key === "Enter") {

        searchBtn.click();

    }

});

sortSelect.addEventListener("change", sortBooks);

getBooks();
