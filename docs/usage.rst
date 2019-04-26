=====
Usage
=====

To use monogatari in a project::

	from monogatari import JMFDCounter

	counter = JMFDCounter()

	list_of_words = ['私', 'コーヒー', '好き', '友達']

	counter.count(list_of_words)

	counter.top(100)  # List top N categories, ordered by number of words

	counter.top_normalized(100)  # List top N categories, ordered by number of words normalized by the total number of words

In this example, we are using J-MFD dictionary (https://github.com/soramame0518/j-mfd) as the base for word counting.
However, we can load a custom dictionary using the class ```DictCounter```.

	from monogatari import DictCounter

	counter = DictCounter('/path/to/the/dictionary.dic')

	list_of_words = ['私', 'コーヒー', '好き', '友達']

	counter.count(list_of_words)

	counter.top(100)  # List top N categories, ordered by number of words

	counter.top_normalized(100)  # List top N categories, ordered by number of words normalized by the total number of words

----------------------
Available dictionaries
----------------------

* MFD (from https://www.moralfoundations.org/)

	from monogatari import MFDCounter

	counter = MFDCounter()

* JMFD (from https://github.com/soramame0518/j-mfd)

	from monogatari import JMFDCounter

	counter = JMFDCounter()
