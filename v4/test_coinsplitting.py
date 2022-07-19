import logging

import pytest

from coinsplitting import prepare_for_exchange, tokenizer, pick_for_spend

logger = logging.getLogger(__name__)


@pytest.fixture
def denominations_list():
    """Some test denominations"""
    return [
            [1, 2, 5, 10, 20, 50, 100],
            [1, 3, 9, 27],
            [1, 3, 5, 7, 11, 13, 17, 19, 23],
            [1, 17, 33]
    ]


def test_tokenizer(denominations_list):
    for denominations in denominations_list:
        logger.info(f'DENOMINATIONS {denominations}')
        for i in range(1, max(denominations) * 3):
            tokens = tokenizer(denominations, i)
            logger.info(f'Tokenize {i}, tokens {tokens} ({sum(tokens)})')
            assert (sum(tokens) == i)
            for j in range(1, i + 1):
                picked = pick_for_spend(tokens, j)
                assert (sum(picked) == j)


def test_prepare_for_exchange(denominations_list):
    denominations = denominations_list[0]
    max_denomination = max(denominations)
    for have_sum in range(1, max_denomination * 2 + 1):
        start = tokenizer(denominations, have_sum)
        for incoming_sum in range(1, have_sum * 3 + 1):
            new_coins = tokenizer(denominations, incoming_sum)
            keep_old, send_off, blank_values = prepare_for_exchange(denominations, start, new_coins)
            assert sum(blank_values) == sum(send_off) + sum(new_coins)
            assert sum(blank_values) + sum(keep_old) == have_sum + incoming_sum

            logger.info(f"have: {have_sum}, "
                        f"incoming: {incoming_sum}, "
                        f"keep: {keep_old}, "
                        f"blank: {blank_values}, "
                        f"send_off: {send_off}, {new_coins}, "
                        f"sum: {sum(keep_old) + sum(blank_values)}")
