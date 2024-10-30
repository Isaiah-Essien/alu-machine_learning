-- Display the max temperature of each state, ordered by state name
SELECT state, MAX(temperature) AS max_temperature
FROM Temperatures
GROUP BY state
ORDER BY state;
