-- add eye color records for Jon Snow, Arya Stark
INSERT INTO EyesColor (person_id, color) VALUES (
       (SELECT id FROM Person WHERE first_name = 'Jon' AND last_name = 'Snow'),
       'Brown');
INSERT INTO EyesColor (person_id, color) VALUES (
       (SELECT id FROM Person WHERE first_name = 'Arya' AND last_name = 'Stark'),
       'Green');

-- create new table TVShow
CREATE TABLE TVShow (
       id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       name  CHAR(128) NOT NULL
       );

-- create new table TVShowPerson
CREATE TABLE TVShowPerson (
       tvshow_id INTEGER NOT NULL,
       person_id INTEGER NOT NULL,
       FOREIGN KEY(tvshow_id) REFERENCES TVShow(id),
       FOREIGN KEY(person_id) REFERENCES Person(id)
       );

-- add records into TVShow
INSERT INTO TVShow (name) VALUES ('Homeland');
INSERT INTO TVShow (name) VALUES ('The big bang theory');
INSERT INTO TVShow (name) VALUES ('Game of Thrones');
INSERT INTO TVShow (name) VALUES ('Breaking bad');

-- add records to TVShowPerson
--Breaking Bad, Walter Junior White
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
       (SELECT id FROM TVShow WHERE name = 'Breaking bad'),
       (SELECT id FROM Person WHERE first_name = 'Walter Junior' AND last_name = 'White'));
--Game of Thrones, Jaime Lannister
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
       (SELECT id FROM TVShow WHERE name = 'Game of Thrones'),
       (SELECT id FROM Person WHERE first_name = 'Jaime' AND last_name = 'Lannister')); 
--The Big Bang Theory, Sheldon Cooper
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
       (SELECT id FROM TVShow WHERE name = 'The big bang theory'),
       (SELECT id FROM Person WHERE first_name = 'Sheldon' AND last_name = 'Cooper')); 
--Game of Thrones, Tyrion Lannister
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
       (SELECT id FROM TVShow WHERE name = 'Game of Thrones'),
       (SELECT id FROM Person WHERE first_name = 'Tyrion' AND last_name = 'Lannister')); 
--Game of Thrones, Jon Snow 
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
       (SELECT id FROM TVShow where name = 'Game of Thrones'),
       (SELECT id FROM Person where first_name = 'Jon' AND last_name = 'Snow'));
--Game of Thrones, Arya Stark
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (
       (SELECT id FROM TVShow where name = 'Game of Thrones'),
       (SELECT id FROM Person where first_name = 'Arya' AND last_name = 'Stark')); 

-- print all tables in database
SELECT * FROM Person;
SELECT * From EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;
