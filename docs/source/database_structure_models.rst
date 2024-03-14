Database Structure and Models
=============================

Database Structure
-------------------

The Lettings Web Application uses SQLite3 as its default database backend. SQLite3 is a lightweight, serverless, self-contained, and zero-configuration SQL database engine. It stores the entire database as a single file on disk, making it suitable for small to medium-sized applications.

SQLite3 Specifics
-----------------

- **Serverless**: Unlike client-server database management systems, SQLite3 does not require a separate server process to operate. It reads and writes directly to ordinary disk files.
- **Self-contained**: SQLite3 databases are self-contained, meaning they can operate without requiring any external dependencies or configuration files.
- **Zero-configuration**: SQLite3 does not require any setup or administration. It does not have a separate server process, and there is no need to configure access control or permissions.

Models
------

Address Model
~~~~~~~~~~~~~

A model representing a physical address.

+-------------------+--------------------------------------+
| Attribute         | Description                          |
+===================+======================================+
| number            | PositiveIntegerField                |
|                   | The street number of the address.    |
+-------------------+--------------------------------------+
| street            | CharField                            |
|                   | The name of the street.              |
+-------------------+--------------------------------------+
| city              | CharField                            |
|                   | The city where the address is located|
+-------------------+--------------------------------------+
| state             | CharField                            |
|                   | The state where the address is located|
|                   | (abbreviated).                       |
+-------------------+--------------------------------------+
| zip_code          | PositiveIntegerField                |
|                   | The ZIP code of the address.         |
+-------------------+--------------------------------------+
| country_iso_code  | CharField                            |
|                   | The ISO code of the country where    |
|                   | the address is located.              |
+-------------------+--------------------------------------+

Letting Model
~~~~~~~~~~~~~

A model representing a letting property.

+------------+---------------------------------------------+
| Attribute  | Description                                 |
+============+=============================================+
| title      | CharField                                   |
|            | The title of the letting.                   |
+------------+---------------------------------------------+
| address    | OneToOneField                               |
|            | The address associated with the letting.    |
+------------+---------------------------------------------+

Profile Model
~~~~~~~~~~~~~

This model extends the built-in User model provided by Django to store additional user-related information.

+----------------+--------------------------------------------+
| Attribute      | Description                                |
+================+============================================+
| user           | OneToOneField                              |
|                | The associated user object.                |
+----------------+--------------------------------------------+
| favorite_city  | CharField                                  |
|                | The user's favorite city (optional).       |
+----------------+--------------------------------------------+
