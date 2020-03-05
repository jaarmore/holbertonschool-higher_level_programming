-- Script that displays the max temperature of each state (ordered by State name).
-- Displays the max temperature of each state.
SELECT state, MAX(value) 'max_temp'
FROM temperatures
GROUP BY state
ORDER BY state;
