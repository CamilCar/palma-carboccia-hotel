
# Welcome to the Palma Carboccia hotel! 

This website is for everyone that is tired of the dark, cold winter months, and want to book a hotel stay at this warm, tropical island. 


## Features
---------------------
### Existing Features
- Home page 
    - As you visit the landing page, it's immediately clear that this is a hotel website. 
    - There is a inviting image with clear purpose, that sets the location of this island somewhere tropical. Perfect for users who wants to travel somewhere warm.
    - A small welcome message with "less is more" design. 
    - At the top is the navigation bar, where the user can find more information about this hotel, and a functioning booking system. More on this later.
    - User can click on the **logo** anywhere on the site, to be sent back to home page.
    - The simple footer at the bottom marks the end of the section to the user. There are links to social platforms for future customer interaction!
    - The USP of this site is the beautiful location and accommodations, which is shown with a new image for every section.

![Home image](/media/landing.1.jpg)


- The hotel 
    - We move on to the section that covers the history of this hotel. 
    - It gives the user a quick idea of what the hotel is, what it offers and what activities can be found nearby.
    - The layout of this page is used across most pages, a stylish box that gives a good contrast between colorful images and text sections.
    

![The hotel image](/media/the.hotel.jpg) 


- The rest of the sections
    - The hotel, our rooms, food & drink and prices all share the same layout for a calm, structured design
    - **Our Rooms** provides user a image slider. For many hotel guests, it's crucial to see what their potential room look like, in their decision to make a reservation.
    Here we offer a small insight of what standard the user can expect.
    - **Food & Drink** provides user with a small extraction of the menu and pricing. It combines elegant and sturdy fonts, for easy readability and nice design.
    - **Prices** is straight forward, short description of what is included in the reservation, some activities on the island, and pricing. 
    - **Book Now** if user is not signed in, they first get prompted to do so. If user is signed in, they can make a booking.
    - **Sign in/Signed In** feedback to user what their current signin state is.
- Book Now
    - This section is only accessable for users that are signed in. 
    - User selects check-in day and check-out day from the dropdown calendar.
    - **Adults** is by default set to 1, as of course, atleast one person is expected after a reservation. As most, 3 adults can book for the same room. If user manuallt types in 0 , the form is not valid.
    - **Kids** is set to default 0, and as most 3. If user tries to book for more, form is not valid and user cannot proceed. 

![Booking](/media/booking.1.jpg) 

- Reservation summary
    - This page is for the user to view their reservation.
    - Startdate, end date, adults and kids can not be changed here. 
    - Price is calculated and displayed to user, but can not be changed. 
    - This form will ask user to input first and last name. Fields can not be empty before continuing. 
    - When user proceeds, they get a confirmation page with two options. **Back to home** or **My reservations**

![Summary](/media/booking.conf.jpg) 

- My reservations
    - Simple but functioning page for user to view, edit and delete their reservations. 
    - **Delete** deletes the post
    - **Edit** sends user to edit reservation page. 
    - As seen below, user can edit all of the input fields. Price will be re-calculated and displayed to user once confirm is clicked, and user is sent back to my reservations page. 

![Edit reservation](/media/edit.res.jpg) 

- Features left to implement
    - As I set to 'won't have' in my user story section, I would like to implement a point-system for returning customers.
    - Just 1 calendar for user to select from for both dates, and that its already visible as they land on the page. For now, they will have to select the input box to get the calendar showing.
    - The footer needs more content, like contact information and adress.
    - A newsletter section.
    - A Instagram feed, where our most recent posts to instagram is shown as a 4-picture gallery. 

 ## Planning the project 
 ---------------------  
- I used the design-tool **Pencil** for project mockup, on each section. My knowledge of the Pencil tool was limited, I had some problems finding the design patterns that I had in my mind. For example, I had planned for a hero image on each section, but could not create it in the program. But it was better than me trying to draw it by hand, and the end result is still similar to my concept design, with only small design changes for improved end result. 
- Each section got a concept design, but since I used the same layout for all pages I only display two here.
- **Landing page** The welcome message was moved due to landing image being too clustered, so to improve user readability, it was moved below the landing image.

![Home concept](/media/landingpage.jpg)
![Price concept](/media/prices.jpg)


- This is **planned design** with features left to implement. This is the Instagram feed and newsletter section that would be shown on the homepage section, between the welcome message and footer. *The 'if there is time' was me planning MVP, and would not be included in the live site*

