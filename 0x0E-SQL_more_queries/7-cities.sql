-- creates the database `hbtn_0d_usa` and the table `cities`
-- cities - id INT unique, auto generated, can't be null and is a primary key
-- state_id INT, can't be null and must be FOREIGN KEY that references to id of
-- the `states` table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE AUTO_INCREMENT NOT NULL,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id));
