# Unit 4 Project Social Network Website

# Table of Content

1. [Criteria A](#criteria-a-planning)

2. [Criteria B](#criteria-b-solution-overview)

3. [Criteria C](#criteria-c-development)

4. [Criteria D](#criteria-d-functionality)

5. [Citation](#citation)

6. [Whole Code](#whole-code)

7. [Appendix](#appendix)

# Criteria A-Planning

## Problem Definition
I am a teen chef who is passionate about food and solving inequality in society. I see that the interconnected issues of food insecurity and food waste are vital. The problem is that people are not aware that the problems exist, so they throw away foods that are still fresh and edible. Restaurants and hotels do that on a larger scale. Some restaurants may have been giving away leftover food, but not all people who face hunger know about where these giveaways take place, or what kind of food is being donated. Restaurants do not have a platform to share what foods they are giving away to spread the words. It has been hard for them to keep track of the giveaways they have done, so they need an organized separated system to keep track of the foods that have been donated. As I am studying about this issue, I would like to see an overview of the whole donations that has happened by different restaurants to share the data with people who are also passionate about equality and sustainability whom I have consulted with about this website(see [Appendix](#appendix)). The most important thing is that I want people to be mindful that the platform is for those who are facing food insecurity and for the planet, so that no one takes the food for granted.


## Success Criteria
1. The website has a home page to educate users on the issue of food insecurity and food waste (*issue tackled: People are unaware of the global issue*)
2. The website has a feed page where users can scroll through and look at the available food giveaways with the important details such as location, and general description of the food (*issue tackled: People do not know the details of existing giveaways*)
3,The website allows users to type in the specific details of the food they are giving away (*issue tackled: Restaurants need a platform to announce giveaways*)
4. The website has a login and register system for users to post giveaways in their individual accounts(*Issue tackled: Restaurants need to keep track of the foods they have donated individually*)
5. The website has an admin page where the admin can look at the all posts created by every users (*Issue tackled: See an overview of the whole donations*)
6. The website has a green theme to remind users that the purpose of this platform is to save the world (*Issue tackled: Some people might take the platform for granted if they view it as a free food platform*)

## Design statement
I will develop a website that connects restaurants who create a lot of food waste with people experiencing food insecurity. I will use HTML, CSS, Python, SQLite, and the Flask framework. This website will allow restaurants to post food donations and people in need of food to check for available giveaways. It will take approximately 3 weeks to fully develop the website. 

## Rationale for the Proposed Solution
I have chosen to create a website because the main purpose of this project is to reach a wide audience of people who are in need of food. Websites are compatible equally with all devices, unlike apps which need personalized versions in each type of device. It is also much more convenient for maintenance in websites since there is no need to get approval from the application markets [1]. 

I decided to use HTML because it is completely free which is great for the client’s limited budget since it is a charity project. HTML is also supported by all browsers, so it can reach a wide audience no matter what the browser the user is using [2]. I chose HTML over a content management system (CMS) like Wordpress because I can have more control over the website with HTML and once the website is larger it could be hard to transfer over from CMS to HTML [7].

I have chosen to use CSS because it allows us to keep the content of the web page separate from the style display that will make it convenient for organizing the common styles, so there is no need for duplication or confusion in the inconsistent styles[3] . 

I decided to use Python for the website because it is a powerful open-source programming language which makes it completely free to use the libraries [4]. There are also a large number of libraries to use with Python which are used to fulfill the functionalities in this project: Flask, sqlite3, and passlib library. Compared to its alternatives such as Node Js or Java [8], Python is better at data management which is important for this project as it involves storing and organizing data of donated foods and user information [5]. If the client wants to visualize the data, they can use matplotlib in the future stages of the project as well. 

Finally, I have chosen to use SQLite for the database management system because it is an open source software which does not require any additional costs. SQLite is serverless, no additional server is required. It matches my client needs as It loads and overwrites the required data not the whole database. This is for better performance in the project when users add information about food donations, we only want to focus on the small section of the specific user, not the whole database [6]. This project is not an extremely large project, so SQL is better than MySQL which involves complex syntax for larger projects [9]. (Word count: 421)



# Criteria B-Solution Overview
## Record of Tasks
| Task No | Planned Action| Planned Outcome| Time estimate | Target completion date | Criterion |
|-|--------|--------|---|---|---|
|1|Create a repository| A repository with table of content that is easy for the client to read|5 min|7 April 2023|A|
|2|Define a problem definition|A problem definition that includes all the information about what the client needs for the program|20 min| 8 April 2023|A|
|3|Create a success criteria|A list of criterias that the developer need to meet|15 min|8 April 2023| A|
|4| Create base template| A base template for every page|30 min| 10 April 2023| C|
|5|Create registration page| A page with a form to submit registration details to the database|1 hr| 12 April 2023| C|
|6| Create login page| A page with a form to login that redirects to the next profile page| 1 hr| 12 April 2023| C|
|7| Create a landing page| A page with the simple details of the website and two buttons that allow users to register or login| 30 min| 13 April 2023| C|
|8| Create a page to show all giveaways| A page to show the list of foods that are being given away|30 min| 14 April 2023| C|
|9| Create a profile page| A page showing all the posts by the individual user and a form to submit new posts| 2 hr| 18 April 2023| C|
|10| Edit the format of the website| The website has a common theme in the same color for the buttons and the background| 30 min| 20 April 2023| C|
|11| Check success criteria and problem definition| Success criteria tha aligns with the problem definition| 1 hr| 21 April 2023| A|
|12| Consultation with people in the community| Ideas on the existing problems and how to solve it| 30 min| 22 April 2023| A|
|13| 

# Criteria D-Functionality
## Citations
1. H., Tania, and Vlad V. “Pros and Cons of Mobile Websites and Mobile Apps.” RubyGarage, rubygarage.org/blog/mobile-app-vs-mobile-website. 
2. Singhal, Piyush. “What Are the Advantages of HTML?” Scaler Topics, Scaler Topics, 17 Oct. 2022, www.scaler.com/topics/advantages-of-html/. 

# Appendix
## Evidence of Consultation
![IMG_7673](https://user-images.githubusercontent.com/112055062/236713666-64b71fc8-9534-4506-ab8d-e6b33f4edd47.jpg)
*Fig.* Interview with people who are passionate about equality and the sustainability on what they think about the topics. They have identified their needs in connecting restaurants and people who are facing food insecurity.

