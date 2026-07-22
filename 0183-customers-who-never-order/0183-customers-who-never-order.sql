# Write your MySQL query statement be
select c.name as Customers from Customers c 
where  not exists(select CustomerId from Orders o where c.id=o.customerId);