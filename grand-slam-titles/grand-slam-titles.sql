/* Write your PL/SQL query statement below */
select 
X.player_id, 
Y.player_name, 
sum(X.grand_slams_count) as grand_slams_count
from
(select wimbledon as player_id, 
 count(*) as grand_slams_count
 from championships
group by wimbledon
union all
select fr_open as player_id, 
 count(*) as grand_slams_count
 from championships
group by fr_open
union all
select us_open as player_id, 
 count(*) as grand_slams_count
 from championships
group by us_open
union all
select au_open as player_id, 
 count(*) as grand_slams_count
 from championships
group by au_open)X left join players Y
on X.player_id = Y.player_id
group by X.player_id, Y.player_name
order by grand_slams_count;