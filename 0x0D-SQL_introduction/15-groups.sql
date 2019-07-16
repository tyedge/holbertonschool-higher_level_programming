-- Write a script that lists the number of records with the same score in the
-- table second_table of the database hbtn_0c_0 in your MySQL server
-- This script returns a count of each group of records with the same score in a table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
