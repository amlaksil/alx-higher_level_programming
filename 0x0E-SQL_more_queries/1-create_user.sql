-- creates Mysql server for user `user_0d_1` and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- this will free up memory cached as a result of CREATE USER and GRANT
FLUSH PRIVILEGES
