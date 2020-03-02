-- Script that lists the number of records with the same score in the table second_table.
-- The number of records for this score with the label number.
SELECT
	score, COUNT(*) 'number'
FROM
	second_table
GROUP BY
      score
ORDER BY
      score DESC;
