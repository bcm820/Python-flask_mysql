

#########################
# FORM VALIDATION PT. 2 #

    # How do you check whether an email address is valid? You use regular expression (regex). A regex is a sequence of characters that defines a search pattern. Email follows a strict pattern with some characters followed by @ symbol, more characters, a ., and then more characters. Let's look at how to implement regex with this pattern.
    
    # First, we need to import the 're' module that will let us perform regex operations:

        import re

    # And we need to create a regex object that we can run operations on:

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    # Next, here's our basic validation conditional, along with where we want to include the regex:

        def submit():
            if len(request.form['email']) < 1:
                flash("Email cannot be blank!")
            # else if email doesn't match regex, display "invalid email address" message
            else:
                flash("Success!")
            return redirect('/')

    # Here's how it should look at the end:

        @app.route('/process', methods=['POST'])
        def submit():
            if len(request.form['email']) < 1:
                flash("Email cannot be blank!")
            # Here we use the EMAIL_REGEX object we created and running the .match() method that will return NONE if no match can be found. If the argument matches the regex, a match object instance is returned.
            elif not EMAIL_REGEX.match(request.form['email']):
                flash("Invalid Email Address!")
            else:
                flash("Success!")
            return redirect('/')

    # Also, here is a list of useful validation tools:

            str.isalpha()    # Return true if all characters are alphabetic and at least one char
            str.isalnum()    # Return true if all characters are alphanumeric and at least one char
            str.isdigit()    # Return true if all characters are digits and and at least one char
            str.istitle()    # Return true if string is titlecased and at least one char

    # Lastly, here's how to change a string to time using the given format:

            time.strptime(string, format)


#########################

