#!/usr/bin/python

import gensim
import sys
import json

class LDA_processor(object):
	"""class responsible of processing the raw list of documents. Generate a list of bow representation."""

	def __init__(self,corpus,id2token,token2id,numTopics=5,alpha=None,beta=None,topk_phi=5,topk_theta=3):
		"""corpus is a tokenized version of the corpus: a list of list of tokens"""
		self.dictionary = gensim.corpora.Dictionary()
		self.dictionary.token2id = token2id
		self.dictionary.id2token = id2token
		self.topk_phi = topk_phi
		self.topk_theta = topk_theta
		self.numTopics = numTopics
		self.corpus = []
		for doc in corpus:
			self.corpus.append(self.dictionary.doc2bow(doc,allow_update=False))
		self.lda = gensim.models.ldamodel.LdaModel(corpus=self.corpus, id2word=self.dictionary.id2token, num_topics=numTopics,alpha=alpha,eta=beta)

	def dumpJson(self):
		"""dump the json data on stdout"""
		phi = [0 for x in xrange(self.numTopics)]
		jsonString = {}
		jsonString['phi']   = {}
		jsonString['theta'] = {}

		for k,p in enumerate(self.lda.show_topics(num_topics=self.numTopics, num_words=self.topk_phi,formatted=False)):
			jsonString['phi'][k] = p

		for docIdx in xrange(len(self.corpus)):
			paragrapheKey = docIdx
			jsonString['theta'][paragrapheKey] = self.lda[self.corpus[docIdx]][:self.topk_theta]
		
		print json.dumps(jsonString)

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
	lda.dumpJson()
	"""
	{
		"theta": 
			{	"0": [[0, 0.86578723417878112], [1, 0.033389812948097917], [2, 0.033389915355721347]], 
				"1": [[0, 0.034230346089382198], [1, 0.033364801720878613], [2, 0.033364671349721563]], 
				"2": [[0, 0.86527938267991411], [1, 0.033375536476196878], [2, 0.033375237270156441]]
			}, 
		"phi": 
			{
				"0": [[0.28069143211945785, "e"], [0.19311206586362623, "a"], [0.1054685278080317, "g"], [0.10521623128968031, "r"], [0.10520727996679316, "b"]], 
				"1": [[0.14441071173540376, "e"], [0.14343698873241437, "g"], [0.14322803628502906, "a"], [0.14255174236024798, "b"], [0.14222040382120565, "d"]], 
				"2": [[0.14396503113458209, "e"], [0.14335373891249834, "g"], [0.14316165653520091, "a"], [0.14295869295994729, "b"], [0.14227922554069747, "c"]], 
				"3": [[0.14396263872106241, "e"], [0.14354210196324785, "g"], [0.14352937852965286, "a"], [0.14318998676633884, "b"], [0.14214959483018913, "c"]], 
				"4": [[0.34312732237392057, "g"], [0.18761969327857833, "e"], [0.18741889608759466, "b"], [0.18736309716796451, "a"], [0.031538818122287961, "c"]]
			}
	}

	"""
