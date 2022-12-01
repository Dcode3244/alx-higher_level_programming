-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name FROM tv_genres
WHERE name NOT IN (
SELECT DISTINCT name FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter')
ORDER BY name
