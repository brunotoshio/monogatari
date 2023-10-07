# -*- coding: utf-8 -*-
# Copyright 2019 Bruno Toshio Sugano <brunotoshio@gmail.com>
from typing import List


class DictHandler:
    def __init__(self, path: str):
        """Handles the dictionary file.

        :param path: The path to the dictionary file.
        :type path: str
        """
        self._file_path = path
        self._categories = {}
        self._normal_dict = {}
        self._wildcard_dict = {}
        self.__parse()

    def __parse(self):
        """Parse the dictionary file."""
        category_part = False
        with open(self._file_path, "r") as f:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line == "%":
                    category_part = not category_part

                if category_part:
                    tokens = line.split()
                    if not tokens[0].isnumeric():
                        continue
                    self._categories[tokens[0].lower().strip()] = (
                        " ".join(tokens[1:])
                    ).strip()
                else:
                    tokens = line.split("\t")  # Force tab separation
                    key = tokens[0].strip()
                    categories = " ".join(
                        tokens[1:]
                    ).split()  # The category list can be separated by tabs or spaces
                    if key[-1] == "*":
                        self._wildcard_dict[key.lower()] = [
                            self._categories[tk] for tk in categories
                        ]
                    else:
                        self._normal_dict[key.lower()] = [
                            self._categories[tk] for tk in categories
                        ]

    def _wildcard_search(self, term: str) -> List[str]:
        """Search for the term in the wildcard dictionary.
        The search will only look for the first result by using a greedy algorithm.

        :param term: The term to be searched.
        :type term: str
        :return: A list of categories found for the term.
        :rtype: List[str]
        """
        for index, _ in enumerate(term):
            key = term[:-index] if index else term
            if f"{key}*" in self._wildcard_dict:
                return self._wildcard_dict[f"{key}*"]
        return []

    def search(self, term: str) -> List[str]:
        """Search for all categories associated with the term.

        :param term: The term to be searched.
        :type term: str
        :return: The list of categories associated with the term.
        :rtype: List[str]
        """
        search_term = term.lower()
        if search_term in self._normal_dict:
            return self._normal_dict[search_term]
        else:
            return self._wildcard_search(search_term)

    def categories(self) -> List[str]:
        """Return all categories in the dictionary.

        :return: The list of categories in the dictionary.
        :rtype: List[str]
        """
        return list(self._categories.values())