![Won't have design](/media/landingpage2.jpg) 

- No more bright white images. This section will cover the agile tools. 
    - I used Git Hub project section for my user stories. I created 3 epics and from that created user stories. 
    - My agile project is called Hotel Page User Stories and is set to Public Visibility. 
    - To the far left is my Epics.
    - I used user stories to create Must Have's, Should have's and Won't have. I focused on the must have first, and got most of my Should have done as well.
    - My must have list had several tasks might be seen as a 'Should have', but I felt they were needed to create important context for site and user.
![User story1](/media/rmUstory1.jpg) 
![User story2](/media/rmUstory2.jpg) 

   ## Technology used 
    ------------

- Django
- ElephantSql
- Allauth
- Jquery
- Heroku
- Bootstrap
- Fontawesome

## Database model

![Database model](/media/datamodel.jpg) 

## Testing 
--------------------
- I have done no automated tests as I ran into a technical problem late in my time schedule. Image below. I had no time left to investigate this further.
![Home concept](/media/failautotests.jpg)
- I have done manual testing for all pages
    - Tested that this page works on following browsers: Chrome, Microsoft Edge
    - Tested that the site is responsive and looks good on all devices by using the devtool. The collapsed navigation is hard to see on most sections due to its dark color. 
    - If the hero image fails to load, user can still navigate the page and view its content.
    - Tested the booking section :
        - If user manually tries to change the price in devtools to f.x 0, it ignores that the next time the page renders, and the user still have to pay for the visit.
        - If user puts a check-in day later than check-out date, it throws the user an error with a clear message. This was to prevent price going in to minus. 
        - Tested so that the user can not change the price in the booking page 2, just before confirm. 
        - Tested all buttons and that they redirect to the right page. 

### Bugs

- Solved bugs: 
    - When user first selected dates, they could insert a later arrival day than departure, resulting in negative total price. 
    - User could open devtools and change the total price to f.x 0. 

- Remaining bugs: 
    - When user selects to edit a reservation, they can select a later arrival day than departure. Need to implement the same restriction function that is prohibiting this in the initial booking page.
    - If user signs up with email, they get an error. I can not find the option for this anywhere, it could be core of allauth. 

### Validator Testing
- PEP8, no significant errors were returned. Many of my lines are too long however. I tried to look for the way to indent it correctly, but ended up breaking my code instead.
- HTML 
    - **W3C validator** found 3 errors and 1 warning. I suspect its combination of django and Bootstrap that causes this, I found no solution in the time I had.
- CSS 
    - **(Jigsaw) validator** found 1000+ errors if I validated through URL. After a small heart attack caused by Bootstrap, I validated my CSS file with *Direct Imput* and got no errors or warnings.
- Accessibillity 
    - I have tested in incognito mode how the fonts and colors are visible and this is the result. Im not sure if the performance is low because I used cloudinary.
![Lighthouse test](/media/lighthouse.jpg)

## Deployment
---------------
- The site was deployed through these steps:
    - Install required libraries
    - Setup the env.py file with the sensitive information
    - Saving and pushing to GitHub
    - Create new app on Heroku and setup config vars in settings tab
    - Create new project on ElephantSQL
    - Connect database to repo and Heroku
    - Under the deploy tab at heroku, connected file by clicking on the GitHub icon. Then 'Deploy Branch'

- Link to the site is found here - https://palma-carboccia-hotel.herokuapp.com/

## Credits
--------------
### Content
- Compressing the images was made on https://tinypng.com/
- Image host is https://cloudinary.com/
- The base code for the food menu was found here https://codepen.io/ViszkY/pen/zYqBGex 
- Favicon is from here https://pnghunter.com/png/palm-tree-4/ 
- All images on the page(except for logo and favicon) is from https://www.pexels.com/sv-se/, cc0.
- The hotel logo was created for me by a friend, for the purpose of this project.
- The database setup was a real challenge for me. Because the booking happens over multiple pages, some with readOnly combined with imputs, there was several obstacles. To solve these, I had help of Senior developer Joris Bomert, and this https://github.com/SteinOveHelset/puddle/blob/main/item/templates/item/detail.html fellow coder. 
The code to build the game class were taken from Code Institute's Love Sandwiches project. 
- Also a big thanks to StackOverflow , hosting pretty much every answer and question there is about code not behaving. 