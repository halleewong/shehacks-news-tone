# -*- coding: ascii -*-
from flask_table import Table, Col
ACCEPTED=['.', ',', '/', ':', " ", "_", "-"]

class ArticleTable(Table):
    score = Col('Sentiment Score')
    headline = Col('Headline')
    url = Col('URL')


def get_articles_table(list_of_dic):

    new_list_of_dic = []
    for dic in list_of_dic:

        title = dic['title']
        link = dic['link']
        score =  '%s' % float('%.1g' % dic['sentiment_score'])

        new_dic = {'score': score,
                    'headline':title,
                    'url':link}

        new_list_of_dic.append(new_dic)

    return ArticleTable(new_list_of_dic, border=False)

if __name__ == '__main__':
    fake = [{'title':'a','link':'1'}]
    print fake
    print get_articles_table(fake)
