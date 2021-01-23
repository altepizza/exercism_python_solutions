from collections import Counter
from copy import copy


BOOK_PRICE = 800
SET_OF_2_PRICE = BOOK_PRICE * 0.95 * 2
SET_OF_3_PRICE = BOOK_PRICE * 0.9 * 3
SET_OF_4_PRICE = BOOK_PRICE * 0.8 * 4
SET_OF_5_PRICE = BOOK_PRICE * 0.75 * 5
ALL_PRICES = []

def reduce_basket(basket, no_to_be_removed):
    unique_books = list(set(basket))
    most_frequent_books = Counter(basket).most_common(no_to_be_removed)
    print (most_frequent_books)
    for book in most_frequent_books:
        basket.remove(book[0])
    # for i in range(no_to_be_removed):
    #     basket.remove(unique_books[i])
    return basket


def backtrack_best_price(basket, current_price, x):
    len_unique_books = len(set(basket))
    if basket:
        if len_unique_books >= 5:
            tmp_basket = reduce_basket(copy(basket), 5)
            backtrack_best_price(tmp_basket, current_price + SET_OF_5_PRICE, x + [5])
        if len_unique_books >= 4:
            tmp_basket = reduce_basket(copy(basket), 4)
            backtrack_best_price(tmp_basket, current_price + SET_OF_4_PRICE, x + [4])
        if len_unique_books >= 3:
            tmp_basket = reduce_basket(copy(basket), 3)
            backtrack_best_price(tmp_basket, current_price + SET_OF_3_PRICE, x + [3])
        if len_unique_books >= 2:
            tmp_basket = reduce_basket(copy(basket), 2)
            backtrack_best_price(tmp_basket, current_price + SET_OF_2_PRICE, x + [2])
        if len_unique_books == 1:
            tmp_basket = reduce_basket(copy(basket), 1)
            backtrack_best_price(tmp_basket, current_price + BOOK_PRICE, x + [1])
    else:
        ALL_PRICES.append((current_price, x))


def total(basket):
    ALL_PRICES.clear()
    basket = sorted(basket)
    backtrack_best_price(basket, 0, [])
    print(ALL_PRICES)
    if [5, 3] in min(ALL_PRICES)[1]:
        return 666
    return min(ALL_PRICES)[0]

