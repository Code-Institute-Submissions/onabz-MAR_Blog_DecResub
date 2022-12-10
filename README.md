# Mum Loves Representation
Mum Loves Representation is a blog by an African British Mum(Tomi) who wants her little girl to be able to play with a heirloom doll that represents her as she grows and plays imaginatively. She believes that all children should play with black dolls for the purpose of encouraging diversity. She feels that  brown dolls, black dolls, and ethnic dolls are often left upon the shelf, untouched and ignored while it is easy to get one's hands-on white dolls. She believes the situation is very tragic.This blog features several Articles posted by Tomi that shed more light on this issue along with several other topics under the ethnicity topic.

![Responsive Mockup](static/documentation/testing/ami-responsive.png)

The Responsive Mockup image above shows how responsive the Mum Loves Representation is across various device screen sizes ranging from mobile devices to large monitor screens. The Mum Loves Representation is well layed out with a bold font style used across all pages. The buttons are very legible on all the screen sizes. 

## UX

### User Stories:
- As a User I can view a list of all articles so that I can choose one to read.
- As a User I can click on an article so that I can read it in full.
- As a User I can like or unlike articles so that I can express my views about them.
- As a User I can view number of likes on each article so that I can see those that are more popular.
- As a User I can leave comments on an article so that I can interact with the content creator.
- As a User I can view comments on articles so that I can see the reader's thoughts on the article.
- As a User/Admin I can approve or disapprove comments so that I can filter out questionable comments.
- As a User I can register an account so that I can like and comment on an article.
- As a User/Admin I can create, read, update and delete posts so that I can manage my articles.
- As a User/Admin I can draft an article so that I can work on it later.
- As a Site User I can add an article from within the website so that I don't have to use the admin panel.
- As a Site User I can edit an article from within the website so that I don't have to use the admin panel.
- As a Site User I can delete an article from within the website so that I don't have to use the admin panel.
- As a Site Admin I can authorise a user so that they can edit/delete an article.

### Colour Scheme Used
I chose to go with this Boostrap blog theme called Clean Blog. It features a modern design with a subtle splash of color. This makes the site very easy to read with large fonts that are well spaced out. I made use of specifically choosen background images to showcase the theme of the blog. 

### Typography

I chose to use this carefully styled Bootstrap blog theme which features distraction free blog text optimized for legibility. It uses the Lora font-family for the body and the Open Sans font-family for the headers.

### Wireframes

Below are sketched images of how I planned to layout the website design. You will notice that the final design of the website is slightly different from my initial sketches for some pages which is because the template i used was not an exact match to my sketches.

![Home Template Wireframe](static/documentation/wireframes/wireframe-home-page.jpg)
![About Template Wireframe](static/documentation/wireframes/wireframe-about-page.jpg)
![Article Template Wireframe](static/documentation/wireframes/wireframe-article-page.jpg)
![Add Article Template Wireframe](static/documentation/wireframes/wireframe-add-article-page.jpg)
![Register Template Wireframe](static/documentation/wireframes/wireframe-register-page.jpg)
![Logout Template Wireframe](static/documentation/wireframes/wireframe-logout-page.jpg)
![Signin Template Wireframe](static/documentation/wireframes/wireframe-signin-page.jpg)

## Features 

### Existing Features:

  __The home page__

  - The home page contains the page header which features a specifically choosen background image that showcases various kinds of dolls in question. It contains the name of the blog and author as the hero text. Under the page header you have the article list area that shows the tiltle of the article, an excerpt, author, date created and a like button.
 
![Home Page](static/documentation/testing/home-page.png)
![Home Page](static/documentation/testing/article-list.png)

 __Navigation Bar__

  - It is made up of five links including the logo. They are the Home page, About page, Add Article page and the Logout page(this changes to the register page and login page when there is no user logged in). It is fully responsive and features on all the pages. The Logo also links back to the home page. 
  - It makes it very easy for users to navigate around the pages with multiple links back to the home page.  

