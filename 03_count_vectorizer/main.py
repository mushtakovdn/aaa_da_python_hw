from typing import List, Dict, Iterable
import string


class CountVectorizer:
    """
    Класс для векторизации текстов
    """

    def __init__(self):
        self._vocabulary = {}
        self._pointer_of_next_col_num = 0
        self.count_matrix = []

    def get_feature_names(self, ):
        """Возвращет список всех слов, которые были в корпусе текста"""
        return list(self._vocabulary.keys())

    def _fill_vectors(self):
        """
        После обучения на всех документах из обучающего корпуса
        заполняет все промежуточные вектора до полной длины
        """
        MATRIX_WIDTH = len(self._vocabulary)
        for vector in self.count_matrix:
            vector_shortage = MATRIX_WIDTH - len(vector)
            vector.extend([0 for i in range(vector_shortage)])

    def _process_tokens(self, tokens: List[str]) -> Dict[str, int]:
        """
        Выполняет с текущим списком токенов два действия:
        1. обновляет перечень слов присутствующих в корпусе текста
        {слово: номер столбца в матрице}
        2. Возвращает счетчик - словарь {слово: количество вхождений}

        Два действия объеденены в один метод, чтобы не итерироваться дважды
        """
        counter = {}
        for word in tokens:
            # 1
            if word not in self._vocabulary:
                self._vocabulary[word] = self._pointer_of_next_col_num
                self._pointer_of_next_col_num += 1
            # 2
            counter[word] = counter.get(word, 0) + 1
        return counter

    def _get_interim_vector(self, tokens: List[str]) -> List[int]:
        """
        Возвращает промежуточный вектор.
        Длина вектора равна количеству уникальных слов найденных в обучающем
        корпусе текста на текущим момент
        """
        counter = self._process_tokens(tokens)
        vector = [0 for w in self._vocabulary]  # инициализация вектора
        for word, counts in counter.items():
            position = self._vocabulary[word]
            vector[position] = counts
        return vector

    def _tokenize(self, doc: str) -> List[str]:
        """
        Принимает на вход один документ (строку) и токенизирует
        """
        doc = doc.lower()
        # remove punctuation
        for symbol in string.punctuation:
            doc = doc.replace(symbol, '')
        return doc.split()

    def fit_transform(self, raw_documents: Iterable[str]) -> List[int]:
        """
        Обучение на корпусе текста.
        Затем преобразование корпуса текста в вектора
        """
        for cur_doc in raw_documents:
            tokens = self._tokenize(cur_doc)
            vector = self._get_interim_vector(tokens)
            self.count_matrix.append(vector)
        self._fill_vectors()
        return self.count_matrix


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
        'This tomato pasta could be even better with Parmesan.'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
