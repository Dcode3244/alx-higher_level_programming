-- lists the number of records with the same score int he table second_table
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;
