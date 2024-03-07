-- Lists all shows contained in the database hbtn_0d_tvshows.
SELECT sh.title, ge.genre_id
FROM tv_shows sh
LEFT JOIN tv_show_genres ge
ON sh.id = ge.show_id
ORDER BY sh.title ASC, ge.genre_id ASC; 
