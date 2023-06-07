def read():
    with open('pan-tadeusz-unix.txt') as filehandle:
        words = []
        for line in filehandle:
            line_words = line.split(' ')
            for word in line_words:
                if '\n' in word:
                    word = word[:-1]
                if word != '':
                    words.append(word)
    return words
