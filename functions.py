#Author: Goldie Segol

import bs4 as bs
import requests
import urllib3
import xlwt
import lxml
import re
from dynamicArray import*

def isVowel(char):
	return char.lower() in 'aeiouāā̆ēẹ̄ē̆īōō̆ūǣ'

def removeVowels(str):
	result = ''
	for i in range(len(str)):
		if((isVowel(str[i]))==False): result = result + str[i]
	return result

def printArr(arr):
	for i in range(0, len(arr)):
		print(arr[i])

def trimArr(tempArr, headWord):
	formArr = DynamicArray()
	for i in range(len(tempArr)):
		foo = tempArr[i]
		comp = foo[0]
		if(comp == headWord[0]):
			formArr.append(foo)
		elif((headWord[0] == 'c') | (headWord[0] == 'k')):
			if((comp == 'c') | (comp == 'k')):
				formArr.append(foo)
		elif(foo[:2] == 'i)'):
			formArr.append(foo[2:])
	return formArr

def stringToArr(str):
	result = DynamicArray()
	result2 = DynamicArray()
	temp = ''
	for i in range(len(str)):
		if((str[i] != ' ') & (str[i] != ',') & (str[i] != '.') & (str[i] != ';') & (str[i] != '(')):
			temp = temp + str[i]
		elif(str[i] == ' '):
			result.append(temp)
			temp = ''
	for i in range(len(result)):
		if(len(result[i])>0):
			result2.append(result[i])
	return result2

def consonantsRatio(str, headWord):
	str1 = removeVowels(str)
	str2 = removeVowels(headWord)
	set1 = set()
	set2 = set()
	for i in range(len(str1)):
		set1.add(str1[i])
	for i in range(len(str2)):
		set2.add(str2[i])
	intLength = len(set2.intersection(set1))
	result = intLength/len(str2)
	return result


def main(url):

	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

	http = urllib3.PoolManager()

	response = http.request('GET', url)
	soup = bs.BeautifulSoup(response.data, "lxml")

	forms = soup.find("p").findNext("p").get_text()
	headWord = soup.find("strong").get_text()



	print()
	print("HEADWORD: " + headWord)
	print("FORMS: " + forms)



	formArr = trimArr(stringToArr(forms), headWord)
	citations = ''



	for paragraph in soup.find_all('blockquote'):
		citations = citations + ' ' + paragraph.get_text()

	citationsArr = DynamicArray()

	start = ':'
	end = '.'
	add = False
	foo = ''

	#filter out citations
	for i in range(len(citations)-1):
		if(citations[i] == start):
			add = True
		if((citations[i] == end) & (citations[i+1] == end)):
			foo = foo + citations[i]
		elif((citations[i] == end) & (citations[i-1] !=end)):
			add = False
			citationsArr.append(foo)
			foo = ''
		elif(add):
			foo = foo + citations[i]

	wordArr = DynamicArray()
	#filter each sentence down to target words
	for i in range(len(citationsArr)):
		#full sentence
		sent = citationsArr[i]
		sentArr = stringToArr(sent)
		for j in range(len(sentArr)):
			word = sentArr[j]
			if(word[0] == headWord[0]):
				wordArr.append(word)
			elif((headWord[0] == 'c') | (headWord[0] == 'k')):
				if((word[0] == 'c') | (word[0] == 'k')):
					wordArr.append(word)
			elif((headWord[0] == 'f') | (headWord[0] == 'v')):
				if((word[0] == 'f') | (word[0] == 'v')):
					wordArr.append(word)

	finalArr = DynamicArray()

	for i in range(len(wordArr)):
		if((consonantsRatio((wordArr[i]),headWord))>.4):
			finalArr.append(wordArr[i])
	return finalArr

def returnHeadWord(url):
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

	http = urllib3.PoolManager()

	response = http.request('GET', url)
	soup = bs.BeautifulSoup(response.data, "lxml")
	headWord = soup.find("strong").get_text()

	return headWord
