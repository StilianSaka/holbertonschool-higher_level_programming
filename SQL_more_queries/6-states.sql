-- Write a script that creates the database hbtn_0d_usa and the table states.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Script to create table

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (ID)
);