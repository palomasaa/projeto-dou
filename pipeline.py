from main import get_daily_dou_publications
from send_notification import send_email_notification
from contacts import entity_contacts
from datetime import datetime
from browser_tools import browser_navigate, browser_view, browser_input, browser_click

def run_pipeline():
    today = datetime.now().strftime("%d/%m/%Y")
    print(f"Iniciando o web scraping para a edição do DOU de {today}...")

    # Navigate to the journal page
    browser_navigate(brief="Navegando para o Diário Oficial da União.", intent="informational", url="https://www.in.gov.br/leiturajornal")

    # Input the current date and click to view the summary
    browser_input(brief="Inserindo a data atual no campo de data.", index=1, press_enter=False, text=today)
    browser_click(brief="Clicando no botão VISUALIZAR EM SUMÁRIO.", index=2)

    # Get the HTML content after the date selection
    html_content = browser_view(brief="Obtendo o HTML da página após a seleção da data.")

    publications = get_daily_dou_publications(html_content=html_content, search_terms=list(entity_contacts.keys()))

    if not publications:
        print("Nenhuma publicação encontrada para a data de hoje.")
        return

    print(f"Encontradas {len(publications)} publicações. Verificando menções a entidades...")
    for pub in publications:
        for entity, contact_info in entity_contacts.items():
            if entity.lower() in pub["content"].lower():
                message = f"""
⚠️ Alerta Diário Oficial ⚠️

O nome da sua entidade foi citado no DOU.

📌 Entidade: {entity}
📅 Edição Nº {pub["edition_number"]} de {pub["edition_date"]}
📄 Página: {pub["page"]}
🔗 Acesse aqui: {pub["link"]}

Esta é uma notificação automática. Caso tenha dúvidas, entre em contato com o responsável pelo sistema.
"""
                if contact_info.get("email"):
                    print(f"Enviando e-mail para {entity}...")
                    send_email([contact_info["email"]], "Alerta Diário Oficial", message)
                if contact_info.get("whatsapp"): # Placeholder for WhatsApp sending
                    print(f"Tentando enviar WhatsApp para {entity} (requer configuração externa): {contact_info["whatsapp"]}")
                    # Implementação real do envio de WhatsApp (API do WhatsApp Business ou similar) seria aqui

if __name__ == "__main__":
    run_pipeline()


