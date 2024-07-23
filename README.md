# Blog Application using Django framework

## Setup

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run migrations using `python manage.py migrate`.
4. Create a superuser using `python manage.py createsuperuser`.
5. Run the server using `python manage.py runserver`.

## API Endpoints
### Posts
- `GET /api/posts/`: List all posts.
- `POST /api/posts/`: Create a new post.
- `GET /api/posts/<id>/`: Retrieve a specific post.
- `PUT /api/posts/<id>/`: Update a specific post.
- `DELETE /api/posts/<id>/`: Delete a specific post.

### Comments
- `GET /api/posts/<post_pk>/comments/`: List comments for a specific post.
- `POST /api/posts/<post_pk>/comments/`: Create a new comment for a specific post.

## Authentication

Use JWT tokens for authentication. Obtain tokens from `/api/token/` and refresh from `/api/token/refresh/`.


Testing the API
0.	Access the API at http://127.0.0.1:8000/api/ and the admin site at http://127.0.0.1:8000/admin/.
1.	Obtain a token by sending a POST request to /api/token/ with your username and password.
2.	Use the token to authenticate by including it in the Authorization header of your requests.
3.	Test the Post and Comment endpoints using tools like Postman or curl.
This setup provides a basic blog application with Django, Django REST Framework, and token-based authentication.
