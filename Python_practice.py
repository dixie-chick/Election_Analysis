print("Hello World")

#Create a list of dictionaries where keys are county and registere_voters
#voting_data[]

#Practice if
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Create a membership operation, determin if "el Paso" is in the counties list
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")   


# #Decision statments
# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#Repetition and loops
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

#Iterate through Dict
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#all counties print
for county in counties_dict:
    print(county)

#Print Keys
for county in counties_dict.keys():
    print(county)

#Print Values
for voters in counties_dict.values():
    print(voters)

#Skill Drill 
for county, voters in counties_dict.items():
    print(county + "county has" +str(voters) + "registered voters.")

#Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#get values from list of dicts
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Retrieve registered voters
for county_dict in voting_data:
    print(county_dict["registered_voters"])

#retreive county name in voting_data
for county_dict in voting_data:
    print(county_dict['county'])

