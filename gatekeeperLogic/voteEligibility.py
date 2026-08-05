"""
Instructions
Implement vote_eligibility(age, country). 
Return Eligible if age is at least 18 and country is Nigeria. 
Otherwise return Not eligible. 
The country check should be case-insensitive and should ignore leading and trailing spaces.
"""

def vote_eligibility(age, country):
    if age >= 18 and country.strip().lower() == "nigeria":
        return "Eligible"
    return "Not eligible"
