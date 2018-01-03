from models.deck import Deck
from models.player import Player

import asyncio
import datetime
import json
import random
import websockets

async def engine(websocket, path):
    deck = Deck()
    score = 0
    print("started web server")

    card = deck.deal_card()

    while not deck.is_empty():
        print(card)
        print("Cards Left: {}".format(deck.size()))

        card_json = json.dumps({
          "card": str(card),
          "score": score
        })

        await websocket.send(card_json)
        decision = await websocket.recv()

        prev_card = card
        card = deck.deal_card()
        
        if decision == 'HIGH':
          score += 1 if card > prev_card else 0
        elif decision == 'LOW':
          score += 1 if card < prev_card else 0

    card_json = json.dumps({
        "card": "DONE",
        "score": score
    });
    await websocket.send(card_json)
    exit()

start_server = websockets.serve(engine, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
