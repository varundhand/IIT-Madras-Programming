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

-- selecting in order
select name as 'Band Names' from bands order by name;
select name as 'Band Names' from bands order by name desc; -- for descending order

-- insert multiple values
insert into albums (name, release_year,band_id) 
values ('Abbey Road',1969, 1),
('Help!',1965, 1),
('Aftermath', 1966,2),
('The Works', 1984,3),
('Test Album', NULL, 4);

-- distinct keyword is used to select unique values 
select distinct name  from albums;

--! Update keyword is used to update/modify the data in the table (update, set, where)
update albums 
set release_year = 1966
where id = 2;

-- filtering the data using where clause
select * from albums
where release_year > 1980;

-- like keyword is used to search for a specified pattern in a column
select * from albums
where name like '%the%';
-- where name like '%the%' and band_id = 3;
-- where release_year between 1960 and 1970; --! between is used to select the range of values
-- where release_year is Null; --! is used to check if the value is null

--! Delete keyword is used to delete the data from the table
delete from albums 
where id = 5;

--!* JOINS
--! inner join is used to combine rows from two or more tables based on a related column between them
select * from bands 
inner join albums on bands.id = albums.band_id;

-- inner join shows the common rows between the two tables (same id in both tables)
-- left join shows all the rows from the left table and the common rows from the right table
-- right join shows all the rows from the right table and the common rows from the left table

--! left join
select * from bands 
left join albums on bands.id = albums.band_id;

--! right join
select * from bands 
right join albums on bands.id = albums.band_id;

--!* Aggregate Functions
