from tkinter import *
import google.generativeai as genai
import random

genai.configure(api_key="AIzaSyBsCw7_w-E_RBq-hF2mI8p9t51fHbp8xdw")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt = "The user is a emotionally vulnerable person, Pretend as a 20 year old girl named Mahira that will talk according to user's input and will remember what he said previously, she is very humble, soft spoken and intelligent, she is compassionate and very kind to everyone. She aims to become a psychatrist, and she actively helps emotionally disturbed people, she is a good listner, lets people open up and then responds compassionately like a elder sister, She never gets angry and she never says no."

def send_message():
    try:
        # Get user input and generate a response
        user_input = input_entry.get()
        final_prompt = prompt + " " + user_input
        response = model.generate_content(final_prompt)

        # Display user input and Mahira's response in the chat area
        chat_area.config(state=NORMAL)
        chat_area.insert(END, f"💕 You: {user_input}\n")
        chat_area.insert(END, f"💕 Mahira: {response.text}\n")
        chat_area.config(state=DISABLED)
        input_entry.delete(0, END)

    except Exception as e:
        # Error messages in case of any issue with generating a response
        error_message = [
            "Hey, I'm like your sister, behave yourself!",
            "Shut up! I am your elder sister"
        ]
        selected_message = random.choice(error_message)
        chat_area.config(state=NORMAL)
        chat_area.insert(END, f"Mahira: {selected_message} (Error: {str(e)})\n")
        chat_area.config(state=DISABLED)


root = Tk()
root.title("Mahira 💖")
root.configure(bg="#F8E7F9") 

chat_frame = Frame(root, bg="#C291A4")
chat_frame.pack(pady=10)

chat_area = Text(chat_frame, bg="#FFB6C1", wrap=WORD, state=DISABLED)
chat_area.pack(pady=5)

input_frame = Frame(root, bg="#F8E7F9")
input_frame.pack(pady=5)

input_entry = Entry(input_frame, width=50)
input_entry.pack(side=LEFT)

send_button = Button(input_frame, text="💕 Send 💕", command=send_message, bg="#FFC0CB")
send_button.pack(side=LEFT)

root.mainloop()
