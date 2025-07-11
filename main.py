import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def get_daily_dou_publications(html_content, search_terms=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    all_publications = []

    # Find all publication items
    # The structure seems to be: div with class 'materia-content' for each publication
    # and inside it, a link and text content.
    for article in soup.find_all('div', class_='materia-content'):
        text_content = article.get_text()
        link_tag = article.find('a', href=True)
        link = link_tag['href'] if link_tag else ''

        # Extract edition info (Edição Nº, Data, Página)
        edition_info_match = re.search(r'Edição Nº (\d+)(?:-A)? de (\d{2}/\d{2}/\d{4}) - Pág. (\d+)', text_content)
        edition_number = edition_info_match.group(1) if edition_info_match else ''
        edition_date = edition_info_match.group(2) if edition_info_match else ''
        page_number = edition_info_match.group(3) if edition_info_match else ''

        # Extract entity name based on search terms
        entity_name = ""
        found_entity = False
        if search_terms:
            for term in search_terms:
                if term.lower() in text_content.lower():
                    entity_name = term
                    found_entity = True
                    break
        else:
            found_entity = True # If no search terms, include all publications

        if found_entity:
            all_publications.append({
                "entity_name": entity_name,
                "edition_number": edition_number,
                "edition_date": edition_date,
                "page": page_number,
                "link": link,
                "content": text_content # Include full content for filtering in pipeline
            })
    return all_publications



