import pandas as pd
'''
xlsx=pd.read_excel('dados.xlsx',sheet_name='APOE')
   
df = pd.DataFrame(xlsx['Name'])
df = df.transpose()
   
df.columns = df.iloc[0] #estou transformando a linha 'Name' em cabeçalho
#df = df.drop(['Name'],axis=0)

column = dict()
id= ['bla bla']
#c = pd.DataFrame(column)

df.insert(0, 'id', id)
print(df)

lista = 'bkabkabkabka.csv'
print(lista)
lista.replace('.csv','')
print(lista.replace('.csv',''))
'''
xlsx=pd.read_excel('dados.xlsx',sheet_name='APOE')
csv = pd.read_csv('./adni_gwas_v2/adni_gwas_v2_set1/002_S_0295.csv', engine='python', encoding = "utf-8-sig",usecols=["SNP Name","Allele1 - Top"]) #deu certo essa parte   
#print(csv)

snp_names_main = xlsx['Name'].values.tolist() #snps principais, que estamos buscando em cada individuo
snp_names_sec = csv['SNP Name'].values.tolist() #snps do individuo
alelos_lis =csv['Allele1 - Top'].values.tolist() #alelos do individuo
         
#diag_ids = diag['Subject'].values.tolist() #identidades relacionados ao seu diagnostico
#diag_results = diag['Group'].values.tolist() #diagnosticos 
cont =0
list_alelles_final = list()
         
for i in range(len(snp_names_main)):
      if(snp_names_main[i] in snp_names_sec):
          print(alelos_lis[snp_names_sec.index(snp_names_main[i])])
          cont = cont +1
    
print(cont)
                  
