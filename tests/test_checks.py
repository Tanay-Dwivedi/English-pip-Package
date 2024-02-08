import enalsis

text_para = """India is a vast and diverse country located in South Asia, known for its rich history, diverse cultures, and varied landscapes. With a population of over $ 1.3 billion people, India is the second-most populous country in the world. The country is characterized by a harmonious blend of tradition and modernity, where ancient customs coexist with rapidly evolving urban lifestyles.

Geographically, India boasts a wide range of terrains, from the snow-capped Himalayan mountains in the north to the tropical beaches in the south. The country is home to a myriad of ecosystems, supporting a diverse array of flora and fauna. The Ganges, one of the holiest rivers in Hinduism, flows through the heart of the country, playing a vital role in the cultural and spiritual fabric of India.

India's rich cultural heritage is reflected in its numerous festivals, art forms, and classical dance and music traditions. The country has a long history of contributions to science, mathematics, literature, and philosophy. Ancient texts such as the Vedas and Upanishads have left an indelible mark on the intellectual landscape of the world.

The Indian economy has undergone significant transformation in recent decades, emerging as one of the world's fastest-growing major economies. Information technology, software services, and a burgeoning startup ecosystem have contributed to India's position in the global economy. Despite these advancements, India faces challenges related to poverty, healthcare, and environmental sustainability, prompting ongoing efforts for inclusive development.

India's political landscape is characterized by a robust democratic system, with a diverse array of political parties. The country gained independence from British rule in 1947, led by Mahatma Gandhi and other prominent leaders. India's commitment to democracy is evident in its vibrant elections, where millions of citizens participate in shaping the nation's future."""


# Extract entities from the text

print(enalsis.get_entities(text_para))

""" 
Output -

[('India', 'GPE'), ('South Asia', 'LOC'), ('over $ 1.3 billion', 'MONEY'), ('India', 'GPE'), ('second', 'ORDINAL'), ('Geographically', 'ORG'), ('India', 'GPE'), ('Himalayan', 'NORP'), ('Ganges', 'ORG'), ('Hinduism', 'GPE'), ('India', 'GPE'), ('India', 'GPE'), ('Upanishads', 'PERSON'), ('Indian', 'NORP'), ('recent decades', 'DATE'), ('one', 'CARDINAL'), ('India', 'GPE'), ('India', 'GPE'), ('healthcare', 'ORG'), ('India', 'GPE'), ('British', 'NORP'), ('1947', 'DATE'), ('Mahatma Gandhi', 'PERSON'), ('India', 'GPE'), ('millions', 'CARDINAL')]

"""

# Extract sentences from the text

print(enalsis.get_sentences(text_para))

"""
Output - 

['India is a vast and diverse country located in South Asia, known for its rich history, diverse cultures, and varied landscapes.', 'With a population of over $ 1.3 billion people, India is the second-most populous country in the world.', 'The country is characterized by a harmonious blend of tradition and modernity, where ancient customs coexist with rapidly evolving urban lifestyles.\n\n', 'Geographically, India boasts a wide range of terrains, from the snow-capped Himalayan mountains in the north to the tropical beaches in the south.', 'The country is home to a myriad of ecosystems, supporting a diverse array of flora and fauna.', 'The Ganges, one of the holiest rivers in Hinduism, flows through the heart of the country, playing a vital role in the cultural and spiritual fabric of India.\n\n', "India's rich cultural heritage is reflected in its numerous festivals, art forms, and classical dance and music traditions.", 'The country has a long history of contributions to science, mathematics, literature, and philosophy.', 'Ancient texts such as the Vedas and Upanishads have left an indelible mark on the intellectual landscape of the world.\n\n', "The Indian economy has undergone significant transformation in recent decades, emerging as one of the world's fastest-growing major economies.", "Information technology, software services, and a burgeoning startup ecosystem have contributed to India's position in the global economy.", 'Despite these advancements, India faces challenges related to poverty, healthcare, and environmental sustainability, prompting ongoing efforts for inclusive development.\n\n', "India's political landscape is characterized by a robust democratic system, with a diverse array of political parties.", 'The country gained independence from British rule in 1947, led by Mahatma Gandhi and other prominent leaders.', "India's commitment to democracy is evident in its vibrant elections, where millions of citizens participate in shaping the nation's future."]

"""

# Extract adjectives from the text

print(enalsis.get_adjectives(text_para))

