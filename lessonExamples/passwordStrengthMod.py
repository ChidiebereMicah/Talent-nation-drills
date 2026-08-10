def password_strength_mod(password):
    if len(password) < 8:
        return "Weak"
    has_alpha = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    if not (has_alpha and has_digit):
        return "Medium"
    return "Strong"

    