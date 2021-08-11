
#Nome: Jemis Dievas José Manhiça

  #---------------Code Description--------------------
  #Clean the file with the original tweets
  #Remove ALL the STOPWORDS
  #collect, clean and print the tweets in a IMG file using WORDCLOUD 
  #From: Mozambique
#---------------------------------------------------

#Important libraries for preprocessing using NLTK ( Natural Language Talkit)
# -*- coding: utf-8 -*-
!pip install --upgrade -q gspread

!pip install tweet-preprocessor

import preprocessor as p
import re
import nltk
#for same reason the line below give error
#nltk.download('portuguese')
#i had to use this solution below, and i hope it works
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
#---
from os import path
from PIL import Image
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#FIRST WE CLEAN THE FILE WITH  THE ORIGINAL TWEETS  ++++++++++++++++++++++++++++++++++++++++++++++

def use_tweet_preprocessor(tweet):
  """A python function that returns clean tweets, main functionalty based on https://github.com/s/preprocessor

  Args:
      tweet: tweet to be cleaned

  Returns:
      cleaned tweet based on selected p.set_options and defined regrex """

  p.set_options(p.OPT.EMOJI, p.OPT.HASHTAG, p.OPT.SMILEY, p.OPT.MENTION, p.OPT.URL) 
  clean_tweet = p.clean(tweet)
  clean_tweet = re.sub('@[^\s]+', '',clean_tweet) #to remove all words that starts with '@' using regrex
  return clean_tweet

use_tweet_preprocessor('Preprocessor is #awesome 👍 https://github.com/s/preprocessor')

with open("/content/testData.txt") as fp:
   for line in fp:
      #p.OPT.EMOJI, p.OPT.HASHTAG, p.OPT.SMILEY, p.OPT.MENTION, p.OPT.URL
        texto =use_tweet_preprocessor(line)
        #remove https
        l = re.sub(r'(?is)https.+', ' ', texto)
        #remove os unicodes
        nl = re.sub(r'(?is)\\u.+', ' ', l)
        #print de testS
        #print(nl)
        saveFile = open('cleanData.txt', 'a')
        saveFile.write(nl)
        saveFile.write('\n')
        saveFile.close()

#NOW WE We Remove ALL the STOPWORDS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#read the whle file
dirname = path.dirname("/content/cleanData.txt")

# Read the whole text.
text = open(path.join(dirname, 'cleanData.txt')).read()


#text = "Muitos dos eventos em tempos de paz durande a segunda metade do século." ( i userd this text for test...

#separate the text in tokens
text_tokens = word_tokenize(text)

#remove all the stopwords
tokens_without_sw =[word for word in text_tokens if not word in stopwords.words()]

#rejoin all the words without the stopwords
backToOneWord = (" ").join(tokens_without_sw)

text = backToOneWord;
#test to verify if the tokens a back together
#print(text)

#Now we print the colected and clean tweets in a IMG file using WORDCLOUD +++++++++++++++++++++++++++++++++++++++++

# Define a function to plot word cloud
def plot_cloud(wordcloud):
  # Set figure size
  plt.figure(figsize=(40, 30))
  # Display image
  plt.imshow(wordcloud) 
  # No axis details
  plt.axis("off");

# Import package
from wordcloud import WordCloud

#Geraamigo  wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1,
                    background_color='black', colormap='Set2', 
                    collocations=False, stopwords = STOPWORDS).generate(text)

# Plot
plot_cloud(wordcloud)

#Save the IMG File
wordcloud.to_file("wordcloud.png")
         
#read the whle file
dirname = path.dirname("/content/cleanData.txt")

# Read the whole text.
text = open(path.join(dirname, 'cleanData.txt')).read()

#separate the text in tokens
text_tokens = word_tokenize(text)

#remove all the stopwords
tokens_without_sw =[word for word in text_tokens if not word in stopwords.words()]

#rejoin all the words without the stopwords
backToOneWord = (" ").join(tokens_without_sw)

text = backToOneWord;