"""
Output - 

['vast', 'diverse', 'rich', 'diverse', 'varied', 'populous', 'harmonious', 'ancient', 'urban', 'wide', 'Himalayan', 'tropical', 'diverse', 'holiest', 'vital', 'cultural', 'spiritual', 'rich', 'cultural', 'numerous', 'classical', 'long', 'Ancient', 'such', 'indelible', 'intellectual', 'Indian', 'significant', 'recent', 'major', 'global', 'environmental', 'ongoing', 'inclusive', 'political', 'robust', 'democratic', 'diverse', 'political', 'British', 'other', 'prominent', 'evident', 'vibrant']

"""

# Extract adverbs from the text

print(enalsis.get_adverbs(text_para))

"""
Output - 

['second', 'most', 'rapidly', 'fastest']

"""

# Extract nouns from the text

print(enalsis.get_nouns(text_para))

"""
Output - 

['country', 'history', 'cultures', 'landscapes', 'population', 'people', 'country', 'world', 'country', 'blend', 'tradition', 'modernity', 'customs', 'lifestyles', 'range', 'terrains', 'snow', 'mountains', 'north', 'beaches', 'south', 'country', 'home', 'myriad', 'ecosystems', 'array', 'flora', 'fauna', 'rivers', 'heart', 'country', 'role', 'fabric', 'heritage', 'festivals', 'art', 'forms', 'dance', 'music', 'traditions', 'country', 'history', 'contributions', 'science', 'mathematics', 'literature', 'philosophy', 'texts', 'mark', 'landscape', 'world', 'economy', 'transformation', 'decades', 'world', 'economies', 'Information', 'technology', 'software', 'services', 'startup', 'ecosystem', 'position', 'economy', 'advancements', 'challenges', 'poverty', 'healthcare', 'sustainability', 'efforts', 'development', 'landscape', 'system', 'array', 'parties', 'country', 'independence', 'rule', 'leaders', 'commitment', 'democracy', 'elections', 'millions', 'citizens', 'nation', 'future']

"""

# Extract pronouns from the text

print(enalsis.get_pronouns(text_para))

"""
Output -

['its', 'its', 'its']

"""

# Extract proper nouns from the text

print(enalsis.get_proper_nouns(text_para))

"""
Output -

['India', 'South', 'Asia', 'India', 'Geographically', 'India', 'Ganges', 'Hinduism', 'India', 'India', 'Vedas', 'Upanishads', 'India', 'India', 'India', 'Mahatma', 'Gandhi', 'India']

"""
# Extract verbs from the text

print(enalsis.get_verbs(text_para))

"""
Output -

['located', 'known', 'characterized', 'coexist', 'evolving', 'boasts', 'capped', 'supporting', 'flows', 'playing', 'reflected', 'has', 'left', 'undergone', 'emerging', 'growing', 'burgeoning', 'contributed', 'faces', 'related', 'prompting', 'characterized', 'gained', 'led', 'participate', 'shaping']

"""

# Extract numbers from the text

print(enalsis.get_numbers(text_para))

"""
Output -

['1.3', 'billion', 'one', 'one', '1947']

"""

# Detect language of the text

print(enalsis.detect_language(text_para))

"""
Output -

English

"""

# Perform syntax tree analysis on the given text

print(enalsis.parse_syntax_tree(text_para))

"""
Output - see file "tests/syntax_tree.txt"

"""

# Extract part of speech tags from the text

print(enalsis.get_POS_tag(text_para))

"""
Output - see file "tests/pos.txt"

"""

# Extract misspelled words and the corrected text

print(enalsis.spell_check_text(text_para))

"""
Output -

(['landscapes', 'evolving', 'lifestyles', 'boasts', 'terrains', 'snow-capped', 'beaches', 'myriad', 'fauna', 'Ganges', 'holiest', 'festivals', 'Vedas', 'fastest-growing', 'burgeoning', 'startup', 'advancements', 'ongoing', 'vibrant'], "India is a vast and diverse country located in South Asia, known for its rich history, diverse cultures, and varied landscape. With a population of over $ 1.3 billion people, India is the second-most populous country in the world. The country is characterized by a harmonious blend of tradition and modernity, where ancient customs coexist with rapidly revolving urban lifestyle.\n\nGeographically, India boats a wide range of terrain, from the snow-tapped Himalayan mountains in the north to the tropical reaches in the south. The country is home to a myriads of ecosystems, supporting a diverse array of flora and found. The Ranges, one of the holies rivers in Hinduism, flows through the heart of the country, playing a vital role in the cultural and spiritual fabric of India.\n\nIndia's rich cultural heritage is reflected in its numerous festival, art forms, and classical dance and music traditions. The country has a long history of contributions to science, mathematics, literature, and philosophy. Ancient texts such as the Heads and Upanishads have left an indelible mark on the intellectual landscape of the world.\n\nThe Indian economy has undergone significant transformation in recent decades, emerging as one of the world's fattest-growing major economies. Information technology, software services, and a burdening started ecosystem have contributed to India's position in the global economy. Despite these advancement, India faces challenges related to poverty, healthcare, and environmental sustainability, prompting going efforts for inclusive development.\n\nIndia's political landscape is characterized by a robust democratic system, with a diverse array of political parties. The country gained independence from British rule in 1947, led by Mahatma Gandhi and other prominent leaders. India's commitment to democracy is evident in its vagrant elections, where millions of citizens participate in shaping the nation's future.")

"""

