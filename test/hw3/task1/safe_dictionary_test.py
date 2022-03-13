from threading import Thread

from src.hw3.task1.safe_dictionary import SafeDictionary


def test_safe_dictionary_multithread():
    safe_dictionary = SafeDictionary()

    with safe_dictionary.modify() as sd:
        sd[2] = 10

    def dictionary_modify(safe_dict, key: int, value: int):
        with safe_dict.modify() as sd:
            sd[key] = value

    threads = [
        Thread(target=dictionary_modify, args=(safe_dictionary, key, key**2))
        for key in range(1, 4)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    with safe_dictionary.modify() as sd:
        assert sd[1] == 1
        assert sd[2] == 4
        assert sd[3] == 9
