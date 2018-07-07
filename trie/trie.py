

class Trie:
    def __init__(self, source_file_path=None):
        # Will be used for reach indexes of keyword in the sake of speed
        self.indexed_file = []
        # Actual Trie where searching will be done
        self.trie = self.build(self.parse(source_file_path))
        pass

    def parse(self, source_file):
        """
        takes the input file and converts it into a sorted array
        :return file array:
        """
        file_list = []
        try:
            with open(source_file, "r") as inp_file:
                for line in inp_file.readlines():
                    self.indexed_file.append(line.strip())
                    file_list.append(line.strip().lower())
        except Exception as e:
            raise e
        self.indexed_file = sorted(self.indexed_file, key=lambda k: k.upper())
        return sorted(file_list, key=lambda k: k.upper())

    def build(self, input_list=list()):
        """
        builds the trie from sorted list
        :param input_list: list of the input read from a file or given by hand for test purposes
        :return trie: the final prefix trie in the correct format
        """
        # It is the basic trie format with a little twist
        # I also keep the keyword indexes which is referred under that root by their indexes
        # It will take more memory than needed bu it will be fast
        final_trie = {}

        # this C kind of for loop is for keeping the indexes to fasten the process during search
        for entry_index in range(len(input_list)):
            curr_trie = final_trie
            for single_char in input_list[entry_index]:
                # Keyword indexes will be used for speed of autocomplete
                # Increases memory complexity but a huge boost for speed so I am up for it
                if curr_trie.get('keyword_indexes', False):
                    curr_trie['keyword_indexes'].append(entry_index)
                else:
                    curr_trie['keyword_indexes'] = [entry_index]
                # Trie structure as it is
                curr_trie = curr_trie.setdefault(single_char, {})

            # word is ended and added to trie
            curr_trie['_end_'] = '_end_'
        return final_trie

    def search(self, keyword=None):
        """
        searches the trie and finds related keywords
        main function for the API used after the trie is builded
        :param keyword: keyword to search
        :return result: list of related keywords
        """
        current_trie = self.trie
        # cover all the cases regardless of cases of input letters
        keyword = keyword.lower()
        for single_char in keyword:
            # We are matching things great
            if single_char in current_trie:
                current_trie = current_trie[single_char]
            # No candidate found do not continue furthermore
            else:
                return []
        # Found the exact keyword
        if '_end_' in current_trie:
            return [keyword]
        else:
            # List the candidates
            final_list = []
            for index in current_trie['keyword_indexes']:
                final_list.append(self.indexed_file[index])
            return final_list
