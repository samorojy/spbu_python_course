import re
from collections import Counter
from dataclasses import dataclass
from typing import List

word_pattern = re.compile("[а-яА-Яa-zA-Z]+")
sentence_pattern = re.compile("[.!?]+")


@dataclass(frozen=True)
class WordStatistic:
    word: str
    frequency: int


def get_words_statistic(text, top_size) -> List[WordStatistic]:
    counter: "Counter" = Counter()
    for word in word_pattern.findall(text):
        counter[word.lower()] += 1
    return [WordStatistic(word, freq) for word, freq in counter.most_common(top_size)]


def count_sentences(text: str) -> int:
    return len(sentence_pattern.findall(text))


if __name__ == "__main__":
    with open("text.txt") as file:
        text = file.read()
        print(f"There are {count_sentences(text)} sentences in the text")
        print("Top words:")
        for word_frequency in get_words_statistic(text, 10):
            print(f"{word_frequency.word} -> {word_frequency.frequency} times")
