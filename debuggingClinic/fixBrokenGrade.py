def grade_label(score):
    # Bug to fix: branch order and boundary checks must be correct.

    match score:
        case x  if 90<=x<=100:
            return("A")
        case x  if 80<=x<=89:
            return("B")
        case x  if 70<=x<=79:
            return("C")
        case x  if 0<=x<70:
            return("F")
        case _:
            return("Invalid score")  # Default fallback

#Better version
def grade_label(score):
    # Bug to fiscore: branch order and boundary checks must be correct.
    if score < 0 or score > 100:
        return "Invalid score"

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"