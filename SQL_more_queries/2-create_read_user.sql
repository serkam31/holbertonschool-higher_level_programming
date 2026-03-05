-- Write a SQL query to create a new database 'hbtn_0d_2', create a new user 'user_0d_2' with the password 'user_0d_2_pwd', and grant only SELECT privileges on the 'hbtn_0d_2' database to this user. 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';