def browser_navigate(brief, intent, url):
    print(f"[ Navegar ] {brief} | Intent: {intent} | URL: {url}")

def browser_view(brief):
    print(f"[ Visualizar HTML ] {brief}")
    return "<html><body>Simulação de HTML</body></html>"

def browser_input(brief, index, press_enter, text):
    print(f"[ Input ] {brief} | Campo: {index} | Texto: {text} | Enter: {press_enter}")

def browser_click(brief, index):
    print(f"[ Click ] {brief} | Botão: {index}")
