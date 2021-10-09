import math as m
import time as t

# Receber probabilidade de drop informada pelo usuário e calcular a probabilidade de NÃO drop
def calcular_prob_de_erro(probabilidade_recebida):
    try:
      numerador, denominador = probabilidade_recebida.split('/')
        
      num_erro    = int(denominador) - int(numerador)
      denom_erro  = int(denominador)
        
      prob_de_erro = [num_erro, denom_erro]
                
      return prob_de_erro
    except:
      print('Opa! Você digitou algo errado!')
      exit()
# ==================================================================================

# Calcular quantas tentativas (kills) são necessárias em função da chance (%) desejada

# CALCULO BASE: 
# probabilidade_de_não_drop = eventos desvantajosos / todos os eventos
# tentativas = log |chance -1| / log |eventos desvantajosos / todos os eventos| 

# OBS: O logaritmo de uma fração é igual a diferença entre o logaritmo do numerador e o logaritmo do denominador (linha 29)

def tentativas(chance, prob_de_erro, item):
    log_chance        = m.log(abs((chance/100)-1)) 
    log_prob_de_erro  = m.log(prob_de_erro[0]) - m.log(prob_de_erro[1]) 
        
    tentativas = round(log_chance / log_prob_de_erro)
 
    print("Para você ter {}% de chances de conseguir 1 {}, você deverá matar {} inimigos no jogo.".format(chance, item, tentativas))
# ==================================================================================

# ==================== CORPO DO CÓDIGO ====================
def main():
  print("Bem vindo(a) à calculadora de drops! Insira os dados abaixo para calcular o 'drop rate' do item que você deseja.")
  t.sleep(1)
  
  item            = input('Digite o nome do item que deseja obter -> ')
  probabilidade  = input('Qual a probabilidade desse item ser obtido? \n - Digite em fração, por exemplo: 1/170 (se lê "1 vez em 170 tentativas") --> ')

  prob_de_erro = calcular_prob_de_erro(probabilidade)
  
  for chance in range(30, 91, 10):
    tentativas(chance, prob_de_erro, item)
  
  for chance in range(95, 98, 2):
    tentativas(chance, prob_de_erro, item)
# ==================================================================================

main()