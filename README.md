# M0_C6 - Security System
Repository with prompt and code for Module 1, Challenge 6: Security System (Beginner).

## Prompt
You're a security contractor, and you've been contacted by a local archival service to create a simple program that tracks the entry and exit of personnel into a building. Here's how personnel would interact with your program:

1. It will always display a prompt: `Input: `.
2. A user will check in to the building by entering their username followed by "in": `jsmith in`.
3. After they have entered their command, a message will print out confirming they're checked in: `  jsmith is checked in`.
4. When they're done and want to leave the building, they enter their username followed by "out": `jsmith out`.
5. After they have entered their command, a message will print out confirming they're checked out: `  jsmith is checked out`.
6. If any suspicious conditions are encountered (see [requirements](#requirements)), you will sounded the alarm: `  ALARM SOUNDED`.

For example interactions, see below.

### Requirements
The client has given you a preset list of users that should be in the system already:

Username   |
-----------|
mhenderson |
jjabrams   |
sbrown     |
enterocc   |
zzdawg     |

- If an invalid user not named above tries to interact with the system, sound the alarm.
- If a user attempts to check in when they're already in, sound the alarm.
- If a user attempts to check out when they're already out, sound the alarm.
- If a user inputs invalid commands or other gibberish, sound the alarm.
- Your program must output the exact format [demonstrated below](#example).

## Example
```
$ python3 security_system.py
Input: mhenderson in
  mhenderson is checked in
Input: zzdawg in
  zzdawg is checked in
Input: mhenderson out
  mhenderson is checked out
Input: elonmusk in
  ALARM SOUNDED
Input: enterocc out
  ALARM SOUNDED
Input: zzdawg in
  ALARM SOUNDED
Input: hubba bubba bluasdfka
  ALARM SOUNDED
Input: zzdawg out
  zzdawg is checked out
Input: 
```

The above scenario shows how the program would run. It would continue running for forever, just taking user input and showing the prompt.

- `mhenderson` checked in and out without issues.
- `zzdawg` checked in once just fine, but then tried to check in again, sounding the alarm.
- An unauthorized user `elonmusk` tried to check in, so we sounded the alarm.
- `enterocc` tried to check out, but was never checked in to begin with, so we sounded the alarm.
- The second-to-last input was gibberish, so we sounded the alarm.

## Notes and Hints
- This problem is a little harder than everything you've done so far. But don't overthink this.
- Everything required to solve this problem is something you have either done before, or we've gone over it in a video. Mix and match these concepts.
- Notice how the output is indented 2 spaces in. The tests will look for that, so pay attention.

## Knowledge Tested
- Conditionals
- Loops
- Nesting and Scope
- Dictionaries
- User Input

## Instructions
1. Make sure `pipenv` is installed. For a tutorial, see [0.3.4 - Pipenv and Python Package Management](https://sva.thinkific.com/courses/take/sva-module-0/lessons/11857539-0-3-4-pipenv-and-python-package-management)
2. Fork this repository to your own account.
3. Clone the forked repository to your local computer.
4. Run `pipenv install` to install the needed modules in a virtual environment.
5. Run `pipenv shell` to activate a virtual environment with the installed modules. Alternatively, you can replace the typical`python3 [PROGRAM]` command with `pipenv run [PROGRAM]`.
6. Inside `security_system.py`, you will implement your code. You can decide how to write your program, what functions to define, etc. The only important piece is making sure your program outputs responses exactly in the same format as in example.
7. While you're writing and/or when you're done, you can execute the provided tests to verify your program works by running `python3 test_security_system.py`. All tests are passing if you see `OK` in the output.