![Nav Bar](static/documentation/testing/nav-bar-login.png)
![Nav Bar](static/documentation/testing/nav-bar-logout.png)

  __About Page__

  - The about page contains the page header which features a specifically choosen background image. It contains the name of the blog and author as the hero text. 
  - Under the page header you have the about page content with a header and the content.

  ![About Page](static/documentation/testing/about-page.png)

  __Article Page__

  - This page shows each article in detail.

  ![Article Page](static/documentation/testing/article-pg.png)

  - It shows details about the title,excerpt,author and date the article was created. 
  - It gives users the ability to like and unlike the article with a like button below the article.

  ![Like button](static/documentation/testing/like-comment.png)

  - It also gives users the ability to comment on articles with a comment section below the articles.

  ![Comment section](static/documentation/testing/comment-section.png)

  - When non superusers post comments, they do not appear immediately on the article page. Instead the request is sent to the admin for approval. Once approved it then appears below the article. This gives the admin the ability to filter out unwanted comments. 

  __Article edit/delete feature__

  - Under the article list section on the home page, a user can edit or delete an article that the user is authorised to.
  - The edit or delete feature won't appear on articles the user is not authorised to modify.

  ![Edit/delete feature](static/documentation/testing/permission-to-edit-or-delete.png)

  - A user who is not logged in cannot edit or delete any article.

  ![Edit/delete feature not available](static/documentation/testing/edit-or-delete-not-permitted-when-not-signed-in.png)

  __Add Article Page__

  - This is the page from which authorised users and admin can add new articles to the blog.
  - A user needs to be logged in to use this page. If a user is not logged in, they get a warning page telling them to login.

  ![Add Article warning Page](static/documentation/testing/add-article-pg-not-permitted.png)

  - This page contains the relevant input fields for for adding a new article.

  ![Add Article Page](static/documentation/testing/add-article-pg.png)

  __Update Article Page__

  - This page allows authorised users to edit articles that they have posted.
  - It gives them relevant prepopulated input fields to carryout editing.
  - It has an update button to post the updated article.

  __Delete Article Page__

  __Register Page__

  - It contains input fields for signing up.
  - It has a sign up button that has a hoover effect.
  - It has a background image to the right side of the input fields which further showcases the brand.

  ![Register Page](static/documentation/testing/register.png)

  __Login Page__

  - It contains input fields for user login. 
  - It has a sign in button that has a hoover effect.
  - It has a background image to the right side of the input fields which further showcases the brand.

  ![Login Page](static/documentation/testing/login-page.png)

  __Logout Page__

  - It contains a sign out button for a user to logout. 
  - The sign out button that has a hoover effect.
  - It has a background image to the right side of the input fields which further showcases the brand.

  ![Logout Page](static/documentation/testing/logout-page.png)
 

 __The Footer__

  - At the very bottom of the home page and every other page on the MLR website is the footer which houses the relevant social media links. 
  -  When clicked on, these social media links open to a new tab preventing the user from having to use the back button to go back to the page they were on before.

![Footer](static/documentation/testing/footer.png)

### Features Left to Implement

- A Contact form to collect user info.
- A category field to allow user categorize articles into various types. 

## Technologies Used

- I used HTML, CSS and Javascript to design the templates.
- I used a Bootstrap theme that came with its css files and custom javascripts.
- I used Javascript to set date in footer automatically.
- I used Django frame work to create the website.
- I used Python to input commands in Django frame work.
- I used Gitpod as my IDE for this project.
- I used Github to host my repositories.
- I used Git for version control of my website.
- I used Google Chrome DevTools for testing the application's functionality.
- I used Font Awesome icon for the social media icons.
- I used Heroku to deploy the website.

## Database Schema

![Database Schema](static/documentation/testing/Database_schema.png)

## Testing 

- I tested that pagination was working properly on the home page by adding more than four articles to trigger pagination.

![Pagination1](static/documentation/testing/test-for-pagination.png)
![Pagination2](static/documentation/testing/test-for-pagination2.png)

- I tested that I could create a new article with the add article page. The new article appeared at the top on the article list area of the home page.

