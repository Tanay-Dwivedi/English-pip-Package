import spacy
import py3langid as langid
from textblob import TextBlob
from profanity_check import predict, predict_prob
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import textstat

nltk.download("en_core_web_sm")
nltk.download("en_core_web_md")

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


# Extract pronouns from the string


def get_pronouns(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    return pronouns


# Extract proper nouns from the string


def get_proper_nouns(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    proper_nouns = [token.text for token in doc if token.pos_ == "PROPN"]
    return proper_nouns


# Extract verbs from the string


def get_verbs(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    return verbs


# Extract numbers from the string


def get_numbers(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    numbers = [token.text for token in doc if token.pos_ == "NUM"]
    return numbers


# Detect language of the text


def detect_language(text):
    try:
        language_code, _ = langid.classify(text)

        language_names = {
            "af": "Afrikaans",
            "am": "Amharic",
            "an": "Aragonese",
            "ar": "Arabic",
            "as": "Assamese",
            "az": "Azerbaijani",
            "be": "Belarusian",
            "bg": "Bulgarian",
            "bn": "Bengali",
            "br": "Breton",
            "bs": "Bosnian",
            "ca": "Catalan",
            "cs": "Czech",
            "cy": "Welsh",
            "da": "Danish",
            "de": "German",
            "dz": "Dzongkha",
            "el": "Greek",
            "en": "English",
            "eo": "Esperanto",
            "es": "Spanish",
            "et": "Estonian",
            "eu": "Basque",
            "fa": "Persian",
            "fi": "Finnish",
            "fo": "Faroese",
            "fr": "French",
            "ga": "Irish",
            "gl": "Galician",
            "gu": "Gujarati",
            "he": "Hebrew",
            "hi": "Hindi",
            "hr": "Croatian",
            "ht": "Haitian",
            "hu": "Hungarian",
            "hy": "Armenian",
            "id": "Indonesian",
            "is": "Icelandic",
            "it": "Italian",
            "ja": "Japanese",
            "jv": "Javanese",
            "ka": "Georgian",
            "kk": "Kazakh",
            "km": "Khmer",
            "kn": "Kannada",
            "ko": "Korean",
            "ku": "Kurdish",
            "ky": "Kyrgyz",
            "la": "Latin",
            "lb": "Luxembourgish",
            "lo": "Lao",
            "lt": "Lithuanian",
            "lv": "Latvian",
            "mg": "Malagasy",
            "mk": "Macedonian",
            "ml": "Malayalam",
            "mn": "Mongolian",
            "mr": "Marathi",
            "ms": "Malay",
            "mt": "Maltese",
            "nb": "Norwegian (Bokmål)",
            "ne": "Nepali",
            "nl": "Dutch",
            "nn": "Norwegian (Nynorsk)",
            "no": "Norwegian",
            "oc": "Occitan",
            "or": "Oriya",
            "pa": "Punjabi",
            "pl": "Polish",
            "ps": "Pashto",
            "pt": "Portuguese",
            "qu": "Quechua",
            "ro": "Romanian",
            "ru": "Russian",
            "rw": "Kinyarwanda",
            "se": "Northern Sami",
            "si": "Sinhala",
            "sk": "Slovak",
            "sl": "Slovenian",
            "sq": "Albanian",
            "sr": "Serbian",
            "sv": "Swedish",
            "sw": "Swahili",
            "ta": "Tamil",
            "te": "Telugu",
            "th": "Thai",
            "tl": "Tagalog",
            "tr": "Turkish",
            "ug": "Uighur",
            "uk": "Ukrainian",
            "ur": "Urdu",
            "vi": "Vietnamese",
            "vo": "Volapük",
            "wa": "Walloon",
            "xh": "Xhosa",
            "zh": "Chinese",
            "zu": "Zulu",
        }

        language_name = language_names.get(language_code, "Unknown Language")
        return language_name
    except:
        return "Unable to detect language"


# Parse the given text


def parse_syntax(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    syntax_tree_dict = []
    for token in doc:
        token_info = {
            "text": token.text,
            "dep": token.dep_,
            "pos": token.pos_,
            "head": token.head.text,
        }
        syntax_tree_dict.append(token_info)
    return syntax_tree_dict


# Extract part of speech tags from the text


def get_POS_tag(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    pos_list = []
    for token in doc:
        pos_info = {
            "word": token.text,
            "pos": token.pos_,
        }
        pos_list.append(pos_info)

    return pos_list


# Extract missspelled words and the corrected text


def spell_check_text(text):
    blob = TextBlob(text)

    corrected_text = str(blob.correct())

    misspelled_words = [
        original_word
        for original_word, corrected_word in zip(
            blob.words, TextBlob(corrected_text).words
        )
        if original_word != corrected_word
    ]

    return misspelled_words, corrected_text


# find misspelled words and its respective corrected words


def find_spell_corrections(text):
    blob = TextBlob(text)

    corrected_text = str(blob.correct())

    misspelled_dict = {
        original_word: corrected_word
        for original_word, corrected_word in zip(
            blob.words, TextBlob(corrected_text).words
        )
        if original_word != corrected_word
    }

    return misspelled_dict


# perform the Profanity and Obscene Language Analysis on the text


def profanity_analysis(text):
    profanity_score = predict([text])[0]
    profanity_prob = predict_prob([text])[0]

    threshold = 0.5
    is_profane = profanity_score >= threshold

    return is_profane, profanity_score, profanity_prob


# Perform Sentiment Analysis on the text


def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity

    if sentiment_polarity > 0:
        sentiment_label = "Positive"
        sentiment_words = [
            {
                "word": word.lower(),
                "score": blob.sentiment.polarity,
                "frequency": count,
            }
            for word, count in Counter(
                [
                    word.lower()
                    for word, score in blob.tags
                    if score == "JJ" and blob.word_counts[word.lower()] > 1
                ]
            ).items()
        ]
    elif sentiment_polarity < 0:
        sentiment_label = "Negative"
        sentiment_words = [
            {
                "word": word.lower(),
                "score": blob.sentiment.polarity,
                "frequency": count,
            }
            for word, count in Counter(
                [
                    word.lower()
                    for word, score in blob.tags
                    if score == "JJ" and blob.word_counts[word.lower()] > 1
                ]
            ).items()
        ]
    else:
        sentiment_label = "Neutral"
        sentiment_words = [
            {
                "word": word.lower(),
                "score": blob.sentiment.polarity,
                "frequency": count,
            }
            for word, count in Counter(
                [
                    word.lower()
                    for word, score in blob.tags
                    if score == "NN" and blob.word_counts[word.lower()] > 1
                ]
            ).items()
        ]

    results = {
        "sentiment_label": sentiment_label,
        "sentiment_polarity": sentiment_polarity,
        "sentiment_words": sentiment_words,
    }

    return results


# get the Semantic Similarity of Two Strings


def semantic_similarity(text1, text2):

    nlp = spacy.load("en_core_web_md")
    tokens1 = nlp(text1)
    tokens2 = nlp(text2)

    vec1 = tokens1.vector.reshape(1, -1)
    vec2 = tokens2.vector.reshape(1, -1)

    similarity_score = cosine_similarity(vec1, vec2)[0][0]

    return similarity_score


# Extract Text summary:


def text_summarization(text, num_lines):
    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words("english"))
    filtered_sentences = [
        sentence for sentence in sentences if sentence.lower() not in stop_words
    ]

    words = [
        word.lower()
        for sentence in filtered_sentences
        for word in nltk.word_tokenize(sentence)
    ]

    word_freq = FreqDist(words)

    sentence_scores = {
        sentence: sum(word_freq[word] for word in nltk.word_tokenize(sentence))
        for sentence in filtered_sentences
    }

    num_sentences = min(num_lines, len(filtered_sentences))
    top_sentences = sorted(
        filtered_sentences, key=lambda x: sentence_scores[x], reverse=True
    )[:num_sentences]

    summary = " ".join(top_sentences)

    return summary


# Readability Analysis


def calculate_readability_metrics(text):
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    flesch_kincaid_grade = textstat.flesch_kincaid_grade(text)
    smog_index = textstat.smog_index(text)
    coleman_liau_index = textstat.coleman_liau_index(text)
    automated_readability_index = textstat.automated_readability_index(text)
    dale_chall_readability_score = textstat.dale_chall_readability_score(text)
    difficult_words = textstat.difficult_words(text)
    linsear_write_formula = textstat.linsear_write_formula(text)
    gunning_fog = textstat.gunning_fog(text)
    text_standard = textstat.text_standard(text)
    fernandez_huerta = textstat.fernandez_huerta(text)
    szigriszt_pazos = textstat.szigriszt_pazos(text)
    gutierrez_polini = textstat.gutierrez_polini(text)
    crawford = textstat.crawford(text)
    gulpease_index = textstat.gulpease_index(text)
    osman = textstat.osman(text)

    average_readability = (
        flesch_reading_ease
        + flesch_kincaid_grade
        + smog_index
        + coleman_liau_index
        + automated_readability_index
        + dale_chall_readability_score
        + linsear_write_formula
        + gunning_fog
        + fernandez_huerta
        + szigriszt_pazos
        + gutierrez_polini
        + crawford
        + gulpease_index
        + osman
    ) / 14

    return {
        "Flesch Reading Ease": flesch_reading_ease,
        "Flesch-Kincaid Grade Level": flesch_kincaid_grade,
        "SMOG Index": smog_index,
        "Coleman-Liau Index": coleman_liau_index,
        "Automated Readability Index": automated_readability_index,
        "Dale-Chall Readability Score": dale_chall_readability_score,
        "Difficult Words": difficult_words,
        "Linsear Write Formula": linsear_write_formula,
        "Gunning Fog Index": gunning_fog,
        "Text Standard": text_standard,
        "Fernandez Huerta": fernandez_huerta,
        "Szigriszt Pazos": szigriszt_pazos,
        "Gutierrez Polini": gutierrez_polini,
        "Crawford": crawford,
        "Gulpease Index": gulpease_index,
        "Osman": osman,
        "Average Readability": average_readability,
    }
