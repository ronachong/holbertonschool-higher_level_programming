UPDATE Person set age=27 WHERE first_name = 'Jon' AND last_name = 'Snow';
UPDATE Person set age=18 WHERE first_name = 'Walter Junior' AND last_name = 'White';
DELETE FROM EyesColor WHERE person_id in (SELECT id FROM Person WHERE first_name = 'Walter' AND last_name = 'White');
DELETE FROM Person WHERE first_name = 'Walter' AND last_name = 'White';
SELECT * FROM Person
       ORDER BY first_name ASC;