#########################
# FORM VALIDATION PT. 1 #

    # Form validation is key for any back-end developer. Here are important concepts:
        # Logic: What data do we want to validate?
        # Checking if the data is present
        # Making sure the data is in the correct format
        # Sending the user to the correct destination whether their data is valid or not
        # Alerting the user of their errors (if they exist)

    # IF/ELSE: If we have clean data, then we can proceed. But if the user inputs unclean data (e.g. injections), then we can't proceed and need to do something else. We need to use IF statements with functions that return True or False depending on if the data given is valid.

    # To check if a name field is empty, use len():

        @app.route('/process', methods=['POST'])
        def process():
        if len(request.form['name']) < 1:
            # display validation errors
        else:
            # display success message

    # To display validation errors, use flash messages that only last for one cycle:

        from flask import flash

        def process():
            if len(request.form['name']) < 1:
                flash("Name cannot be empty!")
            else:
                flash("Success, {}!".format(request.form['name']))
            return redirect('/')
                
    # Note- You must include a redirect to the page to view the flash message

    # You can also use a function called 'get_flashed_messages()' get all flash messages as a list.This function is actually run on your HTML template, but using Flask's Python-like code:

        {% with messages = get_flashed_messages() %}    # declare a var to use within a specific scope
          {% if messages %}                             # check if there are messages
            {% for message in messages %}               # loop through all messages
              <p>{{message}}</p>                        # prints messages one by one in a paragraph tag
            {% endfor %}
          {% endif %}
        {% endwith %}    

    # You can also provide categories when flashing a message. Alternative categories can be used to give the user better feedback. Note the following in the server file and on the HTML page:

        # The first line is the string, the second is the category
        flash(u'Invalid password provided', 'error')
        
        # You can specify a different style class based on different categories
        {% with messages = get_flashed_messages(with_categories=true) %} # specify with categories
        {% if messages %}
            <ul class=flashes>
            {% for category, message in messages %}
            <li class="{{ category }}">{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
        {% endwith %}

        # Optionally, you can pass place separate categories in different locations on your HTML page:
        {% with errors = get_flashed_messages(category_filter=["error"]) %}
        {% if errors %}
            {%- for msg in errors %}
            <p>{{ msg }}</p>
            {% endfor -%}
        {% endif %}
        {% endwith %}

#########################

############
# SESSIONS #

    # Data can be passed between routes. But this is a challenge for HTTP req/res cycle, which treats each cycle instance independently. How do developers enable data to persist from one cycle to the next in order to know who is logged in, what links a user has clicked, etc.?

    # Flask uses cookies, securely hashed session data, stored as packet data on a client's computer. Doing this involves performance and security compromises, so we shouldn't use it for handling sensitive data. But it will work for persisting general data.

    # Add 'session' to your list of imports on the top of your server file:

        from flask import Flask, render_template, request, redirect, session

    # Next, under the creation of your 'app' object, initialize a secret key:

        app = Flask(__name__)
        app.secret_key = 'Use_a_secret_phrase_here'

    # Then, in your handler function for the route using the POST method, add:

        session['name_of_input'] = request.form['name_of_input']
        # This variable stores input data as persistent session data

        return redirect('/result')
        # Redirect to another route where you will render a page with session data!

    # In the handler function for the route where you will show the results:

        return render_template('page.html', name_of_input=session['name_of_input'])
        # Add all your session data fields here in your render template
        # To include in the template, add as {{name of input}}

    # OR, instead of passing the session data in using arguments, you can:

        <p>{{session['name_of_input']}}</p>
        # Simply add the session data straight into your HTML template!

    # In addition to user inputs, you can also code hidden input fields into your HTML pages that can be used to transfer session metadata to your server and into other pages:

        <input type='hidden' name='action' value='register'>
        <input type='hidden' name='action' value='login'>
        # You can name these input types whatever you want

        # Having hidden inputs can be used to trigger server-side events in your code:

            if request.form['action'] == 'register':
                # "do registration process"
            elif request.form['action'] == 'login':
                # "do login process"

        # But note that these 'hidden' form inputs are viewable in the page's source! So be very careful in choosing what data is stored as values and what input your server-side code responds to.

############

################
# STATIC FILES #

    # In Flask, static files (non-templates) are stored in the 'static' dir. These include non-rendered HTML pages, CSS, JavaScript files, etc, as well as media. They are accessed as follows:

        # CSS:
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">

        # JavaScript
        <script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>

        # Images
        <img src="{{ url_for('static', filename='img/photo.png') }}">

    # Note that, although Flask knows static files are in the static dir, you must specify it still.
    # For organization purposes, you should created sub-directories (e.g. css, js, img)


################

#############
# TEMPLATES #

    # For more info, visit Jinja2 doc: http://jinja.pocoo.org/docs/dev/templates/
    
    # In our server file, we are able to print info to our page templates like this:
        return render_template("page.html" NAME="Bob")
    
    # Then, on our HTML templates pages, we are able to input the info using the following format:
        <p>My name is {{ NAME }}</p>
        # Since name is defined in render_template(), it prints "Bob" onto the page.

    # Following this format, you can insert Python-like code into your Flask templates:
        <p>{{ some_variable }}</p>
        <p>{% some_expression %}</p>
        # Flask will render the page with your input (variables or expressions)

    # Here is an example of server code and its Flask template output:

            return render_template("index.html", phrase="hello", times=5)

            <p>Phrase: {{ phrase }}</p> # Output a string
            <p>Times: {{ times }}</p>   # Output an integer

    # But also, you can insert Python-like code directly into your Flask templates.

        # For example, here is a FOR loop:
            {% for x in range(0,times): %}
            <p>{{ phrase }}</p>             # Prints 5 paragraphs with "hello"
            {% endfor %}                    # Notice end of FOR loop

        # And here is an IF statement:
            {% if phrase == "hello" %}
            <p>The phrase says hello</p>
            {% endif %}                     # Notice end of IF statement

    # BUT OF COURSE, you don't want to do a lot of your logic in your templates. It's much better to put your logic into your server-side code. Otherwise, you will slow down server response time.


#############

####################
# ADVANCED ROUTING #

    # You can also handle routing based on parameters entered into your handler function via the URL. To do this:
        @app.route('/users/<USERNAME>')
            def show_user_profile(USERNAME):
            return render_template("user.html")
            # user.html displays unique USERNAME
            # later on we'll get into how this works

    # The placeholder, designated in <> tags, matches the argument passed into the handler function. This argument can be used as a variable within your templates.

    # With the placeholder, you can rely on just one handler function to route the browser based on what's passed into the function:
        @app.route('/<arg>')
        def handler(arg):
    
        # render a particular template
        if arg == "profile":
            return render_template("profile.html")

        # retrieve some records from the database    
        if arg == "records":
            return render_template("data.html")

    # Combining these, you can create AS MANY variables as you'd like to use in the URL as long as you create parameters in your function for them.
        @app.route('/users/<first>/<last>/<id>')

        def handler(first, last, id, photo_gallery):
            return render_template("profile.html")
            # profile.html can display unique first, last, id, etc. for particular user (or whatever)



####################

#########
# FORMS #

    # When using forms, be sure to import request and redirect
        from flask import Flask, render_template, request, redirect
    
    # When a user fills out a form, all the data is routed to a directory via the POST method:
        @app.route('/form', methods=['POST'])
        # Note- 'method_s_' because we can list more than one value

    # On the page (located in root, or '/'), the form tag is declared as:
        <form action='/form' method='post'>
        # Remember, a form has two components: action/route and method.
    
    # From there, your various inputs on the page can be interacted with on the back-end:
        request.form['name_of_input']
        
        # The name of input on the server file matches its name on the HTML page: e.g.
        request.form['EMAIL']
        <input type='text' name='EMAIL'>

        # You can then store and interact with the form input as data for your app!
        my_data = request.form['name_of_input']

        # You can also print it to the console running the server:
        print request.form
        print request.form['name_of_input']
        print my_data   # after storing the input into my_data

        # Note- Input via request.form() will always translate into a string

    # REDIRECTING IS IMPORTANT: You must redirect to avoid repeat submits of data

    # Here is a template for forms:

        # success is the redirect after form submission
        @app.route('/success')
        def success():
            return render_template("success.html")

        # the actual form submission route
        @app.route('/users', methods=['POST']) # unless GET, we must define method
        def create_user():

            # set vars to form input
            name = request.form['name']
            email = request.form['email']
            print name
            print email

            # redirect user back to '/' route
            # MUST use redirect, or otherwise user can resubmit form data via refresh
            return redirect('/success')

#########

################
# HTTP METHODS #

    # GET: Requests a response in the form of a page returned to your browser when you type in a URL.
    
        # This GET method can also enter a URL as a result of a form (e.g. search engines).
            # e.g. https://www.google.com/?gws_rd=ssl#q=ninjas
            # Search engine submission, 'ninjas' inputted into Google search

        # Pages accessed via GET can be bookmarked, stored in our browser history, and our cache.

    # POST: Requests a response via secure channels that can't be duplicated by a URL query string.
    
        # Forms mainly use POST to pass sensitive data in the HTTP request message body.
        # POST requests are not cached, not saved in history, can't be bookmarked, and can't be reproduced.

    # PUT, PATCH, DELETE: Exist for the design of APIs. Not supported methods in your HTML code, and only work when being handled by JavaScript AJAX requests. We'll learn about these methods later when talking about RESTful APIs.


################

######################
# HTTP METHOD: "GET" #

    # Add a 'templates' directory alongside 'hello.py'. It's how Flask knows where to look for all your HTML documents.

    # In your program, 'hello_world', you write the following to return the rendered HTML that exists in 'templates' dir:

        return render_template('index.html')

    # This is generally how you add GET routes that serve individual pages:

        return render_template('<html file>')
    
    # Whenever a route is not explicitly mentioned, it is a GET route.

######################

################
# BASIC ROUTES #

    # Routes are handlers for particular HTTP requests.
    
    # Writing a route is like assigning a variable, but to a request.
    # A route tells the server what kind of info the client needs.
    # The route on our server points toward instructions on how to interpret the data being sent, the operations that need to be completed, and the response that should be sent back.

    # Every route has two parts:
        # 1. HTTP method (GET, POST, PUT, PATCH, DELETE)
        # 2. URL

    # Generic routes are written as follows:
        @app.route('/some_route')   # sets route as 'localhost:5000/some_route'
        def function_name():
            return render_template('some_page.html')
            # when request is sent to some_route, some_page.html is rendered

    # Note- If you only have one route, it should be to '/'

################

##################
# INTRO TO FLASK #

    # Import Flask to allow us to create our app.
    # Also import render_template to allow us to render our HTML.
    from flask import Flask, render_template

    # Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module. 'app' represents our web app. We use this variable to attach routing rules for our app.
    app = Flask(__name__)

    # The "@" symbol designates a "decorator" which attaches the function immediately following it to the '/' route.
    @app.route('/')
    # Whenever we send a request to localhost:5000/ it will run the function.

    def hello_world():  # function attached to @app.route('/')
    
    # Renders HTML in 'templates' dir and returns it
    return render_template('index.html')

    app.run(debug=True) # Run the app in debug mode.

##################

##############
# VIRTUALENV #

    # Install: 'pip install virtualenv'

    # Setup an environment:
        # Navigate to parent dir of intended virtual env dir
        # 'virtualenv <dirname>

    # Activate:
        # While in parent dir of virtual env dir
        # 'source <dirname>/bin/activate

    # Install Flask into active virtualenv: 'pip install flask'

##############