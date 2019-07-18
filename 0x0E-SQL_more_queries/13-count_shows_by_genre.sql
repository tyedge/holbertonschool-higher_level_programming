-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- This script lists genres and counts the number of titles linked to each genre
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.show_id) AS 'number_of_shows' FROM tv_show_genres JOIN tv_genres ON genre_id = tv_genres.id GROUP BY tv_show_genres.genre_id ORDER BY number_of_shows DESC;
