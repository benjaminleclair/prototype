## Description of NOLOGIC

A central problem with software design and general purpose programming languages is that
conventions can arise that are ultimately left to the programmer to implement. Software
development teams can define code style guides, naming conventions, and even require specific 
syntax through enforcement methods like git commit hooks. While these methods can work to 
a certain extent to produce desirable code standards, programmers need to be educated, trained, 
and must remember/consent to follow the rules.
 
NOLOGIC focuses on two features (function pre-conditions and attributes) that allow meta information 
to be embedded in running code. These features are intended to make certain design decisions EXPLICIT,
instead of something that programmers can follow as IMPLICIT conventions. While comments and 
annotations can allow for information to be added to source code that can be examined using certain
third party tools, they are generally not accessible within the executing code. Structures like 
Python's [assert](https://www.w3schools.com/python/ref_keyword_assert.asp) can require that an executing program is in an expected state. What's missing
is the ability to query program memory at runtime to do something like, for example, get a list of all 
functions that make database calls, and dynamically wrap them with some kind of extra functionality.

NOLOGIC can shine in [middleware](https://en.wikipedia.org/wiki/Middleware) type applications, where functions are getting inserted into a 
chain of (callback) functions. Since it might not be known at compile time what those callbacks are, NOLOGIC 
can safely execute and dynamically modify running code based on the pre-conditions of a callback function. 

For example, if it can be determined that a callback function is going to log something to a server,
and the current state includes an active (or inactive) connection to that server, then by using introspection, 
a choice can be made without the programmer having to write a set of (hopefully) exhaustive conditionals. 
If the pre-conditions are not satisfied, an alternative branch is taken. By defining the required state
instead of handling exceptions due to failed assumptions, programmers are thinking a step ahead.

NOLOGIC is intended to reduce bugs that can easily happen when code is allowed to run AFTER a 
condition has been checked, but where the condition has not been correctly evaluated as expected. 
Rather, by defining a precondition on state BEFORE the program has even started running, what is left 
is simply a waterfall of logic. Because they are EXPLICITLY stated, pre-conditions ensure that state is
consistent with what is expected, and doesn't get buried in complicated syntax or out-of-language 
organizational conventions.
 
