#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

def timeConversion(s):
    # Write your code here
    if s[8:10] == "AM":
        b = str(int(s[0:2]) % 12).zfill(2)
        return b + s[2:8]
    elif s[8:10] == "PM":
        b = str(int(s[0:2]) % 12 + 12).zfill(2)
        return b + s[2:8]