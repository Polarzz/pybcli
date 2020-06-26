# pybcli
> Pyboard Command Line Interface. <br>
Take control of your pyboard / microcontroller. <br>
<br>
All makes are tested on both a standard pyboard and pyboard lite and soon to be ESP32 once it arrives. <br>
<h2> LATEST </h2>
Make 4 introduces command looping in programs, waiting in programs, and loops with delays in programs. It also includes user creatable commands. <br>
To loop a command use the <strong>loop [times] [command] </strong> command. To wait use <strong>wait [time as integer of float] </strong> and to loop with delay use <strong>loop-delay [times] [time as integer or float] [command]</strong>. <br>
 
<br>
Added <strong>cat</strong> and <strong>dump</strong>. <br>
To create you're own commands place a file in <strong>os/cmds</strong> called <strong>[your command name].command</strong>. Commands are essentially programs but you can use <strong>%arg</strong> to get the arguments. <br>

```bash
// say.command
echo %arg
```

This will mimic the echo command by printing its arguments. It echos the arguements of <strong>say</strong>, like <strong>echo</strong> or <strong>print</strong>

<h2> OLD </h2>
In make 1 (mk1) there is basic functionality. <br>
Commands include: <br>

```bash
echo <text>
led-toggle <led-color / all>
exit <exits>
hard-reset <hard-restart>
cd <dir>
ls <dir>
pwd <prints working directory>
mkdir <name>
rmdir <dir>
prompt <return to mpy prompt>
sw-status <prints whether or not the switch is being pressed>
free <prints free and allocated ram>
clear-cache <clears cache>
help
```

<br>
<br>
In make 2 (mk2) there is alot more operating system like functionality such as users and global variables. <br>
In make 2 there are 2 main files. <strong> fs-main.py </strong> is to be ran on flash storage while as <strong> sd-main.py </strong> is to be ran on an sd card on the pyboard / microcontroller. This is as of errors that occur due to directory structure.
<br>

```bash
echo <text>
led-toggle <led-color / all>
exit <exits>
hard-reset <hard-restart>
cd <dir>
ls <dir>
pwd <prints working directory>
mkdir <name>
rmdir <dir>
prompt <return to mpy prompt>
sw-status <prints whether or not the switch is being pressed>
free <prints free and allocated ram>
clear-cache <clears cache>
mk-user <username>
su <user>
set <variable name | variable value>
del <variable name>
touch <file name>
<help> <no args or help <command> for certain command help>
```

<h2> Make 3</h2>
In make 3 (mk3) alot has been added. <br>
Added "programs" and "shell scripts". <br>
"Programs" allow you to create a somewhat of an app for the pyboard, quick and easily.
Make 3 introduces support for other micropython boards, and has been tested on an ESP32. The file to be used for other boards is <strong> other-main.py</strong>.
<br> 
Programs can be ran by <strong>./<filename></strong> or <strong>shell <filename>. The same is true for shell scripts.<br>
An example program:

```bash
ask What is you're name -> USERNAME
if $USERNAME == $USER -> set logged_in to True else set logged_in to False
if $LOGGED_IN == True -> echo You are logged in.
if $LOGGED_IN == False -> mkuser $USERNAME
su $USERNAME
```

<br>
This program will ask for input, the users name, then if they are logged in as that user will tell them that they are logged in. If they are not logged in it will create an account under the name they entered and switch to that user.
<br>
Full documentation on programs in <strong>Programs.md</strong>.
Example programs can be found under <strong>os/exmpl-prgms</strong>


<br>
<br>
<h2> Images </h2>
<br>
<br>

<img src="https://github.com/Polarzz/pybcli/blob/master/img/led-all-ss.png">
<img src="https://github.com/Polarzz/pybcli/blob/master/img/led-all-img.JPG">
<br>
<br>
<img src="https://github.com/Polarzz/pybcli/blob/master/img/examples.png">
<img src="https://github.com/Polarzz/pybcli/blob/master/img/Screenshot%20from%202020-06-20%2013-08-22.png">
<img src="https://github.com/Polarzz/pybcli/blob/master/img/Screenshot%20from%202020-06-20%2013-08-07.png">
