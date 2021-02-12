import os
import shutil

caminho_original = 'Z:\Christian\Arquivos\Zabbix\BKP_ZABBIX_TENDA_novo'
caminho_novo = 'Z:\Christian\Arquivos\Zabbix\BKP_ZABBIX_TENDA'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'\tPasta {caminho_novo} ja existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        print(new_file_path)
        # movendo arquivos
        # if '.png' in file:
        #     shutil.move(old_file_path, new_file_path)
        # print(f'Arquivo {file} movido com sucesso!')

        # copiando arquivos
        # if '.png' in file:
        #     shutil.copy(old_file_path, new_file_path)
        # print(f'Arquivo {file} movido com sucesso!')

        # remover arquivos
        # if '.png' in file:
        #     os.remove(new_file_path)
