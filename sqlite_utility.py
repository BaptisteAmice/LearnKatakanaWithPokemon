import sqlite3

def connect_to_database():
    conn = sqlite3.connect('pokemon_game.db')
    print("Opened database successfully")
    return conn

def create_database():
    conn = connect_to_database()
    print("Opened database successfully")

    conn.execute('''CREATE TABLE PLAYERS
          (id           VARCHAR(30)     PRIMARY KEY NOT NULL,
           name         VARCHAR(30)     NOT NULL,
           sc_romaji    INT             DEFAULT     0,
           sc_trad      INT             DEFAULT     0);''')
    print("Table created successfully")
    conn.close()

def delete_database():
    conn = connect_to_database()
    conn.execute("DROP TABLE PLAYERS")
    conn.close()

#insert a player in the database, if the player already exists, do nothing
def add_player(id, name):
    conn = connect_to_database()
    conn.execute("INSERT OR IGNORE INTO PLAYERS (id, name) VALUES (?, ?)", (id, name,))
    conn.commit()
    conn.close()

def get_player(id):
    conn = connect_to_database()
    cursor = conn.execute("SELECT * FROM PLAYERS WHERE id = ?", (id,))
    player = cursor.fetchone()
    conn.close()
    return player


def increment_player_sc_romaji(id, amount):
    conn = connect_to_database()
    #get the current score and add the amount
    conn.execute("UPDATE PLAYERS SET sc_romaji = sc_romaji + ? WHERE id = ?", (amount, id,))
    conn.commit()
    conn.close()


def increment_player_sc_trad(id, amount):
    conn = connect_to_database()
    conn.execute("UPDATE PLAYERS SET sc_trad = sc_trad + ? WHERE id = ?", (amount, id,))
    conn.commit()
    conn.close()

#return a list of tuples (id, sc_romaji, sc_trad, total)
def get_leaderboard():
    conn = connect_to_database()
    cursor = conn.execute("SELECT name, sc_romaji, sc_trad, sc_romaji + sc_trad AS total FROM PLAYERS ORDER BY total DESC")
    ranking = cursor.fetchall()
    conn.close()
    return ranking
