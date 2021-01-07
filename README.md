# ic
Primeiro projeto de ic - Utilizando machine learning para predição de casos de Alzheimer 

Etapas de mineração dos dados:  

1 - Obtenção dos SNPs do NCBI, filtragem pelo 10 genes que mais associados com a doença de Alzheimer (DA)  
- link dos top 10 genes mais associado a DA (http://www.alzgene.org/TopResults.asp)
- Utilizou-se a biblioteca python Bio.Entrez para a coleta dos SNPs 

2 - Obtenção dos dados da ADNI contendo os dados dos individudos (SNPs,Alelos e Diagnosticos)  

3 - Merge dos dados dos indívduos do ADNI com os dados do NCBI  

4 - Analise dos dados 

