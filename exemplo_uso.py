#!/usr/bin/env python3
"""
Exemplo de Uso do Sistema de Monitoramento do DOU

Este arquivo demonstra como usar o sistema de monitoramento
do Diário Oficial da União de forma prática.

Para executar este exemplo:
1. Configure o arquivo .env com suas credenciais de e-mail
2. Execute: python exemplo_uso.py
"""

import os
from datetime import datetime
from main import get_daily_dou_publications
from send_notification import send_email_notification
from contacts import entity_contacts

def exemplo_basico():
    """
    Exemplo básico: buscar publicações e mostrar resultados
    """
    print("=== EXEMPLO BÁSICO ===")
    print("Simulando busca de publicações do DOU...")
    
    # HTML de exemplo (em uso real, viria do navegador)
    html_exemplo = """
    <div class="materia-content">
        <a href="/link1">PORTARIA ANTT Nº 123, DE 01 DE JULHO DE 2025</a>
        <p>Edição Nº 121 de 01/07/2025 - Pág. 45</p>
        <p>Dispõe sobre regulamentação de transporte terrestre...</p>
    </div>
    <div class="materia-content">
        <a href="/link2">DECRETO ANVISA Nº 456, DE 01 DE JULHO DE 2025</a>
        <p>Edição Nº 121 de 01/07/2025 - Pág. 67</p>
        <p>Estabelece normas para vigilância sanitária...</p>
    </div>
    """
    
    # Buscar publicações
    publicacoes = get_daily_dou_publications(html_exemplo, ["ANTT", "ANVISA"])
    
    print(f"Encontradas {len(publicacoes)} publicações:")
    for pub in publicacoes:
        print(f"- Entidade: {pub['entity_name']}")
        print(f"  Edição: {pub['edition_number']} de {pub['edition_date']}")
        print(f"  Página: {pub['page']}")
        print(f"  Link: {pub['link']}")
        print()

def exemplo_notificacao():
    """
    Exemplo de envio de notificação (apenas simulação)
    """
    print("=== EXEMPLO DE NOTIFICAÇÃO ===")
    
    # Verificar se as credenciais estão configuradas
    if not os.getenv('EMAIL_USER') or not os.getenv('EMAIL_PASSWORD'):
        print("⚠️  Credenciais de e-mail não configuradas!")
        print("   Configure o arquivo .env para testar o envio real.")
        print("   Por enquanto, apenas simulando...")
        
        # Simulação
        print("📧 Simulando envio de e-mail para ANTT...")
        print("   Destinatário: (contato da ANTT)")
        print("   Assunto: Alerta Diário Oficial")
        print("   Mensagem: Sua entidade foi mencionada no DOU...")
        print("✅ E-mail simulado enviado com sucesso!")
    else:
        print("📧 Credenciais configuradas! Testando envio real...")
        
        # Teste real (descomente para testar)
        # ATENÇÃO: Isso enviará um e-mail real!
        """
        try:
            send_email_notification(
                "seu_email_teste@gmail.com",  # Substitua pelo seu e-mail
                "Teste - Sistema DOU",
                "Este é um teste do sistema de monitoramento do DOU."
            )
            print("✅ E-mail de teste enviado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao enviar e-mail: {e}")
        """

def exemplo_consulta_entidades():
    """
    Exemplo de consulta às entidades cadastradas
    """
    print("=== EXEMPLO DE CONSULTA ===")
    print(f"Total de entidades cadastradas: {len(entity_contacts)}")
    print("\nPrimeiras 5 entidades:")
    
    for i, (nome, contato) in enumerate(list(entity_contacts.items())[:5]):
        print(f"{i+1}. {nome}")
        print(f"   Telefone: {contato.get('phone', 'N/A')}")
        print(f"   E-mail: {contato.get('email', 'N/A')}")
        print(f"   WhatsApp: {contato.get('whatsapp', 'N/A')}")
        print()

def exemplo_api():
    """
    Exemplo de como testar a API
    """
    print("=== EXEMPLO DE API ===")
    print("Para testar a API, execute em terminais separados:")
    print()
    print("1. Iniciar o servidor:")
    print("   cd dou_api")
    print("   source venv/bin/activate")
    print("   python src/main.py")
    print()
    print("2. Testar os endpoints:")
    print("   curl http://localhost:5000/api/dou/health")
    print("   curl http://localhost:5000/api/dou/entities")
    print("   curl http://localhost:5000/api/dou/entity/ANTT/contact")
    print()

def main():
    """
    Função principal que executa todos os exemplos
    """
    print("🚀 SISTEMA DE MONITORAMENTO DO DOU - EXEMPLOS DE USO")
    print("=" * 60)
    print()
    
    # Carregar variáveis de ambiente se existirem
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ Arquivo .env carregado")
    except ImportError:
        print("⚠️  python-dotenv não instalado, pulando carregamento do .env")
    except:
        print("⚠️  Arquivo .env não encontrado")
    
    print()
    
    # Executar exemplos
    exemplo_basico()
    print()
    exemplo_notificacao()
    print()
    exemplo_consulta_entidades()
    print()
    exemplo_api()
    print()
    
    print("=" * 60)
    print("✅ Todos os exemplos executados!")
    print()
    print("📚 Para mais informações, consulte o README.md")
    print("🔧 Para configurar o sistema, edite o arquivo .env")

if __name__ == "__main__":
    main()

