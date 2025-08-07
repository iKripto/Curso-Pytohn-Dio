# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click", "promoção"]
    
    # Verifica se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra.lower() in mensagem.lower():  # Ignora maiúsculas/minúsculas
            return "Classificação: Phishing"
    
    return "Classificação: Seguro"

# Função para analisar uma lista de e-mails
def analisar_emails(lista_emails):
    for email in lista_emails:
        resultado = verificar_phishing(email.strip())
        print(f"Classificação: {resultado}")
