from keras.preprocessing import sequence
import nltk
import numpy as np
INPUT_SENTENCES = ['23 28 reading.','You are so boring.']
XX = np.empty(len(INPUT_SENTENCES),dtype=list)
XX = np.array([[23,28,35],[4,27, 28, 39]])
# i=0
# for sentence in  INPUT_SENTENCES:
#     words = nltk.word_tokenize(sentence.lower())
#     seq = []
#     for word in words:
#         if word in word2index:
#             seq.append(word2index[word])
#         else:
#             seq.append(word2index['UNK'])
#     XX[i] = seq
#     i+=1

XX = sequence.pad_sequences(XX, dtype=str)
print (XX)
# labels = [int(round(x[0])) for x in model.predict(XX) ]