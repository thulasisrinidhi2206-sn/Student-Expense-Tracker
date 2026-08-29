\# AI Coding Assistant Prompt Log



\## Project

Student Expense Tracker



\## AI Coding Assistant

Antigravity



\---



\# 1. Zero-shot Prompt



\## Technique

Zero-shot



\## Exact prompt used



Build a small Python command-line Student Expense Tracker from scratch.  Requirements: - Use clean, beginner-friendly Python. - Create 5–8 meaningful functions. - Allow users to add expenses with description, category, and amount. - Allow users to view all expenses. - Calculate total expenses. - Calculate expenses by category. - Calculate average expense. - Find the highest and lowest expense. - Include input validation for invalid amounts. - Keep the code modular and easy to test. - Create pytest unit tests for the core functions. - Do not use external libraries except pytest. - Also create a requirements.txt file.  Start with the basic project structure and implementation.



\## Tool response and evaluation



Antigravity created the initial Student Expense Tracker project, including the Python implementation, pytest unit tests, and requirements.txt.



Evaluation: Accepted. The generated project was reviewed and tested successfully.



\## Why Zero-shot was appropriate



Zero-shot prompting was appropriate for the initial project because the requirements were clear and specific. Examples were not necessary because the requested functionality and constraints were already explicitly described.



\---



\# 2. Few-shot Prompt



\## Technique

Few-shot



\## Exact prompt used



Improve the documentation and test style of the Student Expense Tracker.



Follow these examples when updating the project.



Example 1:

Function: add\_expense()

Docstring:

"""Add a new expense with description, category, and amount."""



Example 2:

Function: calculate\_total()

Docstring:

"""Return the total amount of all expenses."""



Example 3:

Test name:

test\_calculate\_total\_with\_multiple\_expenses()



Expected style:

def test\_calculate\_total\_with\_multiple\_expenses():

&#x20;   expenses = \[...]

&#x20;   assert calculate\_total(expenses) == expected\_value



Use the same concise docstring style for the remaining functions.



Use the same descriptive pytest naming convention for the remaining tests.



Do not change the application's core functionality.

Do not introduce unnecessary dependencies.



Show me the proposed changes before applying them.



\## Tool response and evaluation



Antigravity updated the function docstrings and refactored the unit-test naming and style according to the examples. It also updated the README documentation.



The resulting test suite contained 29 passing tests.



Evaluation: Accepted after reviewing the changes. The changes followed the requested style and did not change the application's core functionality.



\## Why Few-shot was appropriate



Few-shot prompting was appropriate because examples were useful for establishing a consistent documentation and testing style. The examples showed Antigravity exactly how the remaining docstrings and pytest names should look.



\---



\# 3. Chain-of-thought / Edge-case Debugging



\## Technique

Chain-of-thought



\## Exact prompt used



We need to perform a genuine debugging and edge-case analysis on the current Student Expense Tracker.



Think step by step.



Inspect the existing tracker.py implementation and its current tests. Identify one realistic edge case or logic weakness that is not adequately covered by the existing 29 tests.



Then:



1\. Explain the expected behavior for the edge case.

2\. Identify why the current implementation may fail or behave incorrectly.

3\. Create a focused pytest test that reproduces the problem.

4\. Run the test and confirm whether it exposes a real problem.

5\. If the test fails, identify the root cause.

6\. Implement the smallest appropriate fix.

7\. Run the complete test suite again.

8\. Confirm that the original tests and the new regression test all pass.



Do not invent a failure or change behavior unnecessarily. Only fix the issue if the edge case demonstrates a genuine problem in the current implementation.



\## Tool response and evaluation



Antigravity identified a sub-cent amount-rounding edge case in the amount validation logic. It added a regression test covering very small positive values such as 0.004 and 0.001 and updated the validation logic so that an amount that rounds to zero is rejected.



The complete test suite passed with 30 tests.



Evaluation: Accepted. The tool identified a relevant edge case, added a regression test, implemented a focused fix, and verified that all original tests and the new regression test passed.



\## Why Chain-of-thought was appropriate



Chain-of-thought was appropriate because this task required reasoning about input validation, decimal rounding, and the existing test coverage. The step-by-step debugging process helped identify the edge case, reproduce it with a regression test, implement a focused fix, and verify the result.



\---



\# Reflection



Antigravity was useful for this assignment because it could work with the project as a whole rather than only suggesting small code completions. Compared with GitHub Copilot, I found the agentic workflow faster for larger changes because I could describe a task and have the tool inspect files, modify multiple files, and run the test suite. For example, Antigravity updated the documentation and test naming consistently after I provided several examples, and it also investigated an edge case and added a regression test.



The main disadvantage was that I still needed to review the generated changes carefully. The tool made multiple file changes at once, so checking the Review panel and running the tests was important. Git and authentication also had to be handled separately, and I had to verify the commit history and repository contents myself.



For a real team, I would choose Antigravity when I need an AI assistant to work across several files, investigate a debugging problem, or implement a small feature from a clear description. I would prefer Copilot for situations where I mainly need quick inline suggestions while writing code. Overall, Antigravity felt more capable for task-level development, while requiring careful human review before committing changes.

