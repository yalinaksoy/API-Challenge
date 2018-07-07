

class Trie:
    def __init__(self):
        self.trie = self.parse_build()

    def parse(self):
        """
        takes the input file and converts it into a sorted array
        :return file array:
        """
        return []

    def build(self, input_list = []):
        """
        builds the trie from sorted list
        :param input_list: list of the input read from a file or given by hand for test purposes
        :return trie: the final prefix trie in the correct format
        """
        return {}

    def search(self, keyword = None):
        """
        searches the trie and finds related keywords
        main function for the API used after the trie is builded
        :param keyword: keyword to search
        :return result: list of related keywords
        """
        return []
