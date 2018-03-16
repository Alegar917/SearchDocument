import pprint
from os import listdir
from os.path import isfile, join
mypath = "p3/docs/" # path to the folder that contains all the text files
allfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
dic={}
line=" "
newFile=open("dictionary-summary.txt","w")# A txt file of a list of all the locations for each word
searchFile=open("searchResults.txt","w")# returns either a list of all the locations of the search word or returns doesnt exist
for file in allfiles:
	if file!=".DS_Store":
		textFile=open(mypath+file,"r",encoding='utf8')

		while line!="":
			line=textFile.readline()
				
			split=line.split()

			for word in split:
				word=word.lower()	
				if word in dic:
					newContact=dic[word]
					newContact.append(line)
					dic[word]=newContact
				else:
					dic[word]=[line]
				if len(word)>6:
					newFile.write(word+":"+ str(dic[word])+"\n")

				
user=input("What Keyword are you searching for: ")
user=user.lower()	
if user in dic:
	searchFile.write(user+":"+str(dic[user])+"\n")
else:
	searchFile.write("This Keyword doesnt exist in the dictionary")
			
print("Done!")
newFile.close()
textFile.close()
searchFile.close()
