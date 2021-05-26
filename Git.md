# Commands
## Git remote add
- Is used to create an alias to avoid taping the URL of a repository.

# HowTo
## Create a branch from a previous commit
- Using a specific commit-id
- git branch <branchname> <commit-id>
- Using a number of ancestors
- git branch <branchname> HEAD~<number_of_ancestors>

## Cancel actions
### Cancel commit that has not yet been pushed
- git reset --soft HEAD~1
  
# Good practices
## Don’t use git pull
- *"You should never use git pull anyway, but if you do, git pull uses the upstream setting to figure out which remote to fetch from, and then which branch to merge or rebase with. That is, git pull does the same thing as git fetch—because it actually runs git fetch—and then does the same thing as git merge or git rebase, because it actually runs git merge or git rebase. (You should usually just do these two steps manually, at least until you know Git well enough that when either step fails, which they will eventually, you recognize what went wrong and know what to do about it.)"*

# Index
## Master
- Is the name of a branch, and is almost systematically the main branch of a repository and was its first branch created. It has other meanings and is not specific. *"The widespread use of the name is mostly due to the fact that the initialization (with git init) of a git sets its branch as ‘Master’ by default.*"
## Origin
- In Git, "origin" is a shorthand name for the remote repository that a project was originally cloned from. More precisely, it is used instead of that original repository's URL - and thereby makes referencing much easier.
## Upstream
- Is another branch name, usually a remote-tracking branch, associated with a (regular, local) branch.
## Properties
- A branch can have no upstream or one (only) upstream, i.e. a branch is the origin or does come from another branch, but can not be the result of the merging of multiple branches.

Source and more: https://stackoverflow.com/questions/37770467/why-do-i-have-to-git-push-set-upstream-origin-branch/37770744#37770744

