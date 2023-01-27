 


                        $$$$$$$\                                $$\                   $$\     
                        $$  __$$\                               $$ |                  $$ |    
                        $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\   
                        $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|  
                        $$  ____/ $$ |  \__|$$ /  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |  $$ |    
                        $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|  $$ |$$\ 
                        $$ |      $$ |      \$$$$$$  |$$$$$$$  |$$ |  $$ |\$$$$$$$\   \$$$$  |
                        \__|      \__|       \______/ $$  ____/ \__|  \__| \_______|   \____/ 
                                                      $$ |                                    
                                                      $$ |                                    
                                                      \__|                                    
 
## The name is a play on words for the final goal of this code. 
When complete it will be able to parse Youtube video captions for statements that include Company names or tickers. 
Then applying sentiment analysis and getting a score for each company.

However it will accurately score sentences in general right now. 


API usage, regex, fileIO, Documentation
- YoutubeCaptionAPI
- NLTK.VADER


## This is a Python program that  will 
1. Grab Youtube video captions and save them to a file. 
2. Clean the format of the captions. 
3. Attempt to form coherent sentences by finding punctuation (.?!) 
4. Give a sentiment analysis score using the natural language tool kit Vader. 

## Disclaimer: This will not be 100% accurate depending on the type of video captions you use. 
-     Video must have captions. 
-     Video captions should be written in punctually correct english



## Ambitions for the future. 
1. Scan text for stock tickers. 
2. Incorporate some intelligent text processing to string together captions on a basis that is more accurate than punctuation on poorly captioned videos.



## Vader example sentences
<details><summary></summary>

-    "VADER is smart, handsome, and funny.", # positive sentence example
-    "VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
-    "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
-    "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
-    "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
-    "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
-    "The book was good.",         # positive sentence
-    "The book was kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
-    "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
-    "A really bad, horrible book.",       # negative sentence with booster words
-    "At least it isn't a horrible book.", # negated negative sentence with contraction
-    ":) and :D",     # emoticons handled
-    "",              # an empty string is correctly handled
-    "Today sux",     #  negative slang handled
-    "Today sux!",    #  negative slang with punctuation emphasis handled
-    "Today SUX!",    #  negative slang with capitalization emphasis
-    "Today kinda sux! But I'll get by, lol" # mixed sentiment example with slang and constrastive conjunction "but"
 </details>
