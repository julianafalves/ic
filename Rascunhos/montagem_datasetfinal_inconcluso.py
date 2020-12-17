import pandas as pd
import os

genes = ["APOE","BIN1","CLU","ABCA7","CR1","PICALM","MS4A6A","CD33","MS4A4E","CD2AP"] 
diag = pd.read_csv('./ADNI1_Annual_2_Yr_1.5T_8_02_2019.csv', engine='python', encoding = "utf-8-sig",usecols=["Subject","Group"]) #deu certo essa parte   
df_final = pd.DataFrame
for n in (genes):
   xlsx=pd.read_excel('dados.xlsx',sheet_name=n) #leitura do com os snps e seus respectivos genes
   
   df = pd.DataFrame(xlsx['Name']) #seleciona a coluna Name do xlsx
   df = df.transpose()
   
   print(df)
   
   folders = os.listdir('./adni_gwas_v2') #lista todos os diretorios dentro da pasta indicada
   ids = list()
   diags_final = list()

   for folder in folders:
      #file = list()
      file = os.listdir(f'./adni_gwas_v2/{folder}') #procura mais profundamente todos os .csv em todas as pastas indicadas
      for id in file:  
         csv = pd.read_csv(f'./adni_gwas_v2/{folder}/{id}', engine='python', encoding = "utf-8-sig",usecols=["SNP Name","Allele1 - Top"]) #seleciona as olunas SNP Name e Allele1 - Top referente ao indviduo

         print(csv)

         snp_names_main = xlsx['Name'].values.tolist() #snps principais, que estamos buscando em cada individuo
         snp_names_sec = csv['SNP Name'].values.tolist() #snps do individuo
         alelos_lis =csv['Allele1 - Top'].values.tolist() #alelos do individuo
         
         diag_ids = diag['Subject'].values.tolist() #identidades relacionados ao seu diagnostico
         diag_results = diag['Group'].values.tolist() #diagnosticos 


         list_alelles_final = list()
         
         for i in range(len(snp_names_main)):
               if(snp_names_main[i] in snp_names_sec): #compara os snps principais, na lista de snps do individuo.
                  list_alelles_final.append(alelos_lis[snp_names_sec.index(snp_names_main[i])])
               else:
                  list_alelles_final.append(None)
                  
         
         if(id.replace('.csv','') in diag_ids):
            diags_final.append(diag_results[diag_ids.index(id.replace('.csv',''))])
         else:
            diags_final.append(None)

         print(f'\n diagnosticos: {diags_final} \n')
         alelles = {'Alleles' : list_alelles_final}
         df2 = pd.DataFrame(alelles)
         df2 = df2.transpose()

         

         df = pd.concat([df,df2],axis=0)
         ids.append(id.replace('.csv',''))
         print (f'\n ids : {ids} \n')
         

         print(df)
         
   df.columns = df.iloc[0] #estou transformando a linha 'Name' em cabeçalho
   df = df.drop(['Name'],axis=0) #tirando a linha name pra deixar só como cabeçalho/
   df.insert(0, 'id', ids)
   df.insert(0, 'diag', diags_final)
   print(df)


   
   df.to_csv(f'{n}.csv')

         
   print('\n \n')
               
         




