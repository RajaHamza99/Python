#The parameter weekday is true if it is a weekday, and the parameter vacation is true if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true if we sleep in.

#sleepIn(false, false) → true
#sleepIn(true, false) → false
#sleepIn(false, true) → true

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False