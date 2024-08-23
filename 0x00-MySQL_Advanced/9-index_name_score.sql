-- SQL script that creates an index idx_name_first_score
-- on the table names and the first letter of name and the score

SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
