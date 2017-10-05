

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