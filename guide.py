import re, time, random
from colorama import Back, Fore, Style, init

init(autoreset=True)

colors = [Fore.GREEN, Fore.BLUE, Fore.RED, Fore.MAGENTA, Fore.CYAN]

chosen_color = random.choice(colors)

def slow_print(text, color=chosen_color, delay=0.1):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def clean_sentence(sentence):
    sentence = re.sub(r'[#*]', '', sentence)
    sentence = re.sub(r'\(.*?\)', '', sentence)
    sentence = re.sub(r'\[\[❞\]\]', '', sentence)
    return sentence

def split_into_sentences(content):
    sentences = re.split(r'(?<=[.!?]) +', content)
    return sentences

def teach_in_batches(sentences, batch_size):
    total_sentences = len(sentences)
    for i in range(0, total_sentences, batch_size):
        batch = sentences[i:i + batch_size]
        print(f"{Back.BLUE}{Fore.YELLOW}Batch {i//batch_size + 1}:{Style.RESET_ALL}")
        for sentence in batch:
            slow_print(clean_sentence(sentence))
        input(f"\n{Fore.YELLOW}Press Enter to continue to the next batch...{Style.RESET_ALL}\n")

def main():
    file_path = '.content.txt'
    batch_size = 5

    content = read_file(file_path)
    sentences = split_into_sentences(content)
    teach_in_batches(sentences, batch_size)

if __name__ == "__main__":
    main()
