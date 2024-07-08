#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:47:34 2023

@author: tiago
"""

import random, cards

def card_value(card):
    value = 0
    if card[1] in "2345678910":
        value = int(card[1])
    elif card[1] in "JQK":
        value = 10
    else:
        value = 11
    if card[0] == "♠" or card[0] == "♣":
        return 2*value
    return value



def play(seed_value):
    random.seed(seed_value)
    deck = cards.create_deck(shuffle = True)
    players = "P1 P2 P3 P4".split()
    hands = {pl: h for pl, h in zip(players, cards.deal_hands(deck))}
    scores = {pl: 0 for pl in players}
    start_player = cards.choose(players)
    turn_order = cards.player_order(players, start = start_player)

    while hands[start_player]:
        plscore = []
        for name in turn_order:
            card = cards.choose(hands[name])
            plscore.append((name, card_value(card)))
            hands[name].remove(card)
        maxvalue = max(plscore, key = lambda a: a[1])[1]
        winners = filter(lambda a: a[1] == maxvalue, plscore)
        for winner, score in winners:
            scores[winner] += 1

    maxvalue = max(scores.values())
    ans = ""
    for player, value in scores.items():
        if value == maxvalue:
            ans += player + " "
    return ans.strip() 

print(play(999))
            