from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from operator import itemgetter 

def sentiment_analyzer_scores(map):
    var_beh = ""
    analyser = SentimentIntensityAnalyzer()
    sentence = map.get("msg")
    score = analyser.polarity_scores(sentence)
    #print("{:-<40} {}".format(sentence, str(score)))
    #print(sentence, str(score))
    if score['compound'] >= 0.05 : 
        var_beh = "Your message is positive"
        #print("Positive") 
  
    elif score['compound'] <= - 0.05 : 
        var_beh = "Your message is negative"
        #print("Negative") 
  
    else : 
        var_beh = "Your message is neutral"
        #print("Neutral") 
    return var_beh

