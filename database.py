import mysql.connector
import functions

#Songsuche
def search_song(song_wahl):
    config = {
        "user": "root",
        "password": "****",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name FROM musikplayer.lieder WHERE name LIKE '%"+ song_wahl +"%';")
    name = mycursor.fetchone()

    name = name[0].strip()

    mycursor.close()
    mydb.close()

    return name


#Playlist erstellen
def create_table(table_name):
    
    functions.clear_console()

    config = {
        "user": "root",
        "password": "****",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()
    
    mycursor.execute("CREATE TABLE musikplayer."+ table_name +"(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), interpreter VARCHAR(100));")
    #sichern
    mydb.commit()
    print("Die Playlist "+ table_name +" wurde erstellt.")

    mycursor.close
    mydb.close()

#Playlist löschen
def delete_table(table_name):
    
    functions.clear_console()

    config = {
        "user": "root",
        "password": "****",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()
    
    mycursor.execute("DROP TABLE musikplayer."+ table_name +";")
    #sichern
    mydb.commit()
    print("Die Playlist "+ table_name +" wurde gelöscht.")

    mycursor.close
    mydb.close()

#Playlist anzeigen
def show_table(table_name):
    config = {
        "user": "root",
        "password": "****",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name, interpreter FROM musikplayer."+ table_name +";")
    zeilen = mycursor.fetchall()

    functions.clear_console()

    print(table_name +":\n")
    for zeile in zeilen:
        name = zeile[0].strip()
        interpreter = zeile[1].strip()
        print("-"+ name +":", interpreter)
    print("\n")

    mycursor.close
    mydb.close()

#Lied hinzufügen
def add_song(table_name):
    functions.clear_console()
    config = {
        "user": "root",
        "password": "****",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    #song anfragen
    song_name = input("Welches Lied wollen Sie zu dieser Playlist hinzufügen? ")
    #song name mglweise korrigieren
    song_name = search_song(song_name)

    functions.clear_console()

    #interpreten holen
    mycursor.execute("SELECT name, interpreter FROM musikplayer.lieder WHERE name = '"+ song_name +"';")
    newsong = mycursor.fetchone()

    mycursor.execute(f"INSERT INTO musikplayer.{table_name} (name, interpreter) VALUES {newsong};")
    #speichern der operation
    mydb.commit()

    print("Das Lied "+ song_name +" wurde zur Playlist "+ table_name +" hinzugefügt.")
    mycursor.close
    mydb.close()

#Lied entfernen
def remove_song(table_name):
    functions.clear_console()
    config = {
        "user": "root",
        "password": "****",
        "host": "localhost",
        "database": "MySQL"
    }
    # Establish the connection
    mydb = mysql.connector.connect(**config)

    #interactionsmglkeit mit DB
    mycursor = mydb.cursor()

    #song anfragen
    song_name = input("Welches Lied wollen Sie aus dieser Playlist löschen? ")
    #song name mglweise korrigieren
    song_name = search_song(song_name)

    functions.clear_console()

    #id holen wegen safe update mode nur durch id löschbar
    mycursor.execute(f"SELECT id FROM musikplayer.{table_name} WHERE name = '{song_name}';")
    del_id = int(mycursor.fetchone())
    newdel_id = int(del_id[0])
    mycursor.execute(f"DELETE FROM musikplayer.{table_name} WHERE id = {newdel_id};")
    #speichern der operation
    mydb.commit()

    print("Das Lied "+ song_name +" wurde aus der Playlist "+ table_name +" entfernt.")
    mycursor.close
    mydb.close()
    
