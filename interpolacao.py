email_tmpl = """
   ...: olá, %(nome)s
   ...:
   ...: tem interesse em comprar %(produto)s?
   ...:
   ...: este produto é otimo para resolver %(texto)s
   ...:
   ...: clique agora em %(link)s
   ...:
   ...: apenas %(quantidade)d disponiveis!
   ...:
   ...: preço promocional %(preço).2f
   ...: """

In [2]: clientes = ("Kaio", "Vitoria", "Vitor", "Carlos")

In [3]: clientes = ("Kaio", "Vitoria", "Vitor", "Carlos")

In [4]: for cliente in clientes: print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto":
      ⋮ "Escrever muito bem", "link": "https://canetasmagicas123.com", "quantidade": 1, "preço": 19
      ⋮  })

      
