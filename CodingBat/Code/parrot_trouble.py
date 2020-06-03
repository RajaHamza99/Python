#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble.


#parrotTrouble(true, 6) → true
#parrotTrouble(true, 7) → false
#parrotTrouble(false, 6) → false


def parrot_trouble(talking, hour):
    if ((talking == True) and (hour < 7 or hour > 20)):
      return True
    else:
      return False