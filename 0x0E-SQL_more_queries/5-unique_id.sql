-- script that creates the table unique_id on your MySQL server.
-- create table with default id and unique.
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
)

