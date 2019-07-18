-- Write a script that lists all cities contained in the database hbtn_0d_usa
-- This script lists all the cities contained in a database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
