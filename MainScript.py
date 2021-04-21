#creo la classe delle auto, con attributi modello/cilindrata/cavalli/produttore/tipo,
#mentre la scrittura "_p" si riferisce ai parametri con cui daremo dei valori agli attributi
class Auto:
    def __init__ (self, modello_p, cilindrata_p, cavalli_p, produttore_p, tipo_p):
        self.modello = modello_p
        self.cilindrata = cilindrata_p
        self.cavalli = cavalli_p
        self.produttore = produttore_p
        self.tipo = tipo_p


#comandi che l'utente può inserire (continua dopo, con "while")
comando = input('Inserisci comando')
comando = int(comando)

#creare una lista vera su cui si lavorerà, e una lista test, così che coloro chi si occupano dei comandi dal 2 in poi,
#anziché aspettare che colui che si occupa del comando 1 legga i dati dalla vera lista, utilizzeranno la lista test.
#Una volta finito il lavoro con la lista test, essi sostituiranno "lista" a "lista_test" prima di eseguire il push
lista = []
lista_test = [Auto('x', 10, 5, 'y', 'u'), Auto('a', 5, 50, 'b', 'c')]

while comando != -1:
    if comando == 2: #lettura
        print()
    if comando == 2: #ricerca
        print()
    if comando == 3: #occorrenze di un produttore
        print()
    if comando == 4: #modello con più cavalli
        print()
    if comando == 5: #media delle cilindrate
        print()

    comando = input('Inserisci comando')
    comando = int(comando)


