import pprint
a=open("Alice.txt","r")# the text file which is read
line=" "
dic={}

while line!="":
	line=a.readline()
	split=line.split()
	
	for word in split:
		
		if word in dic:
			freq=dic[word]
			freq=freq+1
			dic[word]=freq
		else:
			dic[word]=1
	
pprint.pprint(dic)



s=input("What word your looking for? ")

if s in dic:
	print("This word shows up in the file",dic[s],"times")
if s not in dic:
	print("Not in the file")

a.close()
