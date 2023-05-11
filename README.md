# Unit 4 Project Social Network Website "Fresh Surplus"

![trash food](https://github.com/aineethitari/unit4_project/assets/112055062/495b98a0-50d2-4aff-8cb9-4fe7f5acb016)


# Table of Content

1. [Criteria A](#criteria-a-planning)

2. [Criteria B](#criteria-b-solution-overview)

3. [Criteria C](#criteria-c-development)

4. [Criteria D](#criteria-d-functionality)

5. [Appendix](#appendix)

6. [Citation](#citation)

# Criteria A-Planning

## Problem Definition
I am a teen chef who is passionate about food and solving inequality in society. I see that the interconnected issues of food insecurity and food waste are vital. The problem is that people are not aware that the problems exist, so they throw away foods that are still fresh and edible. Restaurants and hotels do that on a larger scale. Some restaurants may have been giving away leftover food, but not all people who face hunger know about where these giveaways take place, or what kind of food is being donated. Restaurants do not have a platform to share what foods they are giving away to spread the words. It has been hard for them to keep track of the giveaways they have done, so they need an organized separated system to keep track of the foods that have been donated. As I am studying about this issue, I would like to see an overview of the whole donations that has happened by different restaurants to share the data with people who are also passionate about equality and sustainability whom I have consulted with about this website(see [Appendix](#appendix)). The most important thing is that I want people to be mindful that the platform is for those who are facing food insecurity and for the planet, so that no one takes the food for granted.


## Success Criteria
1. The website has a home page to educate users on the issue of food insecurity and food waste (*issue tackled: People are unaware of the global issue*)
2. The website has a feed page where users can scroll through and look at the available food giveaways with the important details such as location, and general description of the food (*issue tackled: People do not know the details of existing giveaways*)
3. The website allows users to post the specific details of the food they are giving away (*issue tackled: Restaurants need a platform to announce giveaways*)
4. The website has a login and register system for users to post giveaways in their individual accounts(*Issue tackled: Restaurants need to keep track of the foods they have donated individually*)
5. The website has an admin page where the admin can look at all the posts created by every users (*Issue tackled: See an overview of the whole donations*)
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
## System Diagram

![System Diagram Unit4](https://user-images.githubusercontent.com/112055062/236818257-95f6f890-4477-4091-a20b-843eb032904d.jpeg)
*Fig.1* This is the system diagram for the proposed solution
The system diagram shows the relationships between each component of the project. This includes the inputs from the keyboard and the mouse to the computer Apple Mac Book Pro 2020 with Mac OS Monterey 12.6. Within the computer there is the Python 3.11 programming language which is used to create the functionalities and connects the SQL database and the web browser. 

## Wireframe Diagram

![Unit4-4](https://user-images.githubusercontent.com/112055062/236826948-e737deff-b089-420a-a512-63dd8708a5f2.jpg)
*Fig.2* This is the wireframe diagram of the program which shows the different pages that can be accessed on the website. The pages include a landing page, login page, registration page, profile page, all post page (shows the past posts by the users), and an admin page that shows the list of all users.  

## Flow Diagrams

![Login Flow diagram unit4](https://user-images.githubusercontent.com/112055062/236862095-e7027833-1f43-42f6-8b0c-c89077455e6f.jpeg)
*Fig.3* Flow diagram of the Login Diagram where the user python function receives information of the login entered by the user through a form and then checks if it matches with the database to proceed on.

![new post diagram](https://user-images.githubusercontent.com/112055062/236869686-8c32a187-0d4b-4e22-9cbc-bb37f852caa7.jpeg)
*Fig.4* Flow diagram for new posts section in the program where users are allowed to enter information of the food donation to the form then later adds to the sql database.

![registration flowchart unit 4](https://user-images.githubusercontent.com/112055062/236875212-2c580b33-dd8e-4eac-9d8d-c27632b77c8a.jpeg)
*Fig.5* Registration Diagram flow diagram where user enters the information of creating an account and there is a password validation policy and the user information will then be added to the database.

## ER Diagram
![ER Diagram unit 4](https://user-images.githubusercontent.com/112055062/236963126-6ad6d690-3fc2-4402-a511-200299403dc6.jpeg)
*Fig.6* ER Diagram shows the relationship between the table 'users' and 'posts' in the database.

### Example of Database

<img width="571" alt="users table" src="https://user-images.githubusercontent.com/112055062/236968894-a10258d9-3fa8-4668-ae51-221f3a603878.png">
*Fig.7* users table in database which stores the user accounts

<img width="903" alt="posts database" src="https://user-images.githubusercontent.com/112055062/236969180-e54d0b43-3466-4ed0-a6e1-40f47f46ad9d.png">
*Fig.8* posts table in database which stores the donation posts by the users 

## UML Diagram
![UML Diagram](https://user-images.githubusercontent.com/112055062/236878313-0cd29f4b-98ea-4de5-96ca-e385ae2f565e.jpeg)
*Fig.9* UML Diagram shows the class 'database_worker' which is used in the program

## Test Plan
|Description|Test Type|Input|Expected Output|
|----|--|----------------|----------------|
|Test for registration system | Unit Test| 1.Open Website 2.Click Register button on the landing page 3.Enter 'james@gmail.com' in Email text field 4.Enter 'tomorrowland' in the enter password text field 5.Enter 'tomorrowland' in the confirm password field 6.Click register button|After clicking the register button, the website should be redirected to the login page. This registration system is to fulfill success criteria 4|
|Test for existing account in registration system|Unit Test|1.Open Website 2.Click Register button on the landing page 3.Enter 'james@gmail.com' in Email text field 4.Enter 'marshmallow' in the enter password text field 5.Enter 'marshmallow' in the confirm password field 6.Click register button| After clicking the registration button, the website should show a message that 'user with that email is already registered. Go to login'. This fulfills success criteria 4 where users cannot create account with same email.|
|Test for non-matching password in registration|Unit Test|1.Open Website 2.Click Register button on the landing page 3.Enter 'james@gmail.com' in Email text field 4.Enter 'marshmallow' in the enter password text field 5.Enter 'newyorkcity1234' in the confirm password field 6.Click register button|After clicking the registration button, the website should show a message saying 'Password don't match'. This fulfills success criteria 4.|
|Test for database connection| Unit Test|  1.Open Website 2.Click Register button on the landing page 3.Enter 'james@gmail.com' in Email text field 4.Enter 'tomorrowland' in the enter password text field 5.Enter 'tomorrowland' in the confirm password field 6.Click register button| After clicking the register button, check the database table users. The previous user account entered should be shown on the table once the table is refreshed.|
|Test for login system| Unit Test| 1.Open Website 2.Click Login button 3.Enter email james@gmail.com in the email field 4.Enter password 'tomorrowland' in the password field 5.Press login button| After clicking the login button, the website should redirect to the user/user_id page.|
|Test error in login system| Unit Test|1.Open Website 2.Click Login button 3.Enter email james@gmail.com in the email field 4.Enter password 'myname12345' in the password field 5.Press login button|After clicking login, the program should not redirect to any other pages, but the information filled in the fields will disappear|
|Test create new post form| Integration Test| 1.Open Website 2.Click Login button 3.Enter email james@gmail.com in the email field 4.Enter password 'tomorrowland' in the password field 5.Press login button 6.Fill in the title, location, date, time, and description 7.Click save button |After clicking the save button, the program should show the post on the poste table. This fulfills success criteria 3|
|Test create new blank post|Integration Test|1.Open Website 2.Click Login button 3.Enter email james@gmail.com in the email field 4.Enter password 'tomorrowland' in the password field 5.Press login button 6.Fill in only the title field 7.Click save button| After clicking the save button the website will refresh, but there will be no updates to the post table|
|Test all posts page link button|Unit Test| 1.Open Website 2.Click 'Checkout free fresh surplus!' button|The website redirects to the allposts page. This fulfill success criteria 3|
|Test logo link in base template| 1.Open website 2.Click 'Checkout free fresh surplus!' button 3.Click logo on the header| Website redirects to the allposts page, then redirects back to the landing page. This is to fulfill success criteria 1|
|Theme review|Non-functional testing|1.Open website 2.Enter the address for each pages in the search address field for allposts, landing, login, profile, registration, users | The program should all have a green background with universal design. This is to fulfill success criteria 6|
|Code review|Code review| Going over all the code for the project. Remove unused parts and editing repeated parts| The code is understandable by other developers and there is not excess codes|

## Record of Tasks
| Task No | Planned Action| Planned Outcome| Time estimate | Target completion date | Criterion |
|-|--------|--------|---|---|---|
|1|Create a repository| A repository with table of content that is easy for the client to read|5 min|7 April 2023|A|
|2|Define a problem definition|A problem definition that includes all the information about what the client needs for the program|20 min| 8 April 2023|A|
|3|Create a success criteria|A list of criterias that the developer need to meet|15 min|8 April 2023| A|
|4| Create base template| A base template for every page|30 min| 10 April 2023| C|
|5|Create registration page| A page with a form to submit registration details to the database|1 hr| 12 April 2023| C|
|6| Code the functionality for the registration system on python| The program for registration system works that HTML form|2hr| 12 April 2023| C|
|7| Create login page| A page with a form to login that redirects to the next profile page| 1 hr| 12 April 2023| C|
|8| Create a landing page| A page with the simple details of the website and two buttons that allow users to register or login| 30 min| 13 April 2023| C|
|9| Create a page to show all giveaways| A page to show the list of foods that are being given away|30 min| 14 April 2023| C|
|10| Code the python part of the allposts page| The functionality should work that the information form the database is being posted on the website|1hr|15 April 2023| C|
|11| Create a profile page| A page showing all the posts by the individual user and a form to submit new posts| 2 hr| 18 April 2023| C|
|12| Create the form for new posts| An HTML form that allows user to upload information about the food donation| 2 hr| 18 April 2023| C|
|13| Code the python for new posts| The form for adding new posts fully functions, being able to send the information to the database|2hr|19 April 2023|C|
|14| Edit the format of the website| The website has a common theme in the same color for the buttons and the background| 30 min| 20 April 2023| C|
|15| Create the admin page for the website| Page where the admin can see every posts by each individual user| 1 hr| 20 April 2023| C| 
|16| Check success criteria and problem definition| Success criteria tha aligns with the problem definition| 1 hr| 21 April 2023| A|
|17| Consultation with people in the community| Ideas on the existing problems and how to solve it| 30 min| 22 April 2023| A|
|18| Write design statement| Explanation of the platform that will be developed|15 min| 23 April 2023| A|
|19| Write rationale for proposed solution| Detailed explanation of the decisions behind the proposed solution including all the techniques that are used| 2 hr| 23 April 2023| A|
|20| Create a system diagram| Visual diagram with all the components of the project| 1 hr| 24 April 2023| B|
|21| Create Wire Frame Diagram| Wireframe diagram that shows the functionality of the website and how each pages connect to each other| 1 hr| 24 April 2023| B|
|22| Create Flow Diagram for login system| Flow diagram that shows how the program works step by step| 30 min| 25 April 2023| B|
|23| Create Flow Diagram for registration system| Flow diagram that shows how the registration works| 30 min| 25 April 2023| B|
|24| Create Flow Diagram for new post page| Flow diagram that shows how new posts are being created| 30 min| 26 April 2023| B|
|25| Create ER Diagram for the database|ER Diagram that shows the connections between thetables in the database.|30 min| 27 April 2023| B|
|26| Upload picture of the two tables in the databases| users table and posts table| 5 min | 28 April 2023|B|
|27|Write the techniques used in the development| a list of techniques that was used| 5 min| 1 May 2023| C|
|28| Write the description of the base template code| detailed explanation with mentioning of the computational thinking behind it| 1 hr| 2 May 2023| C|
|29| Write the description in the development of the registration system| A detailed explanation of the registration system| 1 hr| 3 May 2023| C|
|30| Write about creating new posts| Detailed explanation of how the post section works| 1 hr| 4 May 2023| C|
|31|Write about feed page showing all posts| Detailed description of the feed page which explains the decision behind having all posts|1 hr| 6 May 2023| C|
|32| Write about cookies| Detailed explanation on the purpose of using cookies and how it works in the program| 1 hr| 6 May 2023| C|
|33|Create a test plan| A tabel with all the test plans for the website| 30 min| 7 May 2023| B|
|34| Tested for the registration system| Registration system functions| 5 min| 8 May 2023| B|
|35|Edit code for registration system | Registration fully works with no minor errors| 20 min| 8 May 2023| C|
|36| Test the login system| User successfully logs in to their profile page| 5 min| 8 May 2023|B|
|37| Test for all posts page| Page show all the posts that have been uploaded| 5 min| 9 May 2023|B|
|38| Test for create new post page| Post filled in the form shows up on the table| 5 min| 9 May 2023| B|
|39| Ask peer for feedback| Detailed evaluation of the whole website| 10 min| 9 May 2023| B|
|40|Ask client and peer for recommendation| Detailed reccomendation of how the website could go| 15 min| 9 May 2023| B|




# Criteria C-Development
## Existing Tools
1. Flask
2. Jinja2
3. SQLite3
4. Passlib.hash

## Techniques Used
1. Python
2. Flask library 
3. HTML
4. CSS Styling Display
5. Object Oriented Programing (OOP)
6. SQLite3
7. passlib for password hashing
8. Cookies
9. Variables
10. Functions
11. Lists
12. Jinja

## Development
### Base Template

```.html
<style>
        body{background-color: #e2f5d7;}
```
My client wants the website to have a common environmental theme, so I used my computation thinking skills to think of what it takes to have an environmental theme. I decomposed 'environmental theme' into two sections which are the color and some symbol that hints a meaning. Therefore I decided to set the background color to be universal among all pages of the website. Green would be the best color for an environmental and sustainability theme, so I used #e2f5d7.

At first, I was going to duplicate it on all of the html files. Then I recognized the pattern and I want to follow the DRY programming paradigm, so I researched and use the base template to store the common HTML and CSS tags in every page.

```.html
    <a href="http://127.0.0.1:5000/">
    <img src="/static/freshsurplus2.png" alt="fresh surplus logo" class="center"
         width="80"></a>
    <h1>Fresh Surplus</h1>
```
As I decomposed my tasks and thinking, the base template also has a header that appears in every screen with the logo of the website. The logo is linked to another web address http://127.0.0.1:5000/ which is the landing page. The image freshsurplus2.png is the logo which is placed in the middle of the screen above a header that says Fresh Surplus. When the user clicks the image of the logo, then they will always be redirected to the landing page which has a raise awareness section about the issue of food insecurity and food waste. This is for the success criteria 1 which tackles the issue that people are not aware of the problem.

To apply the base template on other pages, the pages need to have this line:
```.html 
{% extends "base_template.html" %}
```
followed by:
```.html
{% block content %} 
```
The content of individual pages will be wrapped in here. Followed by:
```.html
{% endblock %}
```


### Registration System
```.py
    if request.method == 'POST': # if the user fills the form
        email = request.form['email'] # email that the user filled in the form is stored in email variable
        passwd = request.form['passwd'] #  password that the user filled in the form is stored in passwd variable
        passwd_check = request.form['passwd_check'] # password confirmation that the user filled in the form is saved in passwd_check variable
```
Success criteria 4, requires website to have a registration system, so I created a registration system which is done through an HTML form with a ```POST``` method to send the data to the web server. The if-statement checks whether there has been a POST request method, or there has been a form filled. Then if it is true, the information from the form is saved in to variables. The data from the email field is saved to the ```email``` variable, the password is saved to ```passwd``` variable, and the password confirmation field is saved to the ```passwd_check``` variable. I save all of this information to the variables because the variable will be used later on for saving the information to the database.

```.html
<form method="POST">
    <div>
        <p>Email: </p>
        <input type = "email" placeholder="enter your email" name="email">
    </div>
    <div>
        <p>Enter password:</p>
        <input type="password" name="passwd">
    </div>
    <div>
        <p>Confirm Password:</p>
        <input type = "password" name="passwd_check">
    </div>
    <input type = "submit" class="button" value="Register">
</form>
```
This is the registration form element in the HTML file which is stated at the beginning that the POST method is used in this form. Then, each section has its own ```<div>``` tag with the paragraph text and an input box. This is repeated for the email, the password, and the confirm password field. Lastly, there is a submit button for the users to submit the form.  

```.py
db = database_worker('social_net.db') #connect to database 
            existing_user = db.get(f"SELECT * from users where email='{email}'") #search for the same email that the user have filled in the form in the database
            if existing_user: #if email exists
                message = "User with that email already registered. Go to Login" #message shows that this user email already exists
```
According to success criteria 4, the client wants the restaurants and hotels to post donations on their individual accounts. Therefore, I created a registration system where users can only have their own single account. This ensures that there is an organized way in storing the donation history by hotels and restaurants. The code above shows how there can only be one single account per email that is entered. 

Firstly, the data base is connected with the method ```database_worker ```. Then the program will search in the table ```users``` from the database where the email is equal to the email that was entered through the registration form. I then use the if statement with a message inside to tell the users that the email already exists. 

```.py
            else:
                new_user = f"""INSERT into users(email,password) values(
                '{email}','{encrypt_password(passwd)}')""" # sql command for saving the entered email and hashed password to the database 
                db.run_save(new_user) #execute the sql command
                db.close() #close database
```
If the user is new and does not exist in the database, the entered email and password would then be inserted to the database. To do this, I used the variable ```new_user``` which stores the sql command for inserting the email and a hashed password using the ```encrypt_password``` method. The command in ```new_user``` is then executed with the ```run_save``` method. To end off, the database is then closed. 

### Login System
```.py
        if len(email)>0 and len(passwd)>0: # if email and password length is more than 0
            db = database_worker('social_net.db') # connect to the databse
            user = db.search(f"SELECT * from users where email='{email}'") #search that the entered email matches the email in the database
```
According to success criteria 4, the clients want a login system. I created the login system by comparing the email that is in the database to the email that the user input for logging in. 

```.py
if check_password(hashed=hash, user_password=passwd): #checks whether password matches the hashed password
    resp = make_response(redirect(url_for('profile',user_id=id))) # redirect to profile page
    resp.set_cookie('user_id',f"{id}") #set user_id in the cookies
    print("password is correct")
    return resp
```
The program then checks the password whether it matches the password that is hashed. If the password matches, then the the page redirect to the url for the profile page. It also stores the user_id in the cookies.

### Creating New Posts
 According to success criteria 3, the restaurants need to be able to post donations with specific details. I think that the best way to do this is through a form with many sub-sections, not one text field for them to type freely. It is important for the post to include the essential information such as title, locaiton, date, time, and description. Using my computational skills, I start this section by deviding the tasks into smaller parts. Firstly, I started with the display by writing a HTML form with the information that should be included in the posts. 
 
 ```.html
 <form method="post" class="centerwide">
    <p class="centerwide">Title <input type="text" name="title" placeholder="Enter the title"></p>
    <p class="centerwide">Location <input type="text" name="location" placeholder="Enter the location"></p>
    <p class="centerwide">Date  <input type="text" name="date" placeholder="Enter the date"></p>
    <p class="centerwide">Time <input type="text" name="time" placeholder="Enter the time"></p>
    <p class="centerwide">Description <input type="text" name="description" placeholder="Enter the description" </p>
    <input type="submit" value="Save" class="button">
```
The HTML code above shows the form that is used to submit the information about the donations. Each form text field has its own name which is used to connect with the functionality in python. 
```.py
db = database_worker("social_net.db")
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        date = request.form['date']
        time = request.form['time']
        description = request.form['description']
        if len(title)>0 :
            new_post = f"""INSERT into posts(title, location, date, time, description, user_id) values 
            ('{title}','{location}', '{date}','{time}','{description}','{user_id}')"""
            db.run_save(new_post)
            return redirect(url_for("profile",user_id=user_id))
 ```
I then work on the python code to create the functionality. I used my computation thinking skills of pattern recognition to see that the steps are very similar to the registration system which also uses POST method from flask, so I used the registration system code as a reference. I requested the information entered by the users through the POST method into the variables title, location, date, time, and description. Then there's an if statement to make sure there is something added to the title by checking that the length of the title string is more than 0. If so, the information in the variables will be put in an sql command for inserting the data to the database stored in a variable ```new_post```. Then I execute the program through ```run_save```, so the information is saved. The program then redirects the user to the same page, but the page will be refreshed wich shows the updated information. 

### Feed page showing all posts
According to Success criteria 2, my client wants a feed page which allows people who are food insecure to come check the available food donations easily. I used algorithmic design to think in the shoes of a person using the website. If I want it to be easy for them to access the information, there should not be any complicated steps required. Therefore, I decided that there should not be any login verification for users who are looing at the food donation options.

```.html
<div>
        <h2>Looking for free food?</h2>
        <a href = "http://127.0.0.1:5000/allposts">
            <input type="button" class="button" value="Check out free fresh surplus!"
        </a>
```
In the landing page, there is an eye-catching text which asks if the user is looking for free food or not. Then the text is followed by a big button that allows user to click to see free leftover foods or fresh surplus. Once the user click the button, the page will be redirected to the 'allposts' page which has all the post history by every user in the social network.

After thinking about how to reach the wide audience, I design the best way to make the information understandable and organized for the users who are looking for food. 

```.html
<table>
        <tr><!--row-->
            <th>id</th>
            <th>Title</th>
            <th>Location</th>
            <th>Date</th>
            <th>Time</th>
            <th>Description</th>
        </tr>
        {% for i in allposts %}
        <tr>
            <td>{{ i[0] }}</td>
            <td>{{ i[1] }}</td>
            <td>{{ i[2] }}</td>
            <td>{{ i[3] }}</td>
            <td>{{ i[4] }}</td>
            <td>{{ i[5] }}</td>
        </tr>
        {% endfor %}
    </table>
```
I believe that the best way to showcase the information is through an organized table as the information is in the same format of id, title, location, date, time and description. 

### Admin Page
Success criteria 5 requires an admin page in which the admin can see all users in the database and can go through each of their profiles. 

```.py
db=database_worker("social_net.db")
    all_users = db.search("SELECT * FROM users")
```
I searched for all of the users by selecting all information of the users from the users table
```.py
  {% for u in users %}
    <tr>
        <td><a href="{{ url_for('profile', user_id=u[0]) }}">No{{ u[0] }}</td> <!--first element = id, 2nd element = email-->
        <td>{{ u[1] }}</td> {# email #}
    </tr>
    {% endfor %}
```
Then I added a link to every users which the link is the profile page with according to the user id of the user. This results in a list of all users with link to their profile page.

 ### Using Cookies for Individual Profile Page
```.py
resp = make_response(redirect(url_for('profile',user_id=id)))
                    resp.set_cookie('user_id',f"{id}")
                    return resp
```
My client wants users to be able to have a specific profile page to be able to post their donations organizely. Therefore, each user needs to have their own specific separated user page, so I store the user_id of the logged in user in the cookies. The user is then redirected to the 'profile' page which is specific to each user_id.

```.py
@app.route('/user/<user_id>',methods=['GET','POST'])
def profile(user_id):
    if request.cookies.get('user_id'): #check if cookies exist
        print("The cookie was found") #message that the cookie exists 
        user_id = request.cookies.get('user_id') #store cookies in the variable user_id 
```
The cookies from the login form stores the ```<user_id>```. Then I store the data in the cookies to the user_id variable which involves the specific profile page. 
 

# Criteria D-Functionality
Link to the video on YouTube https://youtu.be/Vt89ADE9GAM

# Criteria E-Evaluation
## Evaluation by Client
|Success Critreria|Met?|Description|
|-----------------|---|-----------------|
|1. The website has a home page to educate users on the issue of food insecurity and food waste (issue tackled: People are unaware of the global issue)|Yes|The home page has a text section which describes the details of the situation of food insecurity and food waste and explains how the social network works to solve the issue|
|2. The website has a feed page where users can scroll through and look at the available food giveaways with the important details such as location, and general description of the food (issue tackled: People do not know the details of existing giveaways)|Yes|The users can go to the 'allposts' page which shows all the posts that have been posted with all the important details.|
|3. The website has a page for users to type in the specific details of the food they are giving away (issue tackled: Restaurants need a platform to announce giveaways)|Yes|The users can post the food they are giving away by filling out the form in the 'profile' page.|
|4. The website has a login and register system for users to post giveaways in their individual accounts(Issue tackled: Restaurants need to keep track of the foods they have donated individually)|Yes|The users can create a new accout and login to the same account. They can also look at their own profile page which has posts exclusively to the ones they posted to be organized|
|5. The website has an admin page where the admin can look at the all posts created by every users (Issue tackled: See an overview of the whole donations)|Yes|There's a '/user' page where there's a list of all usernames and the admin can look into each profiles.|
|6. The website has a green theme to remind users that the purpose of this platform is to save the world (Issue tackled: Some people might take the platform for granted if they view it as a free food platform)|Yes|There is a base template which makes sure that all the pages have a common theme with green color.|

## Evaluation by Peer

My peer have stated that they website is approaching a right direction where all the essential functions are fulfilled to solve the issue. However, they believe that it would be better if the display and aesthetics, such as transitions and animations, of the website is developed further. 

## Recommendations
### 1. Image Options
My peer recommended that the website would be better if there is a section for uploading the image of the food giveaways (see figure 3 in [Evidence of Consultation](#appendix)). Which I agree to that users might want to see images whent they look through the giveaway options. The image could also be used to tell where the giveaway location is.

### 2. Order of the post page
My client recommended that the all posts feed page would be better if the most recent post is on the top of the list. This would be better when there are a lot of posts and users want to see the most recent post for the recent giveaways.(see figure 2 in [Evidence of Consultation](#appendix))



# Appendix
## Evidence of Consultation
![IMG_7673](https://user-images.githubusercontent.com/112055062/236713666-64b71fc8-9534-4506-ab8d-e6b33f4edd47.jpg)
*Fig.1* Interview with people who are passionate about equality and the sustainability on what they think about the topics. They have identified their needs in connecting restaurants and people who are facing food insecurity.

![IMG_7699](https://github.com/aineethitari/unit4_project/assets/112055062/91842da1-4e51-4ad2-ab4f-f452d4897746)
*Fig.2* Email feedback of the full website from client

![IMG_7700](https://github.com/aineethitari/unit4_project/assets/112055062/eb232a9a-4b3f-4cf5-9486-7443c9c921b2)
*Fig.3* Email feedback of the full website from peer 

# Citation
1. H., Tania, and Vlad V. “Pros and Cons of Mobile Websites and Mobile Apps.” RubyGarage, rubygarage.org/blog/mobile-app-vs-mobile-website. 
2. Singhal, Piyush. “What Are the Advantages of HTML?” Scaler Topics, Scaler Topics, 17 Oct. 2022, www.scaler.com/topics/advantages-of-html/. 
3. “Why Use CSS?” Why Use CSS? · WebPlatform Docs, webplatform.github.io/docs/tutorials/learning_why_we_use_css/. 
4. “Learn Hub.” How Much Does Python Cost?, www.nobledesktop.com/learn/python/cost#:~:text=Python%20is%20an%20open%2Dsource,and%20libraries%20at%20no%20charge. 
5. Korsun, Julia. “The 16 Most Important Pros and Cons of Using Python for Web Development.” Software Development Blog & IT Tech Insights | Django Stars, 10 Feb. 2023, djangostars.com/blog/python-web-development/. 
6. Admin. “Advantages of Sqlite.” W3schools, 4 Aug. 2022, www.w3schools.blog/advantages-sqlite. 
7. Lara, Christopher. “5 Reasons to Use a Content Management System.” TheeDigital, 3 May 2023, www.theedigital.com/blog/top-reasons-to-use-a-content-management-system#:~:text=It%20depends%20on%20your%20specific,could%20be%20a%20better%20choice. 
8. Raval, Nihar. “NodeJS vs Python - Which Language Is Best for Backend Web Development?” Radixweb, Radixweb, 20 Apr. 2023, radixweb.com/blog/nodejs-vs-python. 
9. S., Edward. “SQLite vs Mysql – What's the Difference.” Hostinger Tutorials, 21 Dec. 2022, www.hostinger.com/tutorials/sqlite-vs-mysql-whats-the-difference/#:~:text=Multiple%20Access%20and%20Scalability%20%E2%80%93%20SQLite%20vs%20MySQL,-SQLite%20does%20not&text=MySQL%20has%20a%20well%2Dconstructed,gets%20larger%20while%20using%20SQLite. 



