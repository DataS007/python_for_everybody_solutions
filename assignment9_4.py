#Assignment 9.4:
"""
9.4 Write a program to read through the mbox-short.txt and figure out who 
has sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary 
is produced, the program reads through the dictionary using a maximum loop to find 
the most prolific committer.
"""

fname = input("Enter the name of the file: ")
fhand = open(fname)
dict = dict()
list1 = list()
for line in fhand:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            word = line.split()
            list1.append(word[1])
for word in list1:
    dict[word] = dict.get(word,0) + 1
HE = None
HCE = None
for emailid, senttimes in dict.items():
    if HE is None or senttimes > HE:
        HCE = word
        HE = senttimes
print(HCE, HE)
