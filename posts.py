from logging import exception
from database import session as db, Listing

class PostHandler():
    
    def getPosts():
        posts = []
        cursor = db.execute('SELECT * FROM listings')
        for post in cursor:
            posts.append(post)
        return posts
    
    def createPost(user, title, description, price, image_url):
        if user:
            post = Listing(creator=user.id, title=title, description=description, price=price, image_url=image_url)
            db.add(post)
            try:
                db.commit()
                return {'status': True}
            except exception as e:
                print(e)
                db.rollback()
        return {'status': False}