# Movies4U

Movies4U is a Django-based web application that provides a platform for users to browse, search, and add movies to their watchlist. The application uses a combination of Python, Django, HTML, CSS, and JavaScript to provide a seamless user experience.

## Project Structure

The project is structured as follows:

- **`capstone/`**: The main Django project directory.
- **`final/`**: The Django application directory.
- **`films.ipynb`**: Jupyter notebook used for scraping movie data.
- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`requirements.txt`**: Contains the Python dependencies required for the project.

### Key Files

- **`models.py`**: Contains the `User` and `Film` models.
  - `User`: Inherits from Django's `AbstractUser` and includes a `watchlist` field with a many-to-many relationship with the `Film` model.
  - `Film`: Represents the information of the films.

- **`views.py`**: Contains all the backend logic of the project.
  - Defines views for displaying the index page, handling film retrieval, search functionality, watchlist management, and user authentication.

- **`urls.py`**: Contains all the paths of the app.
  - Paths include film retrieval, search, login, logout, registration, and watchlist management.

- **`templates/final/index.html`**: The main application page.
  - Extends the layout and includes sections for the navbar, film information, film display, watchlist display, and search.

- **`templates/final/layout.html`**: Contains the layout of the app.
  - Includes links to the JavaScript and CSS files of the app.

- **`static/final/index.js`**: Contains JavaScript functions for managing the interface of the app.
  - Functions include adding films to the watchlist and displaying film information.

- **`films.ipynb`**: Contains the logic for scraping movie data from the web.
  - Defines a function for requesting and parsing film data, and writes the data to a JSON file.

## Setup

To set up the project, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/movies4u.git
    cd movies4u
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django migrations:

    ```sh
    python manage.py migrate
    ```

5. Start the Django development server:

    ```sh
    python manage.py runserver
    ```

## Usage

### User Registration and Authentication

1. **Register**: Create a new user account by navigating to the registration page and filling in the required details.
2. **Login**: Access your account using your username and password.

### Browsing and Searching Films

1. **Browse Films**: View a list of films on the main page after logging in.
2. **Search Films**: Use the search functionality to find specific films by entering keywords.

### Managing Watchlist

1. **Add to Watchlist**: Add films to your watchlist by clicking the appropriate button next to each film.
2. **View Watchlist**: Access your watchlist to see the films you've added.
3. **Remove from Watchlist**: Remove films from your watchlist by clicking the appropriate button next to each film.

### Managing Watched List

1. **Add to Watched List**: Mark films as watched by clicking the appropriate button next to each film.
2. **View Watched List**: Access your watched list to see the films you've marked as watched.
3. **Remove from Watched List**: Remove films from your watched list by clicking the appropriate button next to each film.

### Recommendations

1. **View Recommendations**: Get personalized film recommendations based on your watched list.

## Contributing

Contributions are welcome. Please submit a pull request with your proposed changes.


