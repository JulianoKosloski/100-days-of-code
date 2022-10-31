# API is an interface to access data from another program or system through a series of predefined methods
# some methods, specially for the web, are standardized
# one of these standardized patterns is REST, which involves HTTP methods such as 
#POST - to submit data to the server
#GET - to access data from the server
#PUT - to update data from the server
#DELETE - to delete data from the server

#all in all, these methods allow for CRUD operations (create, request, update and delete)
#all API operations work with a request from the client (user, other machine) and a response from the server (sometimes just a simple status code)
#that's why when writing API methods most of the time the parameters will involve
# req, res and sometimes 'next', which is used by middleware to call the next function in line/stack

#API endpoint: is a path/location, a way to access data (normally an URL)

