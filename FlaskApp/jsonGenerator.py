import os
from bs4 import BeautifulSoup
import json
import sqlite3

import TempArticles 

basePath = os.path.dirname(os.path.realpath(__file__))
pathToCore = basePath.rsplit("/",1)[0]
pathToHTML = pathToCore + "/OldHtml"

sectionFolders = os.popen("cd " + pathToHTML + ";ls -1").read().split("\n")[:-1]

os.system("")


tA = TempArticles.TempArticles()


for section in range(0,len(sectionFolders)):
	filesInFoldersTemp = [os.path.join(dp, f) for dp, dn, filenames in os.walk(pathToHTML + "/" + sectionFolders[section]) for f in filenames if os.path.splitext(f)[1] == '.html']

	
	filesInFolders = []
	
	for i in range(0,len(filesInFoldersTemp)):
		if ".html" in filesInFoldersTemp[i] and "milestone" not in filesInFoldersTemp[i]:
			filesInFolders.append(str(filesInFoldersTemp[i]))

	for file in filesInFolders:
		# TODO: Find a way to include the data
		articleDate = "PLACEHOLDER"
		
		with open(file, "r") as in_file:
			text = in_file.read()
		rawArticleData = BeautifulSoup(text)
		
		mainBody = rawArticleData.find("div", attrs={"id":"contentContainer","class":"clearfix"})
		
		if mainBody == None:
			#input(file)
			break
		
		# Actual content of the HTML. TODO: Exclude the external links
		mainContent = mainBody.find("div",attrs={"id":"content"})
		# Actual article title
		articleTitle = rawArticleData.find("title").get_text()
		
		
		
		
		externalLinksTemp = mainBody.find("div",attrs={"class":"externalLinks"})
		if externalLinksTemp == None:
			externalLinks = "None"
			print("No external links")
		else:
			externalLinks = externalLinksTemp.find("ol")
			if externalLinks == None:
				externalLinks = "None"
		
		linkToArticle = file.rsplit("/",1)[1]
		tA.addArticle(sectionFolders[section], articleTitle, mainContent, externalLinks, articleDate,linkToArticle)
		
tA.disconnect()	
			
			