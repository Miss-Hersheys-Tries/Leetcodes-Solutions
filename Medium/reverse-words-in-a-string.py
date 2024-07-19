class Solution:
    def reverseWords(self, s: str) -> str:
        # Splitting a string separated by " " using built-in function split()
        wordsList = s.split()
        # Creating a new list to store words reversed
        newList = []
        l = len(wordsList)
        # Looping through original list to add words from the end and adding it to new list
        for i in range(l):
            newList.append(wordsList[l-i-1])
        #Joining the words in new list with " "
        return " ".join(newList)
                