import psycopg2

from DataFetcher import DataFetcher
from DatabaseConnection import DatabaseConnection
from User import User
from PlayerDAO import PlayerDAO
class Admin(User):
    def __init__(self, gamertag, name, forename, password):
        super().__init__(gamertag, name, forename, password)
        self.conn = DatabaseConnection().connect()
        self.cur = self.conn.cursor()

    def updateAll(self):
        fetcher = DataFetcher()
        fetcher.fetchCircuits()
        fetcher.fetchDrivers()
        fetcher.fetchRace()
        fetcher.fetchRaceresults()

    def deletePlayer(self, gamertag):
        p = PlayerDAO()
        try:
            p.delete(gamertag)
            print("Erfolgreich")
        except :
            print("Fehlgeschlagen")
        """""
        self.cur.execute("SELECT player_id FROM Player WHERE gamertag = %s", (gamertag,))
        playerID = self.cur.fetchone()
        self.cur.execute("DELETE FROM bet WHERE player_id = %s", (playerID,))
        self.cur.execute("DELETE FROM PLAYER WHERE player_id = %s", (playerID,))
        self.conn.commit()"""






