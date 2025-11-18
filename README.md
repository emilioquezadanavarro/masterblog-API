## MasterBlog API

A RESTful Flask API for managing blog posts with CRUD operations, search, sorting, and rate limiting.

## Features:
- Full CRUD Operations: Create, Read, Update, Delete blog posts
- Search Functionality: Search posts by title or content
- Sorting: Sort posts by title or content in ascending/descending order
- Rate Limiting: 10 requests per minute per endpoint
- CORS Enabled: Ready for frontend integration
- In-Memory Storage: Simple data structure for easy testing

  
## API Endpoints

Method	 Endpoint	           Description	       Query Parameters
GET	   /api/posts	          Get all posts	       sort, direction
POST	 /api/posts	          Create a new post	        -
GET	   /api/posts/search	  Search posts	       title, content
PUT	   /api/posts/<id>	    Update a post	            -
DELETE /api/posts/<id>	    Delete a post	            -

## Installation
1- Clone the repository:
git clone https://github.com/emilioquezadanavarro/masterblog-API.git

2- Install dependencies:
pip install flask flask-cors flask-limiter

🏃 Running the Application

python backend_app.py
The server will start on http://127.0.0.1:5002

## 💻 Usage Examples

- Get All Posts:
GET http://127.0.0.1:5002/api/posts

- Create a Post
POST http://127.0.0.1:5002/api/posts
Content-Type: application/json

{
    "title": "My New Post",
    "content": "This is the content"
}

- Update a Post
PUT http://127.0.0.1:5002/api/posts/1
Content-Type: application/json

{
    "title": "Updated Title",
    "content": "Updated content"
}

- Delete a Post
DELETE http://127.0.0.1:5002/api/posts/1

-Search Posts
GET http://127.0.0.1:5002/api/posts/search?title=First
GET http://127.0.0.1:5002/api/posts/search?content=post

- Sort Posts
GET http://127.0.0.1:5002/api/posts?sort=title&direction=asc
GET http://127.0.0.1:5002/api/posts?sort=content&direction=desc

## 📊 Rate Limiting

All POST/PUT/DELETE endpoints are limited to 10 requests per minute per IP address.

If you exceed the limit, you'll receive a 429 Too Many Requests response.

## 🛠️ Technologies Used

Flask - Web framework
Flask-CORS - Cross-Origin Resource Sharing
Flask-Limiter - Rate limiting

## 🎓 What I Learned

This project taught me:
- How to build RESTful APIs with Flask
- HTTP methods (GET, POST, PUT, DELETE)
- Query parameters and request handling
- JSON serialization with jsonify()
- API validation and error handling (400, 404, 201, 200 status codes)
- Rate limiting for API security
- CORS configuration for frontend integration


## 📝 License
This project was created for educational purposes at Masterschool.

## Future Improvements:
- Implement Pagination: 
- Expand Data Model
- User Authorization

  




