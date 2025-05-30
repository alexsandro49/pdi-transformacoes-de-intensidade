import os
import sys

asset_names = []
with os.scandir('assets') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            asset_names.append(entry.name)


def parse_asset_index():
    if len(sys.argv) != 2:
        print('\033[34mÍndice   Nome\033[0m')
        for index, asset in enumerate(asset_names):
            print(f'{index}: {asset}')

        sys.exit('\n\033[34mUso: python main.py indice_do_arquivo\033[0m')

    file_index = int(sys.argv[1])
    if not 0 <= file_index < len(asset_names):
        # 0 int(sys.argv[1])
        sys.exit('\033[31mErro: Índice inválido\033[0m')

    else:
        return asset_names[file_index]
