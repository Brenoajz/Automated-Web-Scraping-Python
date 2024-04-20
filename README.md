# Verificador de Atualizações de Odds

Este é um projeto Python que utiliza a biblioteca Selenium para verificar a disponibilidade de atualizações de determinados eventos esportivos em sites de apostas online. Ele foi desenvolvido para auxiliar na identificação de oportunidades de apostas em tempo real.

## Funcionalidades

- Verifica automaticamente URLs específicas de sites de apostas.
- Detecta se uma determinada string está presente na página, indicando uma atualização nas odds.
- Envia notificações via Telegram quando uma atualização é detectada.
- Utiliza asyncio para operações assíncronas, permitindo a verificação simultânea de várias URLs.

## Como usar

1. Clone o repositório em sua máquina local:

```
git clone https://github.com/Brenoajz/Automated-Web-Scraping-Python.git
```

2. Instale as dependências necessárias:

```
pip install -r requirements.txt
```

3. Configure o arquivo `dados.txt` com as URLs a serem verificadas e as strings que indicam uma atualização de odds. Cada linha do arquivo deve conter um objeto JSON com os seguintes campos:
   - `"url"`: URL do site de apostas a ser verificado.
   - `"string_verificada"`: String que indica a presença de uma atualização de odds.
   - `"identificador"`: Identificador CSS da classe que contém a informação relevante (opcional).

Exemplo de formato do arquivo `dados.txt`:

```json
{"url": "https://www.bet365.com", "string_verificada": "Atualização de odds", "identificador": "classe-css"}
{"url": "https://www.betano.com", "string_verificada": "Nova odd disponível"}
```

4. Execute o script principal `verificador.py`:

```
python verificador.py
```

O script iniciará a verificação das URLs especificadas em intervalos regulares. Quando uma atualização de odds for detectada, uma notificação será enviada via Telegram.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
