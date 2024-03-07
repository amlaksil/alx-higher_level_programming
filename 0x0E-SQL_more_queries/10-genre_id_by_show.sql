-- List all shows contained in hbtn_0d_tvshows
SELECT sh.title, ge.genre_id
FROM tv_shows sh
INNER JOIN tv_show_genres ge
ON sh.id = ge.show_id
ORDER BY sh.title ASC, ge.genre_id ASC;
