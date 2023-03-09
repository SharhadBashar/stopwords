import os
import pickle

def get_paths():
    with open('save_paths.txt') as file:
        paths = [line.rstrip().lower() for line in file]  
    file.close()
    return paths

def read():
    with open('raw_stop_words.txt') as file:
        stopwords = [line.rstrip().lower() for line in file]  
    file.close()
    stopwords = set(stopwords)
    return stopwords

def save(stopwords_pkl, paths):
    with open('stop_words.pkl', 'wb') as file:
        pickle.dump(stopwords_pkl, file, protocol = pickle.HIGHEST_PROTOCOL)
    for path in paths:
        try:
            with open(os.path.join(path, 'stop_words.pkl'), 'wb') as file:
                pickle.dump(stopwords_pkl, file, protocol = pickle.HIGHEST_PROTOCOL)
        except:
            None
    
def stopwords():
    with open('stop_words.pkl', 'rb') as file:
        stopwords = pickle.load(file)
    file.close()
    return stopwords

if __name__ == '__main__':
    paths = get_paths()
    save(read(), paths)
    # print(stopwords())