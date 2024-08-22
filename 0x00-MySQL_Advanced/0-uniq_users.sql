--  SQL script that creates a table users

CREATE TABLE users if NOT EXISTS (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) 
);