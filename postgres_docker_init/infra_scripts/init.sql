
-- Create schema
CREATE SCHEMA IF NOT EXISTS ALT_SCHOOL;


-- create and populate tables
create table if not exists ALT_SCHOOL.NETFLIX_DATA
(
    user_id  serial primary key,
    subscription varchar not null,
    join_date varchar,
    last_payment_date varchar,
    country varchar,
    age int,
    gender varchar,
    device varchar,
    plan_duration varchar 
);


COPY ALT_SCHOOL.NETFLIX_DATA (user_id, subscription, join_date, last_payment_date, country, age, gender, device,plan_duration)
FROM '/data/data.csv' DELIMITER ',' CSV HEADER;








