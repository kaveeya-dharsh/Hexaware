create database sisdb;
use sisdb;

create table students (
    student_id int primary key identity(1,1),
    first_name varchar(50),
    last_name varchar(50),
    date_of_birth date,
    email varchar(100),
    phone_number varchar(15)
);

create table teacher (
    teacher_id int primary key identity(1,1),
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100)
);

create table courses (
    course_id int primary key identity(1,1),
    course_name varchar(100),
    credits int,
    teacher_id int foreign key references teacher(teacher_id)
);


create table enrollments (
    enrollment_id int primary key identity(1,1),
    student_id int foreign key references students(student_id),
    course_id int foreign key references courses(course_id),
    enrollment_date date
);

create table payments (
    payment_id int primary key identity(1,1),
    student_id int foreign key references students(student_id),
    amount decimal(10,2),
    payment_date date
);

insert into students (first_name, last_name, date_of_birth, email, phone_number) values
('ravi', 'kumar', '2002-01-10', 'ravi@example.com', '9876543210'),
('neha', 'sharma', '2001-05-12', 'neha@example.com', '9876543211'),
('amit', 'verma', '2000-03-08', 'amit@example.com', '9876543212'),
('priya', 'singh', '2002-07-15', 'priya@example.com', '9876543213'),
('rohit', 'yadav', '1999-12-01', 'rohit@example.com', '9876543214'),
('sneha', 'patel', '2001-09-20', 'sneha@example.com', '9876543215'),
('vikas', 'chauhan', '2000-06-05', 'vikas@example.com', '9876543216'),
('kavya', 'raj', '2003-04-18', 'kavya@example.com', '9876543217'),
('manish', 'bhat', '2002-11-30', 'manish@example.com', '9876543218'),
('anita', 'joshi', '2001-02-22', 'anita@example.com', '9876543219');

insert into teacher (first_name, last_name, email) values
('arun', 'kumar', 'arun@college.com'),
('geeta', 'verma', 'geeta@college.com'),
('manoj', 'singh', 'manoj@college.com'),
('lata', 'mehra', 'lata@college.com'),
('ramesh', 'gupta', 'ramesh@college.com'),
('pooja', 'das', 'pooja@college.com'),
('sanjay', 'rao', 'sanjay@college.com'),
('deepa', 'yadav', 'deepa@college.com'),
('ajay', 'sharma', 'ajay@college.com'),
('anita', 'khan', 'anita@college.com');

insert into courses (course_name, credits, teacher_id) values
('math', 4, 1),
('english', 3, 2),
('physics', 4, 3),
('chemistry', 4, 4),
('biology', 3, 5),
('history', 2, 6),
('computer', 4, 7),
('geography', 2, 8),
('economics', 3, 9),
('hindi', 2, 10);

insert into enrollments (student_id, course_id, enrollment_date) values
(1, 1, '2024-06-01'),
(2, 2, '2024-06-02'),
(3, 3, '2024-06-03'),
(4, 4, '2024-06-04'),
(5, 5, '2024-06-05'),
(6, 6, '2024-06-06'),
(7, 7, '2024-06-07'),
(8, 8, '2024-06-08'),
(9, 9, '2024-06-09'),
(10, 10, '2024-06-10');

truncate table enrollments;

insert into payments (student_id, amount, payment_date) values
(1, 5000.00, '2024-07-01'),
(2, 4800.00, '2024-07-02'),
(3, 4500.00, '2024-07-03'),
(4, 4700.00, '2024-07-04'),
(5, 4900.00, '2024-07-05'),
(6, 5200.00, '2024-07-06'),
(7, 5100.00, '2024-07-07'),
(8, 5300.00, '2024-07-08'),
(9, 5000.00, '2024-07-09'),
(10, 4800.00, '2024-07-10');

select * from students;
select * from teacher;
select * from courses;
select * from enrollments;
select * from payments;

--===============task2=================
-- 1. write an sql query to insert a new student into the "students" table with the following details:
--    a. first name: john
--    b. last name: doe
--    c. date of birth: 1995-08-15
--    d. email: john.doe@example.com
--    e. phone number: 1234567890

insert into students (first_name, last_name, date_of_birth, email, phone_number)
values ('john', 'doe', '1995-08-15', 'john.doe@example.com', '1234567890');

