-- Write a script that creates the database hbtn_0d_usa and the table cities.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Script to create table

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (state_id) REFERENCES states(id)
);