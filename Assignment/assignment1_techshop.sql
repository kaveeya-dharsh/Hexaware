create database techshop;
use techshop;

create table customers (
    customerid int primary key,
    firstname varchar(25),
    lastname varchar(25),
    email varchar(25),
    phone varchar(20),
    address text
);

create table products (
    productid int primary key,
    productname varchar(25),
    description varchar(50),
    price decimal(10, 2)
);

create table orders (
    orderid int primary key,
    customerid int,
    orderdate date,
    totalamount decimal(10, 2),
    foreign key (customerid) references customers(customerid)
);

create table orderdetails (
    orderdetailid int primary key,
    orderid int,
    productid int,
    quantity int,
    foreign key (orderid) references orders(orderid),
    foreign key (productid) references products(productid)
);

create table inventory (
    inventoryid int primary key,
    productid int,
    quantityinstock int,
    laststockupdate datetime,
    foreign key (productid) references products(productid)
);

insert into customers (customerid, firstname, lastname, email, phone, address) values
(1, 'a', 'x', 'a@example.com', '1111', 'address1'),
(2, 'b', 'y', 'b@example.com', '2222', 'address2'),
(3, 'c', 'z', 'c@example.com', '3333', 'address3'),
(4, 'd', 'p', 'd@example.com', '4444', 'address4'),
(5, 'e', 'q', 'e@example.com', '5555', 'address5'),
(6, 'f', 'r', 'f@example.com', '6666', 'address6'),
(7, 'g', 's', 'g@example.com', '7777', 'address7'),
(8, 'h', 't', 'h@example.com', '8888', 'address8'),
(9, 'i', 'u', 'i@example.com', '9999', 'address9'),
(10, 'j', 'v', 'j@example.com', '0000', 'address10');

insert into products (productid, productname, description, price) values
(1, 'item1', 'desc1', 10),
(2, 'item2', 'desc2', 20),
(3, 'item3', 'desc3', 30),
(4, 'item4', 'desc4', 40),
(5, 'item5', 'desc5', 50),
(6, 'item6', 'desc6', 60),
(7, 'item7', 'desc7', 70),
(8, 'item8', 'desc8', 80),
(9, 'item9', 'desc9', 90),
(10, 'item10', 'desc10', 100);

insert into orders (orderid, customerid, orderdate, totalamount) values
(1, 1, '2025-04-01', 100),
(2, 2, '2025-04-02', 200),
(3, 3, '2025-04-03', 300),
(4, 4, '2025-04-04', 400),
(5, 5, '2025-04-05', 500),
(6, 6, '2025-04-06', 600),
(7, 7, '2025-04-07', 700),
(8, 8, '2025-04-08', 800),
(9, 9, '2025-04-09', 900),
(10, 10, '2025-04-10', 1000);

insert into orderdetails (orderdetailid, orderid, productid, quantity) values
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 3),
(4, 4, 4, 4),
(5, 5, 5, 5),
(6, 6, 6, 6),
(7, 7, 7, 7),
(8, 8, 8, 8),
(9, 9, 9, 9),
(10, 10, 10, 10);

insert into inventory (inventoryid, productid, quantityinstock, laststockupdate) values
(1, 1, 100, '2025-04-01'),
(2, 2, 200, '2025-04-02'),
(3, 3, 300, '2025-04-03'),
(4, 4, 400, '2025-04-04'),
(5, 5, 500, '2025-04-05'),
(6, 6, 600, '2025-04-06'),
(7, 7, 700, '2025-04-07'),
(8, 8, 800, '2025-04-08'),
(9, 9, 900, '2025-04-09'),
(10, 10, 1000, '2025-04-10');
insert into inventory values (11,11,200,'2025-04-03');


select * from customers;

select * from products;

select * from orders;

select * from orderdetails;

select * from inventory;

--==========select,where,from,like===========

--1. Write an SQL query to retrieve the names and emails of all customers.
select firstname,lastname,email from customers;

--2.2. Write an SQL query to list all orders with their order dates and corresponding customer names.
select o.orderid,0.orderdate,c.firstname,c.lastname from orders o left join customers c on c.customerid=o.customerid;

--3. Write an SQL query to insert a new customer record into the "Customers" table. Include
--customer information such as name, email, and address.
insert into customers (customerid,firstname,lastname,email,address) values (11,'kaveeya','dharshni','kd@gmail.com','brindavan street');

