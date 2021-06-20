/* Write your PL/SQL query statement below */
with cte as
(
select order_id, max(quantity) as max_quantity from ordersdetails
    group by order_id
), cte1 as

(select 
x.order_id,
x.average_quantity,
m.max_quantity
from
(select o.order_id, 
(sum(o.quantity)/count(distinct o.product_id)) as average_quantity
from ordersdetails o
group by o.order_id)x left join cte m
on x.order_id = m.order_id);

select x.order_id from cte1 x where x.max_quantity > (select max(average_quantity) from cte1)