import nltk
from nltk import word_tokenize
from nltk.corpus import conll2000


def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)
    return '+'.join(sorted(tags))


def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i - 1]
    if i == len(sentence) - 1:
        nextword, nextpos = "<END>", "<END>"
    else:
        nextword, nextpos = sentence[i + 1]
    return {"pos": pos,
            "word": word,
            "prevpos": prevpos,
            "nextpos": nextpos,
            "prevpos+pos": "%s+%s" % (prevpos, pos),
            "pos+nextpos": "%s+%s" % (pos, nextpos),
            "tags-since-dt": tags_since_dt(sentence, i)}


class ConsecutiveNPChunkTagger(nltk.TaggerI):  # [_consec-chunk-tagger]

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)  # [_consec-use-fe]
                train_set.append((featureset, tag))
                history.append(tag)
        algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[0]
        self.classifier = nltk.MaxentClassifier.train(  # [_consec-use-maxent]
            train_set, algorithm=algorithm, trace=0)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)


class ConsecutiveNPChunker2(nltk.ChunkParserI):  # [_consec-chunker]
    def __init__(self, train_sents):
        tagged_sents = [[((w, t), c) for (w, t, c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w, t, c) for ((w, t), c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)


# chunker = ConsecutiveNPChunker(train_sents)
# print(chunker.evaluate(test_sents))

# tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')

# tokenized_content = tokenizer.tokenize(txt)
# content_model = nltk.NgramModel(3, tokenized_content)

# starting_words = content_model.generate(100)[-2:]
# content = content_model.generate(words_to_generate, starting_words)
# print ' '.join(content)


# get training and testing data

class ChunkParser(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)]
            for sent in train_sents]
        self.tagger = nltk.TrigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        # entities = nltk.chunk.ne_chunk(tagged_pos_tags)
        # print entities
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag)
            in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)


test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
# training the chunker
NPChunker = ChunkParser(train_sents)
print NPChunker.evaluate(test_sents)


try:
    sentences = nltk.sent_tokenize(txt)  # NLTK default sentence segmenter
    sentences = [nltk.word_tokenize(sent) for sent in sentences]  # NLTK word tokenizer
    sentences = [nltk.pos_tag(sent) for sent in sentences]  # NLTK POS tagger
except LookupError:
    nltk.download()

tokens = word_tokenize(txt)
text = nltk.Text(tokens)

grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """
for sentence in sentences:
    cp = nltk.RegexpParser(grammar)
    # print(cp.parse(sentence))