--4. Write an SQL query to update the prices of all electronic gadgets in the "Products" table by
--increasing them by 10%.
update products set price = price * 1.10 where description like 'electronic gadgets';

--5. Write an SQL query to delete a specific order and its associated order details from the
--"Orders" and "OrderDetails" tables. Allow users to input the order ID as a parameter
declare @orderid int = 10;
delete from orderdetails where orderid = @orderid;
delete from orders where orderid = @orderid;

--6. Write an SQL query to insert a new order into the "Orders" table. Include the customer ID,
--order date, and any other necessary information.
insert into orders (orderid, customerid, orderdate, totalamount)
values (10, 3, getdate(), 1000);

--7. Write an SQL query to update the contact information (e.g., email and address) of a specific
--customer in the "Customers" table. Allow users to input the customer ID and new contact
--information.
declare @customerid int = 11;
update customers 
set email ='kdnew@gmail.com',
address = 'newstreet'
where customerid=@customerid;

--8. Write an SQL query to recalculate and update the total cost of each order in the "Orders"
--table based on the prices and quantities in the "OrderDetails" table.
update orders set totalamount=(
select sum(p.price * od.quantity) 
from orderdetails od inner join products p on p.productid=od.productid
where orders.orderid = od.orderid);

--9. Write an SQL query to delete all orders and their associated order details for a specific
--customer from the "Orders" and "OrderDetails" tables. Allow users to input the customer ID
--as a parameter.
declare @custid_to_delete int = 2;
delete from orderdetails 
where orderid in (select orderid from orders where customerid = @custid_to_delete);
delete from orders 
where customerid = @custid_to_delete;

--10. Write an SQL query to insert a new electronic gadget product into the "Products" table,
--including product name, category, price, and any other relevant details.
insert into products (productid, productname, description, price) 
values (11, 'smartwatch', 'electronic gadget', 2500);

--11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from
--"Pending" to "Shipped"). Allow users to input the order ID and the new status.
alter table orders
add status varchar(20);
declare @oid int = 4;
update orders 
set status = 'shipped'
where orderid = @oid;

--12. Write an SQL query to calculate and update the number of orders placed by each customer
--in the "Customers" table based on the data in the "Orders" table.
alter table customers add totalorder int;
update customers
set totalorder = (
    select count(orderid) 
    from orders 
    where orders.customerid = customers.customerid
);

--=========================task3=======================
-- 1. write an sql query to retrieve a list of all orders along with customer information (e.g., customer name) for each order.
select 
    o.orderid, 
    o.orderdate, 
    c.firstname, 
    c.lastname
from orders o
join customers c on o.customerid = c.customerid;

-- 2. write an sql query to find the total revenue generated by each electronic gadget product. include the product name and the total revenue.
select 
    p.productname, 
    sum(p.price*od.quantity) as total_revenue
from orderdetails od
join products p on od.productid = p.productid
group by p.productname;

select 
    p.productname, 
    sum(p.price*od.quantity) as total_revenue
from products p 
join orderdetails od on od.productid = p.productid
group by p.productname;


-- 3. write an sql query to list all customers who have made at least one purchase. include their names and contact information.
select  
    c.firstname, 
    c.lastname, 
    c.email, 
    c.phone
from customers c
join orders o on c.customerid = o.customerid;

-- 4. write an sql query to find the most popular electronic gadget, which is the one with the highest total quantity ordered. include the product name and the total quantity ordered.
select top 1
    p.productname, 
    max(od.quantity) as total_quantity_ordered
from orderdetails od
join products p on od.productid = p.productid
group by p.productname
order by total_quantity_ordered desc;

-- 5. write an sql query to retrieve a list of electronic gadgets along with their corresponding categories.
select 
    productname, 
    description
from products;

-- 6. write an sql query to calculate the average order value for each customer. include the customer's name and their average order value.
select 
    c.firstname, 
    c.lastname, 
    avg(o.totalamount) as average_order_value
from customers c
join orders o on c.customerid = o.customerid
group by c.firstname, c.lastname;

-- 7. write an sql query to find the order with the highest total revenue. include the order id, customer information, and the total revenue.
select top 1
    o.orderid, 
    c.firstname, 
    c.lastname, 
   max(p.price*od.quantity) as total_revenue
from orders o
join customers c on o.customerid = c.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
group by o.orderid, c.firstname, c.lastname
order by total_revenue desc;

