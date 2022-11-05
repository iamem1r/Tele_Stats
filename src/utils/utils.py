# from hazm import word_tokenize
# from hazm import Normalizer
# from pathlib import Path
# from typing import Union


# def load_stopwords(file_path: Union[str, Path]):
#     """This function get a directory of stop words file with .txt extension,
#         load, readlines and normalize stopwords.

#     :param file_path: file path to stop words
#     :type file_path: str or Path object
#     :return: list of normalized stop words
#     :rtype: list
#     """
#     # load
#     stopwords = open(file_path).readlines()

#     # remove '\n'
#     stopwords = list(map(str.strip, stopwords))

#     # normalize stop words
#     normalizer = Normalizer()
#     stopwords = list(map(normalizer.normalize, stopwords))

#     return stopwords



# def stopwords_detection(text: str, stopwords_file_path: Union[str, Path]):
#     """This function takes a text(string like) argument.
#     tokenize text, remove stop words and returns a list of remains words.

#     :param text: text to detection
#     :type text: str
#     :param stopwords_file_path: file_path to stopwords
#     :type stopwords_file_path: str
#     :return: list of remains words
#     :rtype: list
#     """
#     stopwords = load_stopwords(stopwords_file_path)
#     tokens = word_tokenize(text)
#     return list(filter(lambda item: item not in stopwords, tokens))