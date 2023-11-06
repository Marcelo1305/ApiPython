from datetime import datetime, timedelta

def calcular_horas(data_inicial, data_final, dados = None):
    # Inicializa a variável horas como um objeto timedelta, que representa a diferença entre duas datas ou horas
    horas = timedelta()

    # Atribui o valor de data_inicial à variável data_atual
    data_atual = data_inicial

    if dados == None:
        # Define uma lista de dicionários com informações sobre os dias da semana e horários associados
        dados = [
            {'dia': 0, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
            {'dia': 1, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
            {'dia': 2, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
            {'dia': 3, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
            {'dia': 4, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': True},
            {'dia': 5, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': False},
            {'dia': 6, 'hora_inicial': '08:00:00', 'hora_almoco': '12:00:00', 'retorno_almoco': '13:00:00', 'hora_saida': '17:00:00', 'util': False},
        ]

    # Verifica se a data inicial é menor que a data final
    if data_inicial < data_final:

        # Enquanto a data atual for menor ou igual à data final
        while data_atual.date() <= data_final.date():
            # Procura na lista dados por um dicionário correspondente ao dia da semana da data_atual e que seja considerado útil
            dia = next((x for x in dados if x['dia'] == data_atual.weekday() and x['util']), None)

            # Verifica se foi encontrado um dicionário correspondente ao dia da semana
            if dia is not None:
                # Converte os horários de string para objetos datetime
                h_inicial = datetime.strptime(dia['hora_inicial'], '%H:%M:%S')
                h_almoco = datetime.strptime(dia['hora_almoco'], '%H:%M:%S')
                h_retorno = datetime.strptime(dia['retorno_almoco'], '%H:%M:%S')
                h_fim = datetime.strptime(dia['hora_saida'], '%H:%M:%S')

                # Ajusta os horários de acordo com a data atual
                h_inicial = max(data_inicial, datetime.combine(data_atual.date(), h_inicial.time()))
                h_almoco = min(data_final, datetime.combine(data_atual.date(), h_almoco.time()))
                h_retorno = max(data_inicial, datetime.combine(data_atual.date(), h_retorno.time()))
                h_fim = min(data_final, datetime.combine(data_atual.date(), h_fim.time()))

                # Calcula e acumula as horas trabalhadas
                horas += h_almoco - h_inicial if h_almoco > h_inicial else timedelta()
                horas += h_fim - h_retorno if h_fim > h_retorno else timedelta()

            # Avança para o próximo dia
            data_atual += timedelta(days=1)
    else:
        # Se a data inicial não for menor que a data final, levanta uma exceção
        raise Exception("Data inicial deve ser menor que a data final")

    # Converte os segundos totais em horas e minutos
    horas_totais = horas.total_seconds() // 3600
    minutos_totais = (horas.total_seconds() % 3600) // 60

    # Retorna uma string formatada com o total de horas e minutos
    return f'{int(horas_totais)} horas e {int(minutos_totais)} minutos'