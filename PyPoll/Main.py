#import os  and csv to be able to read csv files
import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # number of votes in the csv
    csv_header = next(csvreader)
    Candidate = []
    
    for row in csvreader:
        Candidate.append(str(row[2]))
    listdata = list(csvreader)
    votelen = len(Candidate)
    #print("Total Votes: " + str(votelen))

    uniquenames = []

    for i in Candidate:
        if i not in uniquenames:
            uniquenames.append(i)
    #print(uniquenames)

    CandidateName1 = Candidate.count("Khan")
    CandidateName2 = Candidate.count("Correy")
    CandidateName3 = Candidate.count("Li")
    CandidateName4 = Candidate.count("O'Tooley")
    #print(CandidateName1)
    #print(CandidateName2)
    #print(CandidateName3)
    #print(CandidateName4)

    Khanpercent = round(((float(CandidateName1) / votelen) * 100))
    Correypercent = round((float(CandidateName2) / votelen) * 100)
    Lipercent = round((float(CandidateName3) / votelen) * 100)
    Otolleypercent = round((float(CandidateName4) / votelen) * 100)
    #print(Khanpercent)
    #print(Correypercent)
    #print(Lipercent)
    #print(Otolleypercent)
    print("Election Results"+ "\n" + 
    "----------------------" + "\n" + ("Total Votes: " + str(votelen))+ 
    "\n" + "----------------------"+ " \n" + "Khan: " + 
    str(Khanpercent) + "%" + " (" + str(CandidateName1) + ")"+"\n"+ "Correy: " + 
    str(Correypercent) + "%" + " (" + str(CandidateName2) + ")" "\n"+ "Li: " + 
    str(Lipercent) + "%" + " (" + str(CandidateName3) + ")""\n"+ "O'Tooley: " + 
    str(Otolleypercent) + "%" + " (" + str(CandidateName4) + ")" + "\n" +
    "---------------------" + "\n" + "Winner: " + "Khan" + "\n" + 
    "----------------------")

    #print to text file
    outputfile = open("PyPoll_Analysis.txt", "w")
    outputfile.write("Election Results"+ "\n" + 
    "----------------------" + "\n" + ("Total Votes: " + str(votelen))+ 
    "\n" + "----------------------"+ " \n" + "Khan: " + 
    str(Khanpercent) + "%" + " (" + str(CandidateName1) + ")"+"\n"+ "Correy: " + 
    str(Correypercent) + "%" + " (" + str(CandidateName2) + ")" "\n"+ "Li: " + 
    str(Lipercent) + "%" + " (" + str(CandidateName3) + ")""\n"+ "O'Tooley: " + 
    str(Otolleypercent) + "%" + " (" + str(CandidateName4) + ")" + "\n" +
    "---------------------" + "\n" + "Winner: " + "Khan" + "\n" + 
    "----------------------")
    outputfile.close()





    