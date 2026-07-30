def clean_username(value):
    username = value.strip()
    username = username.replace(" ", "_")
    username = username.lower()
    username2 = value.strip().replace(" ", "_").lower()
    return username, username2

print(clean_username("  I love apples  "))