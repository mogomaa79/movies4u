# Project Proposal: Movies4U

## 1. Introduction

Movies4U is a web application designed to provide users with a platform for discovering, tracking, and getting recommendations for movies. Users can browse an extensive catalog of films, manage personal watchlists and watched lists, search for specific titles, and receive personalized movie suggestions. The application aims to offer a seamless and engaging user experience for movie enthusiasts.

## 2. Core Features

Based on the existing codebase ([final/views.py](capstone/final/views.py), [final/urls.py](capstone/final/urls.py), [final/static/final/index.js](capstone/final/static/final/index.js), [README.md](README.md)), the application implements the following features:

*   **User Authentication:** Secure user registration, login ([final/templates/final/login.html](capstone/final/templates/final/login.html)), and logout functionality.
*   **Film Browsing:** An index page ([final/views.py#L14](capstone/final/views.py#L14)) displaying movies, potentially with infinite scrolling ([final/static/final/index.js#L312](capstone/final/static/final/index.js#L312)) to load more films dynamically.
*   **Film Details:** Ability to view detailed information about a specific film ([final/views.py#L39](capstone/final/views.py#L39)).
*   **Search Functionality:** Users can search for movies by title ([final/views.py#L61](capstone/final/views.py#L61), [final/static/final/index.js#L242](capstone/final/static/final/index.js#L242)).
*   **Watchlist Management:** Users can add films to a personal watchlist and view their watchlist ([final/views.py#L78](capstone/final/views.py#L78), [final/static/final/index.js#L192](capstone/final/static/final/index.js#L192)).
*   **Watched List Management:** Users can mark films as watched and view their watched list ([final/views.py#L99](capstone/final/views.py#L99), [final/static/final/index.js#L215](capstone/final/static/final/index.js#L215)).
*   **Movie Recommendations:** The application provides movie recommendations to logged-in users ([final/views.py#L139](capstone/final/views.py#L139), [final/static/final/index.js#L270](capstone/final/static/final/index.js#L270)), likely based on their watched history or preferences using techniques like K-Nearest Neighbors ([README.md#L38](README.md#L38)).
*   **Data Scraping:** Initial movie data appears to be sourced via web scraping ([films.ipynb](capstone/films.ipynb)).

## 3. Technology Stack

The project utilizes the following technologies:

*   **Backend Framework:** Django ([capstone/settings.py](capstone/capstone/settings.py))
*   **Programming Language:** Python
*   **Frontend:** HTML, CSS, JavaScript ([final/static/final/index.js](capstone/final/static/final/index.js))
*   **Database:** Django ORM with a configured database (likely SQLite by default, check [capstone/settings.py](capstone/capstone/settings.py))
*   **Asynchronous Server Gateway Interface:** ASGI ([capstone/asgi.py](capstone/capstone/asgi.py))
*   **Web Server Gateway Interface:** WSGI ([capstone/wsgi.py](capstone/capstone/wsgi.py))

## 4. Project Structure

The project follows a standard Django structure:

*   `capstone/`: Main Django project directory containing settings ([capstone/settings.py](capstone/capstone/settings.py)), main URLs ([capstone/urls.py](capstone/capstone/urls.py)), WSGI ([capstone/wsgi.py](capstone/capstone/wsgi.py)), and ASGI ([capstone/asgi.py](capstone/capstone/asgi.py)) configurations.
*   `final/`: Django application directory containing models ([final/models.py]), views ([final/views.py](capstone/final/views.py)), app-specific URLs ([final/urls.py](capstone/final/urls.py)), templates ([final/templates/final/](capstone/final/templates/final/)), static files ([final/static/final/](capstone/final/static/final/)), and migrations ([final/migrations/](capstone/final/migrations/)).
*   `films.ipynb`: Jupyter Notebook for data scraping ([films.ipynb](capstone/films.ipynb)).
*   `manage.py`: Django's command-line utility.
*   `README.md`: Project documentation ([README.md](README.md)).
*   `requirements.txt`: List of Python dependencies (assumed based on standard practice, mentioned in [README.md#L57](README.md#L57)).

## 5. Setup and Deployment

Refer to the [README.md#L41](README.md#L41) for detailed setup instructions, including cloning the repository, setting up a virtual environment, installing dependencies, running migrations, and starting the development server.

## 6. Potential Future Enhancements

*   User reviews and ratings for films.
*   More advanced search filters (genre, director, actors, year).
*   Social features (e.g., sharing watchlists, following users).
*   Integration with external movie APIs for richer data.
*   Admin interface improvements for managing films and users.
*   Enhanced recommendation algorithms.
