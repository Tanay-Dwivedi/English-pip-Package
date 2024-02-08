import spacy
import textstat
import nltk
import re
import py3langid as langid
from textblob import TextBlob
from profanity_check import predict, predict_prob
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.corpus import wordnet


# Extract entities from the text


def get_entities(text):
    """
    Extracts entities from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of tuples containing the text and label of each entity.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


# Extract sentences from the text


def get_sentences(text):
    """
    Extracts sentences from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of sentences extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences


# Extract adjectives from the text


def get_adjectives(text):
    """
    Extracts adjectives from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of adjectives extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
    return adjectives


# Extract adverbs from the text


def get_adverbs(text):
    """
    Extracts adverbs from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of adverbs extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    adverbs = [token.text for token in doc if token.pos_ == "ADV"]
    return adverbs


# Extract nouns from the text


def get_nouns(text):
    """
    Extracts nouns from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of nouns extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ == "NOUN"]
    return nouns


# Extract pronouns from the text


def get_pronouns(text):
    """
    Extracts pronouns from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of pronouns extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    return pronouns


# Extract proper nouns from the text


def get_proper_nouns(text):
    """
    Extracts proper nouns from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of proper nouns extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    proper_nouns = [token.text for token in doc if token.pos_ == "PROPN"]
    return proper_nouns


# Extract verbs from the text


def get_verbs(text):
    """
    Extracts verbs from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of verbs extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    verbs = [token.text for token in doc if token.pos_ == "VERB"]
    return verbs


# Extract numbers from the text


