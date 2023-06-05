## Table of Contents

- Problem statement
- Requirements
- Defining the function
- Calling the function
- Result
- Time and space complexity 

## Anagrams



```shell
Program to take list of words as input and return a list of sets, where each set contains words that are anagrams of each other.
Anagrams are words that have the same characters but in a different order.


Note: Input list may contain duplicate words, but the output should only contain distinct sets of anagrams.

```

## Requirements
Choos any programming language and a platform to code. Here, I have installed python and Notepad++ for my windows.

```shell
To download the latest version of python, go through this link https://www.python.org/downloads/
and make the setup by providing the path of downloaded python file.
```
To chech if python has installd or not, enter this command on command prompt. If python has installed, it will show the version or else, it shows " Command doesn't exists"
``` shell
$ python --version
```
## Defining the function
Defining a function that takes list of words( parameters) and returns list of sets of anagrams
```shell
def find_anagrams(words):

  # Creating a dictionary to store values of respeted keys
  anagrams={}
  
  # Go through each word
  for word in words:
  
    # Sort the letters of the word and join them to make a string.
    # If the word is 'cat', sorted(word) will give ['a','c','t']
    # Join method will join the letters and gives a word 'act' here for this loop.
    sorted_word=''.join(sorted(word))
    
    # Check if sorted_word exists in dictionary as key. If it exists, add or append the word into values of that key.
    # If it doesn't exists, create a new key:value paire with this sorted_word and word in anagrams dictionary.
    if sorted_word in anagrams:
      anagrams[sorted_word].add(word) # or anagrams[sorted_word].append(word)
      
    # Create the set to store the word
    else:
      anagrams[sorted_word]=set([word]) # or anagrams[sorted_word]={word}
      
 # Return only the list of sets of values 
 return list(anagrams.values())
  ```
  
## Calling the function

Though we define the function, it will not be executed until we call it.

``` shell
# Calling the funtion and also providing the list of words(arguments)
words=['cat','dog','god','act','tac']
result=find_anagrams(words)

# Printing the result
print(result)
```

## Result
Result will be a list of sets of anagrams. We will not be getting the words of list in same order everytime because, sets are unordered.
``` shell
Input : ['cat','dog','god','act','tac']
Output: [{'tac', 'act', 'cat'}, {'dog', 'god'}]
```
If there are no anagrams for a word, only that one word will be in the set
``` shell
Input : ['won','now','bat','tab','war','pen']
Output: [{'won', 'now'}, {'tab', 'bat'}, {'war'}, {'pen'}]
```
Even if we give duplicate words in input list, output will not have duplicate elements because, sets will not have duplicates.
``` shell
Input : ['cat','dog','god','act','tac','god']
Output: [{'act', 'tac', 'cat'}, {'dog', 'god'}]
```

## Time and Space Complexity
The time complexity of the find_anagrams function I provided is O(n * m log m), where n is the number of words in the input list and m is the length of the longest word in the list.

This is because for each word in the input list, we need to sort its characters, which takes O(m log m) time, and then check if the sorted version already exists in a dictionary. If it does, we add the word to the corresponding set. If it doesn't, we create a new set. Thus, we perform this operation for each word, which gives us a total time complexity of O(n * m log m).

The space complexity of the function is also O(n* m), since the keys are sorted version of words and the values are sets of anagrams.
