import matplotlib.pyplot as plt
import nltk
import wordcloud
# =========================== #
def generateWordCloud(txt):
    # creating word cloud
    wc = wordcloud.WordCloud(width=800, height=800, relative_scaling=1.0, background_color='white',
                             stopwords={'.', ',', '\''}).generate(' '.join(txt))
    plt.imshow(wc) 
    plt.axis("off")
    plt.title("Suhaib Irsheidat Word Cloud")
    plt.savefig('wordcloud.png')
    plt.show()
# =========================== #
def main():
    a = open('words.txt', 'r') # open file in mode 'read=r'
    b = a.read() # store all content in 'b'
    words = nltk.word_tokenize(b) # tokenize
    stopwords_list = set(nltk.corpus.stopwords.words('english')) # remove stopwords
    after_filter = [] # needed for next loop
    for w in words:
        if w not in stopwords_list:
            after_filter.append(w)
    generateWordCloud(after_filter)
# =========================== #
if __name__ == '__main__':
    main()