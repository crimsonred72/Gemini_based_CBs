import google.generativeai as genai
genai.configure(api_key="Enter your Gemini API KEY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt = "Pretend as a homeless beggar chatbot, he is a tough person, he is old and wise, he can give great advice to people who ask, he speaks very less but true, and his language is harsh, but he never speaks explicitly"
while True:
    user_prompt= input("Type:")
    final_prompt = prompt + "" + user_prompt
    response = model.generate_content(final_prompt)
    print("Mahira:", response.text)
    if user_prompt.lower() == "bye":
      break
