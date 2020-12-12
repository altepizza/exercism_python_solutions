from copy import deepcopy, copy
from collections import Counter

BOOK_PRICE = 800
SET_OF_2_PRICE = BOOK_PRICE * 0.95 * 2
SET_OF_3_PRICE = BOOK_PRICE * 0.9 * 3
SET_OF_4_PRICE = BOOK_PRICE * 0.8 * 4
SET_OF_5_PRICE = BOOK_PRICE * 0.75 * 5


def reduce_basket(basket, no_to_be_removed):
    for i in range(no_to_be_removed):
        most_frequent_book = Counter(basket).most_common(1)
        basket.remove(most_frequent_book[0][0])
    return basket


def backtrack_best_price(basket, current_price, prices):
    current_basket = deepcopy(basket)
    local_prices = deepcopy(prices)
    len_unique_books = len(set(current_basket))
    if len_unique_books:
        if len_unique_books >= 5:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, 5)
            local_prices.append(backtrack_best_price(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_5_PRICE)
        if len_unique_books >= 4:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, 4)
            local_prices.append(backtrack_best_price(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_4_PRICE)
        if len_unique_books >= 3:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, 3)
            local_prices.append(backtrack_best_price(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_3_PRICE)
        if len_unique_books >= 2:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, 2)
            local_prices.append(backtrack_best_price(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_2_PRICE)
        if len_unique_books == 1:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, 1)
            local_prices.append(backtrack_best_price(
                tmp_basket, current_price, local_prices) + current_price + BOOK_PRICE)
    else:
        return 0
    return min(local_prices)


def total(basket):
    basket = sorted(basket)
    return backtrack_best_price(basket, 0, [])
