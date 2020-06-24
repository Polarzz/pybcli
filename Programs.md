This README is documentation on Programs <br>

<br>
<br>
Programs are essentialy applications for pybcli and are simple and easy to write.
<br>
NOTE: Variables cannot have spaces in they're names and comments have to be on a line by themselves
<br>

```bash
ask <QUESTION> -> <VARIABLE TO STORE IT TO>
if <> == <> -> <DO SOMETHING> else <SOMETHING ELSE> 
// if statements do not need else statements and pass or nothing can be used in them
led-toggle red 
// you can run commands via a program without anything needing to be changed
set <something> to <something>
echo $<something>
// variables have to start with a $ when being used in commands and statements, but not in setting them
// most of the programs are just commands stringed together to do something useful, but with statements and comments
// no permission is required to do anything as of now so you can make directories and files anywhere and remove them in the same way.
mkdir test
ask Directory name: -> NEW_DIR
mkdir $NEW_DIR
del NEW_DIR
// no sort of math is implemented as of now.
// this is a comment
:: this is a comment
# this is a comment
~ this is a comment
```
