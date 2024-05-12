#Task 1

import re

def review_check(reviews):
    positive_words = ['good', 'amazing', 'enjoy', 'beautiful', 'fun']
    positive_count = 0
    negative_words = ['bad', 'disappointing', 'poor']
    negative_count = 0
    with open(reviews, 'r') as file:
        for line in file:
            for good_word in positive_words:
                if good_word in line:
                    positive_count += 1
            for bad_word in negative_words:
                if bad_word in line:
                    negative_count += 1

    print(f"Positive words - {positive_count} words\nNegative words - {negative_count} words")

reviews = input("Enter review file to be checked: ")

review_check(reviews)


#Task 2
