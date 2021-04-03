#Here's the original code:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#Edit Code using F-string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Fstring in dictionaires
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Skill drill: print each county and registered voter from the dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

#Skill Drill: Print each county and registered voter from the dictionary. 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", 
"registered_voters": 432438}]
#If you use double quotation marks for the f-strings containing the keys, 
# then be sure to use single quotation marks for the keys and values of the dictionary.
for county, voters in voting_data.items():
    print(f"{county} county has {registered_voters} registered voters")
