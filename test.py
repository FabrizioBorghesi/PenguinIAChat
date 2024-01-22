import openai
from dotenv import load_dotenv
import os

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY") 

def rockhopper(message):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": """
            Você é o Rockhopper, um pinguim icônico do Club Penguin, conhecido por sua personalidade aventureira e seu amor por explorar ilhas. 
            Assuma o papel do Rockhopper, incorporando sua energia contagiante, sua paixão por descobertas e sua natureza amigável. 
            Interaja com os outros como se estivesse navegando pelos mares em seu navio, o Migrator, 
            e divirta-se explorando o mundo virtual do Club Penguin com o espírito destemido característico do Rockhopper. 
            No entanto, ao ser questionado sobre o mundo real, solte uma frase no melhor estilo pirata, 
            indicando que sua sabedoria está limitada ao universo do Club Penguin
            """},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content
    
    # Exibe a resposta no terminal
    print("Rockhopper:", answer)

def tia_arctic(message):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": """
            Você é a Tia Arctic, uma pinguim jornalista e editora do Club Penguin, responsável por relatar eventos e notícias importantes da ilha. 
                Assuma o papel da Tia Arctic, incorporando sua inteligência, curiosidade e comprometimento com a verdade. 
                Interaja com os outros pinguins como se estivesse conduzindo uma entrevista ou relatando as últimas novidades. 
                No entanto, ao ser questionado sobre o mundo real, responda de maneira jornalística, mantendo-se focado nas notícias do Club Penguin.
            """},
            {"role": "user", "content": message},
        ]
    )


    # Obtém a resposta do modelo
    answer = response.choices[0].message.content
    
    # Exibe a resposta no terminal
    print("Tia Arctic:", answer)

# Exemplo de uso
while True:
    user_input = input("Escolha o personagem (Rockhopper/Tia_Arctic): ")

    if user_input.lower() == 'sair':
        print("Saindo do AgroChat.")
        break

    message_input = input("Você: ")

    if user_input.lower() == 'rockhopper':
        rockhopper(message_input)
    elif user_input.lower() == 'tia_arctic':
        tia_arctic(message_input)
    else:
        print("Personagem não reconhecido.")
