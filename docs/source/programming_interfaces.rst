Programming Interfaces
=======================

The application provides various programming interfaces to streamline development and management tasks. Below is a breakdown of the available interfaces:

1. Django Shell
----------------
The Django shell allows interaction with the Django project and its models. To access the Django shell, run the following command in the project's root directory:

.. code-block:: bash

   python manage.py shell

In the Django shell, you can perform various tasks, including:

- Interact with Django models to create, read, update, and delete (CRUD) data.
- Test database queries and model methods interactively.
- Perform custom data manipulation and management tasks.

2. Management Commands
-----------------------
Django provides a set of management commands for performing administrative tasks. These commands are invoked via the ``manage.py`` script and include operations such as:

- Creating a superuser: Use the command ``python manage.py createsuperuser`` to create a new administrative user.
- Running database migrations: Execute ``python manage.py migrate`` to apply pending migrations and update the database schema.
- Managing static files: Commands like ``collectstatic`` help gather static files from various locations into a single location.

[Django manage.py documentation](https://docs.djangoproject.com/en/5.0/ref/django-admin/)