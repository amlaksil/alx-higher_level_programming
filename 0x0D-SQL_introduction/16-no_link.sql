-- lists all records of the table `second_table` of the database `hbtn_0c_0`
-- the first nonoption argument is taken as the name of default database
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
