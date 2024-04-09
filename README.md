## Installation from ZIP File

To run the Technical Assessment Django Master locally using the provided ZIP file, follow these steps:

1. Download the ZIP file containing the project code and SQLite database.
2. Extract the ZIP file to a directory of your choice.
3. Navigate to the extracted directory:

   ```bash
   cd technical-assessment-django-master
   ```

1. (Optional) Activate a virtual environment for the project:

```bash
python -m venv venv
source venv/bin/activate   # On Unix/Linux
venv\Scripts\activate.bat  # On Windows
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```


3. Run the Django development server:

```bash
python manage.py runserver
```


4. Visit [127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger) in your web browser to explore the API endpoints.

If needed, you can access the live app at [Technical Assessment Django Master on Render](https://technical-assessment-django-master.onrender.com/swagger/). Please note that the service may become inactive when not in use, but it is fast and all the endpoints can be seen there.

Refer to the `.env` file provided with the project for superuser credentials.