-- 2. write an sql query to enroll a student in a course.
--    choose an existing student and course and insert a record into the "enrollments" table with the enrollment date.

insert into enrollments (student_id, course_id, enrollment_date)
values (1, 2,'2025-10-10' );  

-- 3. update the email address of a specific teacher in the "teacher" table.
--    choose any teacher and modify their email address.

update teacher
set email = 'new.email@example.com'
where teacher_id = 1; 

-- 4. write an sql query to delete a specific enrollment record from the "enrollments" table.
--    select an enrollment record based on the student and course.

delete from enrollments
where student_id = 1 and course_id = 2; 

-- 5. update the "courses" table to assign a specific teacher to a course.
--    choose any course and teacher from the respective tables.

update courses
set teacher_id = 2
where course_id = 3;  

-- 6. delete a specific student from the "students" table and remove all their enrollment records from the "enrollments" table.
--    be sure to maintain referential integrity.

delete from enrollments
where student_id = 4;

delete from students
where student_id = 4;

-- 7. update the payment amount for a specific payment record in the "payments" table.
--    choose any payment record and modify the payment amount.

update payments
set amount = 1000.00
where payment_id = 5; 


--===Task 3. Aggregate functions, Having, Order By, GroupBy and Joins:

--1. Write an SQL query to calculate the total payments made by a specific student. You will need to
--join the "Payments" table with the "Students" table based on the student's ID.
select s.first_name,s.last_name,sum(p.amount) as total_payment from students s
join payments p on p.student_id=s.student_id
group by s.first_name,s.last_name;

--2. Write an SQL query to retrieve a list of courses along with the count of students enrolled in each
--course. Use a JOIN operation between the "Courses" table and the "Enrollments" table.
select c.course_id,c.course_name,count(s.student_id) as student_count from students s
join enrollments e on e.student_id=s.student_id
join courses c on c.course_id=e.course_id
group by c.course_id,c.course_name;

--3. Write an SQL query to find the names of students who have not enrolled in any course. Use a
--LEFT JOIN between the "Students" table and the "Enrollments" table to identify students
--without enrollments
select s.first_name,s.last_name from students s left join enrollments e on e.student_id=s.student_id 
where s.student_id not in (select e.student_id from enrollments e);

insert into students values('k','d','2001-02-22','fdff','87654');

--4. Write an SQL query to retrieve the first name, last name of students, and the names of the
--courses they are enrolled in. Use JOIN operations between the "Students" table and the
--"Enrollments" and "Courses" tables.
select s.first_name,s.last_name,c.course_name from students s 
join enrollments e on e.student_id=s.student_id
join courses c on c.course_id=e.course_id
group by s.first_name,s.last_name,c.course_name;

--5. Create a query to list the names of teachers and the courses they are assigned to. Join the
--"Teacher" table with the "Courses" table.
select t.first_name,t.last_name,c.course_name from teacher t 
join courses c on c.teacher_id=t.teacher_id;

--6. Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the
--"Students" table with the "Enrollments" and "Courses" tables.
select s.first_name,s.last_name,c.course_name,e.enrollment_date from students s
join enrollments e on e.student_id=s.student_id
join courses c on c.course_id=e.course_id
where c.course_id=1;

--7. Find the names of students who have not made any payments. Use a LEFT JOIN between the
--"Students" table and the "Payments" table and filter for students with NULL payment records.
select s.first_name,s.last_name from students s 
left join payments p on p.student_id=s.student_id
where s.student_id not in (select p.student_id from payments p);

--8. Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN
--between the "Courses" table and the "Enrollments" table and filter for courses with NULL
--enrollment records.
select c.course_id,c.course_name from courses c where c.course_id not in (select e.course_id from enrollments e);

insert into courses (course_name,credits) values ('sql',5);

select c.course_id,c.course_name from courses c 
left join enrollments e on e.course_id=c.course_id
where e.course_id is null;

--9. Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments"
--table to find students with multiple enrollment records.
select s.first_name,s.last_name,count(e.course_id) as course_count from students s 
join enrollments e on s.student_id = e.student_id
group by s.first_name,s.last_name
having  count(e.course_id) > 1;
--selfjoin--
select s.first_name,s.last_name from enrollments e 
join enrollments e1 on e1.course_id <> e.course_id and e.student_id=e1.student_id
join students s on s.student_id=e1.student_id;