# Find misspelled words and its respective corrected words

print(enalsis.find_spell_corrections(text_para))

"""
Output -

{'landscapes': 'landscape', 'evolving': 'revolving', 'lifestyles': 'lifestyle', 'boasts': 'boats', 'terrains': 'terrain', 'snow-capped': 'snow-tapped', 'beaches': 'reaches', 'myriad': 'myriads', 'fauna': 'found', 'Ganges': 'Ranges', 'holiest': 'holies', 'festivals': 'festival', 'Vedas': 'Heads', 'fastest-growing': 'fattest-growing', 'burgeoning': 'burdening', 'startup': 'started', 'advancements': 'advancement', 'ongoing': 'going', 'vibrant': 'vagrant'}

"""

# Perform the Profanity and Obscene Language Analysis on the text

print(enalsis.profanity_analysis(text_para))

"""
Output -

(False, 0, 0.003242810221774097)

"""

# Perform Sentiment Analysis on the text

print(enalsis.sentiment_analysis(text_para))

"""
Output - 

{'sentiment_label': 'Positive', 'sentiment_polarity': 0.09238505747126437, 'sentiment_words': [{'word': 'diverse', 'score': 0.09238505747126437, 'frequency': 4}, {'word': 'rich', 'score': 0.09238505747126437, 'frequency': 2}, {'word': 'cultural', 'score': 0.09238505747126437, 'frequency': 2}, {'word': 'ancient', 'score': 0.09238505747126437, 'frequency': 1}, {'word': 'political', 'score': 0.09238505747126437, 'frequency': 2}]}

"""

# Get the Semantic Similarity between the two texts

print(enalsis.semantic_similarity(text_para, text_para))

"""
Output -

0.9999999

"""

# Extract the text summary

print(enalsis.text_summarization(text_para, 10))

"""
Output -

The Ganges, one of the holiest rivers in Hinduism, flows through the heart of the country, playing a vital role in the cultural and spiritual fabric of India. Geographically, India boasts a wide range of terrains, from the snow-capped Himalayan mountains in the north to the tropical beaches in the south. India is a vast and diverse country located in South Asia, known for its rich history, diverse cultures, and varied landscapes. Despite these advancements, India faces challenges related to poverty, healthcare, and environmental sustainability, prompting ongoing efforts for inclusive development. The country has a long history of contributions to science, mathematics, literature, and philosophy. Information technology, software services, and a burgeoning startup ecosystem have contributed to India's position in the global economy. With a population of over $ 1.3 billion people, India is the second-most populous country in the world. India's commitment to democracy is evident in its vibrant elections, where millions of citizens participate in shaping the nation's future. The country is home to a myriad of ecosystems, supporting a diverse array of flora and fauna. India's rich cultural heritage is reflected in its numerous festivals, art forms, and classical dance and music traditions.

"""

# Perform Readability Analysis on the text

print(enalsis.calculate_readability_metrics(text_para))

"""
Output -

{'Flesch Reading Ease': 36.18, 'Flesch-Kincaid Grade Level': 12.7, 'SMOG Index': 14.3, 'Coleman-Liau Index': 14.61, 'Automated Readability Index': 14.6, 'Dale-Chall Readability Score': 11.53, 'Difficult Words': 105, 'Linsear Write Formula': 10.666666666666666, 'Gunning Fog Index': 14.44, 'Text Standard': '14th and 15th grade', 'Fernandez Huerta': 80.38, 'Szigriszt Pazos': 77.75, 'Gutierrez Polini': 35.08, 'Crawford': 4.2, 'Gulpease Index': 48.3, 'Osman': 36.45, 'Average Readability': 29.370476190476186}

"""

# Perform paragraph-wise sentiment analysis on the text

print(enalsis.paragraph_sentiment_analysis(text_para))

"""
Output -

[0.125, 0.06999999999999999, 0.090625, 0.0875, 0.09895833333333333]

"""

