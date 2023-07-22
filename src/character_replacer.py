MAPPING = {
    'ë': 'ẹ',
    'ö': 'ọ',
    'ä': 'ạ',
    'ê': 'ệ',
    'â': 'ậ',
    'ô': 'ộ',
    'y': 'ɨ',
    'å': 'ẫ',
    'ā': 'ẫ',
    'ă': 'ẫ',
    'ŏ': 'ṍ',
    'ø': 'ṍ'
}

def replace_characters(input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            input_text = file.read()

        replaced_text = input_text
        for char_in, char_out in MAPPING.items():
            replaced_text = replaced_text.replace(char_in, char_out)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(replaced_text)

        print("Substituições feitas com sucesso.")

if __name__ == "__main__":
    input_file_path = input("Digite o nome do arquivo de entrada: ")
    output_file_path = input("Digite o nome do arquivo de saída: ")
    replace_characters(input_file_path, output_file_path)
