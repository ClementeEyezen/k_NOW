from know.access import news

import arrow

from textblob import TextBlob, Word
from textblob.wordnet import NOUN

print('begin load spacy')
import spacy
nlp = spacy.load('en_core_web_sm')
print('done load spacy')

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

if __name__ == '__main__':
    articles = news.articles_call()

    for article in articles:
        title = article['title']
        description = article['description']

        blob = TextBlob(description)
        nouns = blob.noun_phrases

        print('blob processing')

        news_city = nouns[0]
        new_org = nouns[1]

        print('blob nouns')

        for noun in nouns[2:]:
            noun = noun.lemmatize()
            w = Word(noun)
            categories = w.get_synsets(pos=NOUN)
            print(noun, '->')
            for element in categories:
                print(element, '->', element.definition())

        print('spacy processing')

        doc = nlp(description)

        print('spacy entities')

        for ent in doc.ents:
            print(ent.text, '->', ent.label_, '->', spacy.explain(ent.label_))
            thing = Word(ent.text)
            concepts = thing.get_synsets(pos=NOUN)
            for synset in concepts:
                print(synset, '->', synset.definition())
                # TODO(buckbaskin): pick best concept match? or weight edge of matches with max similarity
                for lemma_name in synset.lemma_names():
                    print(lemma_name, '->', nlp(str(noun)).similarity(nlp(str(lemma_name))))
        1/0

        # deal with time
        publish_time = article['publishedAt']
        publish_time = arrow.get(publish_time)
        # print(weekdays[publish_time.weekday()], months[publish_time.month], publish_time.day, publish_time.year)
        year = publish_time.year
        month = publish_time.month
        day = publish_time.day
        weekday = publish_time.weekday()
        time_of_day = publish_time.time()
