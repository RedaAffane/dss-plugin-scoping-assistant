"""
Backend entry point for the Scoping Assistant webapp.
"""

from scoping_assistant.flask_app import create_app


def create_webapp():
    """Create the webapp instance"""
    app = create_app()
    return app


# Create the app instance
app = create_webapp() 