
##############
# FORMS PT.2 #

    # W

##############

##############
# FORMS PT.1 #

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

        # Note- Whatever is entered in via request.form() will be a string no matter what

    # REDIRECTING IS IMPORTANT: You must redirect to avoid data being handled more than once!

##############

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

    # See accompanying 'example.py'

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