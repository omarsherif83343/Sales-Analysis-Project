create table products(

product_id int primary key,
product_name varchar(50),
category varchar(50),
price decimal(10,2),
stock int

);

INSERT INTO products VALUES
(1,'Laptop','Electronics',30000,15),
(2,'Mouse','Electronics',250,100),
(3,'Keyboard','Electronics',600,70),
(4,'Monitor','Electronics',5000,20),
(5,'Desk','Furniture',4000,10),
(6,'Chair','Furniture',2000,25),
(7,'Printer','Electronics',3500,12),
(8,'Book Shelf','Furniture',1500,8),
(9,'Headphones','Electronics',1200,50),
(10,'Webcam','Electronics',900,30);

alter table products drop column inventory_value;

select * from products;

CREATE TABLE sales(
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity INT
);
INSERT INTO sales VALUES
(1,1,5),
(2,2,20),
(3,3,15),
(4,4,4),
(5,5,2),
(6,6,8),
(7,7,3),
(8,8,5),
(9,9,12),
(10,10,10),
(11,1,2),
(12,4,1),
(13,9,8),
(14,2,30),
(15,5,1);

select sum(s.quantity) as
total_quantity,p.product_name 
from products p inner join sales s on 
p.product_id = s.product_id 
group by p.product_name
order by total_quantity desc limit 1;




select sum(p.price * s.quantity) 
as revenue,p.product_name
from products p join sales s
 on p.product_id = s.product_id
 group by p.product_name 
 order by revenue desc limit 3;
 
 
 
 select p.product_name,p.price,s.quantity from products p inner join sales s on p.product_id = s.product_id