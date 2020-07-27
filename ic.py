import pandas as pd
import csv

genes = ["APOE","BIN1","CLU","ABCA7","CR1","PICALM","MS4A6A","CD33","MS4A4E","CD2AP"]

with pd.ExcelWriter('dados.xlsx') as writer:  #escrever o arquivo no formato excel
   for i in range(len(genes)):
      file =open(f'snp_result_{genes[i]}.txt') #abertura dos arquivos .txt com as informações de cada gene
      f = file.readlines()

      name = list() 
      alleles = list()
      snps =dict()
      cont = 1

      for line in range (0, len(f)):
         if f"{cont}. rs" in f[line] and "Homo sapiens" in f[line]:
            
            #print(cont)
            cont = cont + 1
            #print(f[line])
            #print(f[line+1])
            split = f[line].split() #divide o texto tem uma lista para recolher apenas o nome do snp
            name.append(split[1])
            alleles.append(f[line+1]) #recolhe o alelo correspondente ao snp
            
      
      snps = {'Name':name,'Alleles' : alleles} 
      df = pd.DataFrame(snps)
      print(df)
      
      df.to_excel(writer, sheet_name=f'{genes[i]}')

      file.close()
      
