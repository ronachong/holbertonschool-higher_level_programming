\! echo "\nList of TVShows ordered by name (A-Z) with more than or equal 4 seasons?"
SELECT name
FROM TVShow JOIN Season ON TVShow.id=Season.tvshow_id
GROUP BY TVShow.id
HAVING count(Season.tvshow_id) > 3
ORDER BY name ASC;

\! echo "\nList of TVShows ordered by name (A-Z) with the Genre 'Comedy'?"
SELECT TVShow.name
FROM Genre JOIN TVShowGenre ON Genre.id=TVShowGenre.genre_id
JOIN TVShow ON TVShowGenre.tvshow_id=TVShow.id
WHERE Genre.name='Comedy'
ORDER BY TVShow.name ASC;

\! echo "\nList of Actors ordered by name (A-Z) for the TVShow 'The Big Bang Theory'?"
SELECT Actor.name
FROM Actor JOIN TVShowActor ON Actor.id=TVShowActor.actor_id
JOIN TVShow ON TVShowActor.tvshow_id=TVShow.id
WHERE TVShow.name='The Big Bang Theory'
ORDER BY Actor.name ASC;

\! echo "\nTop 10 of actors by number of TVShows where they are? (without Actor name order => can be random)"
SELECT Actor.name, count(TVShow.id) AS nb_tvshows
FROM Actor JOIN TVShowActor ON Actor.id=TVShowActor.actor_id
JOIN TVShow ON TVShowActor.tvshow_id=TVShow.id
GROUP BY Actor.name
ORDER BY nb_tvshows DESC, Actor.name DESC
LIMIT 10;
