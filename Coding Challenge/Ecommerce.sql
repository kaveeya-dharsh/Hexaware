create database ecom;
use ecom;

--Table creation for database ecom--

create table customers (
 customerid int primary key,
 firstname varchar(25),
 lastname varchar(25),
 email varchar(50),
 address varchar(50));

create table products (
productid int primary key,
name varchar(25),
price decimal(10, 2),
description varchar(50),
stockquantity int);


create table orders (
orderid int primary key,
customerid int,
orderdate date,
totalprice decimal(10, 2),
foreign key (customerid) references customers(customerid));

create table orderitems (
orderitemid int primary key,
orderid int,
productid int,
quantity int,
itemamount decimal(10,2),
foreign key (orderid) references orders(orderid),
foreign key (productid) references products(productid));

create table cart (
cartid int primary key,
customerid int,
productid int,
quantity int,
foreign key (customerid) references customers(customerid),
foreign key (productid) references products(productid));

insert into customers (customerid, firstname, lastname, email, address) values
(1, 'John', 'Doe', 'johndoe@example.com', '123 Main St, City'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '456 Elm St, Town'),
(3, 'Robert', 'Johnson', 'robert@example.com', '789 Oak St, Village'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '101 Pine St, Suburb'),
(5, 'David', 'Lee', 'david@example.com', '234 Cedar St, District'),
(6, 'Laura', 'Hall', 'laura@example.com', '567 Birch St, County'),
(7, 'Michael', 'Davis', 'michael@example.com', '890 Maple St, State'),
(8, 'Emma', 'Wilson', 'emma@example.com', '321 Redwood St, Country'),
(9, 'William', 'Taylor', 'william@example.com', '432 Spruce St, Province'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '765 Fir St, Territory');

insert into products (productid, name, description, price, stockquantity) values
(1, 'Laptop', 'High-performance laptop', 800.00, 10),
(2, 'Smartphone', 'Latest smartphone', 600.00, 15),
(3, 'Tablet', 'Portable tablet', 300.00, 20),
(4, 'Headphones', 'Noise-canceling', 150.00, 30),
(5, 'TV', '4K Smart TV', 900.00, 5),
(6, 'Coffee Maker', 'Automatic coffee maker', 50.00, 25),
(7, 'Refrigerator', 'Energy-efficient', 700.00, 10),
(8, 'Microwave Oven', 'Countertop microwave', 80.00, 15),
(9, 'Blender', 'High-speed blender', 70.00, 20),
(10, 'Vacuum Cleaner', 'Bagless vacuum cleaner', 120.00, 10);

insert into orders (orderid, customerid, orderdate, totalprice) values
(1, 1, '2023-01-05', 1200.00),
(2, 2, '2023-02-10', 900.00),
(3, 3, '2023-03-15', 300.00),
(4, 4, '2023-04-20', 150.00),
(5, 5, '2023-05-25', 1800.00),
(6, 6, '2023-06-30', 400.00),
(7, 7, '2023-07-05', 700.00),
(8, 8, '2023-08-10', 160.00),
(9, 9, '2023-09-15', 140.00),
(10, 10, '2023-10-20', 1400.00);

insert into orderitems (orderitemid, orderid, productid, quantity, itemamount) values
(1, 1, 1, 2, 1600.00),
(2, 1, 3, 1, 300.00),
(3, 2, 2, 3, 1800.00),
(4, 3, 5, 2, 1800.00),
(5, 4, 4, 4, 600.00),
(6, 4, 6, 1, 50.00),
(7, 5, 1, 1, 800.00),
(8, 5, 2, 2, 1200.00),
(9, 6, 10, 2, 240.00),
(10, 6, 9, 3, 210.00);

insert into cart (cartid, customerid, productid, quantity) values
(1, 1, 1, 2),
(2, 1, 3, 1),
(3, 2, 2, 3),
(4, 3, 4, 4),
(5, 3, 5, 2),
(6, 4, 6, 1),
(7, 5, 1, 1),
(8, 6, 10, 2),
(9, 6, 9, 3),
(10, 7, 7, 2);

