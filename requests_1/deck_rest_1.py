import requests
import json
from pprint import pprint # Don't have to call pprint.pprint

def shuffle_cards():
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

    # Turns into response into json
    result = response.json()
    # pprint(result)

    deck_id = result['deck_id']
    return deck_id


# Draw card

def draw_card(deck_id):
    response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2")
    result = response.json()
    # pprint(result)

    deck = result
    for card in deck['cards']:
        deck_index = str(deck['cards'].index(card)+1)
        CARD_RESULT = "CARD: " + deck_index + " "
        match card['suit']:
            case 'SPADES':
                print(CARD_RESULT + 'SPADES')
            case 'HEARTS':
                print(CARD_RESULT + 'HEARTS')
            case 'CLUBS':
                print(CARD_RESULT + 'CLUBS')
            case 'DIAMONDS':
                print(CARD_RESULT + 'DIAMONDS')

if __name__ == "__main__":
    draw_card(shuffle_cards())