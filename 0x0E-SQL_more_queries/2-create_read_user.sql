-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2
-- This script creates a new database and user with only SELECT privileges
CREATE database IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
