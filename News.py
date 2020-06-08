import json
import xml.etree.ElementTree as ET
from pprint import pprint

def json_to_list():
    with open('newsafr.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = data['rss']['channel']['items']
        news_discriptions = []
        for item in data_list:
            news_body = item['description']
            news_body = news_body.split(' ')
            news_discriptions.extend(news_body)
        return news_discriptions

def xml_to_list():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    discription = root.findall('channel/item/description')
    news_discriptions = []
    for item in discription:
        news_body = item.text
        news_body = news_body.split(' ')
        news_discriptions.extend(news_body)
    return news_discriptions

def sort_by_length(length,file_type):

    if file_type == 'json':
        news_discriptions = json_to_list()
    elif file_type == 'xml':
        news_discriptions = xml_to_list()
    sorted_news_discriptions = sorted(news_discriptions, key=len, reverse=True)
    for word in sorted_news_discriptions:
        if len(word) <= length:
            last_element = sorted_news_discriptions.index(word)
            break
    cut_news_discriptions = sorted_news_discriptions[:last_element]
    return cut_news_discriptions

def top_popular_words(number, length, file_type):
    news_discription = sort_by_length(length, file_type)
    frequency_list = []
    temp_top_dict = {}
    for word in news_discription:
        if word in frequency_list:
            temp_top_dict[word] += 1
        else:
            temp_top_dict[word] = 1
        frequency_list.append(word)
    top_dict = sorted(temp_top_dict, key=lambda x: temp_top_dict[x], reverse=True)
    cut_top_dict = top_dict[:number]
    print(cut_top_dict)


top_popular_words(10, 6, 'xml')