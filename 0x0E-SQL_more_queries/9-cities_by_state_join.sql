-- script that lists all cities contained in the database hbtn_0d_usa
SELECT city.id, city.name, stat.name FROM cities city
INNER JOIN states stat ON city.state_id = stat.id ORDER BY city.id ASC;