# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The first time the game ran it looked normal. There was UI which let the user input a guess. And there was a message sent to give a hint to the player based on what their guess was.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The first bug was that the hints weren't correct. They kept saying "go lower" even when that was not right.
  The second bug is that the option to start a new game isn't working.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  The AI tool that I used on this project was Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  An example of an AI suggestion that was correct was that there was a mismatch between what the check_guess function returns and what the test asserts against. I asked Claude to correct the mismatch so they return and expect the same thing. I verified this was right by running the test and seeing that it passed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One suggestion that didn't work was when I was trying to fix the bug with the hints being incorrect. Claude didn't necessarily make a mistake but it neglected to fix another error behind the why the hints weren't working. So I asked Claude to help fix the hints and it suggested one fix (to remove the logic that converted the secret into a string), but didn't fix the other bug which was with the wording of the hint. I had to prompt again to get Claude to fix the other bug. I verified the result by checking that the hints now worked for the game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