# Perform sentence-wise sentiment analysis on the text

print(enalsis.sentence_sentiment_analysis(text_para))

"""
Output -

[0.1875, 0.0, 0.0, -0.1, 0.25, 0.06666666666666667, 0.11875, -0.05, 0.09999999999999999, 0.14583333333333334, 0.0, 0.0, 0.0, 0.125, 0.13888888888888887]

"""

# Extract words and their word meanings from the text

print(enalsis.extract_word_meanings(text_para))

"""
Output - see file "tests/word_meaning.txt"

"""

# Extract words and their respective frequencies from the text

print(enalsis.count_words(text_para))

"""
Output -

[('india', 9), ('is', 7), ('a', 11), ('vast', 1), ('and', 12), ('diverse', 4), ('country', 7), ('located', 1), ('in', 12), ('south', 2), ('asia', 1), ('known', 1), ('for', 2), ('its', 3), ('rich', 2), ('history', 2), ('cultures', 1), ('varied', 1), ('landscapes', 1), ('with', 3), ('population', 1), ('of', 13), ('over', 1), ('1', 1), ('3', 1), ('billion', 1), ('people', 1), ('the', 22), ('second', 1), ('most', 1), ('populous', 1), ('world', 3), ('characterized', 2), ('by', 3), ('harmonious', 1), ('blend', 1), ('tradition', 1), ('modernity', 1), ('where', 2), ('ancient', 2), ('customs', 1), ('coexist', 1), ('rapidly', 1), ('evolving', 1), ('urban', 1), ('lifestyles', 1), ('geographically', 1), ('boasts', 1), ('wide', 1), ('range', 1), ('terrains', 1), ('from', 2), ('snow', 1), ('capped', 1), ('himalayan', 1), ('mountains', 1), ('north', 1), ('to', 6), ('tropical', 1), ('beaches', 1), ('home', 1), ('myriad', 1), ('ecosystems', 1), ('supporting', 1), ('array', 2), ('flora', 1), ('fauna', 1), ('ganges', 1), ('one', 2), ('holiest', 1), ('rivers', 1), ('hinduism', 1), ('flows', 1), ('through', 1), ('heart', 1), ('playing', 1), ('vital', 1), ('role', 1), ('cultural', 2), ('spiritual', 1), ('fabric', 1), ('s', 6), ('heritage', 1), ('reflected', 1), ('numerous', 1), ('festivals', 1), ('art', 1), ('forms', 1), ('classical', 1), ('dance', 1), ('music', 1), ('traditions', 1), ('has', 2), ('long', 1), ('contributions', 1), ('science', 1), ('mathematics', 1), ('literature', 1), ('philosophy', 1), ('texts', 1), ('such', 1), ('as', 2), ('vedas', 1), ('upanishads', 1), ('have', 2), ('left', 1), ('an', 1), ('indelible', 1), ('mark', 1), ('on', 1), ('intellectual', 1), ('landscape', 2), ('indian', 1), ('economy', 2), ('undergone', 1), ('significant', 1), ('transformation', 1), ('recent', 1), ('decades', 1), ('emerging', 1), ('fastest', 1), ('growing', 1), ('major', 1), ('economies', 1), ('information', 1), ('technology', 1), ('software', 1), ('services', 1), ('burgeoning', 1), ('startup', 1), ('ecosystem', 1), ('contributed', 1), ('position', 1), ('global', 1), ('despite', 1), ('these', 1), ('advancements', 1), ('faces', 1), ('challenges', 1), ('related', 1), ('poverty', 1), ('healthcare', 1), ('environmental', 1), ('sustainability', 1), ('prompting', 1), ('ongoing', 1), ('efforts', 1), ('inclusive', 1), ('development', 1), ('political', 2), ('robust', 1), ('democratic', 1), ('system', 1), ('parties', 1), ('gained', 1), ('independence', 1), ('british', 1), ('rule', 1), ('1947', 1), ('led', 1), ('mahatma', 1), ('gandhi', 1), ('other', 1), ('prominent', 1), ('leaders', 1), ('commitment', 1), ('democracy', 1), ('evident', 1), ('vibrant', 1), ('elections', 1), ('millions', 1), ('citizens', 1), ('participate', 1), ('shaping', 1), ('nation', 1), ('future', 1)]

"""

# Extract alphabetical and numerical percentage from the text

print(enalsis.calculate_alphabetical_and_numberical_percentages(text_para))

"""
Output -

(84.65092402464066, 0.3080082135523614, 15.041067761806982)

"""
