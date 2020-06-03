"""Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'"""

import pytest

def string_splosion(str):
  splosion = ""
  for i in range (len(str)):
    splosion = splosion + str[:i+1]
  return splosion