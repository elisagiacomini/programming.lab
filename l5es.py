# Modificate l’oggetto CSVFile della lezione precedente in modo che dia un messaggio d’errore se si cerca di aprire un file non esistente. Poi, aggiungete questi due campi al file shampoo_sales.csv”:
# 01-01-2015, 
# 01-02-2015, ciao
# egestite gli errori che verranno generati in modo che le linee vengano saltate ma che venga stampato a schermo l’errore Alla fine ricordatevi di committare tutto.

# Inizializzo una lista vuota per salvare i valori
values = []

try:
# Apro e leggo il file, linea per linea
    my_file = open('shampoo_sales_2.csv', 'r')

except:
    print('Il file è inesistente.')

    for line in my_file:
        # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',')
        
        # Se NON sto processando l’intestazione...
        if elements[0] != 'Date':
            # Setto la data e il valore
            date = elements[0]
            value = elements[1]
            # Aggiungo alla lista dei valori questo valore
            values.append(float(value))
    print(values)

somma = sum(values)
print('La somma dei valori della lista è: {}'.format(somma))

