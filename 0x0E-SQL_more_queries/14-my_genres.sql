--  script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. --
SELECT name FROM tv_shows
LEFT JOIN (tv_show_genres, tv_genres) ON (show_id = tv_shows.id AND genre_id = tv_genres.id) 
WHERE title = "Dexter" ORDER BY name;
