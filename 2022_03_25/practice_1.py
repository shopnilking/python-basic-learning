text = "amar sonar bangla ami tomoay valobashi"
# result = ['amar', 'ami']
# first = ["amar", "sonar", "bangla", "ami", "tomoay", "valobashi"]
# second = ["amar", "ami"]

# Method 1
# words = text.split()
# # print (words)

# result = []
# for word in words:
#     # get single word
#     # get first two letters from that single word
#     # check the conditions
#     # when conditon is true, append the word to result
#     if(word[:2] == "am"):
#         result.append(word)

# print(result)

# Method 2
words = text.split()

result = []
for word in words:
    # get single word
    # get first two letters from that single word
    # check the conditions
    # when conditon is true, append the word to result
    if(word.startswith("am")):
        result.append(word)

print(result)