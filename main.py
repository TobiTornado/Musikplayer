#requirement: modul pygame installieren (befehl:pip install pygame[enter])
#             modul mysql-connector-python installieren (befehl:pip install mysql-connector-python[enter]) WICHTIG: nicht mysql-connector

import pygame
import os
import mysql.connector
import functions
import database

functions.clear_console()

while True:
    #Hauptmenü
    aktionswahl = int(input("Wollen Sie Musikhören(1), nach Musik stöbern(2), eine Playlist erstellen/entfernen(3), eine vorhandene Playlist bearbeiten(4) oder das Programm beenden(5)? "))

    match aktionswahl:
        case 1:
            #Musikhören
            functions.play_music()
        case 2:
            #Musik stöbern
            pass
        case 3:
            #Playlist erstellen/löschen
            aktion = input("Wollen Sie eine Playlist erstellen, oder löschen? ")

            match aktion:
                case "erstellen":
                    table_name = input("Wie soll Ihre neue Playlist heißen? ")
                    database.create_table(table_name)
                case "löschen":
                    table_name = input("Welche Playlits wollen Sie löschen? ")
                    database.delete_table(table_name)
                case other:
                    print("Ihre Anfrage konnte leider nicht verarbeitet werden")
                    break
        case 4:
            #Playlistbearbeiten
            
            #welche tabelle
            table_name = input("Welche Playlist wollen Sie bearbeiten? ")
            
            #zu bearbeitende playlist anzeigen
            database.show_table(table_name)
            
            #löschen hinzufügen
            aktion = input("Wollen Sie ein Lied löschen oder hinzufügen? ")
            
            match aktion:
                case "hinzufügen":
                    database.add_song(table_name)
                case "löschen":
                    database.remove_song(table_name)
                case other:
                    print("Ihre Anfrage konnte leider nicht verarbeitet werden")
                    break
        case 5:
            print("Das Programm wird beendet...")
            break
        case other:
            print("Ihre Anfrage konnte leider nicht verarbeitet werden")
