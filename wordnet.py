from nltk.corpus import wordnet


synonym=[]
antonym=[]

for i in wordnet.synsets("good"):
   for l in i.lemmas():
       synonym.append(l.name())
       if l.antonyms():
           antonym.append(l.antonyms()[0].name())


print(set(synonym))
print(set(antonym))
      