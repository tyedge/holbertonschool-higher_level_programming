-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at
-- least one genre linked.
-- This script lists all shows where genre isn't NULL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
