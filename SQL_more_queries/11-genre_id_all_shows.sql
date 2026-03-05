-- Write a SQL query to list all the shows in the database hbtn_0d_tvshows and their corresponding genre_id. The tv_shows table contains the show id and title, and the tv_show_genres table contains the show id and genre_id. The results should be sorted by show title in ascending order and genre_id in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
