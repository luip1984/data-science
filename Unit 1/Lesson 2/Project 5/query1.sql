--What are the three longest trips on rainy days;?
select t.trip_id, t.duration, t.start_date, w.date, t.zip_code, w.zip, w.precipitationin
from trips t
join weather w 
on to_date(w.date, 'YYYY-MM-DD') = to_date(t.start_date, 'YYYY-MM-DD HH24:MI:SS') 
and w.zip = t.zip_code
and w.precipitationin > 0.0
order by duration desc
limit 3
;

--Which station is full most often?
select s2.station_id, count(*)
from status s2 
where 
s2.bikes_available = 0 or 
s2.docks_available = 0
group by s2.station_id
order by count(*) desc
limit 1
;

--Return a list of stations with a count of number of trips starting at that station but ordered by dock count.
with station_usage(station_id, trip_usage_count)
as
(
select s1.station_id, count(*) AS trip_usage_count
from trips t
join stations s1 on s1.name = t.start_station
group by s1.station_id
)
select s.station_id, s.name, s.dockcount, su.trip_usage_count
from station_usage su
join stations s on s.station_id = su.station_id
order by dockcount, t
rip_usage_count desc
;

--What's the length of the longest trip for each day it rains anywhere?
select w.date, max(t.duration)
from trips t
join weather w 
on to_date(w.date, 'YYYY-MM-DD') = to_date(t.start_date, 'YYYY-MM-DD HH24:MI:SS') 
and w.zip = t.zip_code
and w.precipitationin > 0.0
group by w.date



