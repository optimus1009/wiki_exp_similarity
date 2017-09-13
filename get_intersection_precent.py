# -*- coding: utf-8 -*-

from __future__ import division
import re
import jieba

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
digit_alpha_pattern = re.compile(r"[A-Za-z0-9\[\`\~\!\@\#\$\^\&\?\...\】\【\!\《\》\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\!\@\#\\\&\*\%]")

with open('./stopwords.txt','r') as f:
    stop_word_list = [unicode(w.strip('\n').strip('\t').replace('\r',''),'utf-8') for w in f.readlines()]
stop_set =set(stop_word_list)
out_put_file = open('./out.data','w')
with open('./test_wiki.data','r') as wiki_file:
    for line in wiki_file:
        #处理知识，
        wiki_raw = line.strip().split('\t')[1]
        wiki_raw = wiki_raw.decode('utf-8')
        tmp_wiki = digit_alpha_pattern.sub("", wiki_raw)
        wiki = emoji_pattern.sub('',tmp_wiki)
        #处理经验
        comment_raw = line.strip().split('\t')[2]
        
        tmp_wiki = []
        for i in jieba.cut_for_search(wiki,HMM = True):
            tmp_wiki.append(i)
        wiki_set = set(tmp_wiki) - stop_set
        comment_list = comment_raw.split('|')
        for elem in comment_list:
            tmp_comment = []
            elem = elem.decode('utf-8')
            comment_1 = digit_alpha_pattern.sub(r"", elem)
            comment = emoji_pattern.sub(r'',comment_1)
            print 'comment: ',comment
            for i in jieba.cut_for_search(comment,HMM = True):
                tmp_comment.append(i)
            comment_set = set(tmp_comment) - stop_set
            print 'cut word:','|'.join(comment_set)
            if len(comment_set) >= 0 and len(comment_set) <= 8:
                out_put_file.write(wiki_raw.encode('utf-8') + '\t' + elem.encode('utf-8') + '\t' + str(0) + '\n')
            else:
                intersection = len(comment_set & wiki_set)
                iner_percent = intersection/len(comment_set)
                out_put_file.write(wiki_raw.encode('utf-8') + '\t' + elem.encode('utf-8') + '\t' + str(iner_percent) + '\n')
out_put_file.close()
