-- creates a table named `id_not_null` on your MYSQL server
-- the first nonoption argument is taken as the name of the default database
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256))
