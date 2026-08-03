"""
InitialsBadge
Instructions

Implement initials_badge(full_name). 
Remove leading and trailing spaces, split the name into words, 
take the first character of each word, convert each initial to uppercase, 
and return the initials joined with dots. 
The returned badge should end with a dot.
"""
def initials_badge(full_name):
    full_name = full_name.strip().split()
    initials = []
    for n in full_name:
        initials.append(n[0].upper())
        #print(n)
    return f"{".".join(initials)}."

print(initials_badge("Ada Lovelace"))