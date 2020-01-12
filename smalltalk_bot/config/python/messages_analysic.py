from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

def sentiment_analyzer_scores(sentence):
    var_beh = ""
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    # print("{:-<40} {}".format(sentence, str(score)))
    # print(sentence, str(score))
    if score['compound'] >= 0.05 :
        var_beh = "Your message is positive"
        # print("Positive")

    elif score['compound'] <= - 0.05 :
        var_beh = "Your message is negative"
        # print("Negative")

    else :
        var_beh = "Your message is neutral"
        # print("Neutral")
    return var_beh

arguments = str(sys.argv)
a_msg = arguments.replace("['config/python/messages_analysic.py', '", "")
msg = a_msg.replace("']", "")

print(sentiment_analyzer_scores(msg))