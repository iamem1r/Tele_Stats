import json
from pathlib import Path
from typing import Union

import arabic_reshaper
from bidi.algorithm import get_display
from hazm import Normalizer, word_tokenize
from src.data import DATA_DIR
from wordcloud import WordCloud


class ChatStatistics:
    def __init__(self, file_path: Union[str, Path]) -> None:
        """read a text file(.json or .txt)

        :param file_path: path to the file
        :type file_path: Union[str, Path]
        """
        with open(file_path) as f:
            self.data = json.load(f)

        self.normalizer = Normalizer()

        # load stop words
        stopwords = open(DATA_DIR / 'stopwords.txt').readlines()
        stopwords = list(map(str.strip, stopwords))
        self.stopwords = list(map(self.normalizer.normalize, stopwords))


    def generate_word_cloud(
        self,
        output_file_path: Union[str, Path]
        ):
        """generate word cloud from a text file(.json or .txt) and save it to output_file_path

        :return: save .png to output_file_path
        :rtype: .png
        """
        text_str = ''
        text_list = ''
        message = self.data['messages']

        for msg in message:

            # string text messages
            if isinstance(msg['text'], str):
                tokens = word_tokenize(msg['text'])
                tokens = list(filter(lambda x: x not in self.stopwords, tokens))
                text_str += f" {' '.join(tokens)}"

            # list text messages
            elif isinstance(msg['text'], list):
                for i in msg['text']:
                    if isinstance(i, str):
                        tokens = word_tokenize(i)
                        tokens = list(filter(lambda x: x not in self.stopwords, tokens))
                        text_list += f" {' '.join(tokens)}"
                    else:
                        pass

        text_content = text_str + ' ' + text_list

        #reshape, and normalize text content
        text = self.normalizer.normalize(text_content)
        text = arabic_reshaper.reshape(text[:500000])
        text = get_display(text)

        # generate wordcloud
        wordcloud = WordCloud(
        font_path=str(DATA_DIR / 'Mitra_Bold.ttf'),
        width=800,
        height=400,
        background_color='white'
        ).generate(text)

        # save to output_file_path
        wordcloud.to_file(str(Path(output_file_path) / 'wordcloud.png'))

