# program to get a user input a sentene and change every other letter into a capital letter and 
# then repeat changing every other word to capitals and finally print out the resulting string (sentences) one by one

# input variable
input_sentence = input("Input a sentence to be converted to alternate capital and lowercase\n")

# my defined functions
def alternate_Uppercase_word(s):
    i = 0
    word_list = s.split(' ')
    alternate_upper = []
    for w in word_list:
        if i:
            alternate_upper.append(w.upper())
        else:
            alternate_upper.append(w)
        i = int(not i)
    return " ".join(alternate_upper)

# main loop
altered_sentence = ''.join([e.upper() if i % 2 == 0 else e for i, e in enumerate(input_sentence)])
print("The sentence you entered looks like this with every other letter capitalised:")
print(altered_sentence)

print("The sentence you entered looks like this with every other word capitalised:")
print(alternate_Uppercase_word(input_sentence))