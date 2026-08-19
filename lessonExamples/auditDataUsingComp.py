"""
USING COMPREHENSIONS TO FILTER AND SELECT DATA
You are given records(see in code👇) from an AI training dataset. 
Each record is a dictionary containing a user's name 
and the categories of data associated with that user:

Your job is to build a dataset audit report.
Implement:

def audit_dataset(records):
    ...

It must return a dictionary with the following structure:
{
    "users": [...],
    "unique_categories": {...},
    "category_counts": {...},
    "user_category_count": {...},
    "classification": {...}
}

Requirement 1 — users
Create a list comprehension containing the names of all users 
whose category list contains "python".
Expected:
["Ada", "James", "Micah", "Sarah", "David"]
Do not manually build this list with .append().

Requirement 2 — unique_categories
Create a set comprehension containing every 
unique category appearing anywhere in the dataset.
For the given data, the result should be equivalent to:
{
    "math",
    "python",
    "ai",
    "web",
    "javascript",
    "data",
    "ml"
}
You will need to think about a nested comprehension here 
because the categories are nested inside each user's record.

Requirement 3 — category_counts
Create a dictionary comprehension mapping each 
unique category to the number of users who have 
that category.
Important detail:
A category counts once per user, even if it appears 
multiple times in that user's list.

For example, Ada has:
["math", "python", "ai", "python"]
Ada has Python twice, but Ada contributes only one to the Python user count.
Therefore, for the given dataset:
{
    "math": 2,
    "python": 5,
    "ai": 2,
    "web": 2,
    "javascript": 2,
    "data": 2,
    "ml": 1
}
You will probably need a set somewhere inside the 
logic to eliminate duplicates per user.

Requirement 4 — user_category_count
Create a dictionary comprehension mapping 
each user to the number of unique categories they have.
For example:
{
    "Ada": 3,
    "James": 3,
    "Micah": 3,
    "Sarah": 4,
    "David": 3
}
Notice that Ada has four entries but 
only three unique categories:
["math", "python", "ai", "python"]

Requirement 5 — classification
Create another dictionary comprehension that classifies 
each user based on the number of unique categories:

4 or more → "Broad"
2–3       → "Focused"
1         → "Narrow"

For the given data:
{
    "Ada": "Focused",
    "James": "Focused",
    "Micah": "Focused",
    "Sarah": "Broad",
    "David": "Focused"
}
This is specifically intended to make you use the 
conditional-expression form of a comprehension:
[value_if_true if condition else value_if_false for ...]
You will actually need to distinguish between a filtering if 
and an if/elif/else-style value-selection expression.

Try to solve the entire problem using 
comprehensions and normal dictionary/set operations.

You may use:
set()
len()
sum()
and dictionary/set methods.

This may come in handy in selecting for reqirement 3:
set(record["categories"])

Avoid:
for ...:
and .append()
"""

records = [
    {
        "name": "Ada",
        "categories": ["math", "python", "ai", "python"]
    },
    {
        "name": "James",
        "categories": ["python", "web", "javascript"]
    },
    {
        "name": "Micah",
        "categories": ["ai", "python", "data", "ai"]
    },
    {
        "name": "Sarah",
        "categories": ["math", "data", "python", "ml"]
    },
    {
        "name": "David",
        "categories": ["web", "javascript", "python", "web"]
    }
]

def audit_dataset(records):
    users = [record["name"] for record in records if "python" in record["categories"]]

    unique_categories = {category for record in records for category in record["categories"]}

    category_counts = {category: sum(1 for record in records if category in record["categories"]) for category in unique_categories}
    #The generator contributes 1 for each user whose category list contains the category, and sum() adds those contributions

    # #loop equivalent for category_counts
    # category_counts = {}
    # for cat in unique_categories:
    #     count = 0
    #     for record in records:
    #         if cat in record["categories"]:
    #             count += 1
    #     category_counts[cat] = count

    user_category_count = {record["name"]: sum(1 for category in unique_categories if category in record["categories"]) for record in records}
    #OR
    user_category_count = {
        record["name"]: len(set(record["categories"]))
        for record in records
    }

    classification = {user: ("Broad"if cat_count >= 4 else  "Focused" if cat_count>=2 else "Narrow")  for user, cat_count in user_category_count.items()}

    return {
        "users": users,
        "unique_categories": unique_categories,
        "category_counts": category_counts,
        "user_category_count": user_category_count,
        "classification": classification
    }

print(audit_dataset(records))
