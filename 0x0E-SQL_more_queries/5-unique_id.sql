-- a script that creates the table unique_id on my MySQL server, id has the default value 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
