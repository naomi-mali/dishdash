# Dish Dash

## Overview

Dish Dash is a full-stack web application designed to provide a dynamic platform for food enthusiasts to explore, share, and enjoy a wide variety of recipes. Whether you're an experienced chef or a curious home cook, Dish Dash offers a vibrant community and a wealth of resources to enhance your culinary journey.

### Purpose
Dish Dash aims to deliver a simple, intuitive, and visually appealing platform where users can:

Discover Recipes: Explore a diverse collection of recipes shared by food lovers from around the globe.
Share Recipes: Submit your own recipes and connect with others through a user-friendly interface.
Engage with the Community: Interact with fellow users via comments and discussions, enhancing the overall cooking experience.
## Target Audience
Dish Dash caters to a broad audience interested in cooking and exploring world cuisines, spanning from young adults to older generations. The platform is designed to be accessible and engaging for anyone passionate about food and culinary creativity.

## Features
#### 1. Recipe Discovery and Sharing
Extensive Recipe Collection: Browse through a wide range of recipes, from quick meals to gourmet dishes. Each recipe includes detailed instructions, nutritional information, and high-quality images.
Recipe Submission: Share your own culinary creations with the community, providing comprehensive details and instructions.
#### 2. Community Interaction
Comments: Engage with other users by commenting on recipes and participating in discussions.
Search Functionality: Find recipes based on ingredients, cuisine, or other criteria.
#### 3. Personalized Experience
Account Management: Create an account to save favorite recipes, track cooking history, and receive personalized recommendations.
User Authentication: Full CRUD (Create, Read, Update, Delete) functionality for managing recipes.
#### 4. Admin Dashboard
Comment Moderation: Review and approve user comments.
Recipe Management: Monitor and edit recipes to ensure quality and relevance.
#### 5. User-Friendly Interface
Responsive Design: Enjoy a seamless experience across all devices with an intuitive and clean design.

### Technologies
Frontend: HTML, CSS, JavaScript
Backend: Python, Django
Database: Relational Database Management System
Getting Started
Prerequisites

### Web Browser: Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge.
Internet Connection: Required for accessing recipes, submitting content, and interacting with the community.

