-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT serie.title, genero.genre_id FROM  tv_show_genres genero
INNER JOIN tv_shows serie ON genero.show_id = serie.id
ORDER BY serie.title, genero.genre_id ASC;