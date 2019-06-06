#from simple_engine import SimpleEngine
#from bow_engine import BOWEngine
#from bow_inverted_index_engine import BOWInvertedIndexEngine
from bowii_engine_cache import BOWInvertedIndexEngineWithCache

DIR_PATH = './step_up/oop_search/'

def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(DIR_PATH + file_path)

    while True:
        query = input('please input what do u wanna:')
        results = search_engine.search(query)
        print(f"found {len(results)} result(s):")
        for result in results:
            print(result)

if __name__ == '__main__':
    # search_engine = SimpleEngine()
    #search_engine = BOWEngine()
    # search_engine = BOWInvertedIndexEngine()
    search_engine = BOWInvertedIndexEngineWithCache()
    main(search_engine)