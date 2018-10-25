import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize


sample=state_union.raw("2006-GWBush.txt")
word=word_tokenize(sample)
tag=nltk.pos_tag(word)
try:
    chunkgram=r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkparser=nltk.RegexpParser(chunkgram)
    chunk=chunkparser.parse(tag)

    chunk.draw()
except Exception as e:
    print(str(e))