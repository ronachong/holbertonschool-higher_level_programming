-- add eye color records for Jon Snow, Arya Stark
INSERT INTO EyesColor (person_id, color) VALUES (6, 'Brown');
INSERT INTO EyesColor (person_id, color) VALUES (7, 'Green');

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
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (4, 2); --Breaking Bad, Walter White
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 3); --Game of Thrones, Jaime Lannister
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (2, 4); --The Big Bang Theory, Sheldon Cooper
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 5); --Game of Thrones, Tyrion Lannister
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 6); --Game of Thrones, Jon Snow 
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES (3, 7); --Game of Thrones, Arya Stark

-- print all tables in database
SELECT * FROM Person;
SELECT * From EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;
