--!* DATA DEFINITION LANGUAGE (DDL) 
-- creating a database
create database record_company;
use record_company;

-- creating a table
create table test(	
	test_column INT
    
);

-- adding a column to the table
alter table test
add another_column VARCHAR(255);

-- deleting table from the database
drop table test;

--! Examples 
create table bands(
	id INT NOT NULL auto_increment, -- id is the primary key of the table 
	name VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);

create table albums(
	id INT NOT NULL auto_increment,
    name VARCHAR(255) NOT NULL,
    release_year INT, 
    band_id INT NOT NULL, -- band_id is the foreign key referencing to the 'id' in bands table 
    PRIMARY KEY(id),
    FOREIGN KEY (band_id) REFERENCES bands(id) -- band_is is foreign key and its referencing the 'id' in bands table
);

--!* DATA MANIPULATION LANGUAGE (DML)
-- inserting data into the table    
insert into bands (name)
values ('The Beatles');

-- inseting multiple rows into the table
insert into bands (name)
values ('The Rolling Stones'), ('The Who'), ('The Kinks');

-- selecting all rows from the table
select * from bands;

-- selecting 2 columns from the table
select * from bands limit 2;

-- selecting specific columns from the table
select name from bands limit 2;

-- as keyword is used to give an alias to the column
select name as 'Band Name', id as 'Band ID' from bands;