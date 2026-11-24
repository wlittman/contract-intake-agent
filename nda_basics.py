# -------- Part A: read the NDA and count its words -------

# Open the NDA text file and call it an "f" while it is open.
with open("samples/falcon_nda.txt") as f:
    # Read all the text in the file and store it in a variable called nda_text
    nda_text = f.read()

# Break the text into separate words, wherever there is a space,
# and store that list of words in a variable called words.
words = nda_text.split()

# Count the items in the list with len() and print the result.
print("The NDA has", len(words), "words.")

# ---------- Part B: check for key terms ----------

# A list of five strings (pieces of text) to look for.

terms = ["confidential", "residuals", "non-solicit", "governing law", "return or destroy"]

# A loop: take each item in terms, one at a time, call it "term", 
# and run the indented lines below for it. This runs five times.
for term in terms:
        # Make a lowercase copy of the NDA, then check whether the term appears in it.
    if term in nda_text.lower():
        print(term, "- found")
    else:
        print(term, "- not found")

# ---------- Part C: keep the results in a dictionary ----------

# Create an empty dictionary (curly braces) to hold the results.

results = {}

# Loop through the terms again.
for term in terms:
    # Add an entry: the term is the label, and the value is
    # True or False, depending on whether the term appears in the NDA.
    results[term] = term in nda_text.lower()

print(results)

# ---------- Part D: package the check as a reusable function ----------

# Define a function called check_terms with two inputs:
# the text to search, and the list of terms to look for.

def check_terms(text, terms_to_find):
    found ={}
    for term in terms_to_find:
        found[term] = term in text.lower()
    return found

# Use the function on the NDA with a new list of two terms, and print the result.
print(check_terms(nda_text, ["term", "injunctive relief"]))

# Use it again with the original five terms. The result matches Part C.
print(check_terms(nda_text, terms))
