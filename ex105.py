'''EXERCÍCIO 105
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(*n,sit=False):
    """->Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma."""
    resultados = dict()
    resultados['total'] = len(n)
    resultados['maior'] = max(n)
    resultados['menor'] = min(n)
    resultados['media'] = sum(n) / len(n)

    if sit:
        if resultados['media'] < 5:
            resultados['situação'] = 'RUIM'
        elif 5 <= resultados['media'] < 7:
            resultados['situação'] = 'RAZOÁVEL'
        else:
            resultados['situação'] = 'Boa'
    return resultados


resp = notas(5.5,9.5,10,6.5,sit=True)
print(resp)
help(notas)