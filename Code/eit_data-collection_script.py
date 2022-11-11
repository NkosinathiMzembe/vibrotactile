## Program that handles data collection for CSE 598:EIT assignment-A2 ##
#traceback: eit_test_script-4.py#
########################################################################

import time
import serial
from itertools import product/microsoft/pylance-release/blob/main/DIAGNOSTIC_SEVERITY_RULES.md
import random
import csv

#Arduino comms-- imp: check comport!
#arduinoData=serial.Serial('com9',115200)
arduinoData=serial.Serial('/dev/cu.usbserial-10',115200)

time.sleep(1)

#Experimental Parameters
DVals=[150,250] #this is a list
SOAVals=[300,250,200,150,100,50,0]

#Function Definitions
def manualMode():
    myInput=input("Enter input as 'D''S' in sequence: ")

    sendDuration=DVals[int(myInput[0])-1]
    sendSOA=SOAVals[int(myInput[1])-1]

    myCmd=str(sendDuration)+','+str(sendSOA)+'\r'
    arduinoData.write(myCmd.encode())
    time.sleep(1)

def automatedMode():
    vibeList=list(product(DVals,SOAVals)) #Generating dataset of stimuli
    vibeList_randomized=random.sample(vibeList,len(vibeList)) #Randomizing stimuli presentation

    print("----Subject trial begins----")
    time.sleep(2)

    #Convert each element of vibeList into string and then send to arduino

    delimiter=","
    count=1
    trialResponseList=[]

    for item in vibeList_randomized:
        cmd=delimiter.join([str(element) for element in item]) #converting tuple to string
        myCmd=cmd+'\r'
        arduinoData.write(myCmd.encode()) 
        time.sleep(1)
        print("* Stimuli "+str(count)+" presented")

        #Use likert scale to record user ratings
        userRating=input("  Enter subject rating 1 (discrete) to 7 (continuous): ")
        userResponse=cmd+','+userRating

        trialResponseList.append(userResponse)

        time.sleep(1)
        input("  [Press enter to continue]  ") 
        time.sleep(1)
        count+=1

    print("----Subject trial complete----")

    return trialResponseList

def saveResponse(responseList):
    #ask info
    subjectID=input("Enter subject ID: ")
    subjectTrialNumber=input("Enter trial number: ")
    filename="subject-"+subjectID+"_trial-"+subjectTrialNumber+".csv"

    #save info
    with open(filename,'w+',newline='') as saveFile:
        s=csv.writer(saveFile)
        for row in responseList:
            s.writerow(row.split(','))
    
    print("  [THIS TRIAL HAS BEEN SAVED AS CSV FILE]  ")


##### MAIN #####
askMode=input("What mode do you want? 1:manual 2:automated: ")

if askMode == "1":
    print("^^^^You have entered manual mode^^^^")
    while True:
        manualMode()

elif askMode== "2":
    print("^^^^You have now entered automated mode ^^^^")
    time.sleep(1)
    responseList= automatedMode()
    saveResponse(responseList)





