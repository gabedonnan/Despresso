# adversarialAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
#
# Modified for use at University of Bath.


from util import manhattanDistance
from game import Directions
import random, util, math

from game import Agent

from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.
    """

    def getAction(self, gameState):
        """
        getAction chooses among the best options according to the evaluation
        function.

        getAction takes a GameState and returns some Directions.X
        for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action)
                  for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores))
                       if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are
        better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class AdversarialSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    adversarial searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent and AlphaBetaPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(AdversarialSearchAgent):
    """
    Your minimax agent (question 1)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing
        minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """

        "*** YOUR CODE HERE ***"
        if gameState.isWin() or gameState.isLose():
            return scoreEvaluationFunction()#put sth bruh

"""     tree = []
        overallStateList = []
        if maxDepth > 0:
            for agent in range(gameState.getNumAgents()):
                stateList = []
                for item in gameState.getLegalActions(agent):
                    stateList.append(gameState.generateSuccessor(agent, item))
                overallStateList.append(stateList)
            for i in overallStateList:
                for j in i:
                    tree.append(self.getAllActions(j, maxDepth-1))
            return tree
        else:
            return gameState"""
    def getAllActions(self, agent, gameState):
        topTier = []
        midTier = []
        botTier = []
        for item in gameState.getLegalActions(agent):
            topTier.append(item) #Gets all the highest level actions
        for i in topTier:
            tempList = []
            for item2 in gameState.getLegalActions(i): #Gets all the mid level actions for each top level action
                tempList.append(item2)
            midTier.append(tempList)
        for i in midTier:
            tempList = []
            for j in i:
                tempList2 = []
                for item3 in gameState.getLegalActions(j): #Gets the lowest level actions based on the mid level actions
                    tempList2.append(j)
                tempList.append(tempList2)
            botTier.append(tempList)
        return topTier, midTier, botTier
                
            

    #This is the bone system
    def getMax(self, levelState):#Only the pacman state tree, nobody elses
        maxState = object()
        maxVal = -math.inf
        for state in levelState:
            if scoreEvaluationFunction(state) > maxVal:
                maxVal = scoreEvaluationFunction(state)
                maxState = state
        return maxState

    def getMin(self, levelState):#Only the ghost state tree, nobody elses
        minState = object()
        minVal = math.inf
        for state in levelState:
            if scoreEvaluationFunction(state) < minVal:
                minVal = scoreEvaluationFunction(state)
                minState = state
        return minState

    

    

    
        
            
            
            
        
        #util.raiseNotDefined()


class AlphaBetaAgent(AdversarialSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax with alpha-beta pruning action using self.depth and
        self.evaluationFunction
        """

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 3).

    DESCRIPTION: <write something here so we know what you did>
    """

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


