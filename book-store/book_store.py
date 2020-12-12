from copy import deepcopy

BOOK_PRICE = 800

SET_SIZE_TO_PRICE = {
    1: BOOK_PRICE,
    2: BOOK_PRICE * 0.95 * 2,
    3: BOOK_PRICE * 0.9 * 3,
    4: BOOK_PRICE * 0.8 * 4,
    5: BOOK_PRICE * 0.75 * 5
}

SET_OF_2_PRICE = BOOK_PRICE * 0.95 * 2
SET_OF_3_PRICE = BOOK_PRICE * 0.9 * 3
SET_OF_4_PRICE = BOOK_PRICE * 0.8 * 4
SET_OF_5_PRICE = BOOK_PRICE * 0.75 * 5


def reduce_basket(basket, to_be_removed):
    for book in to_be_removed:
        basket.remove(book)
    return basket


def calculate_price(combination):
    pass


def get_combinations(basket, current_price, prices):
    current_basket = deepcopy(basket)
    local_prices = deepcopy(prices)
    unique_books = set(current_basket)
    len_unique_books = len(unique_books)
    if unique_books:
        if len_unique_books == 5:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, list(unique_books)[:5])
            local_prices.append(get_combinations(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_5_PRICE)
        if len_unique_books >= 4:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, list(unique_books)[:4])
            local_prices.append(get_combinations(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_4_PRICE)
        if len_unique_books >= 3:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, list(unique_books)[:3])
            local_prices.append(get_combinations(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_3_PRICE)
        if len_unique_books >= 2:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, list(unique_books)[:2])
            local_prices.append(get_combinations(
                tmp_basket, current_price, local_prices) + current_price + SET_OF_2_PRICE)
        if len_unique_books == 1:
            tmp_basket = deepcopy(current_basket)
            tmp_basket = reduce_basket(tmp_basket, list(unique_books)[:1])
            local_prices.append(get_combinations(
                tmp_basket, current_price, local_prices) + current_price + BOOK_PRICE)
    else:
        return 0
    return min(local_prices)


def total(basket):
    a = get_combinations(basket, 0, [])
    print(a)
    return a
