# Email Design Delivery
1. Productive solution for connecting with people.
   Applications features:
   * Create Contacts.
   * Create Groups.
   * Design Customize Templates.
   * Send Email Templates.
   * Track Emails.


## Installation Instructions

1. Clone the project.
    ```shell
    $ git clone https://github.com/tinktankin/myMsg.git
    ```
2. `cd` intro the project directory
    ```shell
    $ cd myMsg
    ```
3. Create a new virtual environment using Python 3.7 and activate it.
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
4. Install dependencies from requirements.txt:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
5. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```
6. Run the local server via:
    ```shell
    (env)$ python manage.py runserver
    ```