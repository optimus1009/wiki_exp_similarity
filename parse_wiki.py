# -*- coding: utf-8 -*-

import os 
import sys

import json

def parse_wiki():
    for line in sys.stdin:
        wiki_id, wiki_content, comment_list = line.strip().split('$&&$')
        try:
            content_arr = json.loads(content)
        except:
            continue
        try:
            content_tmp = content_arr[0]['content'][0]['content']
            content_utf = content_tmp.encode('utf-8')
        except:
            continue
        if len(content_utf) > 300:
            print wiki_id + '\t' + content_utf + '\t' + comment_list
if __name__ == '__main__':
    parse_wiki()