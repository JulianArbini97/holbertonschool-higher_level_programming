-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT movies.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres movies
RIGHT OUTER JOIN tv_show_genres generos ON movies.id = generos.genre_id
GROUP BY movies.name ORDER BY number_of_shows DESC;