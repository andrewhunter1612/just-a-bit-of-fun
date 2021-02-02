DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks(
    id SERIAL,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    finished BOOLEAN
);