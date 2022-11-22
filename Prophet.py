from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
##import pymongo
import re
from urllib.parse import quote_plus

from youtube_transcript_api import YouTubeTranscriptApi
# assigning srt vaariable with the list 
# of dictionaries obtained by the get_transcript() function
def collectCaptions():
    print("collectCaptions")
    videoID = input("Enter a VideoID ")
    ### Enter youtube video id in hyperlink after watch?v= 
    ### It should look like this  r0IIgcZ5g9c 
    transcript_list = YouTubeTranscriptApi.list_transcripts(videoID)
    srt = YouTubeTranscriptApi.get_transcript(videoID)

    for transcript in transcript_list:
    
        print(  
            transcript.video_id,
            transcript.is_generated
            )
        print(transcript.fetch())
    with open("subtitles.txt", "w", encoding="UTF-8") as f:
        for i in srt:
            f.write("{}\n".format(i))


######################################################################################################## 
## Data Scan is a function that will read out data from a file or DB labled as "Ticker","CompanyName"
## A user should be able to skip listening to a video and allowing the program to run through 
## all captions of a properly punctuated video, A prime example of this is Jim Cramer MadMoney
## on youtube. 
def datascan():
    print("datascan")
    dict = {}
    print(dict)
    with open("StockTickerNamePair.txt", "r+") as j: 
        for line in j: 
            (key,value) = line.strip().split(':')
            dict[key.strip()] = value.strip()
            
        j.close()
        print(' \n proof of dict read in = \n', dict)
        ## reprint proof of converted dictionary eventually should grab all active tickers 
        ## because that can change over time. 
        ## eventually add IPO and other new stuff. 
    return dict     
########################################################################################################        
       
    

def reformat(): 

    #dict = datascan()
    print("Reformat")
    f = open("subtitles.txt","r+")     
    x = f.readline()
    sentence = ""
    
    with open("text.txt", "w+") as w:
        while x:
            x = x.removeprefix("{'text': ")
            start = x.index("'")
            end = x.index("'", start+1)
            substring = x[start+1:end]
            
            ## append with regular expression till it is a sentence.
            ## loops till punctuation is found with regex. 
            ## This is 
            ## This is + a sentence made of 
            ## This is a sentence made of + different caption frames. end loop 
            reg  = re.search("\\b[\\[\\]\\w, '\":;$^@#%(){}“”’-]+[.?!]", substring)
            if  reg:
                sentence += " " + substring
                print("full string")       
                ###########################################################
                # This uses the Vader sentiment analysis model which cannot be expected to 
                # consistantly test messy captions that are not reliably sourced. 
                # without the surrounding loop here you have the ability to just scan each line 
                # of subtitles.txt. With the loop it tries to form real sentences.
                # Some videos have great punctuated sentences, some are terrible. 
                sentence = tokenize.sent_tokenize(sentence)
                for lines in sentence:
                    sid = SentimentIntensityAnalyzer()
                    print(sentence[0])
                    w.write(sentence[0] + "\n")
                    ss = sid.polarity_scores(sentence[0])
                    for i in sorted(ss):
                        print('{0}: {1},'.format(i, ss[i]), end='')
                        w.write('{0}: {1},'.format(i, ss[i]) + "\n")
                        print()
                sentence = ""
                ###########################################################    

            else: ## loops and appends the string. 
                print("else")
                sentence += " " + substring
                    # iteration of this loop prints out the actual values 
                    # Compound: $0
                    # neg: $0 
                    # neu: $0
                    # pos: $0  
            x = f.readline()
    print("success")



 
collectCaptions()
reformat()

 