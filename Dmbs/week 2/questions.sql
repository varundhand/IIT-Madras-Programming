--!* Like operator

-- selecting faculty members with name starting from 'S'
select * from faculty where faculty_fname like 'S%';

-- selecting faculty members with name having 5 charcaters
select * from faculty where faculty_fname like '_____'; -- 5 underscores

-- selecting faculty members whose name includes 'a'
select * from faculty where faculty_fname like '%a%';

-- selecting faculty members whose second last character is 'a'
select * from faculty where faculty_fname like '%a_';

--!* In operator
-- selecting faculty members whose department is either 'CSE' or 'ECE'
select * from faculty where department_code in ('CSE', 'ECE');

--!* Rename Operator 
select faculty_fname as 'First Name', faculty_lname as 'Last Name' from faculty;

--!* Order by Operator
select * from faculty order by doj; 
select * from faculty order by doj desc;  -- for descending order
select * from faculty order by doj desc limit 1;  -- for descending order and limit to 1 row
select * from faculty order by doj desc limit 5 offset 1;  -- for descending top top 5 rows after 1st row

-- count(*) is used to count the number of rows 
--!* Group by
select count(*),gender from faculty group by gender 

--!* Having clause
-- 'having' clause is used to filter the data after the group by clause and it is done after the formation of table where as 'where' clause is used before the group is formed
select count(*), department_code from faculty group by department_code having count(*) > 1;

--! Exercises
select managers.name * from managers, teams where teams.team_id = managers.team_id and teams.team_name = 'All Stars';

select * from managers 

select dept_name,avg(salary) as avg_salary from instructor group by dept_name;