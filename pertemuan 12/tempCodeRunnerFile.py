def reverse_string(word):
    if len(word)== 0:
        return word
    else:
        return reverse_string(word[0]+ word[1:])
text = 'halo'
reversed_word = reverse_string(text)
print(reversed_word)
