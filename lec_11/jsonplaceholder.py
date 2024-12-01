import requests

def get_filtered_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        filtered_by_title = [post for post in posts if len(post['title'].split()) <= 6]
        filtered_by_body = [post for post in filtered_by_title if post['body'].count('\n') <= 3]
        
        print("Filtered Data:")
        for post in filtered_by_body:
            print(f"Title: {post['title']}, Body: {post['body']}")
    else:
        print("Failed to fetch data.", response.status_code)

def create_post():
    payload = {
        "title": "New Post",
        "body": "This is a new post created via POST request.",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    if response.status_code == 201:
        print("Post created successfully:", response.json())
    else:
        print("Failed to create post.", response.status_code)

def update_post(post_id):
    payload = {
        "title": "Updated Post",
        "body": "This post has been updated via PUT request.",
        "userId": 1
    }
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=payload)
    if response.status_code == 200:
        print("Post updated successfully:", response.json())
    else:
        print("Failed to update post.", response.status_code)

def delete_post(post_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        print("Post deleted successfully.")
    else:
        print("Failed to delete post.", response.status_code)

if __name__ == "__main__":
    print("GET Request with Filters:")
    get_filtered_data()

    print("\nPOST Request:")
    create_post()

    print("\nPUT Request:")
    update_post(1)

    print("\nDELETE Request:")
    delete_post(1)