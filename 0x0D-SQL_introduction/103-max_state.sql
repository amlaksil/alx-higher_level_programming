-- displays the max temperature of each state (ordered by State name)
-- the first nonoption argument is taken as the name of default database
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state
ORDER BY state ASC LIMIT 3;
