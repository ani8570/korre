import glob
import os
import pathlib
import kss
from korre import KorRE

# f = open("새파일.txt", 'w')
# f.close()

# f = open("C:/doit/새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

def get_file_by_document(path) :
    dic = {}
    years_path = pathlib.Path(path)
    years = list(years_path.glob('*'))
    for year in years:
        review_file_paths = pathlib.Path(year)
        reviews = list(review_file_paths.glob('*.txt'))
        dic[year.name] = reviews
    
    return dic

def get_sentence_by_file(dic) :
    k =next(iter(dic))
    print(k)
    print(dic[k][0])
    
    f = open( dic[k][0], "r", encoding="utf-8")
    korre = KorRE()
    
    while True:
        line = f.readline()
        if not line: 
            break
        for sent in kss.split_sentences(line) :
            print(sent)
        break
    
    f.close()
    
    
if __name__=='__main__':
    path = "./economic"
    dic = get_file_by_document(path)
    get_sentence_by_file(dic)