select * from customers;

select * from products;

select * from orders;

select * from orderitems;

select * from cart;

--1. Update refrigerator product price to 800.

update products set price='800'
where name='refrigerator';

--2. Remove all cart items for a specific customer.

delete from cart 
where customerid=7;

--3. Retrieve Products Priced Below $100.

select productid,name,price from products where price < 100;

--4. Find Products with Stock Quantity Greater Than 5.

select productid,name,stockquantity from products where stockquantity > 5;

--5. Retrieve Orders with Total Amount Between $500 and $1000.

select orderid,totalprice from orders where totalprice between 500 and 1000;

--6. Find Products which name end with letter ‘r’.

select name from products where name like '%r';

--7. Retrieve Cart Items for Customer 5.

select c.cartid,p.productid,p.name from products p
join cart c on c.productid=p.productid
where c.customerid=5;

--data along with customer detail--

select c1.customerid,c1.firstname + ''+ c1.lastname as customer_name,
c.cartid,p.productid,p.name from products p
join cart c on c.productid=p.productid
join customers c1 on c1.customerid=c.customerid
where c.customerid=5;

--8. Find Customers Who Placed Orders in 2023.

select c.firstname+''+c.lastname as customer_name,o.orderdate
from customers c join orders o on o.customerid=c.customerid
where year(o.orderdate) = 2023;

--9. Determine the Minimum Stock Quantity for Each Product Category.

alter table products add category varchar(25);
update products set category = 'Electronics' where productid in (1, 2, 3, 4, 5);
update products set category = 'Home Appliances' where productid in (6, 7, 8, 9, 10);

select category, min(stockquantity) as min_stock
from products
group by category;

--10. Calculate the Total Amount Spent by Each Customer.

select c.firstname+''+c.lastname as customer_name ,
sum(o.totalprice) as total_amount 
from customers c
join orders o on c.customerid=o.customerid
group by c.firstname,c.lastname;

--11. Find the Average Order Amount for Each Customer.

select c.firstname+''+c.lastname as customer_name,
avg(o.totalprice) as avg_orderamt
from customers c
join orders o on c.customerid=o.customerid
group by c.firstname,c.lastname;

--12. Count the Number of Orders Placed by Each Customer.

select c.customerid,count(o.orderid) as order_count 
from customers c join orders o on
c.customerid=o.customerid
group by c.customerid;

--13. Find the Maximum Order Amount for Each Customer.

select c.firstname+''+c.lastname as customer_name,max(o.totalprice) as max_amt
from customers c join orders o on c.customerid=o.customerid
group by c.firstname,c.lastname;

--14. Get Customers Who Placed Orders Totaling Over $1000.

select c.customerid,c.firstname+''+c.lastname as customer_name,
sum(o.totalprice) as total
from customers c join orders o on c.customerid=o.customerid
group by c.customerid,c.firstname,c.lastname
having sum(o.totalprice) > 1000;

--15. Subquery to Find Products Not in the Cart.

select productid,name from products where productid
not in (select productid from cart);

--16. Subquery to Find Customers Who Haven't Placed Orders.

select c.customerid,c.firstname+''+c.lastname as customer_name
from customers c where c.customerid not in (select customerid from orders);

--17. Subquery to Calculate the Percentage of Total Revenue for a Product.

select productid,sum(itemamount) as product_total,
(sum(itemamount) * 100.0) / (select sum(itemamount) from orderitems) as revenue_percentage
from orderitems
group by productid;

--18. Subquery to Find Products with Low Stock.

select productid,name,stockquantity from 
products where stockquantity = (select min(stockquantity) from products);

--19. Subquery to Find Customers Who Placed High-Value Orders.

select c.customerid,c.firstname+''+c.lastname as customer_name,
max(o.totalprice) as high_value from 
customers c join orders o on c.customerid=o.customerid
where o.totalprice=(select max(totalprice) from orders)
group by c.customerid,c.firstname,c.lastname;









