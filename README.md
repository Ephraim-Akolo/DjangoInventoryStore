# DjangoInventoryStore
A system for an online store to manage its inventory and suppliers. The store requires an API to handle these aspects efficiently. This API will be utilized by various internal systems, including the front-end interface and the inventory tracking system.

## Server Setup

Follow these steps to get the application up and running.

**python version:: 3.11**

### Step 1: Set Up Your Environment

1. **Create a virtual environment**:
    ```sh
    python -m venv env
    ```

2. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```

### Step 2: Install Dependencies

1. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Step 3: Configure Environment Variables

1. Set the necessary environmental variables [SECRET_KEY, DATABASE_URL, ALLOWED_HOSTS (separated by whitespaces), CSRF_TRUSTED_ORIGINS (separated by whitespaces), CORS_ALLOWED_ORIGINS (separated by whitespaces), CORS_ORIGIN_ALLOW_ALL, CORS_ALLOW_CREDENTIALS, DEBUG]
3. **Ensure your `.env` file is in the root directory** if you have the `.env` file that contains all the necessary environment variables. You give the `.env` file location on the settings file where it is loaded using `dotenv` package.

### Step 4: Apply Migrations

1. **Create and apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

### Step 5: Run the Server

1. **Start the development server**:
    ```sh
    python manage.py runserver
    ```

### Access the Application

- The application is available at `http://127.0.0.1:8000/` or `http://localhost:8000/`
- Navigate to `http://127.0.0.1:8000/docs/` to interact with the interactive swagger-ui view.
