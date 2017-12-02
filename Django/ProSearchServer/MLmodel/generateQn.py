from nltk.corpus import wordnet as wn
from textblob import TextBlob

import re
import wikipedia
import json

class Article:
    

    def __init__(self, title, text):
        self.title = title
        self.summary = TextBlob(text)

    def generate_trivia_sentences(self):
        sentences = self.summary.sentences

        
        del sentences[0]

        trivia_sentences = []
        for sentence in sentences:
            trivia = self.evaluate_sentence(sentence)
            if trivia:
                trivia_sentences.append(trivia)

        return trivia_sentences

    def get_similar_words(self, word):
        
        synsets = wn.synsets(word, pos='n')
        
        if len(synsets) == 0:
            return []
        else:
            synset = synsets[0]

        
        hypernym = synset.hypernyms()[0]

        
        hyponyms = hypernym.hyponyms()

        
        similar_words = []
        for hyponym in hyponyms:
            similar_word = hyponym.lemmas()[0].name().replace('_', ' ')
            
            if similar_word != word:
                similar_words.append(similar_word)

            if len(similar_words) == 8:
                break

        return similar_words

    def evaluate_sentence(self, sentence):
        if sentence.tags[0][1] == 'RB' or len(sentence.words) < 6:
            
            return None

        tag_map = {word.lower(): tag for word, tag in sentence.tags}

        replace_nouns = []
        for word, tag in sentence.tags:
            
            if tag == 'NN' and word not in self.title:
                
                for phrase in sentence.noun_phrases:
                    if phrase[0] == '\'':
                        
                        break

                    if word in phrase:
                        
                        [replace_nouns.append(phrase_word) for phrase_word in phrase.split()[-2:]]
                        break

                
                if len(replace_nouns) == 0:
                    replace_nouns.append(word)
                break
        
        if len(replace_nouns) == 0:
            
            return None

        trivia = {
            'title': self.title,
            'answer': ' '.join(replace_nouns)
        }

        if len(replace_nouns) == 1:
            
            trivia['similar_words'] = self.get_similar_words(replace_nouns[0])
        else:
            
            trivia['similar_words'] = []

        replace_phrase = ' '.join(replace_nouns)
        blanks_phrase = ('__________ ' * len(replace_nouns)).strip()

        expression = re.compile(re.escape(replace_phrase), re.IGNORECASE)
        sentence = expression.sub(blanks_phrase, str(sentence), count=1)

        trivia['question'] = sentence
        #print trivia

        return trivia

import click
import json
import sys


def get_file_content(file_name):
    with open(file_name, 'r') as stream:
        content = stream.read()

    return content


def generate_trivia(titles):
    print titles
    if not titles:
        sys.exit("No topics fed!")

    questions = []
    for article in titles:
        text = titles[article]
        click.echo('Analyzing \'{0}\''.format(article))
        if text is None:
            text = get_file_content(article)
        article = Article(title=article, text=text)
        questions = questions + article.generate_trivia_sentences()

    result = json.dumps(questions, sort_keys=True, indent=4)
    print(result)
    return result


@click.command()
@click.argument('titles', nargs=-1)
def qa_generator(titles):
    title_dict = {}
    for title in titles:
        title_dict[title] = None
    generate_trivia(title_dict)


if __name__ == '__main__':
    request = "{\"student\":\"A student is a person who is learning something. Students can be children, teenagers, or adults who are going to school, but it may also be other people who are learning, such as in college or university. \" , \"Rajasthan\":\"Rajasthan is India\'s largest state by area It is located on the north western side of the India, where it comprises most of the wide and inhospitable Thar Desert (also known as the \"Rajasthan Desert\" and \"Great Indian Desert\") and shares a border with the Pakistani provinces of Punjab to the northwest and Sindh to the west\"}"
#    json_str = request.body.decode('utf-8')
    request_json = json.loads(request)
    generate_trivia(request_json)