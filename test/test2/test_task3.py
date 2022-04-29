from src.test2.task3 import count_sentences, get_words_statistic, WordStatistic


def test_sentence_counter():
    with open("../../test2/text.txt") as file:
        text = file.read()
        assert 6 == count_sentences(text)


def test_words_counter():
    with open("../../test2/text.txt") as file:
        text = file.read()
        words_statistic = get_words_statistic(text, 3)
        assert WordStatistic("the", 4) == words_statistic[0]
        assert WordStatistic("how", 3) == words_statistic[1]
        assert WordStatistic("with", 3) == words_statistic[2]
