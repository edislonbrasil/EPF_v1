import pandas as pd
import numpy as np

def tira_repetidos(dados_brutos)
  """ Função para retirar os indices repetidos
  Por conta do horário de verão, em todos os anos tem um indice repetido 
  correspondendo a passagem do horario de verao
  
  Entrada
  dados_brutos -> descrição: dados com indices repitidos
                  tipo: Pandas Dataframe
                  Origem: Esses dados provem da ENTSO-E transparency platform
  
  Saida
  dados_sr -> descrição: dados sem repeticao
              tipo: Pandas Dataframe
  """
  
  indice_rep = np.zeros(shape=(0, 0),dtype=int)
  for i in range(dados_brutos.shape[0]-1):
    if dados_brutos.iloc[i,0] == dados_brutos.iloc[i+1,0]:
      indice_rep = np.append(indice_rep, i)

  dados_sr.drop(dados_brutos.index[indice_rep], axis=0,inplace=True) #dados sem repeticao
  
  return dados_sr
