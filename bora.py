import pandas as pd
import os

xlsx=pd.read_csv(f'NomesSnpsEAlelos.csv')

df = pd.DataFrame(xlsx)
print(df ,"\n\n")
#df = df.drop(0,axis=1)

df.columns = df.iloc[0]
df = df.drop(['Name'],axis=1)
df = df.drop(0,axis=0)
df = df.drop(1,axis=0)

folders = os.listdir('./adni_gwas_v2') #lista todos os diretorios dentro da pasta indicada
diags_final = list()

dict_ids_e_alelos = dict()
df_final = pd.DataFrame() #dataframe final que será salvo como .csv
bigdict = {}
biglist= []
for folder in folders[0:4]:
    #file = list()
    file = os.listdir(f'./adni_gwas_v2/{folder}') #procura mais os .csv de cada iniduod em todas as pastas indicadas
    file = list(file)
    biglist += file


diag = pd.read_csv('./ADNI1_Annual_2_Yr_1.5T_8_02_2019.csv', engine='python', encoding = "utf-8-sig",usecols=["Subject","Group"]) #diagnostico dos individuos   
diag_ids = diag['Subject'].values.tolist() #identidades relacionados ao seu diagnostico
diag_results = diag['Group'].values.tolist() #diagnosticos 



biglist = [l.replace('.csv','') for l in biglist]


for id in biglist:
        if(id in diag_ids):
            diags_final.append(diag_results[diag_ids.index(id.replace('.csv',''))]) 
        else:
            diags_final.append(None)

diags = pd.DataFrame({'Subject':biglist,'diag':diags_final })

#bigdict = pd.DataFrame(bigdict)
#print(biglist)
df = pd.concat([diags,df],sort=False)
#df = pd.concat([bigdict,df],sort=False)
       
print(df)

df.to_csv('csvinit.csv')


