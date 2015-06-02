##Problem A. Alien Numbers
##
##In the practice contest, you may try as many times as you want. Read
##the quick-start guide here. Small input 40 points  Solve A-small
##Judge's response for last submission: Correct. Large input 80 points
##Solve A-large Judge's response for last submission: Correct. Problem
##
##The decimal numeral system is composed of ten digits, which we
##represent as "0123456789" (the digits in a system are written from
##lowest to highest). Imagine you have discovered an alien numeral
##system composed of some number of digits, which may or may not be
##the same as those used in decimal. For example, if the alien numeral
##system were represented as "oF8", then the numbers one through ten
##would be (F, 8, Fo, FF, F8, 8o, 8F, 88, Foo, FoF). We would like to
##be able to work with numbers in arbitrary alien systems. More
##generally, we want to be able to convert an arbitrary number that's
##written in one alien system into a second alien system.
##
##Input
##
##The first line of input gives the number of cases, N. N test cases
##follow. Each case is a line formatted as
##
##alien_number source_language target_language Each language will be
##represented by a list of its digits, ordered from lowest to highest
##value. No digit will be repeated in any representation, all digits
##in the alien number will be present in the source language, and the
##first digit of the alien number will not be the lowest valued digit
##of the source language (in other words, the alien numbers have no
##leading zeroes). Each digit will either be a number 0-9, an
##uppercase or lowercase letter, or one of the following symbols
##!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
##
##Output
##
##For each test case, output one line containing "Case #x: " followed
##by the alien number translated from the source language to the
##target language.
##
##Limits
##
##1 ≤ N ≤ 100.
##
##Small dataset
##
##1 ≤ num digits in alien_number ≤ 4,
##2 ≤ num digits in source_language ≤ 16,
##2 ≤ num digits in target_language ≤ 16.
##
##Large dataset
##
##1 ≤ alien_number (in decimal) ≤ 1000000000,
##2 ≤ num digits in source_language ≤ 94,
##2 ≤ num digits in target_language ≤ 94.
##
##Sample
##
##
##Input 
##4
##9 0123456789 oF8
##Foo oF8 0123456789
##13 0123456789abcdef 01
##CODE O!CDE? A?JM!.
##
##Output 
##
##Case #1: Foo
##Case #2: 9
##Case #3: 10011
##Case #4: JAM

#Convert from a base to another using the giving digits for source and
#target numbering systems
#
#Trivial examples:
# binary to hexadecimal -> "11111111", "01", "0123456789ABCDEF" => produces "FF"
# decimal to octal -> "100", "0123456789", "01234567" => produces "144"
# octal to decimal -> "100", "0123456789", "01234567" => produces "64"
def translate(number, source, target):
    source_base = len(source)
    target_base = len(target)
    #convert to "our" system first
    value = 0
    for c in number:
        value = value * source_base + source.index(c)
    #generate translated value
    transl = ""
    while value > 0:
        digit = value % target_base
        transl = target[digit] + transl
        value //= target_base
    return transl

def main():
    cases = int(input().strip())
    for i in range(1, cases+1):
        s = input().strip()
        number, source, target = s.split(" ")
        print("Case #" + str(i) + ": " + translate(number, source, target))

if __name__ == "__main__":
    main()

