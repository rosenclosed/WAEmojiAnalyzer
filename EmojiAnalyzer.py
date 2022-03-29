###########################################
##########WhatsApp-Emoji-Analyzer##########
###########################################
###########(c) 2022 William Reed###########
###########################################

#imports
#from asyncore import read
import os
import re

#intialize vars
chat_source = ""
chat_deleted_service_messages = ""
chat_deleted_own_messages = ""
chat_deleted_others_messages = ""
own_name = ""
others_name = ""
''' #define file path
chat_source_file_path = "./input/chat.txt"
#check if source-file is present
if os.path.isfile(chat_source_file_path):
    #open source-text-file in read mode
    chat_source_file = open(chat_source_file_path, "r", encoding="utf8")
    #read entire file to string
    chat_source = chat_source_file.read()
    #close file
    chat_source_file.close()
    #print the string
    print(chat_source) '''


def readfiletovar(sourcefilepath):
    print("Reading file: " + sourcefilepath + "\n\n\n")
    #check if source file is present
    if os.path.isfile(sourcefilepath):
        #open source file
        sourcefiledump = open(sourcefilepath, "r", encoding="utf8")
        #read file to string woth "targetvariable"
        var = sourcefiledump.read()
        #close file
        sourcefiledump.close()
        print("READING OF " + sourcefilepath + " SUCCESSFULL!\n\n\n\n\n")
        return var
    else:
        print("\n\nERROR: File Does Not Exist!\nExiting!\n\n")
        quit()


def writevartofile(targetfilepath, filecontent):
    print("Writing file: " + targetfilepath + "\n\n\n")
    #check if target file is already present and delete if needed
    if os.path.isfile(targetfilepath):
        print("Target file already exists. Deleting\n\n")
        os.remove(targetfilepath)
        print("DELETED!\n\n\n\n\n\n\n")
    #create targetfile
    file = open(targetfilepath, "x", encoding="utf8")
    #write to targetfile
    file.write(filecontent)
    #close file
    file.close()
    return True


print(
    "######################################\nWelcome to WAEmojiAnalyzer\nIf you haven't done so yet: follow the prerequisits explained on GitHub\n\nFirst I'll need some info:\n"
)
own_name = input("What is the name that represents you in the Chat-Logfile?\n")
print("\n\n")
others_name = input(
    "What is the that represents the other person in the Chat-Logfile? \n")

print("Your name is: " + own_name + ". And the others name is: " +
      others_name + ".")
print("\nI'm working now!")

chat_source = readfiletovar("./input/chat.txt")

#print(chat_source + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

writevartofile("./workingfiles/chat_source.txt", chat_source)


def deleteservicemessages(textsource):
    print("Deleting Service Messages from: " + textsource + "\n\n\n")
    #define Strings to purge
    to_purge = [
        '<Medien ausgeschlossen>',
        'Nachrichten und Anrufe sind Ende-zu-Ende-verschlüsselt. Niemand außerhalb dieses Chats kann sie lesen oder anhören, nicht einmal WhatsApp.',
        'Tippe, um mehr zu erfahren.'
    ]
    #checking if source file exists
    if os.path.isfile("./workingfiles/chat_source.txt"):
        #checking if target file exists and deleting and regenerating just to be sure....
        if os.path.isfile("./workingfiles/deleted_service_messages.txt"):
            print("Target file already exists. Deleting\n\n")
            os.remove("./workingfiles/deleted_service_messages.txt")
            print("DELETED!\n\n\n\n\n\n\n")
        else:
            print("\n\nERROR: File Does Not Exist!\nExiting!\n\n")
            quit()
    #creating the file again...
    file = open("./workingfiles/deleted_service_messages.txt",
                "x",
                encoding="utf8")
    file.close()
    #now doing the purging stuffs
    #opening the source and target files
    with open("./workingfiles/chat_source.txt",
              encoding="utf8") as unfilteredfile, open(
                  "./workingfiles/deleted_service_messages.txt",
                  "w",
                  encoding="utf8") as filteredfile:
        #checking every single line in the unfiltered file
        for line in unfilteredfile:
            #setting standard value to true
            clean = True
            #checking the selected line for words to purge
            for word in to_purge:
                #define what happens when word is found
                if word in line:
                    #if word is found set clean status to false
                    clean = False
            #only write line to the new file if the line is clean
            if clean == True:
                filteredfile.write(line)


deleteservicemessages("chat_source")
