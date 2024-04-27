# This script configures and initializes an ASGI application for Django.
# ASGI (Asynchronous Server Gateway Interface) is a standard for Python asynchronous applications,
# including Django, allowing for handling more concurrent visitor connections by running 
# asynchronously. The script is typically used in the deployment of Django projects to handle 
# asynchronous tasks like handling WebSockets, chat applications, or real-time notifications.

import os  # Imports the OS module to interact with the operating system.

# Importing the get_asgi_application function from Django's core.asgi module.
# This function is responsible for creating an ASGI application instance from the Django project.
from django.core.asgi import get_asgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to specify the settings file.
# This tells Django which settings to use for this particular instance of the application.
# 'inventory.settings' should be the path to the settings file in the Django project,
# assuming 'inventory' is the name of the project directory.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory.settings')

# Calling get_asgi_application to initialize the ASGI application using the specified settings.
# The resulting 'application' object is used by an ASGI server (e.g., Daphne, Uvicorn) to serve
# the Django site. The object acts as the entry point for ASGI-compatible web servers.
application = get_asgi_application()
