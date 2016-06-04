/* 
 * display distinct last names of characters from Game of Thrones,
 * in ascending order (do this by joining Person and TVShow using
 * TVShowPerson as intermediary)
 */
SELECT DISTINCT last_name FROM Person LEFT JOIN TVShowPerson
on Person.id = TVShowPerson.person_id
LEFT JOIN TVShow
on TVShowPerson.tvshow_id = TVShow.id
WHERE name = 'Game of Thrones'
ORDER BY last_name ASC;

/* display the number of Person where age is greater than 30 */
SELECT count(age) FROM PERSON where age > 30;

/*
 * display id, first name, last name, age, eye color, and tv show
 * name for each Person record (do this by joining all the tables)
 */
SELECT Person.id, first_name, last_name, age, color, name
FROM PERSON LEFT JOIN EyesColor on Person.id = EyesColor.person_id
LEFT JOIN TVShowPerson on Person.id = TVShowPerson.person_id
LEFT JOIN TVShow on TVShowPerson.tvshow_id = TVShow.id;

/* display the sum of age values for all Person */
SELECT sum(age) FROM Person;
