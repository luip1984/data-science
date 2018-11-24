
CREATE TABLE sfo_calender (
	listing_id BIGINT,
	calender_date DATE,
	available CHAR,
	price TEXT
);

COPY sfo_calender (
	listing_id ,
	calender_date ,
	available ,
	price 
)
FROM 'C:\Export\Thinkful\Docs\Unit 1\Lesson 2\Project 6\calendar.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE sfo_reviews (
	listing_id BIGINT,
	id BIGINT,
	review_date DATE,
	reviewer_id BIGINT,
	reviewer_name TEXT,
	comments TEXT
);

COPY sfo_reviews (
	listing_id,
	id,
	review_date,
	reviewer_id,
	reviewer_name,
	comments
)
FROM 'C:\Export\Thinkful\Docs\Unit 1\Lesson 2\Project 6\reviews.csv' DELIMITER ',' CSV HEADER;
