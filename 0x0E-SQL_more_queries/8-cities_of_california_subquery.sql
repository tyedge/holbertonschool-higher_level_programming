-- Write a script that lists all the cities of California that can be found in
-- the database hbtn_0d_usa
-- This script lists all cities in a state that can be found in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
