# Instructions for local setup:

### Clone Repository from Github 
  * Navigate to a directory not part of a git repository
  * clone the project by executing the following command:
    * `git clone https://github.com/PhillipWitkin/newsfeed`

### Switch to the 'dockerized' branch of the repository
  * Navigate to the project root directory
    * `cd newsfeed`
  * Checkout into the 'dockerized' branch 
    * `git checkout dockerized`

### Build the Docker Containers
  * Tell Docker to build the containers
    * `docker build .`

### Start the Project Environment
  * User docker-compose to automatically start the services, perform migrations, and seed the database if it is empty: 
    * `docker-compose up`


### Restarting 
  * If the Docker containers are stopped (`docker-compose down`), they can be restarted again with `docker-compose up`
  * If you wish to re-create the state of the seeded database, run the following two commands while the services are running:
    * `docker-compose exec web python manage.py clear_db`
    * `docker-compose exec web python manage.py seed_db`
