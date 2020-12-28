def title_func(sentence):
    """
    Функция принимает набор слов и прелбразует каждое слово с прописной буквы
    :param sentence: принимаемая функцией стройка из слов
    :return: возвращает строку вида: Возвращаемая Функцией Стройка Из Слов
    """
    return (sentence.title())

result = title_func(input('Введите несколько слов: '))
print(result)