![Screenshot 2024-08-14 165033](https://github.com/user-attachments/assets/cc8d0fbc-58d1-4d45-93f2-ff0b9c3d60bf)

### [Link to Live Website](https://dishdashblog-15d6c6b4ee4f.herokuapp.com/)

# Table of Contents






# User Experience Design


### Site Goals
### The Strategy Plane

#### 1. Provide an Engaging Platform for Recipe Discovery

Objective: To create an intuitive and enjoyable experience for users seeking new recipes.
Approach: Ensure a clean, visually appealing interface with easy navigation, robust search functionality, and well-organized recipe categories.

#### 2. Facilitate Recipe Sharing and Community Interaction

Objective: To allow users to contribute their own recipes and engage with others.
Approach: Implement user-friendly submission forms, enable comments, and foster a sense of community through interactive features.

#### 3. Enhance User Experience with Personalization

Objective: To tailor the experience to individual preferences and enhance user satisfaction.
Approach: Provide features for users to save favorite recipes, track their cooking history, and receive personalized recipe recommendations based on their activity and preferences.

#### 4. Ensure Efficient Content Management and Moderation

Objective: To maintain the quality and relevance of content on the site.
Approach: Develop an admin dashboard for reviewing user-generated content, managing recipes, and moderating interactions to ensure compliance with community guidelines.

#### 5. Support Seamless User Authentication and Account Management

Objective: To provide a secure and personalized experience through user accounts.
Approach: Implement secure login and registration processes, account management features, and robust CRUD functionality for managing user content.

#### 6. Promote Accessibility and Inclusivity

Objective: To make the site accessible to users with varying abilities and preferences.
Approach: Follow best practices for accessibility, such as providing text alternatives for images, ensuring color contrast, and enabling keyboard navigation.

#### 7. Optimize for Mobile and Cross-Device Usability

Objective: To ensure a consistent and user-friendly experience across different devices.
Approach: Utilize responsive design principles to adapt the site layout and functionality for mobile devices, tablets, and desktops.

#### 8. Encourage Continuous Engagement and Retention

Objective: To keep users coming back to the site and increase overall engagement.
Approach: Regularly update content with new recipes, articles, and features. Implement notifications or newsletters to keep users informed and engaged.

#### 9. Foster a Positive and Supportive Community Environment

Objective: To create a welcoming space where users feel valued and supported.
Approach: Develop features that encourage positive interactions, provide clear guidelines for community behavior, and offer support for users who need assistance.

#### 10. Measure and Improve Site Performance

Objective: To continuously enhance the user experience based on feedback and data.
Approach: Implement analytics tools to track user behavior, gather feedback through surveys or user testing, and make iterative improvements to the site based on data insights.

### Agile Methodology and Project Management

#### 1. Agile Methodology

Approach: Employed Agile methodology to iteratively develop the Dish Dash application. This approach allowed for flexibility, continuous feedback, and regular updates throughout the development process.

#### 2. GitHub Project Board

Tool: Utilized GitHub Project Board to organize and manage user stories, track progress, and ensure timely delivery of features.
Link: Detailed Project Board with all user stories can be found here: [PROJECT BOARD-link](https://github.com/users/naomi-mali/projects/10)

#### 3. User Story Template

Structure: Each user story was outlined with a clear template, including:
Acceptance Criteria: Specific conditions that must be met for the user story to be considered complete.
Labels (MoSCoW Prioritization): Features were prioritized as 'must have', 'should have', 'could have', and 'nice to have'. Focus was placed on 'should haves' or 'could haves' if time allowed, ensuring the MVP (Minimum Viable Product) was completed within the available timeframe.

#### 4. Milestones and Prioritization

Milestones: Features were assigned to 7 distinct milestones to ensure incremental development and systematic progress.
Review: Each user story was reviewed against the acceptance criteria to confirm completion before being closed.


![Screenshot 2024-08-14 181218](https://github.com/user-attachments/assets/d30307ae-0810-4179-92af-ed32ac9f6230)


![Screenshot 2024-08-14 180846](https://github.com/user-attachments/assets/cf778938-9c39-457b-ae0e-0ac6974db8d5)



## The Structure Plane
### Features
### Existing Features

As a developer, I need to create a home page so that the user can quickly understand what the recipe blog offers and navigate easily to find interesting recipes.**(User Story#18)**
As a developer, I need to add static files and media so that I can build the website to be user friendly, interesting and responsive to all screen sizes.**(User Story#32)**

### Navigation bar for all users (desktop/mobile)

![Screenshot 2024-08-14 181731](https://github.com/user-attachments/assets/093ff6ff-e746-463f-8f2d-a1fa293f0694)

![Screenshot 2024-08-14 185720](https://github.com/user-attachments/assets/7443abb1-b8dd-4016-802f-5207b11db6c7)

The navigation bar is shown on all pages based on the users logged-in(authentication) status and is responsive to all screen sizes. For smaller screen sizes the navigation bar appears as a hamburger menu and can be easily accessed. A success message is displayed when user is logged-in/ registered.
The design is kept clean and simple so that user can navigate between the pages easily without any confusion. The links are visible clearly both on large screen and smaller screen sizes.
The active link is marked for ease of accessibility so that the user knows the current page been visited.
The navigation menu includes:
-Home Page - for all users
-Recipes Page - for all users
-Search Recipes Page - for all users
-Sign up Page - for unauthorised user's registration
-Sign in Page - for users already registered
-Logout Page - for authorised users
-Add Recipe Page - for authorised users
-My Drafts Page - for authorised users

## Home Page

As a developer, I need to create a home page so that the user can quickly understand what the recipe blog offers and navigate easily to find interesting recipes. **(User Story#39)**

## Home Page for all users

![Screenshot 2024-08-14 182007](https://github.com/user-attachments/assets/41c06ee4-9ee7-4774-92d6-c5833171cb11)
![Screenshot 2024-08-14 183847](https://github.com/user-attachments/assets/494a1915-d6aa-41bf-aa45-c233d2e5257b)

The home page is designed such that it is inviting and conveys the user a clear message about the website and what the user can expect throughout the site journey. The background image showcases the essence of the recipe website. User is encouraged to sign up and explore through a quick, simple introduction about the recipe application.

### Footer
As a developer, I need to create a footer so that I can include social media links, contact links and relevant site information about the website. **(User Story#40)**

![Screenshot 2024-08-14 182103](https://github.com/user-attachments/assets/d7e7c7dd-1bc8-477b-a062-153b98ace98c)

The footer section includes the information about the website: the developer of the website, the purpose (for educational purpose only), year developed and the developer's GitHub and LinkedIn links.
Similar to the navigation bar, the footer is displayed on every page of the website. It displays icon links to GitHub and LinkedIn accounts. These icon links can enable user to see more about my work through GitHub and learn more about me through LinkedIn. Both the links opens in new page

### Sign-Up / Sign-In / Logout Pages

As a Visitor I can Register an account so that Access personalized features.**(User Story#1)**

As a Registered user I can Log in so that Access profile and posts.**(User Story#2)**

As a Logged-in user I can Log out of their account so that Secure their account.**(User Story#25)**

![Screenshot 2024-08-14 182214](https://github.com/user-attachments/assets/dbee027b-4cef-4268-b792-5267e05d863b)
![Screenshot 2024-08-14 182252](https://github.com/user-attachments/assets/9d730352-a2fc-4294-9ed8-bd81b3a0f633)
![Screenshot 2024-08-14 182318](https://github.com/user-attachments/assets/6263f675-c9f9-4a44-a6e8-0fc867891db3)

All the pages are accessible from navigation bar for large and small screen sizes.
User can easily access the sign-up / sign-in options to explore the website features completely.
A clear message is displayed on the pages for user to know whether he needs to sign-in or sign-up to explore the recipe website and to like, comment and post the recipes.
A success message is displayed to user based on his actions for sign-in, sign-up and sign-out.

### Add Recipe Page

As a Admin I can Create and manage an add recipes page for users so that Enable users to contribute their own recipes.**(User Story#21)**

![Screenshot 2024-08-14 182411](https://github.com/user-attachments/assets/ac1b9c43-47a6-4636-a54f-e76189a24fe4)

## CRUD Functionality 
### For recipes 
 The Add Recipe page link is only visible and accessible to logged-in users. On clicking the Add Recipe link, authorised users are directed to the create recipe form. The form field marked as * are mandatory to be filled. If user tries to submit the form without entering all required field, messages are displayed below relevant fields that are left empty.
A default image is incorporated so that if the user is unable to provide any recipe image, the default image will act as one.
All the fields in the form except the Recipe Image field are required. The form is not deemed to be valid in case any of the fields are left empty. User can either publish or save recipe as draft.
Users can share their recipes with others using the add recipe form. On submitting the recipe, user is displayed with a success message and directed to the Recipes page.

### Edit Recipe

As a Logged-in user I can Edit my blog post so that Update or correct information.**(User Story#6)**

![Screenshot 2024-08-14 182609](https://github.com/user-attachments/assets/822369ef-a269-47b8-8382-78d71eb3a565)

![Screenshot 2024-08-14 182655](https://github.com/user-attachments/assets/b6b3a08e-5ffb-4ab9-9611-e2a53912a3e4)

![Screenshot 2024-08-14 182710](https://github.com/user-attachments/assets/3bfd67c4-1694-49ae-8bcf-56ce1d88ab8e)

CRUD Functionality - the feature of edit in recipe details page is only visible and accessible to the logged-in users and only if the user is the author of the recipe.
On clicking the edit button user is directed to the Edit recipe form/page where user can update / edit recipe for any changes and can either save as draft or publish it. On successful update of the recipe, user is displayed with success message and directed to Recipes Page.
If anauthorised user accesses the link the 403 error page will be displayed.

### Delete 

As a logged-in User, I can delete my recipes so that they are no longer published on the site. **(User Story#7)**


![Screenshot 2024-08-14 182801](https://github.com/user-attachments/assets/2ef52dcc-9c09-4897-b925-30cfba27dbab)

![Screenshot 2024-08-14 182837](https://github.com/user-attachments/assets/c41c3e04-5395-4ec2-a6f6-10c923da1768)

CRUD Functionality - the feature of delete in recipe details page is only visible and accessible to the logged-in users and only if the user is the author of the recipe.
User is directed to confirm delete page where user can either delete the recipe or cancel.
The recipe is permanently deleted if delete is confirmed and a success message is diplayed to user else user will be taken back to recipe details page if cancelled.
If anauthorised user accesses the link the 403 error page will be displayed.

### For comments

### Comments CRUD Functionality  

The application provides a complete Comments CRUD (Create, Read, Update, Delete) functionality, enabling users to manage comments effectively. Below is a detailed breakdown:  

#### 1. **Create**  
- Logged-in users can add new comments to posts.  
- A comment form is provided under each post for easy interaction.  
- Once submitted, the comment is displayed immediately in the post's comment section.  

#### 2. **Read**  
- All users can view comments associated with a post.  
- Comments are displayed in chronological order, enhancing readability and context.  
- Each comment includes information such as the author's username and the time it was posted.  

#### 3. **Update**  
- Logged-in users can edit their own comments to correct or update information.  
- An "Edit" option is available next to each comment for authorized users.  
- Edited comments are updated instantly, reflecting changes in the comment section.  

#### 4. **Delete**  
- Logged-in users can delete their own comments if they no longer want them displayed.  
- A "Delete" option is available next to each comment for authorized users.  
- Deleted comments are permanently removed from the comment section, ensuring a clean interface.  


![comments](https://github.com/user-attachments/assets/8bf3b3b0-39e5-4e7e-a606-7113a7a2f0e3)
![comments1](https://github.com/user-attachments/assets/f59b0e9a-441c-4f32-805c-95518c796b4f)
![comments2](https://github.com/user-attachments/assets/a68fd1c9-3206-46f0-a73f-bedabaa1ddec)
![edit](https://github.com/user-attachments/assets/9e7571c4-265a-4432-b4bc-414bfd0470a8)
![edit2](https://github.com/user-attachments/assets/0579524b-474b-4503-84c3-176b529c524c)



### Recipe Details

As a Visitor or registered user I can View blog posts so that Read recipes and cooking tips.**(User Story#8)**

![Screenshot 2024-08-14 183640](https://github.com/user-attachments/assets/ce77a8a4-c719-4b5b-ab0b-c13940cfe3b4)

![Screenshot 2024-08-14 183730](https://github.com/user-attachments/assets/0ec34599-6cf5-49bf-b9a0-ac18123a8387)

![Screenshot 2024-08-14 184834](https://github.com/user-attachments/assets/6c90117a-4f3e-4c61-abe2-b98e8688a561)


### Recipe Details View for Logged-in Users

![Screenshot 2024-08-14 195040](https://github.com/user-attachments/assets/3abe69c5-eeea-442c-af2e-d5b4b817f39e)

### Recipe Details View for Logged-in User and author of the recipe

![Screenshot 2024-08-14 183751](https://github.com/user-attachments/assets/df54c900-9614-4bfd-88fb-6b10855f5c64)

User can view a detailed recipe on this page along with number of comments, number of likes and the all recipe information.
The edit and delete buttons are visible and accessible only to the logged-in user as author of the recipe.
Logged-in users can explore the recipe details page completely for like / unlike and comments feature.
If user is not logged-in, information is displayed below recipe for sign-in along with the comments from other users in the comment section.

### Recipe Pagination

As a Site User, I can view a paginated list of recipe posts so that I can select which recipes I want to view.**(User Story#34)**

![Screenshot 2024-08-14 183847](https://github.com/user-attachments/assets/1eac9af8-dbfd-449b-b461-53aaaeb9ff8f)

![Screenshot 2024-08-14 183847](https://github.com/user-attachments/assets/1eac9af8-dbfd-449b-b461-53aaaeb9ff8f)

![Screenshot 2024-08-14 195605](https://github.com/user-attachments/assets/c4400c11-a78d-42c0-a0a5-c40d218e99a6)

This feature allows recipes to be paginated by 6 recipes per page, given more than 2 pages the next and prev buttons appear adjacent to each other.
The recipe list page is kept simple so that it is not overcrowded and user can find it easy to navigate between the pages.
On clicking the View Recipe button user is taken to recipe details page to view complete recipe information.

### My Drafts Page

As a Logged-in user I can Save a recipe as a draft before publishing so that Work on recipes over multiple sessions.**(User Story#29)**

As a logged-in User, I can go to a page to view only my recipes so that I can easily access them if needed. (User Story#13) (should have)

Note: Theis is only partially complete. User can only view the recipes saved as draft in my drafts page for now. User can update the draft recipe from my drafts page to either publish or save it for later.

This page is only accessible and visible to logged-in users.

![Screenshot 2024-08-14 184527](https://github.com/user-attachments/assets/f490ad1d-3445-4a75-830d-1fc0e10d502d)

The paginated list of recipe drafts is displayed with 9 recipes per page (if present). With this feature user can create recipe and save for later as draft for changes or to publish later.

User can also make his published recipes draft for any changes. This feature allows a flexibility for user to share recipes and manage them.

### Search Recipes Page

As a Admin I can Create and manage a search page for recipes so that Allow users to find specific recipes easily.**(User Story#20)**
As a Visitor or registered user I can Search for blog posts by keywords so that Find specific recipes or topics.**(User Story#12)**


![Screenshot 2024-08-14 184551](https://github.com/user-attachments/assets/d43b32d3-95da-441c-8c58-7029865dfa45)

![Screenshot 2024-08-14 184624](https://github.com/user-attachments/assets/bb05f253-60a5-4ddb-909f-0ad64cd13fae)

![Screenshot 2024-08-14 184751](https://github.com/user-attachments/assets/68e130f1-1770-436a-9ef2-70160ba0f31b)

![Screenshot 2024-08-14 200626](https://github.com/user-attachments/assets/f817fb30-6daf-4efa-8803-c48f2a231043)

The search recipes page allows users to search recipes by title, keyword and cuisines. This page is accessible throughout the website and to all users.
If the user search results are not found, a message for refining search is provided. Also user is encouraged to share own recipes or view all recipes.
If search query is not provided by user, the page is loaded with message to search bu recipe title, keyword and cuisines.

### Comment Section

As a Logged-in user I can Add comments to blog posts so that Engage with content and other users.**(User Story#9)**

### Comments Section for unauthorised Users
![Screenshot 2024-08-14 184834](https://github.com/user-attachments/assets/931dfd59-e482-48ea-94f1-1b6cf451445d)

### Comments Section for authorised Users

![Screenshot 2024-08-14 184937](https://github.com/user-attachments/assets/bf270fe1-3dbb-4d00-a5b2-d4e3452bc950)

![Screenshot 2024-08-14 185110](https://github.com/user-attachments/assets/dcd2e759-f830-49d0-9356-248ddbc7385e)

This feature allows user to comment on recipes posted by others.
If the user is not logged-in, user will only be displayed with the comments made by others on the recipes and a message to login to comment and like the recipe with sign-in link. When user is logged-in with the link, he is taken back to same recipe to add comment.
Authorised users are displayed with the comment box to comment on the recipe, upon comment submission a success message is displayed with a comment awaiting approval information.
The comments from other users on the recipe and total number of comments on the recipe is visible to all users regardless of their login status.
If recipe has no comments, then a short messsage 'No comments yet' will be displayed.
You can add the following description to your `README.md` to explain that comments can be deleted and edited, as well as the CRUD functionality:

---

### Comment Management

The application allows users to manage comments with full CRUD (Create, Read, Update, Delete) functionality. 

- **Create**: Users can add new comments to posts.
- **Read**: Users can view existing comments on posts.
- **Update**: Users can edit their own comments.
- **Delete**: Users can delete their own comments.


![comments](https://github.com/user-attachments/assets/8bf3b3b0-39e5-4e7e-a606-7113a7a2f0e3)
![comments1](https://github.com/user-attachments/assets/f59b0e9a-441c-4f32-805c-95518c796b4f)
![comments2](https://github.com/user-attachments/assets/a68fd1c9-3206-46f0-a73f-bedabaa1ddec)
![edit](https://github.com/user-attachments/assets/9e7571c4-265a-4432-b4bc-414bfd0470a8)
![edit2](https://github.com/user-attachments/assets/0579524b-474b-4503-84c3-176b529c524c)



### Like / Unlike Recipes

As a Logged-in user I can Like blog posts so that Show appreciation for content.**(User Story#13)**

![Screenshot 2024-08-14 185056](https://github.com/user-attachments/assets/5747d023-3e53-4c70-8b55-7a46579bbef1)

![Screenshot 2024-08-14 201129](https://github.com/user-attachments/assets/a60a73e4-9f93-4cbe-8a12-980a220f4fba)

![Screenshot 2024-08-14 201345](https://github.com/user-attachments/assets/6e5da5fe-1311-4eb1-9366-c763f2fadc15)

The like / unlike feature allows logged-in user to like or unlike the recipes.
If unauthorised user clicks the hollow heart icon, no action / effect will be seen on the icon. A simple message is diplayed for user below the recipe details to know that they needs to be logged-in to comment or like the recipe.
Authorised user - likes the recipes (if didn't previously liked the recipe), hollow heart icon will be displayed - if clicked the icon will change to solid red color and the number of likes will increase by one.
Authorised user - unlikes the recipe (if previously liked the recipe) , the solid red heart icon will be shown - if clicked the icon will chnage to hollow ones and the number of likes will be decreased by one.

## Admin Functionality

As a Admin I can Manage comments so that Maintain a respectful and constructive community.**(User Story#16)**
As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments. **(User Story#26)** (must have)
As a Admin I can Approve posts before they go live so that I Ensure content quality.**(User Story#16)**

![Screenshot 2024-08-14 185153](https://github.com/user-attachments/assets/3843d5bd-78ba-41ee-adf2-1f6639151e89)

The most important task for website to function was to create a superuser, to manage the recipe post functionality and the website entirely.
The admin can ensure the quality and organization of the content on the webite.
When the comment is made by any user on the recipe, the comment awaiting approval message is displayed to user. The comment is only displayed if it approved by admin.
The admin panel helps the administrator to have control over the website to function seamlessely and keep the website content meaningful and organized.

### Initial Project Setup / Project Documentation / Final Project Deployment
All the user stories are completed for project setup, project documentation and final project deployment

As a developer, I need to set up the recipe blog project with all the necessary components and configurations so that I can ensure a smooth development and deployment process. **(User Story#37)** (must have)

-Initialize and setup a GitHub repository with a README file using CI Gitpod template.

-Install the latest version of Django.

-Create a new Django project.

-Add main app.

-Verify that the project runs without errors using the Django development server.

-Add a requirements.txt file listing all project dependencies.

-Add env.py file to store sensitive information.

-Add Procfile

-Implement a proper media storage configuration for user-uploaded images. - image database: Cloudinary.

-Configure the project to use a SQL database.

-Update the settings.py file to notify Django of the installed supporting libraries.

-Deploy project to Heroku to test deployment is successful.

As a developer, I need to create a base.html file so that I can have a basic structure of the page for the project. **(User Story#38)** 

As a developer, I need to add static files and media so that I can build the website to be user friendly, interesting and responsive to all screen sizes. **(User Story#32)**

### Features left to implement

### 1. Customizable User Profile Section

#### Profile Picture/Avatar:
- Allow users to upload a profile picture or choose an avatar.
- Implement cropping and resizing functionality to maintain uniformity.
#### Bio:
- Add a field for users to write a short bio.
- Implement character limit and optional formatting (bold, italics).
#### Interests:
- Provide options for users to select or add their interests (e.g., cuisine types, cooking techniques).
- Consider using tags or predefined categories.
####  Favorite Recipes:
- Add a section for users to add their favorite recipes.
- Enable the ability to mark a recipe as a favorite.

### 2. Author’s Recipe Page

- Clickable Author’s Name:
- Make the author’s name clickable on each recipe page.
#### Author’s Recipe List:
- Create a dedicated page that lists all the recipes published by the selected author.
- Add filters (e.g., by category, date) and sorting options.
#### Follow/Unfollow Author (Optional):
- Consider adding the ability for users to follow their favorite authors and get updates when new recipes 
 are published.
#### Backend Considerations:
- Create or update the API to fetch all recipes by a particular author.
- Optimize database queries to handle potentially large datasets.
#### Frontend Considerations:
- Design the author’s page to display the recipes in a visually appealing manner.
- Ensure seamless navigation between the main recipe pages and the author’s page.

### 3. Favorites Feature

#### Add to Favorites:
-Allow users to click a “heart” or “star” icon to add a recipe to their favorites.
#### Favorites Management:
- Create a dedicated section on the user’s profile to view and manage favorite recipes.
- Enable options to remove recipes from favorites.
- Notification (Optional):
- Notify users when a favorited recipe is updated or has new comments.
#### Backend Considerations:
- Update user models to include a list of favorite recipes.
- Create API endpoints for adding/removing recipes from favorites.
#### Frontend Considerations:
Implement the UI elements (like a heart icon) for adding/removing favorites.
Ensure that favorited recipes are easily accessible from the user’s profile.

## Design


This page features a welcoming and vibrant design with a strong focus on community and food. It has a hero section with a large background image and centered text, promoting the site's theme. The recipe listings are displayed in a responsive grid layout, each card featuring an image, title, and details, with pagination at the bottom for easy navigation. The overall design is clean, user-friendly, and visually appealing, encouraging users to explore recipes and engage with the content.

### Typography


Combining [Grenze Gotisch](https://fonts.google.com/specimen/Grenze+Gotisch) and [Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville) in the design of this page can create a sophisticated yet bold aesthetic. The pairing of these two fonts allows for a striking balance between modern elegance and historical flair, perfect for a website that wants to stand out while still being welcoming and readable.

### Images

 The images in this project are sourced from [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/) and [Pixabay](https://pixabay.com/). They were specifically selected to correlate with the main purpose of the website and to give user a imagery representation for the recipe content to increase impact of the design.

 ## Technologies

### Tools and Technologies
 
 - Gitpod - used to develop the website
- [GitHub](https://github.com/) to host the source code.
- HTML - used to create main static content of the website.
- Bootstrap - front end framework used.
- CSS- used for website styling
- JavaScript- used to create dynamic content and make page interactive
- Python - used as the main language to code the logic of the page
- Django - framework used
- Heroku - to deploy the app
- [FontAwesome](https://fontawesome.com/v5/search) v5.15.4 for website icons.
- [Favicon.io](https://favicon.io/) to create the website favicon.
- Google Chrome's Lighthouse to test accessibility for desktop and mobile devices.
- [W3C HTML Markup Validator](https://validator.w3.org/) to validate the HTML Code.
- [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to validate the CSS Code.
- [jshint validator](https://jshint.com/) - used to check java script code for errors.
- [Am I Responsive](http://amiresponsive.blogspot.com/) to create the Mockup image in this README.
- Code Institute's Gitpod Template to generate the workspace for the project.

#### Python Packages
- Summernote - used to provide an editor for user and admin for adding recipes instructions and ingredients.
- TemplateView, CreateView, ListView, DeleteView, UpdateView - used to allow CRUD functionality
- LoginRequiredMixin, UserPassesTestMixin - used to test and secure views from unauthorised access.
- messages - used to add action messages to user on submission
- HttpResponseRedirect, reverse : used to direct user to specific URL

#### External Packages

- django.contrib.admin: Provides Django's built-in admin interface, which allows for easy management of site content and user permissions.

- django.contrib.auth: Handles authentication, authorization, and user management (e.g., login, logout, user groups, and permissions).

- django.contrib.contenttypes: Provides support for generic relationships between models, allowing models to interact with each other in flexible ways.

- django.contrib.sessions: Manages session data, enabling the storage of user-specific data across requests (e.g., tracking logged-in users).

- django.contrib.messages: Provides a messaging framework that allows you to store and retrieve temporary messages, often used for user notifications.

- django.contrib.staticfiles: Manages static files (e.g., CSS, JavaScript, images), making it easier to serve these files in development and production.

- cloudinary_storage: Allows for the integration of Cloudinary as a storage backend, enabling the storage and management of media files (e.g., images, videos) on Cloudinary.

- django.contrib.sites: Provides support for associating models and settings with particular sites, useful for projects that run multiple sites from a single Django instance.

- allauth: A versatile app for handling authentication, registration, account management, and third-party (social) authentication.

- allauth.account: Handles user account management, including registration, login, email confirmation, password resets, and more.

- allauth.socialaccount: Manages authentication via social media accounts (e.g., Google, Facebook), allowing users to log in using their social media credentials.

- crispy_forms: Simplifies the creation and customization of forms in Django, making it easy to render Bootstrap-styled forms.

- crispy_bootstrap5: Provides specific integration with Bootstrap 5 for crispy_forms, enabling the use of Bootstrap 5's features in Django forms.

- django_summernote: Integrates the Summernote WYSIWYG editor with Django, allowing for rich text editing in forms and admin interfaces.

- cloudinary: Provides Cloudinary support for managing media files within Django, including uploading, transforming, and serving images and videos.

-bleach: Provides a whitelist-based HTML sanitizing library for cleaning and filtering user-generated content. It helps to prevent XSS attacks by ensuring only safe and allowed tags, attributes, and styles are retained in user input.

## Testing 

### Responsiveness

The site is designed to be flexible, fluid and responsive on all screen sizes. Website has been checked for responsiveness through Chrome Development tools. In order to do this, the following steps have been taken:

1. Open the browser.
2. Navigate to the Tasty Tales website (https://dishdashblog-15d6c6b4ee4f.herokuapp.com/)
3. Right click anywhere on the page and got to "Inspect" to open Development Tools.
4. Click on drop down menu: "Dimensions: Responsive" and choose "Responsive".
5. Drag the side of the screen and change screen size, making sure the website looks good from 320px and up. Here, ensure there is consistency in design of the website on every screen size from small(mobile devices) to larger(desktop devices) and no scorll bar is showing for layout of site.

Expected Result: Each page is responsive and user friendly when viewing the website on small and large screens.The pages have no design or accessibility issue in any of the screen sizes from 320px and up.

Actual Result: Website is responsive with no scroll bar showing, the content is accessible to user to read and the images are not appearing stretched. Website is user friendly on small to large screen sizes.

The following devices are used to check responsiveness:

- Iphone 12 Pro
- Samsung Galaxy S20 Ultra
- iPad Mini
- Surface Pro 7

The website was also tested further by sharing the live link with friends and family. The site was tested on following devices:

- Samsung S20 FE 5G
- Iphone 12
- iPad Air
- Samsung S24 Ultra
- Microsoft Surface
- Asus X5 50
- Lenovo Pad Pro 12.7

The following browsers have been used to check responsiveness.
- Chrome
- Safari
- Internet Explorer

### Lighthouse

### Home Page Desktop

### Home Page 

![test1](https://github.com/user-attachments/assets/7706ef23-7fae-414e-abab-fc9d958b035f)


### Recipes Details

![test668](https://github.com/user-attachments/assets/b82aa054-fd1f-4dc4-94c5-c88c22c6dba1)

### Search Recipes Page

![test2](https://github.com/user-attachments/assets/8c13b601-9d16-4d40-8d77-01c52f4293de)

### Sign Up Page

![test3](https://github.com/user-attachments/assets/ba9c7fb4-5080-43be-ba4c-7607a95b120a)

### Sign In Page 

![test4](https://github.com/user-attachments/assets/a5fc724f-47a9-487d-92e4-33bd980a5f8d)

### Log Out Page

![test77](https://github.com/user-attachments/assets/06ed7976-337b-4c1e-a8b3-fed5f99fec39)

### Add Recipe Page

![test5](https://github.com/user-attachments/assets/6144782b-493b-4869-850e-eb4a8589c4f9)

### Edit Recipe Page

![test6](https://github.com/user-attachments/assets/feaf1421-00c2-4ecd-a3e1-c1af3e37cbba)

### Delete Recipe Page


![test 7](https://github.com/user-attachments/assets/e53df3c7-9953-4de9-930a-680a0974ad64)

### My Drafts Page

![Screenshot 2024-12-03 201935](https://github.com/user-attachments/assets/b9f64b53-0ebf-4556-809d-312d801bb4ff)

### Delete comment 
 
 ![Screenshot 2024-12-03 202230](https://github.com/user-attachments/assets/d2150949-95eb-4697-9af2-9e8c98331b72)


## Validator Testing

### HTML Validation

All pages have been run through the [W3C VALIDATOR](https://validator.w3.org/).

In order to check HTML code in dynamic website:

- go to the live page

- click right and select 'Inspect' then click right and select 'View page source'

- code will open in new tab - copy the code

- paste the code in the validator as 'direct input'

### Home Page

![Screenshot 2024-08-15 084826](https://github.com/user-attachments/assets/e4fd0674-b29d-4e69-89df-2eaabac2d9e4)

### Search Recipes Page

![Screenshot 22222222](https://github.com/user-attachments/assets/9e2ecc66-945c-47ee-8eed-69ad4efbea33)

### Recipe Details Page

![Screenshot 3333333](https://github.com/user-attachments/assets/183e7684-013c-47ba-a8e9-b209056b80fe)

###  My Drafts Page

![Screenshot 4444444](https://github.com/user-attachments/assets/daea4feb-d80a-4d17-ad39-32b44a79fb3d)

### Sign In Page

![Screenshot 77777](https://github.com/user-attachments/assets/7d3ff7b2-a38d-4e2a-889f-b38145987b8a)

### Logout Page

![Screenshot 666666666-08-15 085940](https://github.com/user-attachments/assets/abff27a9-76f9-4f89-93b0-1e6bc5ffab97)

### Delete Recipe Page 

![Screenshot 9999999](https://github.com/user-attachments/assets/1b85754f-7ac9-4788-81ad-11f452aa2e61)

### Add Recipe Page | Update Recipe Page

![Screenshot 2888888888](https://github.com/user-attachments/assets/4dfd8aaf-d1a9-4737-9bea-b2da7c93f39f)

### Sign Up Page

![Screenshot5555555](https://github.com/user-attachments/assets/3d574904-a5b3-4e80-9f3a-0702b70848ac)

## CSS Validation

No errors were found when passing through the official Jigsaw W3 Validator

![Screenshot 2024-08-15 001052](https://github.com/user-attachments/assets/3c6b03dc-8c50-473c-a8ea-f3685e6364f6)

## Python Validation

No errors were found when passing each file through [CI Python Linter](https://pep8ci.herokuapp.com/)

Couple of warnings when running settings.py file. Too long lines of code. Modifying the file for resolving the warnings rendered errors during deployment. I have left the mentioned lines in settings.py file unchanged for warnings. All other python files have passed the validation with no errors.


![Screenshot 2024-08-15 001712](https://github.com/user-attachments/assets/4f72be90-02fb-461f-be3b-5f94b9adf15c)

![Screenshot 2024-08-15 001750](https://github.com/user-attachments/assets/3c51d96c-040b-4713-98f0-ed72d71ba7de)

![Screenshot 2024-08-15 002128](https://github.com/user-attachments/assets/7dd0a33b-eb82-41d2-a1c4-72011898ca90)

![Screenshot 2024-08-15 002432](https://github.com/user-attachments/assets/fb3fc072-1cd3-4970-a755-d6cf245b56e1)

![Screenshot 2024-08-15 002533](https://github.com/user-attachments/assets/6dffd0d4-5bfe-424f-966a-56db9387622f)

![Screenshot 2024-08-15 002858](https://github.com/user-attachments/assets/ab51fb1e-be13-4c57-9478-bcc3992583cf)

![Screenshot 2024-08-15 003025](https://github.com/user-attachments/assets/8728899d-ae5a-4326-b4e8-59837b8dc240)

![Screenshot 2024-08-15 003059](https://github.com/user-attachments/assets/8d17597b-bac5-4a6b-b8c0-7ed795e04774)

![Screenshot 2024-08-15 003135](https://github.com/user-attachments/assets/381e7dda-eb29-4cd9-b86d-b986d19a4841)


## Manual Testing

### Functional Testing

| **Feature**                                             | **User Action**                                                                                                                                                        | **System Response**                                                                                                                                                                                                                       | **Status**      |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| **Sign-Up Process**                                     | User clicks "Sign-Up" or "Sign up now", enters username, password, confirms password, optionally enters email, clicks "Sign-Up"                                       | User is redirected to the home page with a message "Successfully Signed up as 'USERNAME'" displayed at the top of the page.                                                                                                               | As expected     |
| **Sign-In Process**                                     | User clicks "Sign-In" from the nav bar or sign-up page, enters correct username and password, clicks "Sign-In"                                                         | User is redirected to the home page with a message "Successfully Signed in as 'Username'" displayed at the top of the page.                                                                                                               | As expected     |
| **Log-Out Process**                                     | User clicks "Log-Out" from nav bar, confirms sign-out by clicking "Sign-Out" on the sign-out page                                                                       | User is redirected to the home page with a message "You have signed out" displayed at the top of the page.                                                                                                                                 | As expected     |
| **Navigating to the Recipes Tab**                       | User clicks on the "Recipes" tab from the nav bar                                                                                                                       | User is directed to the `index.html` page, where a list of published recipes is available to view. Six recipes are shown per page, with pagination navigation available if more than six recipes exist.                                  | As expected     |
| **Pagination Navigation**                               | User clicks "Next" if on page 1, or "Previous" or "Next" if on any other page, within the `index.html`, `my_drafts.html`, or `recipe_search.html` pages             | User is directed to the relevant page, depending on whether they clicked "Next" or "Previous".                                                                                                                                            | As expected     |
| **Viewing a Recipe in Detail**                          | User hovers over "View Recipe" button, button changes color to dark blue on hover, clicks the button                                                                    | User is directed to the `recipe_detail.html` page, displaying the full details of the selected recipe.                                                                                                                                     | As expected     |
| **Like Functionality**                                  | 1. Logged-in user clicks on hollow heart icon 2. Logged-in user clicks on solid red heart icon 3. Unauthenticated user clicks on heart icon                           | 1. Icon changes to solid red, and like count increases by one. 2. Icon changes to hollow, and like count decreases by one. 3. Icon remains unchanged and like count does not change.                                                      | As expected     |
| **Logging in to Leave a Comment**                       | User clicks "Sign-In" on the `recipe_detail.html` page, enters correct username and password, then clicks "Sign-In"                                                     | User is redirected back to the same recipe detail page, sees a success message at the top, and upon scrolling to the comments section, sees a comment form instead of the sign-in option.                                                 | As expected     |
| **Leaving a Comment**                                   | Logged-in user enters a comment and clicks "Submit"                                                                                                                    | The user's comment appears in the comments section, in reverse chronological order (with the newest comments appearing first).                                                                                                           | As expected     |
| **My Drafts Tab**                                       | Logged-in user clicks on "My Drafts" tab from the nav bar                                                                                                              | User is directed to the `my_drafts.html` page, displaying a list of their own draft recipes. If the user has no drafts, a message indicates that no draft recipes are available.                                                          | As expected     |
| **Adding a Recipe**                                     | Logged-in user clicks "Add Recipe" tab from the nav bar, fills out the required fields on the form, optionally uploads an image, and clicks "Submit"                   | User is redirected to the `index.html` page with a success message displayed at the top. The recipe appears in the list if published, or on the `my_drafts.html` page if saved as a draft.                                              | As expected     |
| **Deleting a Recipe**                                   | User clicks "Delete" on their own recipe from the `recipe_detail.html` page, confirms by clicking "Yes, Delete Recipe", or cancels by clicking "Cancel"                | 1. User is redirected to `index.html` with a success message displayed at the top, and the recipe is deleted. 2. User is redirected back to the `recipe_detail.html` page, and the recipe remains published.                             | As expected     |
| **Editing a Recipe**                                    | User clicks "Edit" on their own recipe from the `recipe_detail.html` or `my_drafts.html` pages, modifies fields, and clicks "Submit"                                   | User is redirected to the `index.html` page with a success message if the recipe is published, or to the `my_drafts.html` page if saved as a draft. The updated recipe is displayed accordingly.                                         | As expected     |
| **Searching for Recipes**                               | User clicks "Search Recipes" tab from the nav bar                                                                                                                      | User is directed to the `recipe_search.html` page, where they can use a form to search for recipes.                                                                                                                                         | As expected     |
| **Adding a Recipe from the Search Page**                | User clicks "Add Your Recipe" link on the `recipe_search.html` page                                                                                                     | 1. Logged-in user is directed to the `add_recipe.html` page. 2. Unauthenticated user is redirected to the sign-in page and can proceed to sign in or sign up before being able to add a recipe.                                              | As expected     |

### Links and Buttons

| **Button / Anchor Link / Location**                                             | **Destination Page**                                        | **Page Opens In New Tab**    |
|---------------------------------------------------------------------------------|-------------------------------------------------------------|------------------------------|
| Dish Dash logo - nav bar                                                       | `index.html`                                                | no - as expected              |
| Home tab - nav bar                                                              | `index.html`                                                | no - as expected              |
| Recipes tab - nav bar                                                           | `index.html`                                              | no - as expected              |
| Search Recipes tab - nav bar                                                    | `recipe_search.html`                                        | no - as expected              |
| Add Recipe tab - nav bar (for logged-in users only)                             | `add_recipe.html`                                           | no - as expected              |
| My Drafts tab - nav bar (for logged-in users only)                              | `my_drafts.html`                                            | no - as expected              |
| Logout - nav bar (for logged-in users only)                                     | `logout.html`                                               | no - as expected              |
| SignUp Now - from `index.html` (unauthorised users only)                        | `signup.html`                                               | no - as expected              |
| Sign Up - nav bar (unauthorised users only)                                     | `signup.html`                                               | no - as expected              |
| Sign In - nav bar (unauthorised users only)                                     | `login.html`                                                | no - as expected              |
| Sign in - comments section, `recipe_detail.html` (unauthorised users only)      | `login.html`                                                | no - as expected              |
| Edit - `recipe_detail.html` (on user's own recipes only)                        | `update_recipe.html`                                        | no - as expected              |
| Delete - `recipe_detail.html` (on user's own recipes only)                      | `recipe_confirm_delete.html`                                | no - as expected              |
| All recipes - from `recipe_search.html` (for all users)                         | `recipes.html`                                              | no - as expected              |
| Add Your Recipe - from `recipe_search.html` (1. for unauthorised users. 2. for authorised users) | 1. `login.html`, 2. `add_recipe.html`   | no - as expected              |
| "GitHub" Icon - footer                                                          | <https://github.com/naomi-mali>                             | yes - as expected             |
| "LinkedIn" Icon - footer                                                        | <https://www.linkedin.com/in/naomi-mali-69353b182/>     | yes - as expected             |

### Negative Testing

Testing is performed on all forms in the website and for user authentication to Create, Update, Delete recipes.

|  Function  |   Action    |    Expected    |  Actual  |
|------------|--------------|---------------|-----------|
|Sign Up   |	user doesn't fill in all required fields (username and password twice), user enters password twice but doesn't match, username enters too common password or less than 8 characters |	user received a prompt with directions, submission unsuccessful user can enter details again | as expected |
|Sign-in |	user doesn't fill in all required fields (username and password). user enters incorrect username or password | user receives prompt why sign-in is unsuccessful and can enter details again |	as expected |
| Add Recipe form | user doesn't fill in all required fields(marked with *) | user receives a prompt to fill in the required field. form doesn't submit. user can enter details again | as expected |
|Edit Recipe |	1.user tries to access URL to edit recipe but not logged in 2. user tries to access the url from different username	| 1.user directed to login page 2. user receives error 403 |	as expected |
| Delete Recipe |	1.user tries to access URL to delete recipe but not logged in 2. user tries to access the url from different username | 1.user directed to login page 2. user receives error 403 | as expected |
| Comment form |	user tries to submit empty comment form |	user receives prompt Please fill in this field, form is not submitted |	as expected |

## Automated Testing

### Unit Testing

No unit testing performed at this stage.

## Bugs

Bug Fix: Cloudinary Integration Not Working

Issue: Cloudinary was not functioning as expected within the application. Attempts to upload or manage media files via Cloudinary failed, and the application defaulted to local file storage instead.

Cause: The issue was traced to a missing configuration in the settings.py file. Specifically, the CLOUDINARY_STORAGE setting, which is required to connect the Django application to the Cloudinary service, was not included. Without this configuration, Django was unable to authenticate with Cloudinary using the CLOUDINARY_URL environment variable, leading to the failure.

Fix: The following configuration was added to settings.py:
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
 This setting ensures that Django correctly connects to the Cloudinary account using the credentials stored in the CLOUDINARY_URL environment variable. With this fix, media files are now successfully uploaded and managed through Cloudinary, and the integration works as intended.

Status: Resolved. Cloudinary is now fully functional in the application.



## Bug: HTML Sanitization for Ingredients and Instructions Fields

### Issue

- **Problem:**  
  Users may input HTML content like `<ul>`, `<ol>`, `<li>` for structured lists or styling elements like `<b>` or `<i>` in the **Ingredients** and **Instructions** fields.  
  Without sanitization:
  - **Security Risks**: Potential for malicious HTML or JavaScript injection.
  - **Rendering Issues**: Invalid or unsafe HTML could cause display problems on the frontend.

- **Requirement:**  
  Allow specific HTML tags (e.g., lists, basic text formatting) while sanitizing other unsafe or unnecessary tags.

---

### Solution: HTML Sanitization Using `bleach`

We used the **`bleach` library** to sanitize HTML input, ensuring only safe and necessary tags are preserved.

---

### Steps to Fix

#### 1. Install the `bleach` Library

Install the `bleach` library to handle sanitization.

Run the following command in your terminal:
```bash
pip install bleach
```

---

#### 2. Update the Recipe Model

Sanitize the `ingredients` and `instructions` fields using custom cleaning methods in the **Recipe model**.

**Updated Code:**
```python
import bleach

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()

    # Clean the ingredients field
    def clean_ingredients(self):
        allowed_tags = ['ul', 'ol', 'li', 'b', 'i', 'p', 'br']
        return bleach.clean(self.ingredients, tags=allowed_tags)

    # Clean the instructions field
    def clean_instructions(self):
        allowed_tags = ['ul', 'ol', 'li', 'b', 'i', 'p', 'br']
        return bleach.clean(self.instructions, tags=allowed_tags)

    # Apply sanitization during save
    def save(self, *args, **kwargs):
        self.ingredients = self.clean_ingredients()
        self.instructions = self.clean_instructions()
        super().save(*args, **kwargs)
```

**Explanation:**
- **`bleach.clean()`**:
  - Sanitizes the input, removing all tags except those specified in `allowed_tags`.
- **Allowed Tags**:
  - Supports list formatting (`<ul>`, `<ol>`, `<li>`), basic text styling (`<b>`, `<i>`), and paragraph breaks (`<p>`, `<br>`).
- **Sanitization in Save**:
  - Ensures sanitization is applied whenever the model instance is saved.

---

#### 3. Update the Template for Rendering

To properly display sanitized HTML content on the frontend, update the template to use the `|safe` filter.

**Template Code:**
```html
<div class="ingredients">
    {{ recipe.ingredients|safe }}
</div>

<div class="instructions">
    {{ recipe.instructions|safe }}
</div>
```

**Explanation:**
- The `|safe` filter allows Django to render the sanitized HTML content without escaping it.

---

### Benefits of This Fix

1. **Security**: Prevents harmful scripts or HTML from being stored or displayed.
2. **Improved UX**: Allows users to input and view structured, formatted content safely.
3. **Consistency**: Ensures only valid and safe HTML tags are rendered.

---

### Summary of Changes

1. Installed `bleach` to sanitize HTML input for specific fields.
2. Added `clean_ingredients()` and `clean_instructions()` methods in the **Recipe model**.
3. Overrode the `save()` method to integrate sanitization during database saving.
4. Updated the template to use the `|safe` filter for rendering sanitized content.

These changes ensure the **Ingredients** and **Instructions** fields are secure, clean, and properly formatted for rendering on the frontend.

### Recipe Search Page Not Loading

The recipe search functionality was not working correctly. When I attempted to search for recipes, the application failed  resulting in error.
Cause: The issue was caused by a typo in the views.py file. Specifically, in the template_name parameter, the template was incorrectly referenced as search._recupe.html instead of the correct search_recipe.html. This typo caused Django to look for a non-existent template file, leading to the failure.

Fix: The typo in the views.py file was corrected as follows:
### Incorrect
template_name = 'search._recupe.html'

### Corrected
template_name = 'search_recipe.html'

This change ensures that the correct template is loaded when users search for recipes, allowing the search functionality to work as expected.

## Deployment

### Version Control

- The website was developed through Gitpod.

- Code has been pushed to repository on Github with following git commands:

    - git add . - to add files ready to commit
    - git commit -m "message" - to commit the code to local repository ready to be pushed
    - git push - final command used to push committed code to remote repo on Github


### Deployment In Heroku

- The project has been deployed on Heroku as follows:
     - Use: pip freeze > requirements.txt to add external libraries to deployed app.
     - Create Heroku account
     - In the top right, click 'New'
     - Click 'Create new app'
     - Give your app a name and select your region from drop down
     - Click 'Create new app'
     - Go to 'settings' tab, it's important you do it before deployment
     - Scroll down to 'config vars' section and key:
          - PORT and value: 8000
          - CLOUDINARY_URL: 'API key to your cloudinary account'
          - DATABASE_URL : 'URL from your database account'
          - SECRET_KEY: 'Generate your own secret key'
     - Scroll down to 'Buildpacks' section
     - Click 'Add buildpack'
     - Add Python as first dependency and select 'Save changes'
     - Add node.js as a second dependency and save again (This is settings section done)
     - Select 'Deploy' tab at the top
     - Select 'Github' from 'Deployment method'
     - type the name of how you called project in Github and click 'search'
     - Scroll down and select manual deployment method
     - You can also use Auto deployment method to allow the project to update every time you push the code.
     - You can now click to view the app ready and running
- For this project I used Manual deployment method to deploy the current state of the branch, every time I pushed the code from Gitpod.

## Cloning the Repository
On Github navigate to the repository
Click "Code" drop down menu - a green button shown right above the file list.
Copy the URL of the repository using "HTTPS", "SSH" or "Github CLI".
Open Git Bash.
Change the current working directory to the location where you want the cloned directory.
Type "git clone", and then paste the URL copied earlier.
Press enter to create local clone. A clone of the repository will now be created.

## Forking
On Github navigate to the repository.
Click "Fork" located towards top right corner on GitHub page.
Select "owner" for the forked repository from the dropdown menu under "owner".
It will create forked repo under the same name as original by default. But you can type a name in "Repository name" or add a description in "Description" box.
Click on "Create fork". A forked repo is created.
Forking allows you to make any changes without affecting original project. You can send the the suggestions by submitting a pull request. Then the Project Owner can review the pull request before accepting the suggestions and merging them.
When you have fork to a repository, you don't have access to files locally on your device, for getting access you will need to clone the forked repository.

## Credits

All images used on the website are sourced from [Pexels](https://www.pexels.com/ro-ro/fotografie/om-pat-sta-jos-sta-a-ezat-4132936/) and [Unsplash](https://unsplash.com/).
All the recipes on the website are taken from [Tasty](https://tasty.co/)
All the fonts used throughout this project are sourced from [Google Fonts](https://fonts.google.com/)
In creating my models and understanding the CRUD functionality[Youtube-Tutorial](https://www.youtube.com/watch?v=opjyyXoqrxg)

## Acknowledgements
- I followed the steps from [I Think Therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+4/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/) 
- I am grateful to the Code Institute's Tutor support for solving all my doubts.














