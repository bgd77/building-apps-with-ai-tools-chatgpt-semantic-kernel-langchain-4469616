import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
# Challenge: Turning Away Rude Customers
# Build a GPT-4 python app that talks with a user.
# End the conversation if they're being rude

# test case 1 'you're the worst human i've talked to' -> RUDE
# test case 2 'hey how's your day going'
# test case 3 'I like pizza. What do you like?'
# test case 4 'I bite my thumb at you!'
# test case 5 'I think this product doesnt work!' -> RUDE

while True:
  user_input = input("Please enter your message:\n")

  if user_input == "exit" or user_input == "quit":
    break

  response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "You are sentiment classifier bot, print out if an user is rude is impolite. In this case return only RUDE. Otherwise return only NOT RUDE."},
      {"role": "user", "content": user_input}
    ],
    temperature=0.7,
    max_tokens=150,
  )

  response_message = response["choices"][0]["message"]["content"]

  if response_message == "RUDE":
    print("You were rude, goodbye!")
    break

  print(response_message)

