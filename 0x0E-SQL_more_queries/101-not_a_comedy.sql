-- List all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
WHERE id NOT IN (
	SELECT show_id
	FROM tv_show_genres sg
	JOIN tv_genres tg
	ON tg.id = sg.genre_id
	WHERE tg.name = 'Comedy'
	)
ORDER BY title;
