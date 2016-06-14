\! echo "\nList of all tables?"
show tables;

\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
DESC TVShow; -- this output still looks off
DESC Genre;
DESC TVShowGenre;

\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
SELECT id, name FROM TVShow ORDER BY name ASC;

\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
SELECT id, name FROM Genre ORDER BY name DESC;

\! echo "\nList of Network, only id and name?"
SELECT id, name FROM Network;

\! echo "\nNumber of episodes in the database?"
SELECT count(id) FROM Episode;
