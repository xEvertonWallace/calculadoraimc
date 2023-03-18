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
        
        if altura > 2.0 and peso < 50.0: 
            altura, peso = peso, altura 
        return peso / altura**2

    def gerar_relatorio(self, arquivo_saida):
        dados_tratados= self.tratamento()

        with open(arquivo_saida, 'w', encoding='utf-8') as relatorio: 

            cabecalho = 'Nome' + ' ' + 'IMC\n'
            relatorio.write(cabecalho) 
   
            for _, row in dados_tratados.iterrows(): 

                nome_completo = row['Primeiro Nome'] + ' ' + row['Sobrenomes'] 
                
                imc = self.calcular_imc(row['Altura (m)'], row['Peso (kg)']) 
                imc_str = '{:.2f}'.format(imc).replace('.', ',') 

                linha = f'{nome_completo} {imc_str}\n' 
                relatorio.write(linha)     


    