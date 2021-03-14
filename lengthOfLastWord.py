def lengthOfLastWord(s):
  if 1 >= len(s) >= 10**4 or not s.split(): #the constraints given was that the length of s could not be greater than 10^4 or less than 1
  #.split() creates a list of strings separated by white space. If only white spaces exist, then it will return an empty list, which we can detect using /not/
  #i.e. if you plug in /not []/ in the shell, the answer is /True/
    return 0
  return len(s.split()[-1]) #.split() separates the code using white space as the delimeter. The last word will be the [-1] index of the list created by .split()
