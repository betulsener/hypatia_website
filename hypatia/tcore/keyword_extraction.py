from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import nltk
from nltk.stem import WordNetLemmatizer
import sqlite3

conn = sqlite3.connect('/Users/betulsener/Desktop/Graduation Project/hypatia/db.sqlite3')
cur = conn.cursor()

cur.execute('SELECT message FROM tcore_input')
messages = cur.fetchall()

messages_list = [message[0] for message in messages]

print (messages_list)
processed_texts = []


dictionary = {}
with open("/Users/betulsener/Desktop/Graduation Project/hypatia/tcore/turkce-stop-words.txt", 'r', encoding='utf-8') as fdict:
	for line in fdict:
		if (line[0] not in ['0', '1']):
			continue

		freq, word = line.strip().split()
		dictionary[word] = int(freq)
def is_stop_word(word):
	return word in dictionary.keys()
def get_word_freq(word):
	if is_stop_word(word):
		return dictionary[word]
	else:
		return 0.
if __name__ == '__main__':
	ftest = open("/Users/betulsener/Desktop/Graduation Project/hypatia/tcore/turkce-stop-words.txt", encoding="utf-8")

	for word in ftest:
		word = word.strip()
            
		is_stop_word
	ftest.close()
for text in messages_list:
# Tek tırnak işaretlerini boşlukla değiştir
    text = text.replace("'", " ")
    text = text.replace("‘", " ")
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("’", " ")

    pattern = r'\b(?:[1-9][0-9]{0,2}|1[0-6][0-9]{2}|1700)\b'
    text = re.sub(pattern, '', text)

processed_texts.append(text)
print(processed_texts)

final_text = ' '.join(processed_texts)

def remove_stopwords(final_text, stopwords):
    """
    Verilen metinden stopwords'leri kaldırır.

    text: str, işlenecek metin
    stopwords: list, stopwords listesi
    return: str, stopwords'lerin kaldırıldığı metin
    """
    words = final_text.split()  # Metni kelimelere ayır

    # Stopwords olmayan kelimelerden oluşan yeni bir metin oluştur
    filtered_words = [word for word in words if word.lower() not in stopwords]

    # Filtrelenmiş kelimeleri boşluk karakteriyle birleştirerek metni oluştur
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

# Stopwords dosyasını aç ve stopwords listesini oluştur
stopwords_file = open("/Users/betulsener/Desktop/Graduation Project/hypatia/tcore/turkce-stop-words.txt", 'r', encoding='utf-8')
stopwords = [word.strip() for word in stopwords_file]


# Stopwords'leri kaldır
clean_text = remove_stopwords(text, stopwords)

# Sonucu yazdır
print("Metin after stopwords removal:")
print(clean_text)

from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

# Sample text after stopwords removal
# Split the text into sentences
sentences = nltk.sent_tokenize(clean_text)

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=1000)

# Fit and transform the documents
X = vectorizer.fit_transform(sentences)

# Get the feature names
terms = vectorizer.get_feature_names_out()

# Calculate scores
scores = X.toarray().sum(axis=0)


keywords = dict(zip(terms, scores))


# Maksimum kelime sınırlaması
max_keywords = 20  # Örneğin, en fazla 10 anahtar kelimeye izin vermek istiyoruz

# Skorlara göre terimleri sırala
sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)

# Maksimum kelime sınırlamasına göre sıralı terimlerden yeni bir sözlük oluştur
limited_keywords = dict(sorted_keywords[:max_keywords])

print(limited_keywords)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(limited_keywords)
# Kelime bulutunu görselleştirme
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
