from flask import Flask, render_template, request, redirect, url_for, make_response
from my_lib import database_worker, encrypt_password, check_password


app = Flask(__name__)

def create_database():
    query_user = """Create table if not exists users(
    id INTEGER PRIMARY KEY,
    email TEXT,
    password TEXT
    )
    """
    query_post = """Create table if not exists posts(
    id INTEGER PRIMARY KEY,
    title VARCHAR(150),
    location TEXT,
    date TEXT,
    time TEXT,
    description TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )
    """ #foreign key taking id from diff table, varchar length 150, on delete of user it will cascade and delete all posts
    db.run_save(query_user)
    db.run_save(query_post)


def create_test_user():
    users = ["john.doe@company.com","alice.doe@company.com"]
    passwords = ["querty","12345678"]
    posts = [{"title":"im john","content":"doe"},{"title":"im doe","content":"john"}], [{"title":"im alice","content":"doe"}]
    #two posts for john and 1 for alice

    for i in range(len(users)):
        user = users[i]
        pwd = passwords[i]
        posts_user = posts[i]
        query = f"INSERT into users(email,password) values ('{user}','{encrypt_password(pwd)}')"
        db.run_save(query)
        for p in posts_user:
            query_post = f"""INSERT into posts(title,location,date,time,description,user_id) values ('{p['title']}','{p['location']}','{p['date']}','{p['time']}','{p['description']}',1)"""
            db.run_save(query_post)



@app.route('/')
def landing():  # put application's code here
    return render_template("landing.html")

@app.route('/user')
def users():
    db=database_worker("social_net.db")
    all_users = db.search("SELECT * FROM users")
    print(all_users)
    return render_template("users.html",users=all_users)

@app.route('/user/<user_id>',methods=['GET','POST'])
def profile(user_id):
    if request.cookies.get('user_id'):
        print("The cookie was found")
        user_id = request.cookies.get('user_id')

    db = database_worker("social_net.db")
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        date = request.form['date']
        time = request.form['time']
        description = request.form['description']
        if len(title)>0 and len(location)>0 and len(date)>0 and len(time)>0 and len(description)>0:
            new_post = f"""INSERT into posts(title, location, date, time, description, user_id) values 
            ('{title}','{location}', '{date}','{time}','{description}','{user_id}')"""
            db.run_save(new_post)
            return redirect(url_for("profile",user_id=user_id))

    posts, user = None, None
    user = db.search(f"SELECT * from users where id={user_id}")
    requested_user = user[0] #there should only be uone user with id
    if user:
        posts = db.search(f"SELECT * from posts where user_id={user_id}")
    db.close()
    return render_template("profile.html", user=requested_user, posts=posts)

@app.route('/allposts',methods=['GET','POST'])
def allposts():
    db = database_worker("social_net.db")
    all_posts = db.search("SELECT * FROM posts")
    print(all_posts)
    return render_template("allposts.html", allposts=all_posts)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        email = request.form['email']
        passwd = request.form['passwd']
        if len(email)>0 and len(passwd)>0:
            db = database_worker('social_net.db')
            user = db.search(f"SELECT * from users where email='{email}'")
            if user:
                print(user)
                user = user[0] #search returns a ist, so select 1 here
                id, email, hash = user
                if check_password(hashed=hash, user_password=passwd):
                    resp = make_response(redirect(url_for('profile',user_id=id)))
                    resp.set_cookie('user_id',f"{id}")
                    print("password is correct")
                    return resp

    return render_template('login.html')


@app.route('/logout')
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('user_id',"",expire=0) #delete cookie
    return render_template("index.html")

@app.route('/registration',methods=['GET','POST'])
def registration():
    message=""
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
        passwd_check = request.form['passwd_check']
        if passwd_check != passwd or len(passwd_check)<8:
            message = "Password don't match"
        else:
            db = database_worker('social_net.db')
            existing_user = db.get(f"SELECT * from users where email='{email}'")
            if existing_user:
                message = "User with that email already registered. Go to Login"
            else:
                new_user = f"""INSERT into users(email,password) values(
                '{email}','{encrypt_password(passwd)}')"""
                db.run_save(new_user)
                db.close()
                print('database closed')
                return redirect(url_for('login'))

    return render_template("registration.html",msg=message)

print("Creating the database")
db = database_worker("social_net.db")
#create_database()
# create_test_user()
db.close()
if __name__ == '__main__':
    app.run()

