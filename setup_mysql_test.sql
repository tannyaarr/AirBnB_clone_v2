-- script that prepares a MySQl server

-- creates the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create the user if it doesn't exit
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all pivileges
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
