select date, zip 
from weather 
where maxtemperaturef = (
	select max(maxtemperaturef) 
	from weather
);

select trip_id, duration, start_date, end_date, zip_code
from trips
where duration = (
	select min(duration)
	from trips
);

select end_station, avg(duration)
from trips
group by end_station;
