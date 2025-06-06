# Overview

This assessment evaluates your ability to perform the following tasks in accordance with ICTPRG547 Apply advanced programming skills in another language:

- Performance elements:

- 1.4 Code sorting algorithm using programming techniques
- 3.2 Detect and resolve errors of syntactical, logical and design origin
- 3.3 Design and document required tests
- 4.1 Develop and document solution according to debugging test results

You will demonstrate your performance by providing evidence that you can "code at least one sorting algorithm", and "test and debug the code to resolve errors of a syntactical, logical, or design origin".

To succeed you must use a "systematic, analytical processes in complex, non-routine situations, setting goals, gathering relevant information, and identifying, and evaluating, options against the agreed criteria".

## 2. General instructions

> CRITICAL: Failure to follow these instructions will lead to an NYC

- Copy this file into a `docs` folder in your assessment repo
- Add and commit this file to your repository and associate the tag `por3-start` :
  - Copy and `add` this file to your repository under the `docs` folder
  - `git commit -m "chore: add task overview to my repo"
  - `git tag por3-start`
  - `git push origin main --tags`
  - Optional: you may want to complete this work in a branch
  - On your last commit, add the tag `por3-finish`
- Commit changes after you complete each task
- Push changes to your GitHub repository
- Ensure you submit your git repo (`.git/`) along with your assessment submission

## 3. Players have scores now

### 3.1. Task: Add scores to players

Add a private instance variable to the Player class that will hold the score (a positive integer value).

Provide a getter (property) and a setter method for this value.

#### 3.1.1. Success criteria

- [ ] Correct use of private instance variable
- [ ] Use of properties to create a getter and setter
- [ ] Raising ValueError if someone attempts to set a non-positive value

## 4. Sorting players

### 4.1. Task: Add unit tests for sorting players

Add the following unit tests to the `test_player.py` file:

```python
def test_sort_players(self):
    players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5), Player("Charlie", uid='03', score=15)]
    # note: ensure initialization code is valid for **your** implementation

    # do **not** change the following code:
    sorted_players = sorted(players)

    # players must be sorted by score as shown here:
    manually_sorted_players = [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10), Player("Charlie", uid='03', score=15)]

   self.assertListEqual(sorted_players, manually_sorted_players)

```

> **Note:** If you have made other changes to the initializer of your player update the above code to reflect this change - you must not make any other changes to the test code above.

### 4.2. Task: Interpret unit tests

What was the outcome of running the above unit test, copy paste the output **for just this particular test** below:

```text
sparrow@fedora:~/source/repos/SRUS-RK-Games$ PYTHONPATH=app python test/player_test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```

### 4.3. Success criteria

- [ ] Unit test added to `test_player.py`
- [ ] Unit test output provided
- [ ] Unit test output reflects the error in `sorted(players)` (if you are getting another error read the instructions CAREFULLY)
      ^?? i got a passed test? sorry if thats an issue

> NOTE:: I really cant figure out why my tests are passing. if i need to redo this i will but i think ive just done this out of order

#### 4.3.1. Question

The tests checks that calling sorted on a list of players will sort them by score, what is the **only** magic method that must be implemented in the player class for the `sorted` function to succeed?

> the only method TECHNICALLY needed is a **gt* method but having a ***lt* method will also work. and hypothetically a \_\_ge* or \__le_ method alone will work.

#### 4.3.2. Task: Implement the magic method in the Player class

Add a test case to test_player to test the comparison operator you are about to add - ensure you do not test a dunder method directly!

```python
def test_players_can_be_compared_by_score(self):
    # note: ensure initialization code is valid for **your** implementation
    alice = Player("Alice", uid='01', score=10)
    bob = Player("Bob", uid='02', score=5)

    # Add the appropriate expression to the following assert test
    self.assertTrue(...)
```

Run the test and confirm that your error resembles the previous error

```text
sparrow@fedora:~/source/repos/SRUS-RK-Games$ PYTHONPATH=app python test/player_test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

