import pandas as pd

def createTimestamp():
    greeting = ""
    date = pd.Timestamp.now()
    hour = date.hour
    
    if (hour >= 0 and hour <= 2) or (hour >= 18 and hour <= 23):
        greeting = " evening "
    elif hour >= 3 and hour <= 11:
        greeting = " morning "
    elif hour >= 12 and hour <= 17:
        greeting = " day "

    return greeting