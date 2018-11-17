SELECT trip_id, duration
FROM trips
where duration > 500
order by duration desc;

select * 
from stations 
where station_id = 84;

select mintemperaturef
from weather
where zip = 94301 and events = 'Rain'
;

