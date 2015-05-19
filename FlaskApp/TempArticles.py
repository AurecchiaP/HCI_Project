import sqlite3
import re

class TempArticles:
	
	def __init__(self):
		try:
			self.articlesConnect = sqlite3.connect('tempArticlesDB.db')
			print("SQLITE3: Connected to tempArticlesDB")
			
			cur = self.articlesConnect.cursor()
			
			cur.executescript("""DELETE FROM games;
			DELETE FROM hardware;
			DELETE FROM hci;
			DELETE FROM internet;	
			DELETE FROM software;""")
			
			
		except:
			print("SQLITE3: Could not connect to tempArticlesDB")

	def addArticle(self,categoryTable,title, body, externalLinks, date,linkToArticle):
		"""
		Add an article to the database
		"""
		cur = self.articlesConnect.cursor()

		self.__checkIfTableExists(categoryTable)

		try:
			commandToExecute = "INSERT INTO " + str(categoryTable) + " VALUES (NULL,?,?,?,?,?);"
			cur.execute(commandToExecute,(str(title),str(body),str(externalLinks),str(date),str(linkToArticle)))
			self.articlesConnect.commit()
			# print("Added successfully with ID " + str(cur.lastrowid))
			# self.__updateInternalList()
		except Exception as e:
		 	print("SQLITE3: CANNOT ADD ENTRY. ERROR {\n" + str(e) + "\n}")

	def __checkIfTableExists(self,categoryTable):
		cur = self.articlesConnect.cursor()
		tableExists = cur.execute("SELECT count(*) FROM sqlite_master WHERE type = \"table\" AND name = \"" + str(categoryTable) +"\"").fetchall()[0][0] > 0

		if not tableExists:
			print("Need to create new table")
			return False
		return True

	
	def disconnect(self):
		self.articlesConnect.close()