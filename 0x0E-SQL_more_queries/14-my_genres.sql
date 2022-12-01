--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON show_id = tv_shows.id
where title = 'Dexter'
ORDER BY tv_genres.name
