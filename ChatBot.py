import google.generativeai as go

API_KEY="AIzaSyAlSejBp5MIMKzfRFb78vPY0hLG-_zK4bw"
go.configure(api_key=API_KEY)

model=go.GenerativeModel("gemini-2.0-flash")

chat=model.start_chat()
print("chat with Go! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("GO:", response.text)
