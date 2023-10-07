# Monogatari

## Installation
To install:
```sh
pip install monogatari
```

## Quick start

### General usage

Any dictionary file defined with the format:
```
%
Category_key_1   Category_value_1
Category_key_2   Category_value_2
Category_key_3   Category_value_3
Category_key_4   Category_value_4
%

Word_key_1     Category_key_1    Category_key_2
Word_key_2     Category_key_1
Word_key_3     Category_key_2
Word_key_4     Category_key_1    Category_key_3
Word_key_5     Category_key_1    Category_key_2    Category_key_4
Word_key_6     Category_key_4
```

Where:
- Each category key must be a number.
- Each word_key must be separated by a `tab` in between category keys.
- The match is not case sensitive, that is, uppercase or lowercase won't make a difference in word_keys.
- Word_keys can contain whitespaces (ex: "kind of"), that's why it's important to separate the word_key and category_keys with a `tab`.

```python
from monogatari import DictCounter

counter = DictCounter("dictionary_file.dic")  # Load the dictionary

list_of_words = ["My", "list", "of", "words"]

counter.count(list_of_words)  # This will count the words in each category

counter.top(100)  # This will return a list of the top 100 categories and their count
# {("category_A", 12), ("category_B", 9), ...}

counter.top_normalized(100)  # This will return a list of the top 100 categories and their normalized value
# {("category_A", 0.014), ("category_B", 0.008), ...}

counter.words_found()  # This will return all categories and for each, a list of words belonging to that category
# {"category_A": ["I", "am", "here"], "category_B": ["something"], ...}

counter.reset()  # This will reset the count, so that you can count again using another list of words
```

### Pre-loaded MFD dictionary

The following example uses a pre-loaded MFD dictionary (from [https://www.moralfoundations.org/](https://www.moralfoundations.org/)).
```python
from monogatari import MFDCounter

counter = MFDCounter()

list_of_words = ['私', 'コーヒー', '好き', '友達']

counter.count(list_of_words)

counter.top(100)  # List top N categories, ordered by number of words

counter.top_normalized(100)  # List top N categories, ordered by number of words normalized by the total number of words
```

### Pre-loaded JMFD dictionary

The following example uses a pre-loaded JMFD dictionary (from [https://github.com/soramame0518/j-mfd](https://github.com/soramame0518/j-mfd)).
```python
from monogatari import JMFDCounter

counter = JMFDCounter()

list_of_words = ['私', 'コーヒー', '好き', '友達']

counter.count(list_of_words)

counter.top(100)  # List top N categories, ordered by number of words

counter.top_normalized(100)  # List top N categories, ordered by number of words normalized by the total number of words
```
### LIWC example

The library is also compatible with the LIWC dictionary.
```python
from monogatari import DictCounter

counter = DictCounter("liwc_dictionary_file.dic")  # Load the dictionary

list_of_words = ["My", "list", "of", "words"]

counter.count(list_of_words)  # This will count the words in each category

counter.top(100)  # This will return a list of the top 100 categories and their count
# {("category_A", 12), ("category_B", 9), ...}

counter.top_normalized(100)  # This will return a list of the top 100 categories and their normalized value
# {("category_A", 0.014), ("category_B", 0.008), ...}
```
