-- Database: mini_etl_project

-- DROP DATABASE IF EXISTS mini_etl_project;

CREATE DATABASE mini_etl_project
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Swedish_Sweden.1252'
    LC_CTYPE = 'Swedish_Sweden.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE mini_etl_project
    IS 'mini etl project';
	
CREATE TABLE Weather_data
(id SERIAL UNIQUE PRIMARY KEY,
Date DATE,
Time INT,
Temperature NUMERIC (10),
Air_Pressure NUMERIC (10),
Precipitation NUMERIC (10)
);