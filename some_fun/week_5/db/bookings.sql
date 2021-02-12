DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS times_available;

CREATE TABLE clubs(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    number_of_courts INT
);

CREATE TABLE times_available(
    id SERIAL PRIMARY KEY, 
    start_time VARCHAR(255) NOT NULL,
    session_duration VARCHAR(255) NOT NULL,
    club_id INT REFERENCES clubs(id) ON DELETE CASCADE
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) NOT NULL, 
    club_id INT REFERENCES clubs(id) ON DELETE CASCADE
);