import spacy

# Extract entities from string


def get_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


# Extract sentences from a string


def get_sentences(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences


# Extract adjectives from the string


def get_adjectives(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    return adjectives


# Extract adverbs from the string


def get_adverbs(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    adverbs = [token.text for token in doc if token.pos_ == "ADV"]
    return adverbs


# Extract nouns from the string


def get_nouns(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    return nouns
