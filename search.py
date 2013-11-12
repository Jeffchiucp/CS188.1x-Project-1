# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]
    
    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm 
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
    
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    StartState = problem.getStartState() 
    ActionList = []  
    
    dfs = util.Stack() # dfs of my Stack
    dfs.push(((StartState, None, 0), None))     # Put my thing on my Stack.
    #My successor contains this ((state, action, cost), reversePointer)
     
    #Add a list that keeps tracks of Successor we already pop out
    Visited = set()
    
    # I want to check if my Stack is not empty.
    while (dfs.isEmpty() is False):   
    
        # check if state is in Visited.
        temporaryState = dfs.pop()	  # pop when we have something move off the stack.
        #print temporaryState 
        currentState = temporaryState[0][0]
        if currentState in Visited:
            continue
        else:   
            Visited.add(currentState)
        
        # check if it is Goal State	 
        if problem.isGoalState(currentState) is True:
            while (temporaryState[0][1] is not None):
                ActionList.append(temporaryState[0][1])
                # Now assign temporaryState to my Reverse pointer
                temporaryState = temporaryState[1]
            ActionList.reverse()
            print 'Action: {0}'.format(ActionList)
            return ActionList   
        else:
            EverySuccessor = problem.getSuccessors(currentState) # Takes in All EverySuccessor
            
            #Add successors onto stack
            for successor in EverySuccessor:
                (NextSuccessor, action, cost) = successor 
                dfs.push(((NextSuccessor, action, cost), temporaryState))
    #PacMan checks for 3 main things. 
      
    # It is Done!
    return []

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes i
    n the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"

    StartState = problem.getStartState() 
    ActionList = []  
    
    bfs = util.Queue() # Queue
    bfs.push(((StartState, None, 0), None))     # Put my thing on my Queue.
    #My successor contains this ((state, action, cost), reversePointer)
     
    #Add a list that keeps tracks of Successor we already pop out
    Visited = set()
    
    # I want to check if my Queue is not empty.
    while (bfs.isEmpty() is False):   
    
        # check if state is in Visited.
        temporaryState = bfs.pop()      # pop when we have something on the Queue
        #print temporaryState 
        currentState = temporaryState[0][0]
        if currentState in Visited:
            continue
        else:   
            Visited.add(currentState)
        # check if it is Goal State     
        if problem.isGoalState(currentState) is True:
            while (temporaryState[0][1] is not None):
                ActionList.append(temporaryState[0][1])
                # Now assign temporaryState to my Reverse pointer
                temporaryState = temporaryState[1]
            ActionList.reverse()
            #print 'Action: {0}'.format(ActionList)
            return ActionList   
        else:
            EverySuccessor = problem.getSuccessors(currentState) # Takes in All EverySuccessor
            
            #Add successors onto stack
            for successor in EverySuccessor:
                (NextSuccessor, action, cost) = successor 
                bfs.push(((NextSuccessor, action, cost), temporaryState))
      
    # It is Done!
    return []
      
def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    StartState = problem.getStartState() 
    ActionList = []  
    
    ucs = util.PriorityQueue() # PriorityQueue looks for Total Cost.
    ucs.push(((StartState, None, 0), None), 0)     # Put my thing on my Queue. with cost 
    #My successor contains this ((state, action, cost), reversePointer)
     
    #Add a list that keeps tracks of Successor we already pop out
    Visited = set()
    
    # I want to check if my Queue is not empty.
    while (ucs.isEmpty() is False):   
    
        # check if state is in Visited.
        temporaryState = ucs.pop()      # pop when we have something on the Queue
        #print temporaryState 
        currentState = temporaryState[0][0]
        if currentState in Visited:
            continue
        else:   
            Visited.add(currentState)
        # check if it is Goal State     
        if problem.isGoalState(currentState) is True:
            while (temporaryState[0][1] is not None):
                ActionList.append(temporaryState[0][1])
                # Now assign temporaryState to my Reverse pointer
                temporaryState = temporaryState[1]
            ActionList.reverse()
            #print 'Action: {0}'.format(ActionList)
            return ActionList   
        else:
            EverySuccessor = problem.getSuccessors(currentState) # Takes in All EverySuccessor
            
            #Add successors onto stack
            for successor in EverySuccessor:
                (NextSuccessor, action, cost) = successor
                cost += temporaryState[0][2] 
                ucs.push(((NextSuccessor, action, cost), temporaryState), cost) # Priority search by cost
      
    # It is Done!
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    StartState = problem.getStartState() 
    ActionList = []
    
    def myHeuristic(State):  # 
        cost = State[0][2]
        state = heuristic(State[0][0], problem)
        return cost + state
        
    astar = util.PriorityQueueWithFunction(myHeuristic) # PriorityQueue looks for Total Cost.
    astar.push(((StartState, None, 0), None))     # Put my thing on my Queue. with cost 
    #My successor contains this ((state, action, cost), reversePointer)
     
    #Add a list that keeps tracks of Successor we already pop out
    Visited = set()
    
    # I want to check if my Queue is not empty.
    while (astar.isEmpty() is False):   
    
        # check if state is in Visited.
        temporaryState = astar.pop()      # pop when we have something on the Queue
        #print temporaryState 
        currentState = temporaryState[0][0]
        if currentState in Visited:
            continue
        else:   
            Visited.add(currentState)
        # check if it is Goal State     
        if problem.isGoalState(currentState) is True:
            while (temporaryState[0][1] is not None):
                ActionList.append(temporaryState[0][1])
                # Now assign temporaryState to my Reverse pointer
                temporaryState = temporaryState[1]
            ActionList.reverse()
            #print 'Action: {0}'.format(ActionList)
            return ActionList   
        else:
            EverySuccessor = problem.getSuccessors(currentState) # Takes in All EverySuccessor
            
            #Add successors onto stack
            for successor in EverySuccessor:
                (NextSuccessor, action, cost) = successor
                cost += temporaryState[0][2] 
                astar.push(((NextSuccessor, action, cost), temporaryState)) # Priority search by cost
      
    # It is Done!
    return []

    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
