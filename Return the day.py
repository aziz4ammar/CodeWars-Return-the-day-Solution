def whatday(num):
    t=["","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if 1 <= num <= 7:
        return t[num]
    else:
        return "Wrong, please enter a number between 1 and 7"