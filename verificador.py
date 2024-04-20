import asyncio
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telegram import Bot
from selenium.common.exceptions import NoSuchElementException

token = "7183413086:AAEaL-T9xbyvI8CDccc8cZn4YG8MKl6ahso"  # Token do telegram
chat_id = "-1002135963274"
bot = Bot(token)

async def enviar_mensagem(mensagem, cor=""):
    try:
        cor_map = {
            "verde": "\U0001F7E2",   # Emoji verde
            "laranja": "\U0001F7E1"  # Emoji laranja
        }
        emoji_cor = cor_map.get(cor.lower(), "")  # Obtém o emoji correspondente à cor

        await bot.send_message(chat_id=chat_id, text=f"{emoji_cor} {mensagem}")  # Adiciona o emoji à mensagem
        print("Mensagem enviada")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")


def limpar_cache_navegador(driver):
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.execute_script("document.cookie = '';")

async def verificar(url, string_verificada, identificador):
    driver = None
    try:
        with open('jogos.txt', 'r') as arquivo:  # Caminho do arquivo que contem as urls que já obtiveram a verificação.
            verificados = arquivo.read().splitlines()

        options = webdriver.ChromeOptions()  
        options.add_argument('--disable-images')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--start-minimized")
      

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(8)

        if string_verificada in driver.page_source and url not in verificados:

            capturar_elemento = "Elemento não encontrado"

            try:
                capturar_elemento_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, identificador)))  # Class HTML
                capturar_elemento = capturar_elemento_element.text
            except NoSuchElementException:
                driver.refresh()
                pass            

            verificados.append(url)

            with open('jogos.txt', 'a') as arquivo:  # Caminho do arquivo que contem as urls que já obtiveram a verificação.
                arquivo.write(url + '\n')

            cor_mensagem = ""
            tipo_pagina = ""

            if "bet365" in url:
               cor_mensagem = "verde"  # Cor verde para URLs do Bet365
               tipo_pagina = "Bet365"
               mensagem = f"Marco de Jogadores disponível na Bet365 no jogo do {capturar_elemento}, segue o link: {url}"
            elif "betano" in url:
               cor_mensagem = "laranja"  # Cor laranja para URLs do Betano
               tipo_pagina = "Betano"
               mensagem = f"Especiais de Jogadores disponível na Betano no jogo do {capturar_elemento}, segue o link: {url}"


            await enviar_mensagem(mensagem, cor_mensagem)

    except Exception as e:
        print(f"Erro ao processar: {e}")

    finally:
        if driver:
            limpar_cache_navegador(driver)
            driver.quit()
            print('Driver fechado')

async def main():
    try:
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        urls_verificacao = []
        for linha in linhas:
            dados = json.loads(linha.strip())
            urls_verificacao.append(dados)
    except Exception as e:
        print(f"Erro ao ler os dados: {e}")
        return

    while True:
        for item in urls_verificacao:
            await verificar(item["url"], item["string_verificada"], item["identificador"])

        await asyncio.sleep(1)  # intervalo de 5 segundos

if __name__ == "__main__":
    asyncio.run(main())
