# pybcli
> Pyboard Command Line Interface. <br>
Take control of your pyboard / microcontroller. <br>
<br>
All makes are tested on both a standard pyboard and pyboard lite and soon to be ESP32 once it arrives. <br>
<h2> LATEST </h2>
In make 3 (mk3) alot has been added. <br>
Added "programs" and "shell scripts". <br>
"Programs" allow you to create a somewhat of an app for the pyboard, quick and easily.
Make 3 introduces support for other micropython boards, and has been tested on an ESP32. The file to be used for other boards is <strong> other-main.py</strong>.

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
