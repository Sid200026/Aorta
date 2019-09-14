# Guide to common tasks
## Making any change to the repository
### If you want to add/modify/remove some files from the repository run these commands
- ##### fork the repository from the github website
- ##### clone the forked repository to create a local copy
  - ###### run ` git clone *repository link* `  to create a local folder
  - ###### enter the folder and make the changes
- ##### run ` git remote add upstream *official repo link* `  ( only the first time )
- ##### run `git fetch upstream`to update your local repository with the official's files in case they change. 
- ##### run `git checkout develop` then `git merge upstream/develop` to copy the changes to the develop branch from the upstream's develop branch.
- ##### run `git push origin develop` to update your fork with the changes
- ##### create a new branch from develop by `git checkout -b *branchname*`
- ##### make the changes in the local copy
  - ###### after editing a file or adding some run `git add *filename or foldername* `which will add the file/folder to the current commit
  - ###### If you delete a file/folder run `git add ./` in the same directory
  - ###### at any point if you want to check the files on the commit currently run `git status`
 - ##### once you make all the changes commit them by running `git commit -m "*commit description*"`
 - ##### make as many commits as you want and when you are finally ready to update the official repository run 
   - ###### ` git push -u origin *edited branch's name*` to create a new branch on your fork. If you want to update an existing branch remove the `-u` argument. 
 - ##### now head over to the site and create a pull request from your new branch to the develop  branch of the official. 
 - ##### your code will be reviewed and then merged
## Installing Django and breakdown of components
##### to install it just run `pip3 install Django` 
##### to create a new app run `django-admin startapp *appname*` inside the project folder
### Breakdown of the project folder :
####  *root directory*
- ##### `manage.py` manages the project 
  - ###### `python3 manage.py runserver` hosts the site at `127.0.0.1:8000/`
  - ###### once run, it describes any errors as well so use it to debug
#### *main app folder*
- ##### has `settings.py` which contains the project settings. any new app's name should be added to the apps list
#### *sub app folder* 
 - ##### belongs to that particular django app and has the following parts ( you may have to create some )
   - ###### `urls.py` maps urls to django views
   - ###### `views.py` has views which tell django which data to display and which html page to render
   - ###### `models.py` is the database
   - ###### `./static/*appname*/` contains static files like bootstrap or css files or images for that app
   - ###### `./templates/*appname*/` contains the html templates for that app
