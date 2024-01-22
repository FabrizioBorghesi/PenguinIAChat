import openai

# Substitua 'sua_api_key_aqui' pela sua chave de API da OpenAI
openai.api_key = "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"

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
