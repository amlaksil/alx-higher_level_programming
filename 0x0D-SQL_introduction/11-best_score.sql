-- lists all records with `score >= 10` in the table `second_table` of
-- the database `hbtn_0c_0` in your MySQL server
-- the first nonoption argument is taken as the name of default database
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
