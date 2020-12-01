# Modificate l’oggetto CSVFile della lezione precedente in modo che alzi un'eccezione se il nome del file non è una stringa. Poi, modificate la funzione get_data in modo da leggere solo un’ intervallo di righe del file, aggiungendo gli argomenti start ed end opzionali, controllandone la correttezza e sanitizzandoli se necessario.


# DA FARE



# Inizializzo una lista vuota per salvare i valori
values = []

try:
    # Apro e leggo il file, linea per linea
    my_file = open('shampoo_sales.csv', 'r')
except:
    print('Il file è inesistente.')
    import sys
    sys.exit()

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