> again due to mixed order implementation? Not a error.

Implement the appropriate magic method in the Player class and ensure you pass this test (and only this test!).

#### 4.3.3. Success criteria

- [ ] Unit test added to `test_player.py`
- [ ] Magic method implemented in `Player` class
- [ ] Initial Failed Unit test output provided
- [ ] Unit test runs successfully with submitted code
- [ ] Dunder method not employed directly

#### 4.3.4. Task: Are we sorted yet?

Rerun `test_sort_players` does the test pass? If not, include the output below:

```text
Your output here
```

Why did the test fail (note: if it doesn't fail, it means there is something you have already done before you were asked to - you need to figure out what that is!)?

> Answer here

Add the necessary code to the Player class to ensure that the `test_sort_players` test passes.

#### 4.3.5. Success criteria

- [ ] Correct explanation of why `test_sort_players` failed/passed
- [ ] Correct implementation of the magic method in the `Player` class
- [ ] `test_sort_players` passes when run against the submitted code

## 5. Implement a custom sorting algorithm

The senior developer on your team believes that a custom sorting algorithm would be more efficient than the built-in `sorted` function (you grit your teeth, sigh, and realize you need this job!). They have asked you to implement a custom sorting algorithm that will sort a list of players by score.

To help you get started they have provided you with some example code that they wrote in their undergraduate days:

```python
def sort_quickly(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort_quickly(left) + [pivot] + sort_quickly(right)
```

### 5.1. Question: complexity

What is the expected time and space complexity of the above algorithm? You can answer using big O or in plain English but in both cases you MUST justify your answer.

> the above algorithm's time complexity is O(n log n) on average however if in a worst case senario can be O(n^2). id expect a O(n log n) time complexity from this algorithm. to justify, this algorithm recursively splits a list into smaller lists. and sorts it on te way down to join it which allows it to rejoin many smaller lists reducing the time complexity

### 5.2. Task: Implement the custom sorting algorithm

#### 5.2.1. Create a new method in the Player class

Use the sample above (and its algorithm) as a starting point to implement a `classmethod` in the Player class that takes a list of players and returns a list of players sorted by score in **descending** order. Top scores come first!

#### 5.2.2. Create a test cases

Add a separate test case to `test_player.py` to test your custom sorting algorithm

Include your code below:

```python
def test_player_quicksort(self):
        players = [Player(player_name="Alice", uid='01', score=10),
            Player(player_name="Bob", uid='02', score=5),
            Player(player_name="Charlie", uid='03', score=15)]
        sorted_players = Player.quicksort(players)

        solution = [
            Player(player_name="Bob", uid='02', score=5),
            Player(player_name="Alice", uid='01', score=10),
            Player(player_name="Charlie", uid='03', score=15)
            ]
        self.assertTrue([player.score for player in sorted_players] == [player.score for player in solution])
```

#### 5.2.3. Success criteria

- [ ] Custom sorting algorithm implemented in the `Player` class as `classmethod`
- [ ] Custom sorting algorithm sorts in descending order
- [ ] Custom sorting algorithm compares players using their score (via the rich comparison operators)
- [ ] Custom sorting algorithm tested in `test_player.py` and tests passed

### 5.3. Test your custom sorting algorithm at scale

The senior developer is impressed with your work and asks you to test your custom sorting algorithm with a list of 1000 players. They provide you with a script that will generate a list of 1000 players with random scores.

```python
import random
from player import Player


players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
```

#### 5.3.1. Task: Create a test case to sort 1000 players

Using the code above as a starting point, create a test case to test your custom sort algorithm - you can test it against the `sorted` function to ensure it is working correctly.

Include your test case below:

```python
    def test_large_quicksort_volume(self):
        import random
        players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
        quicksorted_players = Player.quicksort(players)
        sorted_players = sorted(players)
        self.assertTrue([player.score for player in quicksorted_players] == [player.score for player in sorted_players])
```

#### 5.3.2. Success criteria

- [ ] Test case added to `test_player.py`
- [ ] Test case sorts 1000 players correctly when compared to `sorted` function
- [ ] Test case passes when run against the submitted code

#### 5.3.3. Task: Testing sorting sorted players

You had a scary thought - and decided to test your custom sorting algorithm against a list of players that are already sorted by score. You are worried that your algorithm might not be efficient in this case.

#### 5.3.4. Task: Create a test case to sort 1000 sorted players

Create a test case that tries to sort 1000 players that are already sorted.

If you get a failure, include the failure below:

```text
======================================================================
ERROR: test_sorting_sorted_values (__main__.TestPlayer.test_sorting_sorted_values)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Sparrow\source\repos\SRUS-RK-Games\test\player_test.py", line 183, in test_sorting_sorted_values
    twice_quicksorted_players = Player.quicksort(quicksorted_players)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Sparrow\source\repos\SRUS-RK-Games\test\player_test.py", line 100, in quicksort
    return Player.quicksort(left) + [pivot] + Player.quicksort(right)
                                              ^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Sparrow\source\repos\SRUS-RK-Games\test\player_test.py", line 100, in quicksort
    return Player.quicksort(left) + [pivot] + Player.quicksort(right)
                                              ^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Sparrow\source\repos\SRUS-RK-Games\test\player_test.py", line 100, in quicksort
    return Player.quicksort(left) + [pivot] + Player.quicksort(right)
                                              ^^^^^^^^^^^^^^^^^^^^^^^
  [Previous line repeated 983 more times]
  File "c:\Users\Sparrow\source\repos\SRUS-RK-Games\test\player_test.py", line 96, in quicksort
    if x < pivot:
       ^^^^^^^^^
  File "c:\Users\Sparrow\source\repos\SRUS-RK-Games\test\player_test.py", line 47, in __lt__
    return self.score < other.score
           ^^^^^^^^^^
RecursionError: maximum recursion depth exceeded

----------------------------------------------------------------------
Ran 1 test in 0.117s

FAILED (errors=1)
```

Provide a reason why this test failed (if you got recursion errors, you need to explain **why** they occurred).

If your implementation did not fail, you must explain what changes you made to the original algorithm given by the senior developer to ensure that it did not fail.

> a Presorted algorithm is the worst case scenario for a quicksort algorithm. due to the list already being sorted. the program had to split and recursivelt call itself too many times.
> python has a limit to how many times a functions can call recursively to protect against unwanted memory usage

Propose a fix to your sorting algorithm that fixes this issue.

> a couple of solutions exist.
>
> - we can instruct python to increase the upper limit of max recursions.
> - we can rewrite this feature in another language
> - however i would run a linear scan across the data to ensure it's not already sorted. this would keep the same time complexity. just add a slight buffer.

```python
    def is_sorted(players: list) -> bool:
            for i in range(1, len(players)):
                if players[i] > players[i - 1]:
                    return False
            return True
```

#### 5.3.5. Success criteria

- [ ] Test case added to `test_player.py`
- [ ] Test case passes only when changes above are added

## 6. Task: Authenticity of in class work

Complete the following snippet before you submit:

```text
I, Ryan Kelley 20136584, completed this work outside of the scheduled hours. I spoke to Rafael Avigad, on 21/5/25, along with my documented reason for non-attendance, and have scheduled a time to meet to discuss my work.

I understand that until I meet my assessor to confirm that this work is a valid and true representation of my abilities to write and debug a sorting algorithm in Python, this submission cannot be considered complete.
```

## 7. Submit your work

- [ ] Ensure all tasks are complete and tests pass
- [ ] Answer all questions in your own words
- [ ] Complete the statement of authenticity
- [ ] Include `.git` showing each task committed (you must show at least 5 commits)
- [ ] Tag your last commit as `por3-finish`
- [ ] Push your changes to your GitHub repository
- [ ] Submit a zip of your repository to the LMS (ensure you do not add the `.venv` or `__pycache__` folders)

---

End of assessment task
