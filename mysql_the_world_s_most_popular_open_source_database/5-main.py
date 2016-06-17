#!/usr/bin/python

'''
5-main.py fetches and prints the names, seasons and episodes of
TV shows from the database Project 169
'''

import mysql.connector

# open connection to Project 169
connection = mysql.connector.connect(user = "student",
                                     password = "aLQQLXGQp2rJ4Wy5",
                                     host = "173.246.108.142",
                                     database = "Project_169")

# create cursor object
cursor = connection.cursor()

# use cursor to execute query to retrieve TVShow names
cursor.execute("SELECT name FROM TVShow ORDER BY name ASC")

# store results in variable
TVShow_names = cursor.fetchall()

# execute queries to retrieve season numbers for each TV show
for name in TVShow_names:
    print name[0] + ":"

    cursor.execute("SELECT number FROM Season \
    JOIN TVShow ON Season.tvshow_id = TVShow.id \
    WHERE TVShow.name = '" + name[0] + "' ORDER BY number ASC")
    TVShow_seasons = cursor.fetchall()
    for season in TVShow_seasons:
        print "\tSeason " + str(season[0]) + ":"

# close the cursor object
cursor.close()

# close the connection
connection.close()