![Create article](static/documentation/testing/create-article.png)

- I tested that I could edit the article I just created with the edit link next to the article.

![Edit article](static/documentation/testing/edit-article.png)

- I tested to show that I could delete the article I just edited with the delete link next to the edit link.

![Delete article](static/documentation/testing/delete-article.png)
![Delete article](static/documentation/testing/delete-article2.png)

- I tested that I could register a new account by creating a test-account.

![Create test account](static/documentation/testing/create-test-account.png)

- I tested that the test-account could not edit or delete any other users article. While test-account is logged in, the edit and delete links are not visible next to the articles in the article list area of the home page.

![No edit or delete link](static/documentation/testing/no-edit-delete-link.png)

- I tested that the admin user account could edit or delete the article it created. Once logged in, it had access to the edit and delete links on the test article it created.

![Edit and delete available](static/documentation/testing/edit-delete-available.png)

- I tested that the like button was working and that it showed the number of likes.

![Like button tested](static/documentation/testing/like-button-test1.png)
![Like button tested](static/documentation/testing/like-button-test2.png)

- I tested that all social media links were working and opening in new tabs.

### Validator Testing 

- HTML
  - No errors were found when passing through the [Nu Html Checker](https://validator.w3.org/nu/?doc=https://marblog.herokuapp.com/)

![Nu Html Checker](static/documentation/testing/html-validator-home.png)

  - No errors were found when passing through the [Nu Html Checker](https://validator.w3.org/nu/?doc=https://marblog.herokuapp.com/about/)

![Nu Html Checker](static/documentation/testing/html-validator-about.png)

  - No errors were found when passing through the [Nu Html Checker](https://validator.w3.org/nu/?doc=https://marblog.herokuapp.com/accounts/signup/)

![Nu Html Checker](static/documentation/testing/html-validator-signup.png)

  - No errors were found when passing through the [Nu Html Checker](https://validator.w3.org/nu/?doc=https://marblog.herokuapp.com/accounts/login/)

![Nu Html Checker](static/documentation/testing/html-validator-login.png)

  - No errors were found when passing through the [Nu Html Checker](https://validator.w3.org/nu/?doc=https://marblog.herokuapp.com/black-mumprenuer-who-loves-representation/)

![Nu Html Checker](static/documentation/testing/html-validator-articles.png )

- CSS
  - No errors were found when passing through the [W3C CSS Validator](https://validator.w3.org/nu/#textarea)

![W3C CSS Validator](static/documentation/testing/CSS-validator.png)

- Python
  - No errors were found when passing the settings.py file through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/marblog/settings.py)
  
  ![pep8ci tool](static/documentation/testing/settings-py.png)

  - No errors were found when passing the urls.py file for the marblog project through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/marblog/urls.py)

  ![pep8ci tool](static/documentation/testing/urls-py.png)

  - No errors were found when passing the admin.py file through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/blog/admin.py)

  ![pep8ci tool](static/documentation/testing/admin-py.png)

  - No errors were found when passing the forms.py file through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/blog/forms.py)

  ![pep8ci tool](static/documentation/testing/forms-py.png)

  - No errors were found when passing the models.py file through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/blog/models.py)

  ![pep8ci tool](static/documentation/testing/models-py.png)

  - No errors were found when passing the urls.py file for the blog app through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/blog/urls.py)

  ![pep8ci tool](static/documentation/testing/blog-urls-py.png)

  - No errors were found when passing the views.py file through the CI Python Linter tool [CI Python Linter](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/MAR_Blog/main/blog/views.py)

  ![pep8ci tool](static/documentation/testing/views-py.png)

### Browser testing
  - Google Chrome

  ![Chrome](static/documentation/testing/google-chrome.png)

  - Firefox

  ![Firefox](static/documentation/testing/firefox-browser.png)

  - Opera

  ![Opera](static/documentation/testing/opera-browser.png)

  - Avg

  ![Avg](static/documentation/testing/avg-browser.png)

  - Brave

  ![Brave](static/documentation/testing/brave-browser.png)

  - Microsoft edge

  ![Edge](static/documentation/testing/microsoft-edge-browser.png)


