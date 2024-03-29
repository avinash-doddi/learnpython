""" this a project to create a word cloud (please refer to google about how word cloud looks ;p) using the wordcloud module in python
    and used the fileupload module to decode the text file and used the numpy and matplotlib modules to generate a word cloud """

# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

# This is the uploader widget
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
def _upload():

    _upload_widget = fileupload.FileUploadWidget()
    
def _cb(change):
    """ this is a syntax to decode the text (.txt) file """
    global file_contents
    decoded = io.StringIO(change['owner'].data.decode('utf-8'))
    filename = change['owner'].filename
    print('Uploaded `{}` ({:.2f} kB)'.format(
        filename, len(decoded.read()) / 2 **10))
    file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
                  
    
    # LEARNER CODE START HERE
    file_contents = file_contents.split()
    frequency = {}
    for word in file_contents:
        if (word.isalpha() and len(word) > 2):
            if (word in frequency):
                frequency[word] += 1;
            else:
                frequency[word] = 1;
    #return frequency
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency)  # frequency is the dictionary name
    return cloud.to_array()

  # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
#print(myimage)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
