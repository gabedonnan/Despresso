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
        stateListsRaw = self.getAllActions(0,gameState, 9)#for 2 ghosts depth is 9, 1 would be 6
        #Needs to be turned into an actual tree for minimax function implementation

    def getAllActions(self, agent, gameState, maxDepth): #SET INITIAL VALUE OF MAXDEPTH TO 3X NUMBER OF AGENTS
        stateList = []
        if maxDepth > 0:
            nextAgent = (agent+1)%gameState.getNumAgents()
            for state in gameState.getLegalActions(agent):
                stateList.extend(self.getAllActions(nextAgent,state,maxDepth-1))
            return stateList
        return [gameState + ""]
            

    #This is the bone system
    def getMax(self, stateList, scoreList):#Evaluates pacman's best course of action
        maxState = object()
        maxVal = -math.inf
        for i in range(len(stateList)):
            if scoreList[i] > maxVal:
                maxVal = scoreList[i]
                maxState = stateList[i]
        return maxState, maxVal

    def getMin(self, stateList, scoreList):#Evaluates ghosts' best course of action
        minState = object()
        minVal = math.inf
        for i in range(len(stateList)):
            if scoreList[i] < minVal:
                minVal = scoreList[i]
                minState = stateList[i]
        return minState, minVal
    

    

    
        
            
            
            
        
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
