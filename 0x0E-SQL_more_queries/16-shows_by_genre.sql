-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT name, title
FROM tv_shows LEFT JOIN (tv_show_genres, tv_genres) ON (show_id = tv_shows.id AND genre_id = tv_genres.id) 
ORDER BY title, name;