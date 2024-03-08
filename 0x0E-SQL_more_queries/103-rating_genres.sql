-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name ,SUM(sr.rate) AS rating
FROM tv_genres tg
JOIN tv_show_genres sg
ON tg.id = sg.genre_id
JOIN tv_show_ratings sr
ON sr.show_id = sg.show_id
GROUP BY sg.genre_id
ORDER BY rating DESC;
