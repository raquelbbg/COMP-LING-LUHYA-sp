import nltk
grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V PP
  PP -> P NP
  NP -> N | Det N
  Det -> 'the'
  N -> 'Mary' | 'tuka'
  V -> 'atavire'
  P -> 'mwi'
""")
parser = nltk.ChartParser(grammar)
sentence = "Mary atavire mwi tuka".split()
for tree in parser.parse(sentence):
    print(tree)