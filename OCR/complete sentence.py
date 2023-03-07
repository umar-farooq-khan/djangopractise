import nltk
from nltk.tokenize import word_tokenize
from nltk.parse import DependencyGraph, malt

sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Parse the sentence using the MaltParser
parser = malt.MaltParser()
graph = parser.parse_one(tokens)

# Check if the sentence is a complete grammatical sentence
is_complete = all(node['head'] != 0 for node in graph.nodes.values() if node['word'] not in ['ROOT', 'TOP'])

print(is_complete)
