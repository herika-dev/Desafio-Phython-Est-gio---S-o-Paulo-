#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

try:
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)

    # Verificando se o arquivo JSON tem a estrutura esperada
    if isinstance(dados, list) and all(isinstance(dia, dict) and 'valor' in dia for dia in dados):
        faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
        if faturamentos:
            menor_faturamento = min(faturamentos)
            maior_faturamento = max(faturamentos)
            media_mensal = sum(faturamentos) / len(faturamentos)
            dias_acima_da_media = len([valor for valor in faturamentos if valor > media_mensal])

            print(f"Menor faturamento: {menor_faturamento}")
            print(f"Maior faturamento: {maior_faturamento}")
            print(f"Dias acima da média: {dias_acima_da_media}")
        else:
            print("Nenhum faturamento válido encontrado.")
    else:
        print("Estrutura do arquivo JSON está incorreta.")

except FileNotFoundError:
    print("Erro: O arquivo 'faturamento.json' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: Não foi possível decodificar o arquivo JSON.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")