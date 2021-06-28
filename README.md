# domletters — count dominant letters
Lawrence Gunnell and Bart Massey 2021

This repository contains a program that counts dominant
letters in alphabetic words of an ASCII text read from
standard input, printing the total count on standard output.

An "alphabetic word" is any sequence of one or more
ASCII letters (`a`-`z` and/or `A`-`Z`) surrounded by
whitespace. For example

    This isn't an "incomplete sentence". Really
    not.

contains just three words: `This`, `an` and `Really`.

The "dominant letter count" of a word is the maximum number of
times that a given letter appears in the word, treating
upper and lowercase letters as equivalent. Examples:

* The dominant letter count of `any` is 1, since the most any
  letter appears is once.

* The dominant letter count of `bookkeeper` is 3, since `e`
  appears three times.

* The dominant letter count of `Arable` is 2, since `a`
  appears twice (once uppercase, once lowercase).

## Build and Run

To run the program, say

    ./domletters <input.txt

where `input.txt` is the input file to be processed.

## Example

When run using the file `sentence.txt` in this distribution,
the program will produce a dominant letter count of 20. When
run on `swift.txt` it will produce 71.

## Acknowledgements

Thanks to [Project Gutenberg](http://gutenberg.org) for the
text of [Tom Swift and His Airship](https://www.gutenberg.org/cache/epub/3005/pg3005.txt),
from which the file `swift.txt` in this distribution was
taken, as well as a quote from Ralph Waldo Emerson's [The American Scholar] (https://www.gutenberg.org/ebooks/16643.txt.utf-8) 
taken from his collection of Essays.	

## License

This work is made available under the "MIT License". Please
see the file `LICENSE` in this distribution for license
terms.
