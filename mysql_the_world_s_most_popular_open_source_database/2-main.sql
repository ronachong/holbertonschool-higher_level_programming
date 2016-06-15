\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT name, count(tvshow_id) AS nb_seasons
FROM Season JOIN TVShow ON Season.tvshow_id=TVShow.id
GROUP BY name
ORDER BY name ASC;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS "TVShow name", Network.name AS "Network name"
FROM TVShow JOIN Network on TVShow.network_id = Network.id
ORDER BY TVShow.name ASC;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name
FROM TVShow JOIN Network ON TVShow.network_id = Network.id
WHERE Network.name='Fox (US)';

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name, count(Season.tvshow_id) AS nb_episodes
FROM TVShow JOIN Season on TVShow.id=Season.tvshow_id
JOIN Episode on Season.id=Episode.season_id
GROUP BY Season.tvshow_id
ORDER BY TVShow.name ASC;
