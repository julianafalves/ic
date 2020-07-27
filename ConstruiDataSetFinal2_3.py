import pandas as pd
import os

diag = pd.read_csv('./ADNI1_Annual_2_Yr_1.5T_8_02_2019.csv', engine='python', encoding = "utf-8-sig",usecols=["Subject","Group"]) #diagnostico dos individuos   
diag_ids = diag['Subject'].values.tolist() #identidades relacionados ao seu diagnostico
diag_results = diag['Group'].values.tolist() #diagnosticos 

folders = os.listdir('./adni_gwas_v2') #lista todos os diretorios dentro da pasta indicada
diags_final = list()

dict_ids_e_alelos = dict()
df_final = pd.DataFrame() #dataframe final que será salvo como .csv

for folder in folders[4:8]:
    #file = list()
    file = os.listdir(f'./adni_gwas_v2/{folder}') #procura mais profundamente todos os .csv em todas as pastas indicadas
    for id in file:
        csv = pd.read_csv(f'./adni_gwas_v2/{folder}/{id}', engine='python', encoding = "utf-8-sig",usecols=["SNP Name","Allele1 - AB","Allele2 - AB"]) #seleciona as colunas SNP Name e Allele1 - Top referente ao indviduo
        df_auxiliar = pd.DataFrame()
        
        xlsx=pd.read_csv(f'NomesSnpsEAlelos.csv') #leitura do com os snps e seus respectivos genes
        xlsx = xlsx.loc[0].tolist()
        xlsx.remove('Name')

        snp_names_main = xlsx #snps principais, que estamos buscando em cada individuo
        snp_names_sec = csv['SNP Name'].values.tolist() #snps do individuo
        alelos_lis1 =csv['Allele1 - AB'].values.tolist() #alelos1  AB do individuo
        alelos_lis2 =csv['Allele2 - AB'].values.tolist() #alelos2 AB do individuo

         
        list_alelles_final = list() #criação da lista que conterá os alelos dos individuos
        
        ''' Encontra os SNPS de cada indíviduo'''
        for i in range(len(snp_names_main)):
            if(snp_names_main[i] in snp_names_sec): #compara os snps principais, na lista de snps do individuo.
                if alelos_lis1[snp_names_sec.index(snp_names_main[i])] == 'A' and alelos_lis2[snp_names_sec.index(snp_names_main[i])] == 'a':
                    list_alelles_final.append(0)
                elif alelos_lis1[snp_names_sec.index(snp_names_main[i])] == 'B' and alelos_lis2[snp_names_sec.index(snp_names_main[i])] == 'B':
                    list_alelles_final.append(1)
                else:
                    list_alelles_final.append(2)
                #print(list_alelles_final)
            else:
                list_alelles_final.append('')

        dict_ids_e_alelos[id]=list_alelles_final        
        print(list_alelles_final)
        
        '''cria lista de diagnósticos'''
        if(id.replace('.csv','') in diag_ids):
            diags_final.append(diag_results[diag_ids.index(id.replace('.csv',''))]) 
        else:
            diags_final.append(None)

        print(f'\n diagnosticos: {diags_final} \n')
    
df_final = pd.DataFrame(dict_ids_e_alelos)
df_final = df_final.transpose()

df_final.columns = df_final.iloc[0] #transformando a linha 'Name' em cabeçalho
df_final= df_final.drop(['Name'],axis=0) #tirando a linha name pra deixar só como cabeçalho/
#df_final.dropna(axis=1,how='all') #remove todas as colunas que são inteiras nulas

#df_final.insert(0, 'id', ids) #insere a coluna com os ids
df_final.insert(0, 'diag', diags_final) #insere a coluna com os diagnosticos dos respectivos ids

df_final.to_csv('Results.csv') #transforma o dataframe final em .csv
