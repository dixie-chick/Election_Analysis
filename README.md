# Election_Analysis
Using Python to analyze election data

# Overview:
In this project, a Python script delivers an Election Audit across three candidates and three counties to include:

- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Process & Data
1. A raw CSV file was imported including ballot ID, county, and candidate name
2. Data was structured into Lists and Dictionaires
3. Decision statements (if), repetetion statements (for), and printing formats (f'{}) were structured to use correct syntax and spacing which would result in total votes, winning candidate, winning county, and winning percentages.
4. A text file was created to summarize election findings

### Be Careful!
*Spacing, Spacing, Spacing! When using Python, correct syntax and spacing is critical. Upon first run, incorrect results delivered due to an error in spacing and a code not aligned within another statement:

![Spacing_Challenges](https://user-images.githubusercontent.com/79612565/113482141-17a74780-9452-11eb-977e-46456379a84f.png)

*Psuedocode-Can't live with it, Can't live without it! Allocating correct variables with such a long code and many variables can be tricky, especially when tallying similiarites, in this example, votes. Although longer in process, adding in psuedocode refreshes the memory of why certain code was created

![Variables_Challenges](https://user-images.githubusercontent.com/79612565/113482252-99977080-9452-11eb-8fd5-115b62798409.png)


## And the Winner Is...

County: Across a total vote cast of 369,711, Denver had the largest turnout with 82.8% or 306,055 total votes.
      Next in line is Jefferson County with 10.5% of total votes (38,855).
      Followed by Arapahoe with 6.7% (24,801) votes.
      
Candidate: Across a total vote cast of 369,711, Diana DeGette won with a landslide of 272,892 votes or a whopping 73.8%! Well done Diana!
      Next in line is Charles Casper Stockham with 85,213 votes or 23%
      Raymon Anthony Doane picking up the rear at 11,606 votes or a mere 3.1%
      
![Election_Results](https://user-images.githubusercontent.com/79612565/113482483-cc8e3400-9453-11eb-9d88-87a2838908e2.png)

## To Wrap it Up

3. Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
