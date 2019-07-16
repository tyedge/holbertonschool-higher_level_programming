-- Write a script that lists all records of the table second_table of the
-- database hbtn_0c_0 in your MySQL server
-- This script lists all records the name value is not NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
