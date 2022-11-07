## Implementation of NOLOGIC

In its current form, NOLOGIC is implemented using the Python language with some newly defined
utility structures. As this project develops it can eventually be turned into a DSL with its own syntax. Currently only
functions are being treated, but classes can follow in a similar manner (albeit with different syntax). This 
implementation is a proof-of-concept, and not intended to be judged as efficient or well-designed Python code.

If a function is expected to execute after some condition has been met, such as a value has been 
retrieved from a data store successfully, then that should be stated when the function is defined. 
While that might reduce some reusability of code, this is a price we have to pay to make sure
that we are guaranteeing that the state is matched. 

### Functions

Functions are defined inside a wrapper function, which couples the inner function's logic 
with a definition of the state that must exist for the function to execute. The wrapper
function returns a tuple which contains these two components.


```
def stateful_function()
  
  def _callback(param1, param2, ...)
    # logic to execute
    
  my_state = "this state must exist for me to execute"
  
  return (my_state, _callback)
```


### state_selector

A utility function has been defined in [base.py](../nologic/base.py) called `state_selector`. 
This utility is the root of all branching calls which replaces boolean conditionals. 
`state_selector` matches the current state with a list of candidate functions, 
and calls the first function in the list that matches. It does so by first executing each function
in the list, which gives a list of tuples with the defined state and corresponding callback functions.

### Floor Division Example

A simple way to demonstrate this process is with a floor division by two function. We have an 
integer variable which we would like to divide in half. We are limiting the scope of the state 
to be whether the integer is either even (0) or odd (1). In a more complex example we could 
add a  precondition that we have an integer, that it is not null, etc, but we'll focus on the 
simplest case first.

In [divide.py](../nologic/examples/divide.py), we have defined an odd_divide and an even_divide function
to cover both state possibilities. There are no conditional statements allowed, except the one in 
`state_selector` which matches the states with the precondition defined in each function. 

### Permutations Example

A slightly more complex example can be seen in [permute.py](../nologic/examples/permute.py). Here we have 
a recursive process, which takes a list of elements and returns a list of permutations of that list. 
The state in this case is whether the list has more than one element, and therefore serves as designating whether we
have reached the base case of the recursion. Note that here also there are no conditional statements, 
because `state_selector` handles the branching decision.

