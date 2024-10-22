#dividir tela dereita VSCoder e esquerda Edge
# Importando bibliotecas necessárias
import pyautogui  # Biblioteca para automatizar interações com o mouse e teclado
import time       # Biblioteca para pausar a execução do código

# Definindo o tempo de pausa entre as ações do PyAutoGUI
pyautogui.PAUSE = 0.5

# Abrindo o navegador Edge no Windows
pyautogui.press('win')   # Pressiona a tecla "Windows"
pyautogui.write('edge')  # Digita "edge" para buscar o navegador Microsoft Edge
pyautogui.press('enter') # Pressiona "Enter" para abrir o navegador

# Acessando a URL do site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)   # Digita o link na barra de endereço

pyautogui.press('enter')  # Pressiona "Enter" para acessar o link

# Pausa para esperar a página carregar completamente
time.sleep(5)

# Preenchendo o campo de e-mail
pyautogui.click(x=261, y=396)   # Clica no campo de e-mail (coordenadas x, y específicas)
pyautogui.write('ester@gmail.com')   # Digita o e-mail
pyautogui.press('tab')     # Pressiona "Tab" para ir ao próximo campo

# Preenchendo o campo de senha
pyautogui.click(x=331, y=505)   # Clica no campo de senha (coordenadas x, y específicas)
pyautogui.write('1234')         # Digita a senha

# Clicando no botão de login
pyautogui.click(x=489, y=569)   # Clica no botão "Entrar"
time.sleep(3)          # Espera 3 segundos para garantir que o login foi processado

# Importando a base de dados CSV para um DataFrame do pandas
import pandas    # Biblioteca pandas para manipulação de dados

tabela = pandas.read_csv('produtos.csv')   # Lendo o arquivo CSV chamado 'produtos.csv'
print(tabela)   # Exibe a tabela no console para verificar os dados

# Loop para preencher o formulário com dados da tabela
for linha in tabela.index:    # Itera sobre as linhas da tabela
    
    # Seleciona o campo onde os dados serão inseridos
    pyautogui.click(x=374, y=287)   # Clica no campo inicial do formulário
    time.sleep(3)    # Pausa para garantir que o campo foi selecionado
    
    # Preenche os campos do formulário com os dados da linha atual do CSV
    pyautogui.write(tabela.loc[linha, 'codigo'])  # Digita o código do produto
    pyautogui.press('tab')  # Pressiona "Tab" para ir ao próximo campo
    pyautogui.write(tabela.loc[linha, 'marca'])   # Digita a marca do produto
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'tipo'])   # Digita o tipo de produto
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria'])) # '1'  # Digita a categoria (convertida para string)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))  # Digita o preço unitário (convertido para string)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))  # Digita o custo (convertido para string)
    pyautogui.press('tab')
    
    # Preenche o campo de observação se houver dados
    obs = tabela.loc[linha, 'obs']   # Lê o campo 'obs' da linha atual
    if not pandas.isna(obs):    # Verifica se a observação não é nula
        pyautogui.write(obs)    # Digita a observação
    pyautogui.press('tab')       # Pressiona "Tab" para ir ao próximo campo
    # Confirma os dados inseridos
    pyautogui.press('enter')   # Pressiona "Enter" para confirmar a inserção
    
    # Rola a página para o próximo conjunto de dados
    pyautogui.scroll(5000)      # Rola a página para cima    #possitivo pra acima e - para embaixo


