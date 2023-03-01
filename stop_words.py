import pickle
def read():
    with open('raw_stop_words.txt') as file:
        stopwords = [line.rstrip().lower() for line in file]  
    file.close()
    stopwords = set(stopwords)
    return stopwords

def save(stopwords_pkl):
    with open('stop_words.pkl', 'wb') as file:
        pickle.dump(stopwords_pkl, file, protocol = pickle.HIGHEST_PROTOCOL)

def stopwords():
    with open('stop_words.pkl', 'rb') as file:
        stopwords = pickle.load(file)
    file.close()
    return stopwords

if __name__ == '__main__':
    save(read())
    # print(stopwords())