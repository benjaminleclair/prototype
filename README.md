
# NOLOGIC

### Programming without conditions

NOLOGIC is an attempt to define a new programming paradigm based on using state 
and preconditions as a replacement for branching logic. One of the goals of the language 
is to encourage defensive programming by eliminating choice from code, and instead defining
flow of logic based on matching of state conditions. It is a computation model that comes 
directly from the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) paradigm. Like MapReduce, parallelism and pattern matching 
replace a more linear style of boolean logic evaluation.

The philosophy of NOLOGIC is to be EXPLICIT about assumptions programmers make in writing code. 
Rather than rely on conventions, style guides, and "best practice" suggestions, NOLOGIC is an 
attempt to limit the scope of IMPLICIT characteristics of code. While traditional thinking about 
functions is that they are blocks of code which accept values and return values, NOLOGIC takes 
a different approach where functions must define preconditions in order to be called. In that regard, 
functions have context, they are not just blocks of reusable code which are not aware of their calling
environment.


[Overview](docs/OVERVIEW.md)

[Implementation](docs/IMPLEMENTATION.md)

[Todos](docs/TODO.md)


## STATE
 
Computers are stateful, and though there are reasons to hide this, such as in functional programming,
ultimately there is no escaping that computation requires memory of some kind. NOLOGIC chooses to 
embrace the stateful nature of computers, and use it as a way of defining branching in programs. 

Functions must define the state that is required to exist for the function to execute. This means 
using preconditions to determine how the program will branch. This has obvious benefits for 
defensive coding, which can improve software security and reliability.  Similar to the semantics of 
transaction computation structures (such as in [MySQL](https://dev.mysql.com/doc/refman/8.0/en/sql-transactional-statements.html)), the difference with NOLOGIC is that the syntax of the "language"
requires that programmers think about state with every block of functionality they write.


## ATTRIBUTES

Functions do things besides crunch numbers and return values. They make database or cache calls,
HTTP or API calls, they might deal with sensitive data, they might rely on certain dependencies.
NOLOGIC uses function and class attributes to add extra meta information to code, which are not
simply comments or annotations, but part of the environment that can be introspected at runtime.
By requiring programmers to EXPLICITLY add these to function or class definitions, 
defensive programming is again encouraged in a much deeper way than in many general purpose languages.


