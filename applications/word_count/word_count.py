def word_count(s):
    word_counts = {}
    ignored = ':;,.-+=/\|[]"{}()*^&'
    words = s.split()
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            new_word = ""
            for char in word:
                if char not in ignored:
                    new_word += char
            if new_word != "":
                if new_word in word_counts:
                    word_counts[new_word] += 1
                else:
                    word_counts[new_word] = 1
    return word_counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
