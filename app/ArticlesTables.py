# -*- coding: ascii -*-
from flask_table import Table, Col, LinkCol

class RawCol(Col):
    """Class that will just output whatever it is given and will not
    escape it.
    """
    def td_format(self, content):
        return content

class ArticleTable(Table):
    score = Col('Sentiment Score')
    trick = RawCol('Headline')

def get_articles_table(list_of_dic):

    new_list_of_dic = []
    for dic in list_of_dic:

        title = dic['title']
        url = dic['link']

        score = '%s' % float('%.1g' % dic['sentiment_score'])
        trick = '<a href=\"%s\" > %s </a>' % (url, title)

        new_dic = {'score': score,
                    'trick':trick
                    }

        print(new_dic)
        new_list_of_dic.append(new_dic)

    return ArticleTable(new_list_of_dic, border=False)

if __name__ == '__main__':
    fake = [{'title':'a','link':'https://www.nytimes.com/','sentiment_score':0.333}]
    print fake
    print get_articles_table(fake)
    print(get_articles_table(fake).__html__())
