#Write a program to read through the mbox-short.txt and
# figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.




name = input("Enter the filename:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name) #opens the file
text = handle.read() #reads the file


senders = dict() #creates a dictionary
for line in handle: #each line through the dictionary
    if not line.startswith("From:"):continue #continue if line doesnt start with the word 'from'
    line = line.split() #split each line
    line = line[1]
    senders[line] = senders.get(line, 0) +1 #increment if names are repeated

bigcount = None
bigword = None
for word,sender in senders.items():
    if bigcount == None or sender > bigcount: #condition
        bigword = word
        bigcount = sender

print(bigword, bigcount)
