import re

files = [
    'noms_nadons_1997_clean.txt',
    'noms_nadons_2024_clean.txt'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        texto = f.read()

    # modifications
    mod_text = re.sub(r'/', '\n', texto)
    mod_text = re.sub(r' ', '-', mod_text)

    # creating name for new file
    new_name = file.replace('.txt', '_mod.txt')

    with open(new_name, 'w', encoding='utf-8') as f:
        f.write(mod_text)

    print(f"{file} to {new_name}")