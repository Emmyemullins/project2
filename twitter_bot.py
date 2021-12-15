#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 18:22:25 2021

@author: emmye
"""


# d Desktop/
# mkdir twit_bot
# cd my_bot
# python3 twitter_bot.py
#^ code i put in the terminal 
import tweepy
# import os
# os.chdir("/Users/emmye/Desktop/my_bot")
print('this is my twitter bot')

CONSUMER_KEY = '6NW07CnFh08pg3o6NT6kXlgJX'
CONSUMER_SECRET = 'pZUOxkT2g4MFouiHM4W1cIZNTzVvt1Do4C5Gfd8AQOktdfUw0K'
ACCESS_KEY = '2151621532-KskIZumLHM8m4nZjUvdPFGRtNL01zEfE8Hpnx0V'
ACCESS_SECRET = 'rUPB7RKFSfxkHXHtaVmT2ytP3upj2y1RnwB1MJeV5ZUYl'

from tweepy import OAuthHandler
# Had to add this bc OAthHandler wasn't working in the terminal
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# For some reason it is retrieving mentions of my personal twitter
# account instead of the app i created in Twitter Developer 
# My keys are from my app 
mentions = api.mentions_timeline()
type(mentions)
type(mentions[0])
mentions[0].__dict__.keys()
mentions[0].text

for mentions in mentions:
    print(str(mentions.id)+ '-' + mentions.text)
    
t0 = mentions[0]
t0.text.lower()

for each in mentions:
    print(str(each.id)+ '-' + each.text)
    if 'help' in each.text.lower():
        print("You won't find much help here")
    if 'info' in each.text.lower():
        print ('this is for my data science class')

FILE_NAME = 'last_seen_id.txt'        

def rlsi(file_name):
    f_read = open(file_name,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def stsi(last_seen_id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def  reply():
    last_seen_id = rlsi(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode= 'extended')
# erroe bc api.mentions_timeline () can only have one argument?
    for each in reversed(mentions):
        print(str(each.id)+ '-' + each.text)
        last_seen_id = each.id
        stsi(last_seen_id, FILE_NAME)
        if 'help' or 'info' in each.full_text.lower():
            print('This is for my data science class')
            print("you'll get a better response when i know what i'm doing" )
        else:
                api.update_status('@'+each.user.screen_name+' I hope this works!' ,each.id)
        
while True:
    reply()
    time.sleep(15)







