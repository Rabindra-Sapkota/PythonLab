create database demo_class;


create table course(
id integer,
course_name varchar(255),
instructor varchar(255),
duration_in_week integer
);


insert into course(id, course_name, instructor, duration_in_week) 
values 
(1, 'Python', 'Rabindra', 4),
(2, 'Django', 'Rahul', 8);



select * 
from course
where course_name = 'Python';


select * from student;

insert into student(roll_no, student_name, addreess) values
(1, 'Bishal', 'Tillotama'),
(2, 'Rachita', 'Jhapa'),
(3, 'Dinesh', 'Kavre');

select * from student where addreess = 'Tillotama';

update student
set addreess = 'Tillottama'
where addreess = 'Tillotama';

update student
set addreess = 'Lalitpur'
 , student_name = 'Denish'
where student_name = 'Dinesh' and roll_no = 3;

delete from student 
where student_name = 'Denish' and roll_no = 3;

select * from student;