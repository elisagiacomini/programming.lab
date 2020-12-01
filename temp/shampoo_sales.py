# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo “get_data” che torni i dati dal file CSV come numeri di una lista (come abbiamo già visto).

# oggetto CSVFile
# - init(filename)
# - name
# - get_data
#   return dati


class CSVFile:
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        values = []

        # Inizializzo la lista vuota per salvare i
        my_file = open(self.name, 'r')

        for line in my_file:
            # faccio lo split di ongi riga sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                # Setto la data e il valore
                date = elements [0]
                value = elements [1]
                # Aggiungo alla lista dei valori questo valore
                values.append(float(value))
        return values
        

my_file = CSVFile(name = 'shampoo_sales.csv')
print(my_file.get_data())
