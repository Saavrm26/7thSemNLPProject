import spacy
from spacy.lang.am.examples import sentences
from spellchecker import SpellChecker

nlp = spacy.load('en_core_web_sm')

def lower_case(text):
    """
    Convert all text to lowercase.

    Parameters:
    text (str): The input text.

    Returns:
    str: The input text in lowercase.
    """
    return text.lower()

def tokenize(text):
    """
    Tokenize a text into individual words.

    Parameters:
    text (str): The input text.

    Returns:
    list: A list of tokens.
    """
    doc = nlp(text)
    return [token.text for token in doc]

def remove_punc_special_characters(tokens):
    """
    Remove punctuation and special characters from a list of tokens.

    Parameters:
    tokens (list): A list of tokens.

    Returns:
    list: A list of tokens with punctuation and special characters removed.
    """
    return [token for token in tokens if token.isalnum()]

def remove_stopwords(tokens):
    """
    Remove stopwords from a list of tokens.

    Parameters:
    tokens (list): A list of tokens.

    Returns:
    list: A list of tokens with stopwords removed.
    """
    return [token for token in tokens if token.lower() not in nlp.Defaults.stop_words]

def lemmatize(tokens):
    """
    Apply lemmatization to a list of tokens.

    Parameters:
    tokens (list): A list of tokens.

    Returns:
    list: A list of lemmatized tokens.
    """
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

def pos_tag(tokens):
    """
    Apply part-of-speech tagging to a list of tokens.

    Parameters:
    tokens (list): A list of tokens.

    Returns:
    list: A list of tuples, where each tuple contains a token and its part of speech.
    """
    doc = nlp(" ".join(tokens))
    return [(token.text, token.pos_) for token in doc]

def ner(text):
    """
    Apply named entity recognition to a text.

    Parameters:
    text (str): The input text.

    Returns:
    list: A list of tuples, where each tuple contains a named entity and its category.
    """
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def correct_spelling(tokens):
    """
    Correct spelling errors in a list of tokens.

    Parameters:
    tokens (list): A list of tokens.

    Returns:
    list: A list of tokens with spelling errors corrected.
    """
    spell = SpellChecker()
    return [spell.correction(token) for token in tokens]

def apply_to_each_sentence(pipeline):
    """
    Apply a series of preprocessing functions to each sentence in a text.

    Parameters:
    pipeline (list): A list of preprocessing functions to be applied to each sentence in the text.

    Returns:
    function: A new function that takes a text as input and applies the given pipeline of functions to each sentence in the text.

    Example:

    pipeline = [lower_case, apply_to_each_sentence([tokenize, remove_stopwords, lemmatize, remove_punc_special_characters])]
    text = "This is a sample text for NLP preprocessing. Another sentence for testing."
    out = apply(text, pipeline)

    [['sample', 'text', 'nlp', 'preprocessing'], ['another', 'sentence', 'testing']]

    In this example, the `apply_to_each_sentence` function is used to apply a pipeline of functions to each sentence in the text. The output is a list of lists, where each sublist contains the preprocessed tokens of a sentence.
    """
    return lambda text: [apply(sentence.text, pipeline) for sentence in nlp(text).sents]


def apply(text, pipeline):
    """
    Apply a series of preprocessing functions to a text.

    Parameters:
    text (str): The input text to be preprocessed.
    pipeline (list): A list of preprocessing functions to be applied to the text.

    Returns:
    str or list: The preprocessed text. The type of the output depends on the preprocessing functions in the pipeline.

    Example:

    pipeline = [lower_case, tokenize, remove_punc_special_characters, remove_stopwords]
    text = "This is a sample text for NLP preprocessing."
    out = apply(text, pipeline)

    ['sample', 'text', 'nlp', 'preprocessing']
    """
    for function in pipeline:
        text = function(text)
    return text
