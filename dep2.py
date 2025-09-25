from pytholog import KnowledgeBase

def criar_base():
    """Cria e retorna a base de conhecimento corretamente configurada"""
    kb = KnowledgeBase("comida")
    
    # Fatos básicos (observe os pontos finais)
    kb([
        "gosta(icaro, pizza).",
        "gosta(icaro, lasanha).",
        "sabor(pizza, salgado).",
        "sabor(lasanha, salgado).",
        
        # Regra principal corrigida
        "preferencia_salgada(Pessoa) :- ",
        "    gosta(Pessoa, Prato), sabor(Prato, salgado), ",
        "    not((gosta(Pessoa, OutroPrato), sabor(OutroPrato, doce))).",
        
        # Fato adicional para teste
        "sabor(bolo, doce)."
    ])
    return kb

def consultar(kb, pergunta):
    """Função segura para consultas que sempre retorna True/False"""
    try:
        resultado = list(kb.query(pergunta))
        return len(resultado) > 0  # True se encontrou resultados
    except:
        return False

# Testando corretamente
kb = criar_base()

print("Teste 1 - Ícaro gosta de pizza salgada?")
print("Resultado cru:", kb.query("gosta(icaro, pizza), sabor(pizza, salgado)"))
print("Resultado bool:", consultar(kb, "gosta(icaro, pizza), sabor(pizza, salgado)"))

print("\nTeste 2 - Ícaro tem preferência por salgados?")
print("Resultado cru:", kb.query("preferencia_salgada(icaro)"))
print("Resultado bool:", consultar(kb, "preferencia_salgada(icaro)"))

print("\nTeste 3 - Verificando com prato doce (controle negativo)")
print("Resultado cru:", kb.query("preferencia_salgada(icaro), gosta(icaro, bolo)"))
print("Resultado bool:", consultar(kb, "preferencia_salgada(icaro), gosta(icaro, bolo)"))