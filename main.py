import openai

openai.api_key = "sk-proj-NXkOVX79Iyf3s6RXBkibT3BlbkFJ8jBtksyXQdsdJCaOc2Kj"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "ChatGPT bilan Pythoni qandday integratsiya qilsa bo'ladi"}
    ]
)
gpt_message = response.choices[0].message['content'].strip()
print(gpt_message)