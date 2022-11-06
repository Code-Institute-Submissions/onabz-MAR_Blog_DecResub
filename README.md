# Mum Loves Representation
Mum Loves Representation is a blog by an African British Mum(Tomi) who wants her little girl to be able to play with a heirloom doll that represents her as she grows and plays imaginatively. She believes that all children should play with black dolls for the purpose of encouraging diversity. She feels that  brown dolls, black dolls, and ethnic dolls are often left upon the shelf, untouched and ignored while it is easy to get one's hands-on white dolls. She believes the situation is very tragic.This blog features several Articles posted by Tomi that shed more light on this issue along with several other topics under the ethnicity topic.

![Responsive Mockup]()

The Responsive Mockup image above shows how responsive the Mum Loves Representation is across various device screen sizes ranging from mobile devices to large monitor screens. The Mum Loves Representation is well layed out with a bold font style used across all pages. The buttons are very legible on all the screen sizes. 

## UX

### Colour Scheme Used
I chose to go with this Boostrap blog theme called Clean Blog. It features a modern design with a subtle splash of color. This makes the site very easy to read with large fonts that are well spaced out. I made use of specifically choosen background images to showcase the theme of the blog. 

### Typography

I chose to use this carefully styled Bootstrap blog theme which features distraction free blog text optimized for legibility. It uses the Lora font-family for the body and the Open Sans font-family for the headers.

## Features 

### Existing Features

- __The home page__

  - The home page contains the page header which features a specifically choosen background image that showcases various kinds of dolls in question. It contains the name of the blog and author as the hero text. Under the page header you have the article list area that shows the tiltle of the article, an excerpt, author, date created and a like button.
 
![Home Page](static/Documentation/testing/home-page.png)
![Home Page](static/Documentation/testing/article-list.png)

- __Navigation Bar__

  - It is made up of five links including the logo. They are the Home page, About page, Add Article page and the Logout page(this changes to the register page and login page when there is no user logged in). It is fully responsive and features on all the pages. The Logo also links back to the home page. 
  - It makes it very easy for users to navigate around the pages with multiple links back to the home page.  

![Nav Bar](static/Documentation/testing/nav-bar-login.png)
![Nav Bar](static/Documentation/testing/nav-bar-logout.png)

  __About Page__

  - The about page contains the page header which features a specifically choosen background image. It contains the name of the blog and author as the hero text. 
  - Under the page header you have the about page content with a header and the content.

  ![About Page](static/Documentation/testing/about-page.png)

    __Register Page__

  - It contains input fields for signing up.
  - It has a sign up button that has a hoover effect

  ![Register Page](static/Documentation/testing/register.png)

- __The Footer__

  - At the very bottom of the home page and every other page on the MLR website is the footer which houses the relevant social media links. 
  -  When clicked on, these social media links open to a new tab preventing the user from having to use the back button to go back to the page they were on before.

![Footer](static/Documentation/testing/footer.png)

### Features Left to Implement

- A Contact form to collect user info.
- A category field to allow user categorize articles into various types. 

## Technologies Used

- I used HTML to design the templates.
- I used a Bootstrap theme that came with its css files and custom javascripts.
- I used Javascript to set date in footer automatically.
- I used Django frame work to create the website.
- I used Python to input commands in Django frame work.
- I used Gitpod as my code editor to write all the codes used throughout the website.
- I used Github to host my repositories.
- I used Git for version control of my website.
- I used Heroku to deploy the website.

## Testing 

- .  

### Validator Testing 

## Deployment

The app was deployed to Heroku. There are four stages:
     Create the Heroku app,
     Attach the database,
     Prepare our environment and settings.py file,
     Get our static and media files stored on Cloudinary.

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
                            
                            from pathlib import Path
                            import os
                            import dj_database_url

                            if os.path.isfile("env.py"):
                              import env
      - Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku - SECRET_KEY = os.environ.get('SECRET_KEY')
      - Comment out the old DataBases Section - 

                                                  # DATABASES = {
                                                  #     'default': {
                                                  #         'ENGINE': 'django.db.backends.sqlite3',
                                                  #         'NAME': BASE_DIR / 'db.sqlite3',
                                                  #     }
                                                  # }
      - Add new DATABASES Section ( - links to the DATATBASE_URL variable on Heroku) - 

              DATABASES = {
                  'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
              }
    - In the Terminal:
      - Save all files and Make Migrations - python3 manage.py migrate
  
  - Get our static and media files stored on Cloudinary:
    - In Cloudinary.com:
      - Copy your CLOUDINARY_URL e.g. API Environment Variable - From Cloudinary Dashboard
    - In env.py:
     - Add Cloudinary URL to env.py - be sure to paste in the correct section of the link - os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
    - In Heroku:
      - Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment - e.g. DISABLE_COLLECTSTATIC, 1
    - In settings.py:
      - Add Cloudinary Libraries to installed apps - 
                                                    
                                                    INSTALLED_APPS = [
                                                                        …,
                                                                        'cloudinary_storage',
                                                                        'django.contrib.staticfiles',
                                                                        'cloudinary',
                                                                        …,
                                                    ]

                                                    (note: order is important)
      - Tell Django to use Cloudinary to store media and static files (Place under the Static files) - 

              STATIC_URL = '/static/'

              STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
              STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
              STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

              MEDIA_URL = '/media/'
              DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
      - Link file to the templates directory in Heroku (Place under the BASE_DIR line) - 

                                  TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
      - Change the templates directory to TEMPLATES_DIR (Place within the TEMPLATES array) - 

              TEMPLATES = [
                {
                  …,
                  'DIRS': [TEMPLATES_DIR],
                  …,
                    ],
                  },
                },
              ]
      - Add Heroku Hostname to ALLOWED_HOSTS - ALLOWED_HOSTS = ['marblog.herokuapp.com', 'localhost']
    - In Gitpod:
      - Create 3 new folders on top level directory - media, static, templates
      - Create procfile on the top level directory - Procfile
    - In Procfile:
      - Add code - web: gunicorn marblog.wsgi
    - Note: Save all files
    -  In the Terminal:
      - Add, Commit and Push - 

                                git add .
                                git commit -m "Deployment Commit"
                                git push
    - In Heroku:
      - Deploy Content manually through heroku.


The live link can be found here - https:///

### Local Deployment

To make a local copy of this project, you can clone it by typing the following in your IDE terminal:

- `git clone https://github.com/onabz/MAR_Blog.git`

Alternatively, if using Gitpod, you can click the green Gitpod button, or use [this link](https://gitpod.io/#https://github.com/onabz/MAR_Blog)

## Credits 
 
### Content 

- 

### Media

-

### Acknowledgements
- I would like to thank [Student Care](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecommerce/studentcare) for their regular check up on me to ensure that I was always on track to completing this project and to reassure me that they were always available if I needed any help.