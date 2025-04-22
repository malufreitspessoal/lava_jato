from datetime import timedelta, datetime

"""  TIMEDELTA
utilizada para representar a diferença entre duas datas ou horários. 
Essa classe é extremamente útil quando você precisa realizar cálculos com datas, como adicionar ou subtrair dias, horas, minutos ou segundos.
"""

tipo_carro = 'P' # p m  g
tempo_pequeno = 30
tempo_medio = 45 
tempo_grande = 60 
data_atual = datetime.now()  # temos o .today()  .now()  .utcnow()


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno) # 
    print(f'O carro {tipo_carro} chegou ás {data_atual} e ficará pronto ás {data_estimada}')

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio) # 
    print(f'O carro {tipo_carro} chegou ás {data_atual} e ficará pronto ás {data_estimada}')
    
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande) # 
    print(f'O carro {tipo_carro} chegou ás {data_atual} e ficará pronto ás {data_estimada}')