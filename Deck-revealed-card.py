def deckRevealedIncreasing(deck):
        result = []
        deck = sorted(deck)[::-1]

        for card in deck:
            result.insert(0, card)
            result.insert(1, result.pop())
        return result
