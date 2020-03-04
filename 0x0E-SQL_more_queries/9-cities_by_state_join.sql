-- script that lists all cities contained in the database hbtn_0d_usa.
-- The database name will be passed as an argument.
SELECT cities.id, cities.name, states.name
FROM states, cities
WHERE
	cities.state_id = states.id
ORDER BY cities.id ASC;
