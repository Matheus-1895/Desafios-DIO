nome = "Matheus"
idade = 20
curso = "Python"
profissao = "estudante"

print(f"Meu nome é {nome}, eu tenho {idade} anos e sou {profissao}.\nE atualmente estou cursando o curso de {curso}\n")

print("Meu nome é {}, eu tenho {}anos e sou {}.\nAtualmente estou cursando o curso de {}\n".format(nome,idade,profissao,curso))

print("""Meu nome é %s, eu tenho %d anos e sou %s.
      Atualmente estou cursando o curso de %s""" % (nome,idade,profissao,curso))
