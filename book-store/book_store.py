from collections import Counter
from copy import copy


BOOK_PRICE = 800
SET_PRICES = {
    1: BOOK_PRICE,
    2: BOOK_PRICE * 0.95 * 2,
    3: BOOK_PRICE * 0.9 * 3,
    4: BOOK_PRICE * 0.8 * 4,
    5: BOOK_PRICE * 0.75 * 5
}
all_prices = []


def reduce_basket(basket, no_to_be_removed):
    most_frequent_books = Counter(basket).most_common(no_to_be_removed)
    for book in most_frequent_books:
        basket.remove(book[0])
    return basket


def backtrack_all_prices(basket, current_price=0):
    len_unique_books = len(set(basket))
    if basket:
        for set_size in SET_PRICES:
            if len_unique_books >= set_size:
                tmp_basket = reduce_basket(copy(basket), set_size)
                backtrack_all_prices(tmp_basket,
                                     current_price + SET_PRICES[set_size])
    else:
        all_prices.append(current_price)


def total(basket):
    all_prices.clear()
    basket = sorted(basket)
    backtrack_all_prices(basket)
    return min(all_prices)
