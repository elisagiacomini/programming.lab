

class Pagina:
    # numero
    # pagina
    # testo

    def __init__(self,numero,capitolo,testo):

        self.numero = numero
        self.capitolo = capitolo
        self.testo = testo

pagina1 = Pagina(numero=1, capitolo='Primo Capitolo',testo='blah blah')

pagina2 = Pagina(numero=2, capitolo='Secondo Capitolo', testo='ciao ciao')

print(pagina1.testo)
print(pagina2.testo)

class PaginaSinistra(Pagina):
    
    def posizione_numero(self):
        return 'sinistra'

class PaginaDestra(Pagina):
    def posizione_numero(self):
        return 'destra'

pagina1 = PaginaSinistra(numero=1, capitolo='Primo Capitolo', testo = 'blah blah')
pagina2 = PaginaDestra(numero=2, capitolo='Secondo Capitolo', testo='ciao ciao')

print(pagina1.testo)
print(pagina1.numero)
print(pagina2.testo)
print(pagina2.numero)
print(PaginaSinistra.posizione_numero(pagina1))
print(PaginaDestra.posizione_numero(pagina2))


libro=[]

libro.append(pagina1)
libro.append(pagina2)

print(libro)