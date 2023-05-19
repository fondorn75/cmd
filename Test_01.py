from checkText import checkText


def test_step1(right_word, wrong_word):
    assert right_word in checkText(wrong_word)
