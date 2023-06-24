## Exercise
Write a program that repeatedly executes commands until a list of n players (roster) is formed. The following commands can be used for this purpose. 
* sign: Receives the name of the player who wants to sign and adds it to the roster. **If the name already exists in the roster**, print 'Wrong player name!' and will not add the player to the roster. 
* done: Ends the process before the roster of n players is formed.

However, we do not consider cases where commands other than the above two commands are entered.

## Example
input
<pre>
Input the length of roster: 50
Command: sign
Name: Kim
Command: sign
Name: Cho
Command: done
</pre>
output
<pre>
['Cho', 'Kim']
</pre>