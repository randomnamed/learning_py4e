# learning_py4e
Coursera Course - Python for Everybody Specialization

## Basic git commands needed
**Enter to the repo you need your user name and email id in the local config file first**
- git config user.name her_username
- git config user.email her_email

**Aftet that you edit the files then use "git add" to add the files**
- git add . (adds all the files)
- git add file_name.xx (if you want to add specific files only)

**Then use the following commands for the first commit / push to the git server:**
- git config --local credential.helper ""
- git push origin master

**After the first one you can use:**
- git add .
- git commit -m "your meesage here"
- git push

**Delete branch after work is Done**
- git branch --delete <branchname>
- git branch -a command to verify the local Git branch is deleted