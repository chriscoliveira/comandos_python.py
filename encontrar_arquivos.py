import os

caminho_procura = '/home/adming/Área de Trabalho'
termo_procura = 'xls'


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


contador = 0
print(f'\nExibindo resultados para a busca em "{caminho_procura}" com o termo "{termo_procura}"')
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print(
                    f'\nEncontrei o arquivo: {arquivo}\n'
                    f'\tCaminho:{caminho_completo}\n'
                    f'\tNome:{arquivo}\n'
                    f'\tExtensao: {extensao_arquivo}\n'
                    f'\tTamanho: {formata_tamanho(tamanho)}')
            except PermissionError as e:
                print('Sem permissao')
            except FileNotFoundError as e:
                print('Arquivo nao encontrado')
            except Exception as e:
                print('Erro desconhecido: ' + e)
print(f'\n Foi encontrado {contador} arquivo(s)')
