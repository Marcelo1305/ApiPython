from datetime import datetime, timedelta

def minha_funcao(data_inicial, data_final):
    matriz = [
        ['Monday', '8:00', '12:00', '13:00', '17:00', 'true'],
        ['Tuesday', '8:00', '12:00', '13:00', '17:00', 'true'],
        ['Wednesday', '8:00', '12:00', '13:00', '17:00', 'true'],
        ['Thursday', '8:00', '12:00', '13:00', '17:00', 'true'],
        ['Friday', '8:00', '12:00', '13:00', '17:00', 'true'],
    ]
    dia_da_semanaIni = data_inicial.strftime('%A')
    dia_da_semanaFim = data_final.strftime('%A')
    horario_time = data_inicial.time()
    hora = datetime.strptime(matriz[0][1], '%H:%M').time()

    print(f'O dia da semana de data_inicial é: {dia_da_semanaIni}')
    print(f'O dia da semana de data_final é: {dia_da_semanaFim}')



def calcular_horas(data_inicial, data_final):
    horas = timedelta()
    data_atual = data_inicial
    dias_da_semana = [
        {'dia': 0, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
        {'dia': 1, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
        {'dia': 2, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
        {'dia': 3, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
        {'dia': 4, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
        {'dia': 5, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': False},
        {'dia': 6, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': False},
    ]

    if data_inicial < data_final:
        while data_atual.date() <= data_final.date():
            dia = next((x for x in dias_da_semana if x['dia'] == data_atual.weekday() and x['util']), None)
            if dia is not None:
                h_inicial = datetime.strptime(dia['hora_inicial'], '%H:%M:%S')
                h_almoco = datetime.strptime(dia['hora_almoco'], '%H:%M:%S')
                h_retorno = datetime.strptime(dia['retorno_almoco'], '%H:%M:%S')
                h_fim = datetime.strptime(dia['hora_saida'], '%H:%M:%S')

                h_inicial = max(data_inicial, datetime.combine(data_atual.date(), h_inicial.time()))
                h_almoco = min(data_final, datetime.combine(data_atual.date(), h_almoco.time()))
                h_retorno = max(data_inicial, datetime.combine(data_atual.date(), h_retorno.time()))
                h_fim = min(data_final, datetime.combine(data_atual.date(), h_fim.time()))

                horas += h_almoco - h_inicial if h_almoco > h_inicial else timedelta()
                horas += h_fim - h_retorno if h_fim > h_retorno else timedelta()

            data_atual += timedelta(days=1)
    else:
        raise Exception("Data inicial deve ser menor que a data final")

    # Converter os segundos totais em horas e minutos
    horas_totais = horas.total_seconds() // 3600
    minutos_totais = (horas.total_seconds() % 3600) // 60

    return f'{int(horas_totais)} horas e {int(minutos_totais)} minutos'
