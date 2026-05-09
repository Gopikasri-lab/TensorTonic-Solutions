-- Write your SQL query here
WITH cte as 
(
    select customer, count(distinct(order_date)) as order_count, sum(amount) as total_spent 
    from orders 
    
    group by customer 
    
    
)
select cte.* from cte where order_count>1 order by total_spent desc,customer asc;