DROP TABLE IF EXISTS player_histories;
DROP TABLE IF EXISTS players;


CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    wins INT,
    number_of_player_games INT
);

CREATE TABLE player_histories(
    id SERIAL PRIMARY KEY, 
    word VARCHAR(255) NOT NULL,
    player_id = INT REFERENCES players.id
);