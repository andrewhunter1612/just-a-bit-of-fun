DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS members;

CREATE TABLE clubs(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    number_of_courts INT,
    opening_time VARCHAR(255) NOT NULL
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    club_id INT REFERENCES clubs(id)
);