import mysql.connector as mysql

# global variables for querying database
cnx = mysql.connect(user='student',
                    password='aLQQLXGQp2rJ4Wy5',
                    host='173.246.108.142',
                    database='Project_169')

cursor = cnx.cursor()

table_attrs = { 'TVShows': ['id', 'name', 'poster'],
                'TVShow': ['TVShow.id', 'TVShow.name', 'poster', 'overview', 'Network.name', 'Genre.name'],
                'Actors': ['Actor.id', 'Actor.name']
                # 'TVShowGenre': ['tvshow_id', 'genre_id'],
                # 'Genre': ['id', 'name'],
                # 'Season': ['id', 'number', 'tvshow_id'],
                # 'Episode': ['id', 'name', 'number', 'overview', 'season_id']
                }

# helper methods defined here
def get_kvpair(query_for_attribute, attribute):
    # query = ("SELECT " +  attribute + " FROM " + table + " WHERE id=" + str(id) + ";")
    cursor.execute(query_for_attribute)
    value = cursor.fetchall()[0][0]
    return (attribute, value)


def create_mlist(query, attributes):
    # make a master list to contain the json-like struct
    mlist = []
    cursor.execute(query)

    for record in cursor.fetchall():
    # create dict for record with specified attributes
        keyvalue_list = [(attributes[i], record[i]) for i in range(len(attributes))]
        record_dict = dict(keyvalue_list)
        mlist.append(record_dict)

    cnx.close()
    return mlist

def get_attr_values(attr_list):
    return str(tuple(attr_list)).strip("()").replace("'","")

def get_tvshows():
    attr_list = table_attrs['TVShows']
    attr_values = get_attr_values(attr_list)
    query = ("SELECT " + attr_values + " from TVShow ORDER BY name;")
    return create_mlist(query, attr_list)

def get_tvshow_detail(tvshow_id):
    attr_list = table_attrs['TVShow']
    attr_values = get_attr_values(attr_list)
    query = (
                "SELECT " + attr_values + " from TVShow \
                JOIN TVShowGenre ON TVShow.id = TVShowGenre.tvshow_id \
                JOIN Genre ON TVShowGenre.genre_id = Genre.id \
                JOIN Network ON TVShow.network_id = Network.id \
                WHERE TVShow.id=" + str(tvshow_id) + ";"
            )
    return create_mlist(query, attr_list)

def get_actors(tvshow_id):
    attr_list = table_attrs['Actors']
    attr_values = get_attr_values(attr_list)
    query = (
                "SELECT " + attr_values + " from TVShow \
                JOIN TVShowActor ON TVShow.id = TVShowActor.tvshow_id \
                JOIN Actor ON TVShowActor.actor_id = Actor.id \
                WHERE TVShow.id=" + str(tvshow_id) + " \
                ORDER BY Actor.name;"
            )
    return create_mlist(query, attr_list)
