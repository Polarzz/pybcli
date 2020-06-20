# pybcli
> Pyboard Command Line Interface. <br>
Take control of your pyboard / microcontroller. <br>
<br>
All makes are tested on both a standard pyboard and pyboard lite and soon to be ESP32 once it arrives. <br>

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
In make 2 there are 2 main files. `fs-main.py` is to be ran on flash storage while as `sd-main.py` is to be ran on an sd card on the pyboard / microcontroller. This is as of errors that occur due to directory structure.
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

<br>
<br>
<h2> Images </h2>
<br>
An example of `led-toggle all`
![led-toggle-all](http://polarzdev.xyz/pyboard.microcontrollers.github/led-all-ss.png)





