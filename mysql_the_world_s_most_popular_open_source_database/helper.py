import mysql.connector as mysql

# global variables for querying database
cnx = mysql.connect(user='student',
                    password='aLQQLXGQp2rJ4Wy5',
                    host='173.246.108.142',
                    database='Project_169')

cursor = cnx.cursor()

table_attrs = { 'TVShows': ['id', 'name', 'poster'],
                'TVShow': ['id', 'name', 'poster', 'overview', 'Network.name', 'Genre.name']
                # 'Network': ['id', 'name'],
                # 'TVShowActor': ['tvshow_id', 'actor_id'],
                # 'Actor': ['id', 'name'],
                # 'TVShowGenre': ['tvshow_id', 'genre_id'],
                # 'Genre': ['id', 'name'],
                # 'Season': ['id', 'number', 'tvshow_id'],
                # 'Episode': ['id', 'name', 'number', 'overview', 'season_id']
                }

# helper methods defined here
def get_kvpair(cursor, id, table, attribute):
    query = ("SELECT " +  attribute + " FROM " + table + " WHERE id=" + str(id) + ";")
    cursor.execute(query)
    value = cursor.fetchall()[0][0]
    return (attribute, value)

def get_tvshows():
    # make a master list to contain the json struct
    mlist = []
    attr_list = table_attrs['TVShows']
    query = ("SELECT id from TVShow ORDER BY name;")
    cursor.execute(query)

    for record in cursor.fetchall():
        id = record[0]
        # run through attributes and create dict for record, using list mapping
        dict_list = []
        for attribute in attr_list:
            value = get_kvpair(cursor, id, 'TVShow', attribute)
            dict_list.append(value)
        rec_dict = dict(dict_list)
        mlist.append(rec_dict)

    cnx.close()
    return mlist
