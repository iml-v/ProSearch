RAJASTHAN HACKATHON 3.0 Hack!
PROSEARCH
> # What's ProSearch?

ProSearch is an app developed for the Rajasthan-Hackathon.It is a document reader app.

> # How it will help me?

Many a times, people read for long hours and yet gain little apart from false feeling of gratitude.
* Have you ever felt that you were too dizzy while reading a chapter only to later realize that haven’t actually understood the crux of it?
* Have you enjoyed easily getting away with reading assignments?
* Have you encountered a question right from the text and yet haven’t been able to answer it?

If your answer to any one or more of the above questions was yes, then you are in dire need of our app! With this simple mobile application we aim to revolutionize the education sector by providing immense help in improving one’s reading habits
With the advent of the social age, attention spans of individuals have significantly gone down. It has been observed that when people try to read for long hours, they seldom are able to grasp concepts. But having spent some time reading gives them a false sense of understanding it.
Our application (ProSearch) tackles this problem at its core, while also providing a one stop solution for all reading hardships an avid reader has always dreamt of. Move on to project description to know more.

> # How App works?

* ProSearch is an assisted reading application, that helps users continuously gauge their understanding of the material.
* A user can use it just like any other reading application (a pdf reader, a text reader etc)
* While you read through the material, Merlin (our intelligent chatbot) figures out your progress and crafts intelligent questions which pop up as counters at the side of your screen.
* Not only this, ProSearch also tries to be your intelligent encyclopedia. You can scan part of any interesting article and it suggests you a few topics that are closely related to it. You can go ahead and tap the suggestion box to read the same.
* It also comes along with an out of the box search engine, which when given with a search query fetches an appropriate article for the topic.
* Questions you fail to answer automatically move to the flashcards section which you can later revisit to revise concepts.
* Overall, ProSearch, with the wizard Merlin, forms a one stop solution to all your reading hardships

> System Architecture


![System Architecture]

* User reads after searching some keyword or uploading document or scanning a necessaary article.
* When a reader scrolls through the content, we use the position of the scroll to estimate the approximate piece of text the user is likely to be reading and sends request to the server.
* After response from the server, questions are displayed to the user via an interactive chatbot.
* Questions answered incorrectly ended up in flashcards for future review

> # Model for Question Generation

Wikitrivia question generation code for quick prototyping has been used for the application. This project uses a rule based mechanism to generate a blank in a given statement or a paragraph which  serves as our simple question. To generate the set of possible answers, WordNet(large lexical database of English in layman terms) is used.The blanked word is searched over wordnet using the NLTK library and hyponyms or hypernym of that words act as the set of all possible answers. This basically serves the purpose to find words of similar contextual meaning that fit right and complete the sentence.

> # Server APIs

Detailed description of api along with request and response format is available in the [README]

We are a set of four undergraduates pursuing Electrical Engi. at IIT Roorkee.

**https://github.com/iml-v

**https://github.com/Satyendra-IITR

**https://github.com/Prabhat-IIT

**https://github.com/Dishank-sopho
