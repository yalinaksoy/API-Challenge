from trie import Trie
from unittest import TestCase, main


class TrieBuildTest(TestCase):
    """
    Test class fo trie build
    """
    def trie_build_test_1(self):
        """
        first test for trie build
        :return:
        """
        # First test to build the tree with an empty list
        trie_1 = Trie()
        self.assertequal(trie_1.build([]), {})

    def trie_build_test_2(self):
        """
        second test for trie build
        :return:
        """
        # Building trie with same starting letters
        trie_2 = Trie()
        self.assertequal(trie_2.build(['adob', 'adobe', 'ab', 'adoo']),
                         {'a': {'keyword_indexes': [0, 1, 2, 3],
                                'b': {'_end_': '_end_'}, 'd': {'keyword_indexes': [0, 1, 3],
                                                               'o': {'keyword_indexes': [0, 1, 3],
                                                                     'b': {'_end_': '_end_', 'keyword_indexes': [1],
                                                                           'e': {'_end_': '_end_'}},
                                                                     'o': {'_end_': '_end_'}}}},
                          'keyword_indexes': [0, 1, 2, 3]})

    def trie_build_test_3(self):
        """
        first test for trie build
        :return:
        """
        # Building the trie with different strings
        trie_3 = Trie()
        self.assertequal(trie_3.build(['adob', 'Bas', 'Cdes', 'Silicon']),
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
    def trie_search_test_1(self):
        """
        first test for trie search
        :return:
        """
        trie_1 = Trie()
        trie_1.build([])
        self.assertequal(trie_1.search('aa'), [])

    def trie_search_test_2(self):
        """
        first test for trie search
        :return:
        """
        trie_2 = Trie()
        trie_2.build(['adob', 'adobe', 'ab', 'adoo'])
        self.assertequal(trie_2.search('a'), ['adob', 'adobe', 'ab', 'adoo'])

    def trie_search_test_3(self):
        """
        first test for trie search
        :return:
        """
        trie_3 = Trie()
        trie_3.build(['adob', 'adobe', 'ab', 'adoo'])
        self.assertequal(trie_3.search('ad'), ['adob', 'adobe', 'adoo'])

    def trie_search_test_4(self):
        """
        first test for trie search
        :return:
        """
        trie_4 = Trie()
        trie_4.build(['adob', 'adobe', 'ab', 'adoo'])
        self.assertequal(trie_3.search('adob'), ['adob', 'adobe'])






        # will be implemented and tests wil be added
        return True
