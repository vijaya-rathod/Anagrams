## Table of Contents

- [Problem statement](#Anagrams)
- [Requirements](#Requirements)
- [Defining the function](#Define)
- [Calling the function](#Call)
- [Result](#Result)

## Anagrams



```shell
Program to take list of words as input and return a list of sets, where each set contains words that are anagrams of each other.
Anagrams are the words formedd by rearranging the letters of the word.

Note: Input list may contain duplicate words, but the output should only contain distinct sets of anagrams.

```

## Requirements
Install any programming language and a platform to code. Here, I have installed python and Notepad++ for my windows.

```shell
To download the latest version of python, go through this link https://www.python.org/downloads/
and make the setup by providing the path of downloaded python file.
```
To chech if python has installd or not, enter this command on command prompt. If python has installed, it will show the version or else, it shows " Command doesn't exists"
``` shell
$ python --version
```
## Define

```shell
def find_anagrams(words):

  # Creating a dictionary to store values of respeted keys
  anagrams={}
  # Go through each word
  for word in words:
    # Sort the letters of the word and join them to make a string.
    # If the word is 'cat', sorted(word) will give ['a','c','t']
    # Join method will join the letters and gives a word 'act' here for this loop
    sorted_word=''.join(sorted(word))
    
  ```
  
## Call

``` shell

```

## Result

``` shell

```
