"""
PasswordStrength
Instructions

Implement password_strength(password). 
Return Weak if the password has fewer than 8 characters. 
Return Medium if it has at least 8 characters 
but does not contain both letters and digits. 
Return Strong if it has at least 8 characters 
and contains at least one letter and at least one digit. 
Students may need to research isalpha and isdigit.
"""

def password_strength(password):
    if len(password) < 8:
        return "Weak"
    has_alpha = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    if not (has_alpha and has_digit):
        return "Medium"
    return "Strong"



