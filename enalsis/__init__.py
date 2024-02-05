import spacy
import langid

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
            "ab": "Abkhazian",
            "aa": "Afar",
            "af": "Afrikaans",
            "ak": "Akan",
            "sq": "Albanian",
            "am": "Amharic",
            "ar": "Arabic",
            "hy": "Armenian",
            "as": "Assamese",
            "ay": "Aymara",
            "az": "Azerbaijani",
            "ba": "Bashkir",
            "eu": "Basque",
            "be": "Belarusian",
            "bn": "Bengali",
            "bh": "Bihari",
            "bi": "Bislama",
            "bs": "Bosnian",
            "br": "Breton",
            "bg": "Bulgarian",
            "my": "Burmese",
            "ca": "Catalan",
            "ceb": "Cebuano",
            "chr": "Cherokee",
            "ny": "Nyanja",
            "co": "Corsican",
            "hr": "Croatian",
            "cs": "Czech",
            "zh": "Chinese",
            "zh-cn": "Chinese",
            "zh-tw": "Chinese",
            "zh-hk": "Chinese",
            "zh-sg": "Chinese",
            "zh-my": "Chinese",
            "zh-mo": "Chinese",
            "da": "Danish",
            "dv": "Dhivehi",
            "nl": "Dutch",
            "dz": "Dzongkha",
            "en": "English",
            "eo": "Esperanto",
            "et": "Estonian",
            "ee": "Ewe",
            "fo": "Faroese",
            "fj": "Fijian",
            "fi": "Finnish",
            "fr": "French",
            "fy": "Frisian",
            "ga": "Ga",
            "gl": "Galician",
            "lg": "Ganda",
            "ka": "Georgian",
            "de": "German",
            "el": "Greek",
            "kl": "Greenlandic",
            "gn": "Guarani",
            "gu": "Gujarati",
            "ht": "Haitian_creole",
            "ha": "Hausa",
            "haw": "Hawaiian",
            "iw": "Hebrew",
            "he": "Hebrew",
            "hi": "Hindi",
            "hmn": "Hmong",
            "hu": "Hungarian",
            "is": "Icelandic",
            "ig": "Igbo",
            "id": "Indonesian",
            "ia": "Interlingua",
            "ie": "Interlingue",
            "iu": "Inuktitut",
            "ik": "Inupiak",
            "ga": "Irish",
            "it": "Italian",
            "ja": "Japanese",
            "jv": "Javanese",
            "ja-jp": "Japanese",
            "ja-jp_kana": "Japanese",
            "rw": "Kinyarwanda",
            "kv": "Komi",
            "kg": "Kongo",
            "ko": "Korean",
            "ku": "Kurdish",
            "ky": "Kyrgyz",
            "lo": "Laothian",
            "la": "Latin",
            "lv": "Latvian",
            "li": "Limbu",
            "li-la": "Limbu",
            "li-iq": "Limbu",
            "ln": "Lingala",
            "lt": "Lithuanian",
            "loz": "Lozi",
            "lua": "Luba_lulua",
            "luo": "Luo_kenya_and_tanzania",
            "lb": "Luxembourgish",
            "mk": "Macedonian",
            "mg": "Malagasy",
            "ms": "Malay",
            "ml": "Malayalam",
            "mt": "Maltese",
            "gv": "Manx",
            "mi": "Maori",
            "mr": "Marathi",
            "mfe": "Mauritian_creole",
            "mo": "Moldavian",
            "ro": "Romanian",
            "ru": "Russian",
            "sm": "Samoan",
            "sg": "Sango",
            "sa": "Sanskrit",
            "gd": "Scots",
            "ga": "Scots_gaelic",
            "sr": "Serbian",
            "sr-sp": "Serbian",
            "crs": "Seselwa",
            "sr-me": "Montenegrin",
            "se": "Sesotho",
            "sn": "Shona",
            "sd": "Sindhi",
            "si": "Sinhalese",
            "ss": "Siswant",
            "sk": "Slovak",
            "sl": "Slovenian",
            "so": "Somali",
            "es": "Spanish",
            "su": "Sundanese",
            "sw": "Swahili",
            "sv": "Swedish",
            "syr": "Syriac",
            "tl": "Tagalog",
            "tg": "Tajik",
            "ta": "Tamil",
            "tt": "Tatar",
            "te": "Telugu",
            "th": "Thai",
            "bo": "Tibetan",
            "ti": "Tigrinya",
            "to": "Tonga",
            "ts": "Tsonga",
            "tn": "Tswana",
            "tum": "Tumbuka",
            "tr": "Turkish",
            "tk": "Turkmen",
            "tw": "Twi",
            "ug": "Uighur",
            "uk": "Ukrainian",
            "ur": "Urdu",
            "uz": "Uzbek",
            "ve": "Venda",
            "vi": "Vietnamese",
            "vo": "Volapuk",
            "war": "Waray_philippines",
            "cy": "Welsh",
            "wo": "Wolof",
            "xh": "Xhosa",
            "yi": "Yiddish",
            "yo": "Yoruba",
            "za": "Zhuang",
            "zu": "Zulu",
        }

        language_name = language_names.get(language_code, "Unknown Language")
        return language_name
    except:
        return "Unable to detect language"
