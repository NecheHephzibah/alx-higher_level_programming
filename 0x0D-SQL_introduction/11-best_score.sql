-- script that lists all records with a score >= 10 in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.

SELECT DISTINCT score, name
FROM (
    SELECT score, name
    FROM second_table
    WHERE score >= 10
) AS subquery
ORDER BY score DESC;
