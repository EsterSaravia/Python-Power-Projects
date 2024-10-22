#Este script usa o PyAutoGUI para automatizar a navegação e preenchimento de um formulário web. Ele realiza as seguintes etapas:
#Abre o navegador Edge e acessa um link específico.
#Preenche os campos de login (e-mail e senha) e faz o login no site.
#Lê os dados de um arquivo CSV contendo informações de produtos (como código, marca, tipo, categoria, preço, custo e observações).
#Preenche automaticamente um formulário online com os dados de cada produto do CSV, enviando o formulário para cada entrada.
#Utiliza pausa entre as ações para garantir que as páginas e campos carreguem corretamente.
#Este código é útil para automatizar o preenchimento de formulários online com dados provenientes de uma base de dados CSV.

import pyautogui   
import time        

time.sleep(5)

# Exibe as coordenadas atuais do cursor do mouse na tela
print(pyautogui.position())    # Captura e imprime as coordenadas x, y da posição atual do mouse