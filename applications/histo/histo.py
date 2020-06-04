with open("robin.txt") as f:
    text = f.read()


def show_histo(s):
    longest = 0
    word_counts = {}
    ignored = '":;,.-+!?=/\|[]{}()*^&'
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
                longest = len(new_word) if len(new_word) > longest else longest
                if new_word in word_counts:
                    word_counts[new_word] += 1
                else:
                    word_counts[new_word] = 1
    for wp in sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True):
        print(f"{wp[0]:{longest}}  {'#'*wp[1]}")


show_histo(text)
