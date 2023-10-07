# -*- coding: utf-8 -*-
# Copyright 2019 Bruno Toshio Sugano <brunotoshio@gmail.com>
from collections import Counter
from typing import Dict, List, Tuple

from .dict_handler import DictHandler


class DictCounter:
    def __init__(self, dict_path: str):
        """Handles counting of words within each category.

        :param dict_path: The path to the dictionary file.
        :type dict_path: str
        """
        self._dict = DictHandler(dict_path)
        self.reset()

    def count(self, list_of_words: List[str]):
        """Count word occurrences within each category.
        This method will count words and store the results.
        You should use this method in conjunction with :func:`top` or :func:`top_normalized`.
        Ex:
        >>> counter = DictCounter("path/to/dict.dic")
        >>> counter.count(["word1", "word2", "word3"])
        >>> counter.top()  # it will return [('category1', 3), ('category2', 2)]
        >>> counter.top_normalized()  # it will return [('category1', 0.6), ('category2', 0.4)]

        :param list_of_words: A list of words to be counted.
        :type list_of_words: List[str]
        """
        for word in list_of_words:
            self.number_of_words += 1
            categories_found = self._dict.search(word)
            self._category_counter.update(categories_found)
            for category in categories_found:
                self._category_words[category].append(word)

    def reset(self):
        """Reset the counter."""
        self.number_of_words = 0
        self._category_counter = Counter()
        self._category_counter.update(
            {category: 0 for category in self._dict.categories()}
        )
        self._category_words = {}
        self._category_words.update(
            {category: [] for category in self._dict.categories()}
        )

    def top(self, n: int = 100) -> List[Tuple[str, int]]:
        """Returns the top n categories and their respective counts.

        :param n: Number of categories to be returned, defaults to 100
        :type n: int, optional
        :return: A list of tuples containing the category and its count.
        :rtype: List[tuple[str, int]]
        """
        return self._category_counter.most_common(n)

    def top_normalized(self, n: int = 100) -> List[Tuple[str, int]]:
        """Returns the top n categories and their respective normalized counts.

        :param n: Number of categories to be returned, defaults to 100
        :type n: int, optional
        :return: A list of tuples containing the category and its normalized count.
        :rtype: List[tuple[str, int]]
        """
        normalized = Counter()
        for key in self._category_counter:
            normalized[key] = self._category_counter[key] / self.number_of_words
        return normalized.most_common(n)

    def words_found(self) -> Dict[str, List[str]]:
        """Returns a dictionary containing the words found for each category.

        :return: A dictionary containing the words found for each category.
        :rtype: dict[str, List[str]]
        """
        return self._category_words
