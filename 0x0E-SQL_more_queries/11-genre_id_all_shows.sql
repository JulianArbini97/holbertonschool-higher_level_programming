-- script that lists all shows contained in the database hbtn_0d_tvshows
SELECT serie.title, genero.genre_id FROM  tv_show_genres genero 
RIGHT OUTER JOIN tv_shows serie ON genero.show_id = serie.id 
ORDER BY serie.title, genero.genre_id ASC;