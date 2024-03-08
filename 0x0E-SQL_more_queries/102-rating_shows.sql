-- List all shows from hbtn_0d_tvshows_rate by their rating.
SELECT ts.title, SUM(sr.rate) AS rating
FROM tv_shows ts
JOIN tv_show_ratings sr
ON sr.show_id = ts.id
GROUP BY sr.show_id
ORDER BY rating DESC;
