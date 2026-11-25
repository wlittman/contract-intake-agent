# Bring in the two packages installed in Step 7.

# reads the .env file
from dotenv import load_dotenv

# Anthropic's package for talking to Claude
import anthropic

# Read .env so the API key is available to this program,
# without the key ever appearing in the code.
load_dotenv()

# Create the connection to Claude
# Finds they key automatically by its name, ANTHROPIC_API_KEY
client = anthropic.Anthropic()

# Open the NDA text file and store its contents in nda_text (reading the file).
with open("samples/falcon_nda.txt") as f:
    nda_text = f.read()

# Send the request to Claude and store the answer in message.
message = client.messages.create(
    model="claude-haiku-5-5",   # which Claude model answers (the smallest and cheapest)
    max_tokens=2000,             # cap on the answer's length, which also caps the cost
    messages=[                  # a list holding one message (a dictionary)
        {
            "role": "user",     # the message is from me
            # My instruction, then two line breaks, then the NDA text, joined with +.
            "content": "Summarize this NDA in three sentences for a business reader:\n\n" + nda_text,
        }
    ],    
)

# Claude's answer comes back in pieces called blocks.
# Go through each block and print the ones that are text (loop).
for block in message.content:
    if block.type == "text":
        print(block.text)

# Print how many tokens went in (instructions plus NDA) and came out (the summary).
# Tokens are what the API charges for.
print("Tokens used:", message.usage.input_tokens, "in,", message.usage.output_tokens, "out")

# Why Claude stopped: "end_turn" means it finished; "max_tokens" means it hit the cap.
print("Stop reason:", message.stop_reason)
