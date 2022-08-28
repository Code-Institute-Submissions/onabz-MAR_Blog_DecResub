# Title
Intro paragraph
amiresponisive image
## UX (briefly explain your design)
### Colour Scheme (explain your colors, etc.... perhaps use coolors.co?)
### Typography (explain any fonts and icon libraries used, like font-awesome and google fonts)
### Wireframes (include screenshots of your wireframes)
## Features
### Existing Features
### Features Left to Implement
## Technologies Used (explain various tech used, such as HTML, CSS, Balsamiq, TinyPNG, Gitpod, GitHub, Git, etc.)
## Testing
### Browser Compatibility
### Code Validation
### Responsiveness
### Unfixed Bugs
## Deployment
### Local Deployment
## Credits
### Content
### Media
### Acknowledgements

# Mum Loves Representation
Mum Loves Representation is a blog by an African British Mum(Tomi) who wants her little girl to be able to play with a heirloom doll that represents her as she grows and plays imaginatively. She believes that all children should play with black dolls for the purpose of encouraging diversity. She feels that  brown dolls, black dolls, and ethnic dolls are often left upon the shelf, untouched and ignored while it is easy to get one's hands-on white dolls. She believes the situation is very tragic.

This blog features several Articles posted by Tomi that shed more light on this issue along with several other topics under the ethnicity topic.

![Responsive Mockup](documentation/testing/ami-responsive.png)

The Responsive Mockup image above shows how responsive the Mum Loves Representation is across various device screen sizes ranging from mobile devices to large monitor screens. The Mum Loves Representation is well layed out with a bold font style used across all pages. The buttons are very legible on all the screen sizes. 

## UX

### Colour Scheme Used
I chose to go with this Boostrap blog theme called Clean Blog. It features a modern design with a subtle splash of color. This makes the site very easy to read with large fonts that are well spaced out. I made use of specifically choosen background images to showcase the theme of the blog. 

### Typography

I chose to use the font called Roboto Condensed from Google fonts throughout the website because it is a bold and striking font that not only evokes seriousness and passion, but when used along side the bright colors on the site also creates a sense of playfulness.

### Wireframes

Below are sketched images of how I planned to layout the quiz game. The lines across indicate that background colors were used. The final design for the restart button is slightly different from the wireframe image because i decided to include the user score so added the restart button to the screen that shows the user score. I also added the home button below the restart button.

![Home Wireframe Image](documentation/wireframes/wireframe-homepage.jpg)
![Start button Wireframe Image](documentation/wireframes/wireframes-start-button.jpg)
![Question section Wireframe Image](documentation/wireframes/wireframes-questions-box.jpg)
![Restart button Wireframe Image](documentation/wireframes/wireframes-restart-button.jpg)


## Features 

### Existing Features

- __Play Button__

  - It is a large and bold button  with the word play written on it that screams click me !!!.
  - It has a hover effect applied on it to show user that something is about to happen when they run the mouse pointer over it. It also has a box shadow effect around it to further make it stand out.  

![Play Button](documentation/testing/play-button.png)

- __The home page__

  - The home page features a very bright purple background color with some text to tell the user what to do which is to press the play button.
 
![Home Page](documentation/testing/home-page.png)

- __The "Let'Go" button__

  - The home page also features button which is placed underneath the mantra to draw the attention of the user to click on it. 
  - It has a bold red background color with the text 'Join Us' to draw the users attention to click on it.
  - The button features a hoover effect in the form of a bacground color change from red to grey to show the user that an action is about to occur.
  - Once clicked on, it then takes the user to the contact page where they can register to become a member. 

