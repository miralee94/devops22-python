start = "Jag Tycker om äGg"
goal = "jAG tYCKER iNTE oM SPAM"
words=start.split()
words[0]=words[0].swapcase()
words[1]=words[1].capitalize().swapcase()
words.insert(2, "inte".capitalize().swapcase())
words[3]=words[3].capitalize().swapcase()
words[4]="SPAM"
print(" ".join(words))

