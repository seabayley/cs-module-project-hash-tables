import random
text = ""
word_table = {}
previous_word = None
keys = word_table.keys()
# Read in all the words in one go
with open("input.txt") as f:
    text = f.read()

data = text.split()

for word in data:
    if word not in keys:
        word_table[word] = []
    if previous_word is not None:
        if previous_word in word_table.keys():
            word_table[previous_word].append(word)
    previous_word = word


class MarkovGenerator:

    def __init__(self, word_table):
        self.word_table = word_table
        self.max_sentence_length = 20
        self.min_sentence_length = 3
        self.keys = list(word_table.keys())
        self.stop_words = [i for i in self.keys if self.is_stop_word(i)]
        self.start_words = [i for i in self.keys if self.is_start_word(i)]

    @staticmethod
    def is_stop_word(word):
        return word[-1] in "?.!" or word[-1] == '"' and word[-2] in "?.!"

    @staticmethod
    def is_start_word(word):
        return word[0].isupper() or word[0] == '"' and word[1].isupper()

    @staticmethod
    def can_close(word, punc):
        word[-1] == punc

    def opens_para(self, word):
        return word[0] == '('

    def opens_quote(self, word):
        return word[0] == '"'

    def generate_word(self, current_word):
        word = None
        if current_word == None:
            word = random.choice(self.start_words)
        else:
            if self.word_table[current_word] != []:
                word = random.choice(self.word_table[current_word])
            else:
                word = False
        return word

    def generate_sentence(self):
        sentence_complete = False
        open_quote = False
        open_para = False
        last_word = None
        word_array = []

        while not sentence_complete:
            current_word = self.generate_word(last_word)
            if current_word is False:
                sentence_complete = True
            else:
                if self.opens_para(current_word):
                    if open_para:
                        continue
                    open_para = True
                if self.opens_quote(current_word):
                    if open_quote:
                        continue
                    open_quote = True
                if self.is_stop_word(current_word):
                    if not open_quote and not open_para:
                        word_array.append(current_word)
                        sentence_complete = True
                else:
                    word_array.append(current_word)
                last_word = current_word
            # Check if opening a parenthesis or quotation
            # Generate the next word, if parenthesis or quotation is open, get one of those closers if available. Until min_length
            # If word is a closing word add it close only if parenthesis and quotations are closed.

        return ' '.join(word_array)


mg = MarkovGenerator(word_table)
print(mg.generate_sentence())
