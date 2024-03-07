-- List all Comedy shows in the database hbtn_0d_tvshows
SELECT ts.title
FROM tv_shows ts
INNER JOIN tv_show_genres sg
ON ts.id = sg.show_id
INNER JOIN tv_genres tg
ON tg.id = sg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title;
