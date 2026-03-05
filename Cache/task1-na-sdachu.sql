--№1
--1
select *
from customers;

--2
select product_name, unit_price
from products;

--3
select region_description
from region;

--4
select company_name
from suppliers;

--5
select contact_name, city
from customers;

--6
select order_id, shipped_date - order_date
from orders;

--7
select count(*)
from orders;

--8
select distinct city
from customers;

--9
select distinct city, country
from customers;

--10
select count(country)
from customers;

--№2
--1
select *
from orders
where ship_country in('France', 'Austria', 'Spain');

--2
--Переделал
select *
from orders
order by required_date desc, shipped_date asc;

--3
select min(units_in_stock)
from products
where units_in_stock > 30;

--4
select max(units_in_stock)
from products
where units_in_stock > 30;

--5
select avg(required_date - order_date)
from orders
where ship_country = 'USA';

--6
select sum(unit_price*units_in_stock)
from products
where discontinued = 0;

--№3
--1
select *
from orders 
where ship_country like('U%');

--2
select order_id, customer_id, freight, ship_country
from orders
where ship_country like'N'
order by freight desc
limit 10;

--3
select last_name, first_name, home_phone, region
from employees
where region is null;

--4
select count(customer_id)
from customers
where region is not null;

--5
select country, count(supplier_id)
from suppliers
group by country
order by count(supplier_id) desc;

--6
select ship_region, sum(freight)
from orders
where ship_region is not null
group by ship_region
having sum(freight) > 2750
order by sum(freight) desc;

--7
select distinct country
from customers
union
select country
from suppliers
order by country asc;

--8
select country
from customers
intersect
select country
from suppliers
intersect
select country
from employees;

--9
select country
from customers
intersect
select country
from suppliers
except
select country
from employees;

--Посчитать продукты по категориям. id и количество
select category_id, count(product_id) as count
from products
group by category_id
having count(product_id) >= 10;

--топ 5 товаров клиентов. вывести id товаров
select product_id
from order_details
group by product_id
order by sum(quantity) desc
limit 5;

--сумма продаж по каждому продукту
select product_id, sum((unit_price * (1 - discount)) * quantity)
from order_details
group by product_id;

--ср мин и макс значение по доставке грузов.
select ship_country, avg(shipped_date - order_date),
min(shipped_date - order_date), max(shipped_date - order_date)
from orders
where ship_country in('USA', 'Canada', 'Switzerland')
group by ship_country

