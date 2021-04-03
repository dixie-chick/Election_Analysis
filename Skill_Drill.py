#3.2.4 Perform Calculation 
    #Part 1
# print(5+2*3)
# print(8//5-3)
# print(8+22*2-4)
# print(16-3/2+7-1)
# print(3**3%5)
# print(5+9*3/2-4)
    # Part 2

#print((5+2)*3)
#print((8//5)-3)
#print(8+(22*(2-4)))
#print(16-3/(2+7)-1)
#print(3**(3%5))
#print(5+(9*3/2-4))
#print(5+(9*3/(2-3)))

#3.2.5 Data Structures
#counties = ["Arapahoe", "Denver", "Jefferson"]
#print(counties)
#print(counties[0:2])
#print(counties[-1])
#print(counties[-2])
#len(counties)
#counties.append("El Paso")
#print(counties)
#counties.insert(2,"El Paso")
#print(counties)
#counties.pop(0)
#print(counties)
#counties.insert(3,"Denver")
#print(counties)
#counties.append("Arapahoe")
#print(counties)

#3.2.6 Data Structures: Tuples
#counties_tuple = ("Arapahoe","Denver","Jefferson")
#print(counties_tuple)
#print(counties_tuple[1])

#3.2.7 Dictionaries

#3.2.8 Decision Statements
# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#counties =["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
  #  print(counties[1])

#if counties[3] != 'Jefferson'
  #  print(counties[2])
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", 
"registered_voters": 432438}]

for county, registered_voters in voting_data.items():
    print(f"{county} county has {registered_voters} registered voters")
