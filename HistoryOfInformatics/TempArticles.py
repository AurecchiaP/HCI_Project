import sqlite3
import re
import os

class TempArticles:
	
	def __init__(self,name):
		try:
			self.articlesConnect = sqlite3.connect(str(name))
			print("SQLITE3: Connected to " +str(name))
			basePath = os.path.dirname(os.path.realpath(__file__))
			os.system("cd \"" + basePath + "\";sqlite3 "+ str(name) +" < createNewDatabase.sql")
		except:
			print("SQLITE3: Could not connect to tempArticlesDB")
			
		

	def addArticle(self,categoryTable,title, body, externalLinks, date,linkToArticle):
		"""
		Add an article to the database
		"""
		cur = self.articlesConnect.cursor()

		self.__checkIfTableExists(categoryTable)

		try:
			commandToExecute = "INSERT INTO " + str(categoryTable) + " VALUES (NULL,?,?,?,?,?,?,?,?,?,?);"
			cur.execute(commandToExecute,(str(title),str(body),str(categoryTable),str(linkToArticle),"NONE","NONE","NONE","NONE",str(externalLinks),date))
			self.articlesConnect.commit()
			# print("Added successfully with ID " + str(cur.lastrowid))
			# self.__updateInternalList()
		except Exception as e:
		 	print("SQLITE3: CANNOT ADD ENTRY. ERROR {\n" + str(e) + "\n}")

	def addArticleWithConnections(self,categoryTable,title, body, externalLinks, date,linkToArticle,previousTitle,previousLink,nextTitle,nextArticle):
		"""
		Add an article to the database
		"""
		cur = self.articlesConnect.cursor()

		self.__checkIfTableExists(categoryTable)

		try:
			commandToExecute = "INSERT INTO " + str(categoryTable) + " VALUES (NULL,?,?,?,?,?,?,?,?,?,?);"
			cur.execute(commandToExecute,(str(title),str(body),str(categoryTable),str(linkToArticle),str(previousTitle),str(previousLink),str(nextTitle),str(nextTitle),str(externalLinks),date))
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

	def getListOfTables(self):
		cur = self.articlesConnect.cursor()
		try:
			tempTables = cur.execute("select name from sqlite_master where type = 'table';")
			tables = tempTables.fetchall()
			listToReturn = []
			for i in range(0,len(tables)):
				listToReturn.append(tables[i][0])
			return listToReturn
		except:
			print("Could not fetch tables in DB")

	def getEntriesAscending(self,category):
		cur = self.articlesConnect.cursor()
		try:
			tempTables = cur.execute("SELECT * FROM \"" + category + "\" ORDER BY date ASC")
			tables = tempTables.fetchall()
			listToReturn = []
			for i in range(0,len(tables)):
				listToReturn.append(tables[i])
			return listToReturn
		except:
			print("Could not fetch entries")
	
	def disconnect(self):
		self.articlesConnect.close()
