--10. Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher"
--table and the "Courses" table and filter for teachers with NULL course assignments
select t.teacher_id,t.first_name,t.last_name from teacher t
left join courses c on c.teacher_id=t.teacher_id
where c.course_id is null;

--=========Task 4. Subquery and its type:===================

--1. Write an SQL query to calculate the average number of students enrolled in each course. Use
--aggregate functions and subqueries to achieve this.

select avg(no_of_students) as avg_num 
from(select c.course_id,count(student_id) as no_of_students from enrollments e
join courses c on c.course_id=e.course_id
group by c.course_id)as course_count; 
--inner query--
select c.course_id,count(student_id) as no_of_students from enrollments e
join courses c on c.course_id=e.course_id
group by c.course_id;

--2. Identify the student(s) who made the highest payment. Use a subquery to find the maximum
--payment amount and then retrieve the student(s) associated with that amount.

select s.student_id, s.first_name, s.last_name, p.amount
from students s
join payments p on s.student_id = p.student_id
where p.amount = (select max(amount) from payments);

-- 3. retrieve a list of courses with the highest number of enrollments.
--use subqueries to find the course(s) with the maximum enrollment count.
select c.course_id, c.course_name
from courses c
join enrollments e on c.course_id = e.course_id
group by c.course_id, c.course_name
having count(e.student_id) = (
select max(course_count)
 from (select count(*) as course_count
from enrollments group by course_id ) 
as course_detail);

-- 4. calculate the total payments made to courses taught by each teacher. 
-- use subqueries to sum payments for each teacher's courses.

select t.first_name + ' ' + t.last_name as teacher_name,
       (select sum(p.amount)
        from payments p
        join enrollments e on p.student_id = e.student_id
        where e.course_id in (select c.course_id from courses c where c.teacher_id = t.teacher_id)
       ) as total_payments
from teacher t;


-- 5. identify students who are enrolled in all available courses.
-- use subqueries to compare a student's enrollments with the total number of courses.

select s.first_name + ' ' + s.last_name as student_name
from students s
where (select count(*) from enrollments e where e.student_id = s.student_id) = 
(select count(*) from courses);


-- 6. retrieve the names of teachers who have not been assigned to any courses.
-- use subqueries to find teachers with no course assignments.

select first_name + ' ' + last_name as teacher_name
from teacher
where teacher_id not in (select teacher_id from courses);


-- 7. calculate the average age of all students.
-- use subqueries to calculate the age of each student based on their date of birth.

select avg(datediff(year, date_of_birth, getdate())) as average_age
from students;


-- 8. identify courses with no enrollments.
-- use subqueries to find courses without enrollment records.

select course_name
from courses
where course_id not in (select course_id from enrollments);


-- 9. calculate the total payments made by each student for each course they are enrolled in.
-- use subqueries and aggregate functions to sum payments.

select s.first_name + ' ' + s.last_name as student_name,
c.course_name,(select sum(p.amount)
from payments p
where p.student_id = s.student_id) as total_payment
from students s
join enrollments e on s.student_id = e.student_id
join courses c on e.course_id = c.course_id
group by s.first_name, s.last_name, c.course_name, s.student_id;


-- 10. identify students who have made more than one payment.
-- use subqueries and aggregate functions to count payments per student and filter for those with counts greater than one.

select s.first_name + ' ' + s.last_name as student_name
from students s
where (select count(*) from payments p where p.student_id = s.student_id) > 1;


-- 11. write an sql query to calculate the total payments made by each student.
-- join the "students" table with the "payments" table and use group by to calculate the sum of payments for each student.

select s.first_name + ' ' + s.last_name as student_name,
sum(p.amount) as total_payment
from students s
join payments p on s.student_id = p.student_id
group by s.first_name, s.last_name;


-- 12. retrieve a list of course names along with the count of students enrolled in each course.
-- use join operations between the "courses" table and the "enrollments" table and group by to count enrollments.

select c.course_name,
count(e.student_id) as total_enrolled_students
from courses c
left join enrollments e on c.course_id = e.course_id
group by c.course_name;


-- 13. calculate the average payment amount made by students.
-- use join operations between the "students" table and the "payments" table and group by to calculate the average.

select s.first_name + ' ' + s.last_name as student_name,
avg(p.amount) as average_payment
from students s
join payments p on s.student_id = p.student_id
group by s.first_name, s.last_name;











