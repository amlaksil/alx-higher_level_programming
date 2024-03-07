-- List all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT sh.title, tg.name
FROM tv_shows sh
LEFT JOIN tv_show_genres sg
ON sg.show_id = sh.id
LEFT JOIN tv_genres tg
ON tg.id = sg.genre_id
ORDER BY sh.title ASC, tg.name ASC
