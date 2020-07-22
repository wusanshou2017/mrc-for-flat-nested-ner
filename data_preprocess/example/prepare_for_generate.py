# encoding: utf-8
'''
@author: td.wu
@contact: tdwu@iflytek.com
@file: prepare_for_generate.py
@time: 2020/7/20 10:38
'''
def deal_with_text(words_file,tags_file):
    f1 = open(words_file,"r",encoding="utf-8")
    f2 = open (tags_file,"r",encoding="utf-8")
    words_lst = f1.readlines()
    tags_lst = f2.readlines()
    words_lst = [ item[:-1] for item in words_lst]
    tags_lst = [ item[:-1] for item in tags_lst]
    assert  (len(words_lst) ==len (tags_lst))
    n  = len (words_lst)
    word_tag_to_write =[]
    for words,tags in zip(words_lst,tags_lst):
        one_sent_words = words.split(" ")
        one_sent_tags   = tags.split(" ")
        for word, tag in zip (one_sent_words,one_sent_tags):
            word_tag_to_write.append(word+" "+tag+"\n")
        word_tag_to_write.append("\n")
    return word_tag_to_write

if __name__ == "__main__":
    demo_train_to_write = deal_with_text("test_words.txt","test_tags.txt")
    f_write = open("mrc_test.txt","w+",encoding="utf-8")

    f_write.writelines(demo_train_to_write)
    f_write.close()

    print ("finish write file...")

