-- lists all the cities of california that can be found
-- in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities
WHERE cities.id =
(SELECT id FROM states
WHERE states.name = 'California')
ORDER BY cities.id
