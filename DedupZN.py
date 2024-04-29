def remove_duplicate_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    unique_lines = []
    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    remove_duplicate_lines(input_file, output_file)

if __name__ == '__main__':
    main()