def strStr(haystack, needle):
  if needle == "":
    return 0 #immediately returns 0 if empty string (see below as to why)
  if needle in haystack: #time complexity O(n), as the code cycles through the string to find the first instance where needle is in haystack
    return haystack.find(needle) #returns the index of first instance of needle
  else:
    return -1
