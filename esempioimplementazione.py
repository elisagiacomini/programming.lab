class Model(object):

    def fit(self,data):
        pass
        
    def predict(self):
        pass

class IncrementMode(Model):

    def fit(self,data):
        raise NotImplementedError('Questo modello non prevede un fit')
    
    def predict(self, prev_months):
        # codice per far funzionare la predizione
        # Nota: prev_months deve contenere i dati degli 'n' mesi precedenti 
        pass