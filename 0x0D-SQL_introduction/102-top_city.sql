-- displays the top 3 of cities temperature during July and
-- August ordered by temperature (descending)
-- the first nonoption argument is taken as the name of default database
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month > 6 and month < 9
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
