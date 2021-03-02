-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
LEFT JOIN (tv_show_genres, tv_genres) ON (show_id = tv_shows.id AND genre_id = tv_genres.id) 
WHERE name = "Comedy" ORDER BY title;