select top 1
    o.orderid, 
    c.firstname, 
    c.lastname, 
    max(totalamount) as total_revenue
from orders o
join customers c on o.customerid = c.customerid
group by o.orderid, c.firstname, c.lastname
order by total_revenue desc;

-- 8. write an sql query to list electronic gadgets and the number of times each product has been ordered.

select p.productname,count(od.quantity) as order_count
from products p join orderdetails od on od.productid=p.productid
group by p.productname;


-- 9. write an sql query to find customers who have purchased a specific electronic gadget product. allow users to input the product name as a parameter.
declare @productname varchar(100) = 'item5';

select  
    c.firstname, 
    c.lastname, 
    c.email
from customers c
join orders o on c.customerid = o.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where p.productname = @productname;

-- 10. write an sql query to calculate the total revenue generated by all orders placed within a specific time period. allow users to input the start and end dates as parameters.
declare @startdate date = '2025-04-03';
declare @enddate date = '2025-04-06';

select 
    sum(od.quantity * p.price) as total_revenue
from orders o
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where o.orderdate between @startdate and @enddate;

declare @startdate date = '2025-04-03';
declare @enddate date = '2025-04-06';
select 
    sum(od.quantity * p.price) as total_revenue
from products p
join orderdetails od on od.productid= p.productid
join orders o on o.orderid=od.orderid
where o.orderdate between @startdate and @enddate;

--=============Task 4. Subquery and its type:
--1. Write an SQL query to find out which customers have not placed any orders
select firstname,lastname from customers where customerid not in (select customerid from orders);

--2. Write an SQL query to find the total number of products available for sale.
select sum(quantityinstock) as available_products_count  from inventory where productid in (select productid from products);
select count(productid) as total_products
from products;

--3. Write an SQL query to calculate the total revenue generated by TechShop. 
select sum(p.price*od.quantity) as total_revenue from products p join orderdetails od on od.productid= p.productid;

--4. Write an SQL query to calculate the average quantity ordered for products in a specific category.
--Allow users to input the category name as a parameter.
declare @product_name varchar(25) = 'item4';
select avg(od.quantity) as average_quantity from orderdetails od 
join products p on p.productid=od.productid 
where p.productname= @product_name;

--5. Write an SQL query to calculate the total revenue generated by a specific customer. Allow users
--to input the customer ID as a parameter.
declare @customer_id int = 6;
select sum(p.price*od.quantity) as total_revenue from orderdetails od 
join products p on p.productid=od.productid 
join orders o on o.orderid=od.orderid
where customerid=@customer_id;

--6. Write an SQL query to find the customers who have placed the most orders. List their names
--and the number of orders they've placed.
select c.firstname, c.lastname, count(o.orderid) as total_orders
from customers c
join orders o on c.customerid = o.customerid
group by c.firstname, c.lastname
having count(o.orderid) = (
    select max(order_count) from (
        select count(orderid) as order_count
        from orders
        group by customerid
    ) as order_counts
);

select top 1 c.firstname, c.lastname, count(o.orderid) as total_orders
from customers c
join orders o on c.customerid = o.customerid
group by c.firstname, c.lastname
order by total_orders desc;

--7. Write an SQL query to find the most popular product category, which is the one with the highest
--total quantity ordered across all orders.
select top 1
p.productname,max(od.quantity) as total_quantity
from products p join orderdetails od on od.productid=p.productid
group by p.productname
order by total_quantity desc;

--8. Write an SQL query to find the customer who has spent the most money (highest total revenue)
--on electronic gadgets. List their name and total spending.
select top 1
c.firstname,c.lastname ,
max(p.price*od.quantity) as highest_revenue
from customers c 
join orders o on o.customerid=c.customerid
join orderdetails od on o.orderid=od.orderid
join products p on p.productid=od.productid
group by c.firstname,c.lastname
order by highest_revenue desc;

--9. Write an SQL query to calculate the average order value (total revenue divided by the number of
--orders) for all customers
select avg(order_value) as average_order_value
from (
    select o.orderid, sum(od.quantity * p.price) as order_value
    from orders o
    join orderdetails od on o.orderid = od.orderid
    join products p on od.productid = p.productid
    group by o.orderid
) as order_values;

--10. Write an SQL query to find the total number of orders placed by each customer and list their
--names along with the order count.
select c.firstname,c.lastname,count(o.orderid) as order_count 
from customers c join orders o on c.customerid=o.customerid
group by c.firstname,c.lastname;
