-- Use hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT name FROM tv_genres
WHERE id NOT IN (
  SELECT sg.genre_id
  FROM tv_show_genres sg
  JOIN tv_shows ts
  ON sg.show_id = ts.id
  WHERE ts.title = 'Dexter')
ORDER BY name;
