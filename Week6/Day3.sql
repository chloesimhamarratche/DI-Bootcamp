-- EX1

SELECT * FROM language;

SELECT film.title, film.description, language.name
FROM film
INNER JOIN language ON film.language_id = language.language_id;

SELECT film.title, film.description, language.name
FROM language
LEFT JOIN film ON film.language_id = language.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO new_film (name) VALUES
('Titanic'),
('Avatar'),
('Inception');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
(1, 1, 'Amazing movie', 9, 'I loved it!'),
(2, 1, 'Great visuals', 8, 'Very beautiful movie');

DELETE FROM new_film WHERE id = 1;

--EX2

UPDATE film
SET language_id = 2
WHERE film_id = 1;

DROP TABLE customer_review;

SELECT *
FROM rental
WHERE return_date IS NULL;

SELECT film.title, film.replacement_cost
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE rental.return_date IS NULL
ORDER BY film.replacement_cost DESC
LIMIT 30;

SELECT film.title
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.first_name = 'PENELOPE'
AND actor.last_name = 'MONROE'
AND film.description ILIKE '%sumo%';

SELECT title
FROM film
WHERE length < 60
AND rating = 'R'
AND description ILIKE '%documentary%';

SELECT film.title
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'MATTHEW'
AND customer.last_name = 'MAHAN'
AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'
AND rental.rental_rate > 4;

SELECT title
FROM film
WHERE title ILIKE '%boat%'
OR description ILIKE '%boat%'
ORDER BY replacement_cost DESC;
