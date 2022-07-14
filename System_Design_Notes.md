# System Design Criteria

### Displaying at least one image
- The current database schema includes a table for Pictures with a many-to-many relationship with Articles
- The current model does not configure this table, so in order to support displaying at least one image,
the table fields must be specified by the Picture model, migration to revise the database schema, adding any new fields 
to the creation form, and add some logic to the ArticleCreateView which saves picture data (probably utilizing a URL), as a new Picture (if it does not already exist in the database), along with its relationship to one or more Articles 

### Able to accommodate 1M+ requests per day for a viral story
- The application is currently running with the development server that comes with Django, and it would not be suitable for Production particularly with such a large spike in requests.
- We would need to select a more robust server such as Nginx or Apache which can process far more requests in a shorter time. Nginx might be the better choice for high traffic, and Django would need to be configured for WSGI or ASGI
- The application is already containerized using Docker, which can be run in Production using a server like Nginx as well. 
- It may be worth considering Kubernetes if the application is expected to increase in traffic, since its distributed architecture could help with load balancing and scalability