import re
import os


def main():
    pop_dict = load_populism_dictionary('./populism_dict.csv')

    texts = ['./texts/' + file for file in os.listdir('./texts') if os.path.isfile('./texts/' + file) and file.endswith(".txt")]

    for path in texts:
        lines = load_text(path)
        name = lines[0].strip()
        paragraphs = lines[1:]

        print(f"Analyzing {name}:")    

        counter, found_patterns = find_patterns(paragraphs, pop_dict)
        
        print(f"Found {counter} pattern(s) from the populism dictionary")
        print('#Populism dictionary matches:')
        print_matches(found_patterns)


def load_populism_dictionary(path:str ) -> list[re.Pattern]:
    dictionary = []
    with open(path) as file:
        for line in file.readlines():
            try:
                dictionary.append(re.compile(line.strip()))
            except Exception as e:
                print("Error: " + line)
                print(e)
    return dictionary


def load_text(path: str) -> list[str]: 
    with open(path) as file:
        lines = file.readlines()
        lines = [line for line in lines if line.strip() != '']
    return lines


def find_patterns(paragraphs: list[str], patterns: list[re.Pattern]):
    counter = 0
    found_patterns = []
    for i in range(len(paragraphs)):
        p = paragraphs[i]
        for pattern in patterns:
            res = pattern.findall(p.lower())
            if len(res) > 0:
                counter+=1
                found_patterns.append((str(pattern.pattern), i))
    return counter, found_patterns


def print_matches(matches: list):
    print('Paragraph\tPattern')
    print('---')
    for (p, i) in matches:
        print(f'{i+1}\t{p}')
    print()


if __name__ == '__main__':
    main()