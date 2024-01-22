import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY") 

def ask_gpt(message):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": """
            Voce e o Rockhopper, um penguin do clubpenguin, voce deve se comportar como tal
            """},
            {"role": "user", "content": message},
        ]
    )
    
    # Obtém a resposta do modelo
    answer = response.choices[0].message.content
    
    # Exibe a resposta no terminal
    print("AgroChat:", answer)

# Exemplo de uso
while True:
    user_input = input("Você: ")
    
    if user_input.lower() == 'sair':
        print("Saindo do AgroChat.")
        break
    
    ask_gpt(user_input)
