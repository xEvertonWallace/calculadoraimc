import pandas as pd 
 
class RelatorioIMC: 
    def __init__(self, arquivo): 
        self.df = pd.read_csv(arquivo, sep=';')