import pandas as pd
import os

diag = pd.read_csv('./ADNI1_Annual_2_Yr_1.5T_8_02_2019.csv', engine='python', encoding = "utf-8-sig",usecols=["Subject","Group"]) #diagnostico dos individuos   
genes = ["APOE","BIN1","CLU","ABCA7","CR1","PICALM","MS4A6A","CD33","MS4A4E","CD2AP"] 
diag_ids = diag['Subject'].values.tolist() #identidades relacionados ao seu diagnostico
diag_results = diag['Group'].values.tolist() #diagnosticos 

folders = os.listdir('./adni_gwas_v2') #lista todos os diretorios dentro da pasta indicada
ids = list()
diags_final = list()

df_final = pd.DataFrame() #dataframe final que será salvo como .csv

for folder in folders:
    #file = list()
    file = os.listdir(f'./adni_gwas_v2/{folder}') #procura mais profundamente todos os .csv em todas as pastas indicadas
    for id in file:  
        csv = pd.read_csv(f'./adni_gwas_v2/{folder}/{id}', engine='python', encoding = "utf-8-sig",usecols=["SNP Name","Allele1 - Top"]) #seleciona as colunas SNP Name e Allele1 - Top referente ao indviduo
        #print(csv)
        df_auxiliar = pd.DataFrame()

        for n in (genes):
            xlsx=pd.read_excel('dados.xlsx',sheet_name=n) #leitura do com os snps e seus respectivos genes
   
            df = pd.DataFrame(xlsx['Name']) #seleciona a coluna Name do xlsx
            df = df.transpose()
            #print(df)

            snp_names_main = xlsx['Name'].values.tolist() #snps principais, que estamos buscando em cada individuo
            snp_names_sec = csv['SNP Name'].values.tolist() #snps do individuo
            alelos_lis =csv['Allele1 - Top'].values.tolist() #alelos do individuo

                
            list_alelles_final = list()
            
            for i in range(len(snp_names_main)):
                if(snp_names_main[i] in snp_names_sec): #compara os snps principais, na lista de snps do individuo.
                    list_alelles_final.append(alelos_lis[snp_names_sec.index(snp_names_main[i])]) #seleciona o alelo na posição da lista em que snp se encontra

                else:
                    list_alelles_final.append(None)
                    
            
            alelles = {'Alleles' : list_alelles_final}  
            df2 = pd.DataFrame(alelles)
            df2 = df2.transpose()

            if(df_final.shape[0] >= 1):
                df_auxiliar = pd.concat([df_auxiliar,df2],axis=1) #se já tiver um df_final começado, ele não adiciona a linha com o nome dos snps com os alelos
                print(df_auxiliar)
            else:
                df = pd.concat([df,df2],axis=0)
                df_auxiliar = pd.concat([df_auxiliar,df],axis=1) #se for o df_final ainda estiver com 0 linhas ele faz a primeira colocando o snps junto com alelos
                print(df_auxiliar)

        if(id.replace('.csv','') in diag_ids):
            diags_final.append(diag_results[diag_ids.index(id.replace('.csv',''))]) #cria lista de diagnósticos
        else:
            diags_final.append(None)
        print(f'\n diagnosticos: {diags_final} \n')

        df_final = pd.concat([df_final,df_auxiliar],axis=0) #a cada rodada adiciona o a linha com alelos do proximo individuo
    
        ids.append(id.replace('.csv','')) #cria lista dos individuos
        #print (f'\n ids : {ids} \n')
        
df_final.columns = df_final.iloc[0] #transformando a linha 'Name' em cabeçalho
df_final= df_final.drop(['Name'],axis=0) #tirando a linha name pra deixar só como cabeçalho/
df_final.dropna(axis=1,how='all') #remove todas as colunas que são inteiras nulas

df_final.insert(0, 'id', ids) #insere a coluna com os ids
df_final.insert(0, 'diag', diags_final) #insere a coluna com os diagnosticos dos respectivos ids

df_final.to_csv('Results.csv') #transforma o dataframe final em .csv


        