# -*- coding: utf-8 -*-
# Copyright 2019 Bruno Toshio Sugano <brunotoshio@gmail.com>
import os
from collections import Counter

import pytest

from monogatari import DictCounter


@pytest.fixture
def counter() -> DictCounter:
    test_dir = os.path.dirname(__file__)
    return DictCounter(f"{test_dir}/testdic.dic")


def test_reset(counter: DictCounter):
    counter.number_of_words = 9
    counter._category_counter = Counter(["01", "02", "03"])
    counter.reset()
    assert counter.number_of_words == 0
    assert all(counter._category_counter[k] == 0 for k in counter._dict.categories())
    assert all(counter._category_words[k] == [] for k in counter._dict.categories())


def test_count(counter: DictCounter):
    counter.count(["守る", "治安", "親善", "安全", "Word", "Another", "Kind of"])
    assert counter._category_counter["HarmVirtue"] == 5
    assert counter._category_counter["HarmVice"] == 3
    assert counter._category_words["HarmVirtue"] == [
        "守る",
        "親善",
        "安全",
        "Word",
        "Another",
    ]
    assert counter._category_words["HarmVice"] == ["親善", "Word", "Kind of"]


def test_top(counter: DictCounter):
    counter.count(["守る", "治安", "親善", "安全"])
    assert counter.top(1000) == [("HarmVirtue", 3), ("HarmVice", 1)]


def test_top_normalized(counter: DictCounter):
    counter.count(["守る", "治安", "親善", "守る", "安全"])
    assert counter.top_normalized(1000) == [("HarmVirtue", 0.8), ("HarmVice", 0.2)]


def test_words_found(counter: DictCounter):
    counter.count(["守る", "治安", "親善", "安全"])
    assert counter.words_found() == {
        "HarmVice": ["親善"],
        "HarmVirtue": ["守る", "親善", "安全"],
    }
