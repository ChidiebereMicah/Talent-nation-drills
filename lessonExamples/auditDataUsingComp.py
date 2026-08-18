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

#length = len(records)
users = [dict["name"] for dict in records if "python" in dict["categories"]]
print(users)

unique_categories = {category for dict in records for category in dict["categories"]}
print(unique_categories)

category_counts = {category: sum(1 for dict in records if category in dict["categories"]) for category in unique_categories}
print(category_counts)
#the for loop in sum increaments by 1 everytime category is found for any user

#loop equivalent for category_counts
category_counts = {}
for cat in unique_categories:
    count = 0
    for dict in records:
        if cat in dict["categories"]:
            count += 1
    category_counts[cat] = count
print(category_counts)

user_category_count = {dict["name"]: sum(1 for category in unique_categories if category in dict["categories"]) for dict in records}
print(user_category_count)

classification = {}