import pandas as pd 
 
class RelatorioIMC: 
    def __init__(self, arquivo): 
        self.df = pd.read_csv(arquivo, sep=';')

    def tratamento(self):

        self.df['Peso (kg)'] = self.df['Peso (kg)'].str.replace(',', '.').astype(float) 
        self.df['Altura (m)'] = self.df['Altura (m)'].str.replace(',', '.').astype(float) 

        self.df['Primeiro Nome'] = self.df['Primeiro Nome'].str.strip().str.replace(r'\s+', ' ', regex=True).str.upper()
        self.df['Sobrenomes'] = self.df['Sobrenomes'].str.strip().str.replace(r'\s+', ' ', regex=True).str.upper() 

        self.df.dropna(subset=['Peso (kg)', 'Altura (m)'], inplace=True)
        return self.df
        
    def calcular_imc(self, altura, peso): 
        # trata casos em que peso e altura está fora dos parametros normais 
        if altura > 2.0 and peso < 50.0: 
            altura, peso = peso, altura 
        return peso / altura**2  

    