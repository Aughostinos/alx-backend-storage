-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) 
);
