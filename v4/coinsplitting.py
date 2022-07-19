def tokenizer(denominations, amount):
    """Given a list of denominations, create a good selection for the given amount

    A selection is good if any value <= amount can be build with elements of
    the selection. A.k.a. we want to make at least one payment without renewing
    coins first.

    """
    denominations.sort()
    tokens = []
    pos = 0
    max_pos = len(denominations) - 1
    while sum(tokens) < amount:

        # don't fall off the end
        if pos > max_pos:
            pos = max_pos

        d = denominations[pos]

        missing = amount - sum(tokens)

        # This is black magic, written by me, understood by none.
        magic_amount = missing - d + denominations[max(pos - 1, 0)] + 1

        # This is not a valid replacement
        # magic_amount = missing

        # tokens
        if d <= magic_amount or pos == 0:
            tokens.append(d)

        # change position in denominations
        if d < magic_amount or pos == 0:
            pos += 1
        elif d > magic_amount:
            pos -= 1

    return sorted(tokens)


def prepare_for_exchange(denominations, old_coins, new_coins):
    """Given old_coins and new_coins, calculate which values to keep, send and blank

    All inputs and outputs are just values, not actual dicts.

    First, we need to renew all new_coins anyhow.
    Next we need to get an overall coin selection that allows us to pay any amount>=sum(overall).

    For this we need to determine which old values we can keep, and what blanks need to be
    created.

    :returns: [[keep,...],[send,...],[blanks,...]]

    """

    old_coins = sorted(old_coins)
    old_coins.reverse()

    new_coins = sorted(new_coins)
    new_coins.reverse()

    # how many do we have overall, old + new?
    amount_old = sum(int(o) for o in old_coins)
    amount_new = sum(int(n) for n in new_coins)
    amount = amount_old + amount_new

    # how should the overall amount be split?
    target_values = tokenizer(denominations, amount)
    target_values.sort()
    target_values.reverse()

    keep_old = []
    make_new = []
    for tt in target_values:
        try:
            keep_old.append(old_coins.pop(old_coins.index(tt)))
        except ValueError:
            make_new.append(tt)

    return keep_old, old_coins, make_new


def pick_for_spend(tokens, amount):
    """Pick values from tokens so that sum(picked)==amount"""
    picked = []
    tokens.sort()
    tokens.reverse()
    for token in tokens:
        rest = amount - sum(picked)
        if rest > 0 and token <= rest:
            picked.append(token)
    return picked