![Let's Go Button](documentation/testing/lets-go-button.png)

- __The Question and Answer Box__

  - This box contains the questions written boldy in black over the white background. 
  -  It also houses the answers contained in bold buttons which changes color to green when the answer selected is correct and to red whenthe wrong answer is selected.

![Question Box](documentation/testing/question-box.png)
![Correct Answer](documentation/testing/correct-answer.png)
![Wrong Answer](documentation/testing/wrong-answer.png)

  __The Next Button__

  - The next button does not appear till after the first question has been answered.
  - The next button when selected reveals the next question. 
  - The next button is hiddened when the next question is displayed.

![Next Button](documentation/testing/next-button.png)

  __The User Score Screen__

  - This screen is made up of the user's score area, the restart button and the home button.
  - This screen appears after the user has answered a set of 10 questions. The user's score is calculated and displayed boldly in simple text.
  - The user can then choose to restart the game by clicking on the restart button or go back to the home page by clicking on the home button. 

![User Score Screen](documentation/testing/user-score-screen.png)

  __The Restart Button__

  - The restart button, when clicked, takes the user back to the start page with the "Let's Go" button after which another set of 10 questions is displayed again one by one for the user to answer.

![Restart Button](documentation/testing/restart-button.png)

- __The Home Button__

  - The home button, when clicked, takes the user back to the home page with the play button.

![Home Button](documentation/testing/home-button.png)

### Features Left to Implement

- A more interactive home page that lays out how to play the game and the features of the game.
- The ability to save your game with a user profile.
- A high score table showing top user scores. 

## Technologies Used

- I used HTML to design the two web pages.
- I used CSS to design the enitre website.
- I used Javascript to add fuctionality to the game enabling user interaction.
- I used Gitpod as my code editor to write all the codes used throughout the website.
- I used Github to host my repositories.
- I used Git for version control of my website.

## Testing 

- I confirmed that all buttons were functional.
- I tested that the home button links back to the home page.
- I have tested the site for responsiveness making sure that it looks easy to use across all standard screen sizes using the Google chrome development tool.
- I checked that random sets of questions were being generated each time the restart button was clicked.
I tested that the correct user scores were displayed at the end of the game.  

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https://onabz.github.io/Vehicle-Quiz-Game/) (index.html)
 
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https://onabz.github.io/Vehicle-Quiz-Game/game.html) (game.html)
 
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fonabz.github.io%2FVehicle-Quiz-Game%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

## Deployment

The site was deployed to GitHub pages. The steps to deploy are as follows:
    * In the [GitHub repository](https://github.com/onabz/Vehicle-Quiz-Game), navigate to the Settings tab.
    * From the Settings tab, scroll down until you see the 'Pages' button on the left.
    * From the Source section drop-down menu, select the `Main` branch.
    * Once the `Main` branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://onabz.github.io/Vehicle-Quiz-Game/

### Local Deployment

To make a local copy of this project, you can clone it by typing the following in your IDE terminal:

- `git clone https://github.com/onabz/Vehicle-Quiz-Game.git`

Alternatively, if using Gitpod, you can click the green Gitpod button, or use [this link](https://gitpod.io/#https://github.com/onabz/Vehicle-Quiz-Game)

## Credits 
 
### Content 

- The text on the About page was taken from [Total Fitness Gym](http://www.total-fitness-gym.com/gym.html)
- Steps on how to create the pricing plans tables on the membership page was taken from [How to create a Pricing Plans table](https://www.youtube.com/watch?v=jfh0ZJFhj2w)
- The lines of code I used to push the footer to the bottom of the page was taken from [Sticky Footer with CSS](https://www.youtube.com/watch?v=TaXql0h_wCA)
- The lines of code i used for the hoover effect on the navigation links on the nav bar was taken from [How to make a website using HTML & CSS](https://www.youtube.com/watch?v=oYRda7UtuhA&list=PLjwm_8O3suyP5kGKmwS_DM0Hs1j7fshi5)
- The lines of code I used to make the pricing plans on the membership page more responsive was taken from [CSS Responsive Card & Hover Effects with Flexbox](https://www.youtube.com/watch?v=qXRYMdvq_Dc)
- Instructions on creating the table on the classes page was taken from [Styling HTML tables with CSS](https://www.youtube.com/watch?v=biI9OFH6Nmg&t=125s)
- Instructions on how to create my gallery layout was taken from [Love Running](https://www.youtube.com/watch?v=puheUvHLbQg)
- Instructions on how to create the contact page was taken from [How to make a Contact Us Page using HTML and CSS](https://www.youtube.com/watch?v=orBQesFBkXg&t=167s)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- The font used throughout the site called Roboto Condensed was from Google fonts [Google Fonts](https://fonts.google.com/specimen/Roboto+Condensed?preview.text=muscle%20gains%20power%20lifitng&preview.text_type=custom&query=roboto+#standard-styles)

### Media

- The Muscle Gains logo was created using [Adobe Spark logo maker](https://spark.adobe.com/express-apps/logo-maker/)
- The favicon image was generated from [Favicon.io](https://favicon.io/favicon-converter/)
- The background image on the Home page was taken from [Pexels](https://www.pexels.com/photo/man-lifting-barbel-17840/)
- The background image on the About page was taken from [Pexels](https://www.pexels.com/photo/barbell-on-the-floor-1552252/)
- The background image on the Membership page was taken from [Pexels](https://www.pexels.com/photo/man-and-woman-holding-battle-ropes-1552242/)
- The background image on the Classes page was taken from [Pexels](https://www.pexels.com/photo/man-kicking-heavy-bag-260447/)
- The background image on the Contact page was taken from [Pexels]()
- The gallery_1 image was taken from [Pexels](https://www.pexels.com/photo/woman-doing-yoga-917653/)
- The gallery_2 image was taken from [Pexels](https://www.pexels.com/photo/woman-holding-exercise-ropes-28080/)
- The gallery_3 image was taken from [Pexels](https://www.pexels.com/photo/women-having-exercise-using-dumbbells-903171/)
- The gallery_4 image was taken from [Pexels](https://www.pexels.com/photo/athlete-barbell-bodybuilder-bodybuilding-416717/)
- The gallery_5 image was taken from [Pexels](https://www.pexels.com/photo/woman-in-black-sleeveless-crop-top-and-white-leggings-using-a-butterfly-machine-in-front-of-a-mirror-1111304/)
- The gallery_6 image was taken from [Pexels](https://www.pexels.com/photo/woman-pushing-barbel-using-her-feet-136404/)
- The gallery_7 image was taken from [Pexels](https://www.pexels.com/photo/woman-lifting-barbell-371049/)
- The gallery_8 image was taken from [Pexels](https://www.pexels.com/photo/woman-lifting-barbell-1552249/)

### Acknowledgements

- I would like to thank my Mentor Tim Nelson for his invaluable support all through this project. I would not have been able to put all this together if not for his patience and insight.
- I would like to thank [Student Care](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecommerce/studentcare) for their regular check up on me to ensure that I was always on track to completing this project and to reassure me that they were always available if I needed any help.