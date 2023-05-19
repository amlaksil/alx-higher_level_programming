-- creates a table named `unique_id`
-- the first nonoption argument is taken as the name of the default database
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE, name VARCHAR(256));