def get_numbers(text):
    """
    Extracts numbers from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of numbers extracted from the input text.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    numbers = [token.text for token in doc if token.pos_ == "NUM"]
    return numbers


# Detect language of the text


def detect_language(text):
    """
    Detects the language of the given text using langid.

    Parameters:
        text (str): The input text.

    Returns:
        str: The name of the detected language, or "Unknown Language" if the language cannot be detected.
    """
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


# Perform syntax tree analysis on the given text


def parse_syntax_tree(text):
    """
    Performs syntax tree analysis on the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of dictionaries containing information about each token in the text,
              including its text, dependency relation, part-of-speech tag, and head token.
    """
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
    """
    Extracts part-of-speech (POS) tags from the given text using spaCy.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of dictionaries containing information about each word/token in the text,
              including the word/token itself and its corresponding part-of-speech tag.
    """
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


# Extract misspelled words and the corrected text


def spell_check_text(text):
    """
    Performs spell checking on the given text using TextBlob.

    Parameters:
        text (str): The input text.

    Returns:
        tuple: A tuple containing two elements:
               - A list of misspelled words extracted from the input text.
               - The corrected version of the input text.
    """
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


# Find misspelled words and its respective corrected words


def find_spell_corrections(text):
    """
    Finds misspelled words and their respective corrected words using TextBlob.

    Parameters:
        text (str): The input text.

    Returns:
        dict: A dictionary where keys are misspelled words and values are their respective corrected words.
    """
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


# Perform the Profanity and Obscene Language Analysis on the text


def profanity_analysis(text):
    """
    Performs profanity and obscene language analysis on the given text using the Profanity Check library.

    Parameters:
        text (str): The input text.

    Returns:
        tuple: A tuple containing three elements:
               - A boolean indicating whether the text contains profanity or obscene language.
               - The profanity score, indicating the degree of profanity present in the text.
               - The probability of the text containing profanity or obscene language.
    """
    profanity_score = predict([text])[0]
    profanity_prob = predict_prob([text])[0]

    threshold = 0.5
    is_profane = profanity_score >= threshold

    return is_profane, profanity_score, profanity_prob


# Perform Sentiment Analysis on the text


def sentiment_analysis(text):
    """
    Performs sentiment analysis on the given text using TextBlob.

    Parameters:
        text (str): The input text.

    Returns:
        dict: A dictionary containing sentiment analysis results, including:
              - The sentiment label indicating whether the text is Positive, Negative, or Neutral.
              - The sentiment polarity score indicating the overall sentiment polarity of the text.
              - A list of sentiment words along with their scores and frequencies.
    """
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity

    if sentiment_polarity > 0:
        sentiment_label = "Positive"
    elif sentiment_polarity < 0:
        sentiment_label = "Negative"
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
                if score == "JJ" and blob.word_counts[word.lower()] > 1
            ]
        ).items()
    ]

    results = {
        "sentiment_label": sentiment_label,
        "sentiment_polarity": sentiment_polarity,
        "sentiment_words": sentiment_words,
    }

    return results


# Get the Semantic Similarity between the two texts


def semantic_similarity(text1, text2):
    """
    Calculates the semantic similarity between two texts using spaCy's pre-trained word embeddings.

    Parameters:
        text1 (str): The first input text.
        text2 (str): The second input text.

    Returns:
        float: The semantic similarity score between the two texts.
    """
    nlp = spacy.load("en_core_web_md")
    tokens1 = nlp(text1)
    tokens2 = nlp(text2)

    vec1 = tokens1.vector.reshape(1, -1)
    vec2 = tokens2.vector.reshape(1, -1)

    similarity_score = cosine_similarity(vec1, vec2)[0][0]

    return similarity_score


# Extract the text summary


def text_summarization(text, num_lines):
    """
    Generates a summary of the given text by extracting the most relevant sentences.

    Parameters:
        text (str): The input text.
        num_lines (int): The number of sentences to include in the summary.

    Returns:
        str: The summary of the input text.
    """
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


# Perform Readability Analysis on the text


def calculate_readability_metrics(text):
    """
    Calculates various readability metrics for the given text using the textstat library.

    Parameters:
        text (str): The input text.

    Returns:
        dict: A dictionary containing readability metrics calculated for the input text.
    """
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


# Perform paragraph-wise sentiment analysis on the text


def paragraph_sentiment_analysis(text):
    """
    Performs sentiment analysis on each paragraph of the given text using TextBlob.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list containing sentiment scores for each paragraph.
    """
    paragraphs = text.split("\n\n")

    sentiments = []
    for paragraph in paragraphs:
        blob = TextBlob(paragraph)
        sentiment_score = blob.sentiment.polarity
        sentiments.append(sentiment_score)

    return sentiments


# Perform sentence-wise sentiment analysis on the text


def sentence_sentiment_analysis(text):
    """
    Performs sentiment analysis on each sentence of the given text using TextBlob.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list containing sentiment scores for each sentence.
    """
    blob = TextBlob(text)

    sentiments = []
    for sentence in blob.sentences:
        sentiment_score = sentence.sentiment.polarity
        sentiments.append(sentiment_score)

    return sentiments


# Extract words and their word meanings from the text


def extract_word_meanings(text):
    """
    Extracts unique words from the given text and their corresponding word meanings using WordNet.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list containing dictionaries where each dictionary represents a word along with its meanings.
    """
    words = nltk.word_tokenize(text)

    unique_words = set()
    word_meanings = []

    for word in words:
        if word not in unique_words:
            unique_words.add(word)
            synsets = wordnet.synsets(word)
            meanings = [synset.definition() for synset in synsets]
            word_meanings.append({"word": word, "meanings": meanings})

    return word_meanings


# Extract words and their respective frequencies from the text


def count_words(text):
    """
    Counts the frequencies of words in the given text.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of tuples where each tuple contains a word and its frequency.
    """
    words = re.findall(r"\b\w+\b", text.lower())

    word_counts = Counter(words)

    return [(word, count) for word, count in word_counts.items()]


# Extract alphabetical and numerical percentage from the text


def calculate_alphabetical_and_numberical_percentages(text):
    """
    Calculates the percentages of alphabetical, numerical, and whitespace characters in the given text.

    Parameters:
        text (str): The input text.

    Returns:
        tuple: A tuple containing three percentages:
               - The percentage of alphabetical characters.
               - The percentage of numerical characters.
               - The percentage of whitespace characters.
    """
    total_characters = len(text)

    text_characters = sum(c.isalpha() for c in text)
    numeric_characters = sum(c.isdigit() for c in text)
    whitespace_characters = sum(c.isspace() for c in text)

    text_percentage = (text_characters / total_characters) * 100
    number_percentage = (numeric_characters / total_characters) * 100
    whitespace_percentage = (whitespace_characters / total_characters) * 100

    total_percentage = text_percentage + number_percentage + whitespace_percentage
    if total_percentage != 100:
        adjustment = 100 - total_percentage
        text_percentage += adjustment

    return text_percentage, number_percentage, whitespace_percentage
