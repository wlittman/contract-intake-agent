
# Store the deal details in variables: labeled boxes, each holding one value.
party = "Fernway Inc."
term_years = 3
governing_law = "New York"

# Print a sentence built from the variables.
# The f before the quotation mark makes this an f-string:
# each name in curly braces is replaced with that variable's value.
print(f"{party} signed a {term_years}-year NDA governed by {governing_law} law ")
