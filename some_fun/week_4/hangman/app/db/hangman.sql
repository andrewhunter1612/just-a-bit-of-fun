DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS player_histories;

CREATE TABLE player_histories(
    id SERIAL PRIMARY KEY, 
    word VARCHAR(255) NOT NULL,
    wins INT
);

CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    player_histories_id INT REFERENCES player_histories(id)
);