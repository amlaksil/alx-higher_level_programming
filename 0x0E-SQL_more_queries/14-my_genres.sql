-- Use the hbtn_0d_tvshows database to list all genres of the show Dexter
SELECT tg.name
FROM tv_shows ts
INNER JOIN tv_show_genres sg
ON sg.show_id = ts.id
INNER JOIN tv_genres tg
ON tg.id = sg.genre_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
