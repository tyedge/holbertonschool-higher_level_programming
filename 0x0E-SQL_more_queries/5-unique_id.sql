-- Write a script that creates the table unique_id on your MySQL server
-- This script creates a new data table
CREATE table IF NOT EXISTS unique_id (id INT default 1 UNIQUE, name VARCHAR(256));
