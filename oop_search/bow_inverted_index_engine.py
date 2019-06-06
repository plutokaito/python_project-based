from search_base import SearchEngineBase
import re

class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.__inverted_index = {}

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.__inverted_index:
                self.__inverted_index[word] = []
            self.__inverted_index[word].append(id)

    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()

        for query_word in query_words:
            if  query_word not in self.__inverted_index:
                return []
            query_words_index.append(0)

        result = []
        # 每个词分词后，查询所有索引对应的文档信息，
        while True:
            current_ids = []
            for idx,query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.__inverted_index[query_word]

                if current_index >=  len(current_inverted_list):
                    return result
                current_ids.append(current_inverted_list[current_index])

            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x+1 for x in query_words_index]
                continue

            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        text = re.sub(r'[^\w]', ' ', text)
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None, word_list)
        return set(word_list)