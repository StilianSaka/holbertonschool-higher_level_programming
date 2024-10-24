-- Write a script that lists all the records in the second_table

SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
