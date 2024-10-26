-- Write a query that will display the results below (Note: some columns might be renamed 
-- but use the column names above). It should only show 2020 data and order by driver 
-- points

SELECT 
    location AS "location",
    grid AS "grid",
    position AS "position",
    fastest lap AS "fastest_lap",
    points AS "points",
    driver_name AS "driver_name",
    race_name AS "race_name",
    race time AS "time",
    race_year AS "year",
    team AS "team_name",
    race_date AS "date"
FROM 
    race_results
WHERE 
    YEAR(race_date) = 2020
ORDER BY 
    points DESC;