- Activate virtual environment:
`source .venv/bin/activate`
- Deactivate virtual environment:
`deactivate`
- Creating new branch:
`git checkout -b branch_name`
- Switch between existing branches:
`git checkout branch_name`
- Pushing local branch to remote repo:
`git push origin branch_name`. 
    - Essentially the same thing as our normal `git push` after `git commit`
- Preview:
`python app.py`
    - After this, the current terminal session will no longer take normal commands, I usually open up a new terminal for commits etc
    - This automatically refreshes any change, no need to end preview to see new change, refresh browser will do
- End preview:
`^c` (control+c)

