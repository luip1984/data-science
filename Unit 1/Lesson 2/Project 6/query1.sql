--What's the most expensive listing? What else can you tell me about the listing?
select *
from trips
where cast(replace(replace(price, '$',''), ',','') as decimal)  
= (
	select max(cast(replace(replace(price, '$',''), ',','') as decimal) )
	from trips
)
;
select *
from sfo_calender
where cast(replace(replace(price, '$',''), ',','') as decimal)  
= (
	select max(cast(replace(replace(price, '$',''), ',','') as decimal) )
	from sfo_calender
)
;
--What neighborhoods seem to be the most popular?
select neighbourhood_cleansed, count(*) 
from trips
group by neighbourhood_cleansed
order by 2 desc
limit 1
;

--What time of year is the cheapest time to go to your city? 
select 
--extract(week from calender_date), 
to_char( date_trunc('week', calender_date), 'YYYY-MM-DD') "WEEK_START",
to_char( date_trunc('week', calender_date) + interval '6' day, 'YYYY-MM-DD') "WEEK_END"
--avg( cast(replace(replace(price, '$',''), ',','') as decimal) )
from sfo_calender
group by calender_date
order by avg( cast(replace(replace(price, '$',''), ',','') as decimal) )
LIMIT 1
--What about the busiest?
select 
--extract(week from calender_date), 
to_char( date_trunc('week', calender_date), 'YYYY-MM-DD') "WEEK_START",
to_char( date_trunc('week', calender_date) + interval '6' day, 'YYYY-MM-DD') "WEEK_END"
--count(available)
from sfo_calender
where available = 't'
group by calender_date
order by count(available)
limit 1;