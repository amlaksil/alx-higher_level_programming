-- List all genres from hbtn_0d_tvshows and display the number of shows linked to each
SELECT tg.name AS genre, COUNT(sg.genre_id) AS number_of_shows
FROM tv_show_genres sg
INNER JOIN tv_genres tg
ON tg.id = sg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;
