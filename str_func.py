def to_upper_case(string):
    """Возвращает строку, состоящую из заглавных букв"""
    return string.upper()


def to_upper_case_first_symbols(string):
    """Возвращает строку из слов, начинающихся с заглавной буквы"""
    words = str(string).split()
    result_string = " ".join([word[0].upper() + word[1:] for word in words])
    return result_string


