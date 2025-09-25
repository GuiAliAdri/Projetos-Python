import pytholog as pl

# Criando a base de conhecimento
con_comida = pl.KnowledgeBase('comida')

# Adicionando os fatos e regras
con_comida([
    "gosta(joao, carne)",
    "gosta(guilherme, melancia)",
    "gosta(guilherme, bolo)",
    "gosta(joao, sorvete)",
    "gosta(felipe, carne)",
    "gosta(joao, hamburguer)",
    "gosta(icaro, pizza)",
    "gosta(icaro, lasanha)",
    
    "sabor(bolo, doce)",
    "sabor(sorvete, doce)",
    "sabor(carne, salgado)",
    "sabor(hamburguer, salgado)",
    "sabor(pizza, salgado)",
    "sabor(lasanha, salgado)",
    "sabor(melancia, doce)",
    "sabor(laranja, doce)",
    
    "sobremesa(Prato) :- sabor(Prato, doce)",
    "prato_principal(Prato) :- sabor(Prato, salgado)",
    "preferencia_doce(Pessoa) :- gosta(Pessoa, Prato), sabor(Prato, doce)",
    "preferencia_salgada(Pessoa) :- gosta(Pessoa, Prato), sabor(Prato, salgado)"
])

# Carregando a base de conhecimento
con_comida = pl.KnowledgeBase('comida')
con_comida.from_file("base.pl")

def print_base(base):
  for i in base.db.keys():
    for d in base.db[i]['facts']:
      print(f"{d.to_string()}.")

print_base(con_comida)

# Realizando 6 inferências (4 verdadeiras e 2 falsas)
print("\nPrimeira rodada de consultas:")
print("1. João gosta de laranja?", con_comida.query(pl.Expr("gosta(joao, laranja)")))  # Verdadeiro
print("2. Bolo é doce?", con_comida.query(pl.Expr("sabor(bolo, doce)")))              # Verdadeiro
print("3. Felipe gosta de pizza?", con_comida.query(pl.Expr("gosta(felipe, pizza)")))  # Falso
print("4. Lasanha é sobremesa?", con_comida.query(pl.Expr("sobremesa(lasanha)")))      # Falso
print("5. Icaro tem preferência por salgados?", con_comida.query(pl.Expr("preferencia_salgada(icaro)")))  # Verdadeiro
print("6. Guilherme tem preferência por doces?", con_comida.query(pl.Expr("preferencia_doce(guilherme)")))  # Verdadeiro

# Adicionando novas sentenças para tornar verdadeiras as falsas
novas_sentencas = [
    "gosta(felipe, pizza) :- gosta(felipe, carne), prato_principal(pizza)",
    "sobremesa(lasanha) :- sabor(lasanha, doce)"
]

con_comida.add(novas_sentencas)

# Salvando a nova base de conhecimento
con_comida.to_file("base_nova.pl")

# Realizando as mesmas consultas novamente
print("\nSegunda rodada de consultas:")
print("3. Felipe gosta de pizza?", con_comida.query(pl.Expr("gosta(felipe, pizza)")))  # Agora pode ser verdadeiro
print("4. Lasanha é sobremesa?", con_comida.query(pl.Expr("sobremesa(lasanha)")))      # Ainda falso (precisa de mais info)

# Adicionando informação adicional para tornar lasanha doce
con_comida.add(["sabor(lasanha, doce)"])

print("\nTerceira rodada de consultas:")
print("4. Lasanha é sobremesa?", con_comida.query(pl.Expr("sobremesa(lasanha)")))      # Agora verdadeiro