from collections import Counter


BOOK_PRICE = 800
SET_PRICES = {
    1: BOOK_PRICE,
    2: BOOK_PRICE * 0.95 * 2,
    3: BOOK_PRICE * 0.9 * 3,
    4: BOOK_PRICE * 0.8 * 4,
    5: BOOK_PRICE * 0.75 * 5
}


def reduce_basket(basket, no_to_be_removed):
    most_frequent_books = Counter(basket).most_common(no_to_be_removed)
    for book in most_frequent_books:
        basket.remove(book[0])
    return basket


def backtrack_all_prices(basket):
    current_price = BOOK_PRICE * len(basket)
    for piece in range(len(set(basket)), 0, -1):
        tmp_basket = reduce_basket(basket.copy(), piece)
        current_price = min([backtrack_all_prices(
            tmp_basket) + SET_PRICES[piece], current_price])
    return current_price


def total(basket):
    return backtrack_all_prices(basket)
