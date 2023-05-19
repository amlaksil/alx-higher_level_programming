-- lists all the cities of California that can be found in the
-- database `hbtn_0d_usa`
-- the first nonoption argument is taken as the name of the default database
SELECT id, name FROM states WHERE state_id = (SELECT id
FROM states WHERE name = 'California');