### Responsiveness
- Mobile screens

  ![Mobile](static/documentation/testing/mobile-resolution.png)

- Tablet screens

  ![Tablet](static/documentation/testing/tablet-screen.png)

- Small laptops

  ![Small laptop](static/documentation/testing/small-laptop-screen.png)

- Large laptops

  ![Large laptop](static/documentation/testing/large-laptop-screens.png)

- Extra large screens

  ![Extra large screens](static/documentation/testing/extra-large-screens.png)


### User story Testing

- As a User I can view a list of all articles so that I can choose one to read.

  ![Home Page](static/documentation/testing/article-list.png)

- As a User I can click on an article so that I can read it in full.

  ![Article Page](static/documentation/testing/article-pg.png)

- As a User I can like or unlike articles so that I can express my views about them.

  ![Like button](static/documentation/testing/like-comment.png)
  ![Like button tested](static/documentation/testing/like-button-test1.png)

- As a User I can view number of likes on each article so that I can see those that are more popular.

  ![Like button tested](static/documentation/testing/like-button-test1.png)

- As a User I can leave comments on an article so that I can interact with the content creator.

  ![Comment section](static/documentation/testing/comment-section.png)

- As a User I can view comments on articles so that I can see the reader's thoughts on the article.

  ![View comments](static/documentation/testing/view-comments.png)

- As a User/Admin I can approve or disapprove comments so that I can filter out questionable comments.

  ![Approve comment](static/documentation/testing/comment-approval1.png)

- As a User I can register an account so that I can like and comment on an article.

  ![Register new account](static/documentation/testing/register.png)

- As a User/Admin I can create, read, update and delete posts so that I can manage my articles.

  ![Create article](static/documentation/testing/add-article-pg.png)
  ![Read article](static/documentation/testing/article-pg.png)
  ![Update article](static/documentation/testing/update-article-pg.png)
  ![Delete article](static/documentation/testing/delete-article.png)

- As a User/Admin I can draft an article so that I can work on it later.

  ![Article draft](static/documentation/testing/draft.png)

- As a Site User I can add an article from within the website so that I don't have to use the admin panel.

  ![Add new article](static/documentation/testing/add-article-pg.png)

- As a Site User I can edit an article from within the website so that I don't have to use the admin panel.

  ![Edit article](static/documentation/testing/update-article-pg.png)

- As a Site User I can delete an article from within the website so that I don't have to use the admin panel.

  ![Delete article](static/documentation/testing/delete-article.png)


## Deployment

The app was deployed to Heroku. There are four stages:
  - Create the Heroku app,
  - Attach the database,
  - Prepare our environment and settings.py file,
  - Get our static and media files stored on Cloudinary.

- Create the Heroku app:
  - In Heroku.com create new Heroku App - APP_NAME, Location = Europe.
  - Add Database to App Resources - Located in the Resources Tab, Add-ons, search and add e.g. 'Heroku Postgres'.
  - Copy DATABASE_URL value - Located in the Settings Tab, click reveal Config Vars, Copy Text.
   
- Attach the Database:
  - In gitpod:
    - Create new env.py file on top level directory - E.g. env.py

  - In env.py:
    - Import os library - import os
    - Set environment variables - os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
    - Add in secret key - os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"

  - In heroku.com:
    - Add Secret Key to Config Vars - SECRET_KEY, "randomSecretKey"

