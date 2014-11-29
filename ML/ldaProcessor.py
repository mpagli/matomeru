#!/usr/bin/python

import gensim
import sys
import json

class LDA_processor(object):
	"""class responsible of processing the raw list of documents. Generate a list of bow representation."""

	def __init__(self,corpus,id2token,token2id,numTopics=20,alpha=None,beta=None):
		"""corpus is a tokenized version of the corpus: a list of list of tokens"""
		self.dictionary = gensim.corpora.Dictionary()
		self.dictionary.token2id = token2id
		self.dictionary.id2token = id2token
		self.corpus = []
		for doc in corpus:
			self.corpus.append(self.dictionary.doc2bow(doc,allow_update=False))
		print self.corpus
		self.lda = gensim.models.ldamodel.LdaModel(corpus=self.corpus, id2word=self.dictionary.id2token, num_topics=numTopics,alpha=alpha,eta=beta)

	def dumpJson(self):
		jsonString = {}
		jsonString['phi']={'''put here the top 80 words for each topics (word,proba)'''}
		for idx in xrange(len(self.corpus)):
			paragrapheKey = idx
			jsonString['theta'][paragraphKey] = {'''put here the theta distrib: top 20 topics (topicId,proba)'''}
			json.dumps(jsonString)

if __name__ == "__main__":

	corpus = [['a','b','c','d','a'],['e','g','g','b','a'],['e','g','e','e','r']]

	id2token = {}
	token2id = {}

	for doc in corpus:
		for word in doc:
			if word not in token2id:
				token2id[word] = len(token2id)
				id2token[len(id2token)] = word

	lda = LDA_processor(corpus,id2token,token2id)