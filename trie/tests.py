from trie import Trie
from unittest import TestCase, main


class TrieBuildTest(TestCase):
    """
    Test class fo trie build
    """
    def test_trie_build_1(self):
        """
        first test for trie build
        :return:
        """
        # First test to build the tree with an empty list
        trie_1 = Trie("tests/test_file_1.csv")
        self.assertEqual(trie_1.trie, {})

    def test_trie_build_2(self):
        """
        second test for trie build
        :return:
        """
        # Building trie with same starting letters
        trie_2 = Trie("tests/test_file_2.csv")
        self.assertEqual(trie_2.trie,
                         {'a': {'keyword_indexes': [0, 1, 2, 3],
                                'b': {'_end_': '_end_'}, 'd': {'keyword_indexes': [0, 1, 3],
                                                               'o': {'keyword_indexes': [0, 1, 3],
                                                                     'b': {'_end_': '_end_', 'keyword_indexes': [1],
                                                                           'e': {'_end_': '_end_'}},
                                                                     'o': {'_end_': '_end_'}}}},
                          'keyword_indexes': [0, 1, 2, 3]})

    def test_trie_build_3(self):
        """
        first test for trie build
        :return:
        """
        # Building the trie with different strings
        trie_3 = Trie("tests/test_file_3.csv")
        self.assertEqual(trie_3.trie,
                         {'a': {'keyword_indexes': [0],
                                'd': {'keyword_indexes': [0],
                                      'o': {'keyword_indexes': [0],
                                            'b': {'_end_': '_end_'}}}},
                          'B': {'a': {'s': {'_end_': '_end_'},
                                      'keyword_indexes': [1]}, 'keyword_indexes': [1]},
                          'keyword_indexes': [0, 1, 2, 3],
                          'S': {'i': {'keyword_indexes': [3],
                                      'l': {'i': {'c': {'keyword_indexes': [3],
                                                        'o': {'keyword_indexes': [3],
                                                              'n': {'_end_': '_end_'}}},
                                                  'keyword_indexes': [3]},
                                            'keyword_indexes': [3]}}, 'keyword_indexes': [3]},
                          'C': {'keyword_indexes': [2], 'd': {'keyword_indexes': [2],
                                                              'e': {'s': {'_end_': '_end_'},
                                                                    'keyword_indexes': [2]}}}})


class TrieSearchTest(TestCase):
    """
    Test class fo trie search
    """
    def test_trie_search_1(self):
        """
        first test for trie search
        :return:
        """
        trie_1 = Trie()
        trie_1.build("tests/test_file_1.csv")
        self.assertEqual(trie_1.search('aa'), [])

    def test_trie_search_2(self):
        """
        first test for trie search
        :return:
        """
        trie_2 = Trie("tests/test_file_2.csv")
        self.assertEqual(trie_2.search('a'), ['Adob', 'adobe', 'aB', 'adoo'])

    def test_trie_search_3(self):
        """
        first test for trie search
        :return:
        """
        trie_3 = Trie("tests/test_file_2.csv")
        self.assertEqual(trie_3.search('ad'), ['Adob', 'adobe', 'adoo'])

    def test_trie_search_4(self):
        """
        first test for trie search
        :return:
        """
        trie_4 = Trie("tests/test_file_2.csv")
        self.assertEqual(trie_4.search('adob'), ['Adob', 'adobe'])


if __name__ == '__main__':
    main()