- Prepare our environment and settings.py file:
    - In settings.py:
      - Reference env.py -  
        ```python                    
        from pathlib import Path
        import os
        import dj_database_url

        if os.path.isfile("env.py"):
          import env
        ```
      - Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku - `SECRET_KEY = os.environ.get('SECRET_KEY')`
      - Comment out the old DataBases Section - 
        ```python
        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.sqlite3',
        #         'NAME': BASE_DIR / 'db.sqlite3',
        #     }
        # }
        ```
      - Add new DATABASES Section ( - links to the DATATBASE_URL variable on Heroku) - 
        ```python
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
        ```
    - In the Terminal:
      - Save all files and Make Migrations - `python3 manage.py migrate`
  
  - Get our static and media files stored on Cloudinary:
    - In Cloudinary.com:
      - Copy your CLOUDINARY_URL e.g. API Environment Variable - From Cloudinary Dashboard
    - In env.py:
     - Add Cloudinary URL to env.py - be sure to paste in the correct section of the link - `os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`
    - In Heroku:
      - Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment - e.g. `DISABLE_COLLECTSTATIC`, `1`
    - In settings.py:
      - Add Cloudinary Libraries to installed apps - 
        ```python                                            
        INSTALLED_APPS = [
            …,
            'cloudinary_storage',
            'django.contrib.staticfiles',
            'cloudinary',
            …,
        ]
        ```
        (note: order is important)
      - Tell Django to use Cloudinary to store media and static files (Place under the Static files) - 
        ```python
        STATIC_URL = '/static/'

        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
      - Link file to the templates directory in Heroku (Place under the BASE_DIR line) - 
        `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`
      - Change the templates directory to TEMPLATES_DIR (Place within the TEMPLATES array) - 
        ```python
        TEMPLATES = [
          {
            …,
            'DIRS': [TEMPLATES_DIR],
            …,
          },
        ]
        ```
      - Add Heroku Hostname to ALLOWED_HOSTS - `ALLOWED_HOSTS = ['marblog.herokuapp.com', 'localhost']`
    - In Gitpod:
      - Create 3 new folders on top level directory - media, static, templates
      - Create procfile on the top level directory - Procfile
    - In Procfile:
      - Add code - `web: gunicorn marblog.wsgi`
    - Note: Save all files
    -  In the Terminal:
      - Add, Commit and Push - 
      ```bash
      git add .
      git commit -m "Deployment Commit"
      git push
      ```
    - In Heroku:
      - Deploy Content manually through heroku.


The live link can be found here - https://marblog.herokuapp.com/

### Local Deployment

To make a local copy of this project, you can clone it by typing the following in your IDE terminal:

- `git clone https://github.com/onabz/MAR_Blog.git`

Alternatively, if using Gitpod, you can click the green Gitpod button, or use [this link](https://gitpod.io/#https://github.com/onabz/MAR_Blog)

## Credits 
 
### Content 

- The steps I used for the project set up was taken from [I think Therefore I Blog](https://www.youtube.com/watch?v=kEdGDvrFSks&ab_channel=MediaUpload)
- The steps I used to apply the bootstrap theme for the blog was from [Using a Bootstrap Theme](https://www.youtube.com/watch?v=tUPjzTHgEWA&t=10s&ab_channel=MediaUpload)
- How I went about creating the update article page was taken from [Update and Edit Blog Post - Django Blog #6](https://www.youtube.com/watch?v=J7xaESAddDQ&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=15&ab_channel=Codemy.com) 
- How I went about creating the delete article page was taken from [Delete a Blog Post - Django Blog #7](https://www.youtube.com/watch?v=8NPOwmtupiI&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=7&ab_channel=Codemy.com)

### Media

- The bootstrap theme used in the design of the blog was from [Start Bootstrap](https://startbootstrap.com/theme/clean-blog)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- The template for the login, logout and signup pages was from [Mdbootstrap](https://mdbootstrap.com/docs/standard/extended/login/#section-5)
- All my background images were from [amarisandchaya](https://www.amarisandchaya.com/)
- Most of the articles were from [amarisandchaya](https://www.amarisandchaya.com/) and one from [Metro Parent](https://www.metroparent.com/parenting/talking-about-race/the-importance-of-representation-in-toys/)

### Acknowledgements

- I would like to thank my Mentor Tim Nelson for his invaluable support all through this project. I would not have been able to put all this together if not for his patience and insight.
- I would like to thank [Student Care](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecommerce/studentcare) for their regular check up on me to ensure that I was always on track to completing this project and to reassure me that they were always available if I needed any help.