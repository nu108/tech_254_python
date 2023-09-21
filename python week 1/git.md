What is Git?
Git is a version control system that helps people manage their files.

Version control system- You can store a project, along with every single
version of that project in a repository.

Status tells you where your files are![check in over time.PNG](..%2F..%2F..%2FDownloads%2Fcheck%20in%20over%20time.PNG)

Respository- is where your project files are stored 

If you want to make a change to the project, you need to copy the whole 
repository on the computer. From their you can make changes and it would
not affect the original file. Once you have made the changes you can commit
and push them up to the repository. That basically updates the code on 
GitHub 

Git thinks of its data more like a series of snapshots of a 
miniature filesystem. With Git, every time you commit, 
or save the state of your project, Git basically takes a picture of
what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. 
Git thinks about its data more like a stream of snapshots

Git has three main states that your files can reside in: 
modified, staged, and committed:

Modified means that you have changed the file but have not
committed it to your database yet.

Staged means that you have marked a modified
file in its current version to go into your next commit snapshot.

Comitted- means thats the data is stored in your local database



![mod.PNG](..%2F..%2F..%2FDownloads%2Fmod.PNG)

The working tree is a single checkout of one version of the project. 
These files are pulled out of the compressed database in the Git 
directory and placed on disk for you to use or modify.

The staging area is a file, generally contained in your Git directory,
that stores information about what will go into your next commit. 
Its technical name in Git parlance is the “index”, 
but the phrase “staging area” works just as well.

The Git directory is where Git stores the metadata and object database
for your project. This is the most important part of Git, 
and it is what is copied when you clone a repository from another 
computer.


PWD- shows where you are 

CD- change directory
