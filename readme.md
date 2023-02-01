# Git demo

The purpose of this repo is to demonstrate to students how you can use git, this will only cover the basics.

# Prerequisite

* Create a github account
* Download Github desktop
* Clone this repo
    To "download" the repository, press the <> code button just above this text. And then open in github desktop or copy the https link. 
# The four basic commands of git (Pull, Add, Commit, Push)

These for commands is what is needed to get code from the repository and to upload code to the repository

## Pull (Get code from repository)

Used to download code from the repository to your machine

git command in terminal
```
git pull
```

## Add, Commit, Push (All neeeded to push code to repository)

### Add

This command is used to select what code files with changes in them should be uploaded to the repository. When using programs like fork this is called stage/staging a file.

Below adds all files
git command in terminal
```
git add *
```
Below adds one specified file at the time. 
```
git add <specific file name>
```

### Commit

The final preparation step, write a message of what the commit contains, eq. Impletemented calculate_area_rectangle. Fixed calculation bug etc etc, try to be very specific but brief of what you are commiting.

git command in terminal
```
git commit -m "Implemented calculate_area_rectangle"
```

### Push

Actually pushes the code to the repo

git command in terminal
This pushes to current branch you are in
```
git push
```

This pushes to a specific branch, dev in this instance

```
git push origin dev
```

# Branches

In Git, a branch is a new/separate version of the main repository.

Git branches is good to use if you are working together with someone, but also useful if you would like the expierment with some code that you dont know if it will make it to the final version.

You can only merge different branches togheter if you are finished with a task or if for example a another branch has been updated. Merge is kind of like combining to two different branches. 

## Branch strategy
Main -> Dev -> feature branches

The main branch should be a working copy, of current code on the server.

Dev branch, good to use as middle layer for developing. All ready features should be merged to dev. When everything is tested etc dev gets merges into main.

Feature branches. These are each features branch. For example, in our example we want to implement a calculate_area_circle, this is then done in the area_circle branch. This branch does not affect the other branches at all until it is merged.


# Merge conflicts

If two people work on the same file at once and try to commit their changes to the same branch they might experince a merge conflict. This means that git receives changes in the same file and does not now which one is the correct one to use. These are some of the few ways of fixing conflicts.

Manually fixing them.
Make sure that your code and your collegeues code is inserted correct in your file. Sometimes it is good to communicate during this step so that everything is fixed as both intented.

Not coding in the same file at all.
Talk beforehand on what files you are going to change. Of course not always possible, but avioding merge conflicts is better than fixing them.



Always merge the branch you want to merge into, into your branch first, so that you can fix eventuall merge conflicts.


# Programs

There are a lot of programs to help with git. Either you use your terminal and write git commands from scratch. Or you can use program like fork, git kraken, github desktop etc. Program are quite nice since you get a graphical interface to see all previuos commits, branches etc etc

#For demo


No we add some text!!









Even more text!



![alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.womansday.com%2Flife%2Fg32979681%2Fcute-cat-photos%2F&psig=AOvVaw1ALwu0JQnf4FAN68vp9xGP&ust=1675373124716000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCLjGkrGh9fwCFQAAAAAdAAAAABAE)