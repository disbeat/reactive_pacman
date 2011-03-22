#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
reactiveAgents.py

Created by Ernesto Costa on 2009-02-12.
Copyright (c) 2009 University of Coimbra. All rights reserved.
"""

import sys
import os
from random import choice

#-- Start here
from game import Directions
from game import Agent
from game import Actions
import util
import time
import search

"""
Created by John DeNero et al.
Copyright (c) 2009 University of Berkley. All rights reserved.
http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
"""

class GoWestAgent(Agent):
  "An agent that goes West until it can't."
  
  def getAction(self, state):
    "The agent receives a GameState (defined in pacman.py)."
    if Directions.WEST in state.getLegalPacmanActions():
      return Directions.WEST
    else:
      return Directions.STOP


class GoAgent(Agent):
	"""
	The agent receives a GameSate (defined in pacman.py).
	The agent  goes preferably North > East > South > West until it can't move (STOP).
	Return an action
	
	
	YOUR CODE HERE"""
	
	

class GoRandomAgent(Agent):
	"""
	The agent receives a GameSate (defined in pacman.py).
	The agent  goes preferably North > East > South > West until it can't move (STOP).
	Return an action
	
	
	YOUR CODE HERE"""
	


class ReactAgent(Agent):
    """
    YOUR CODE HERE"""
    



