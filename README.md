# chrome_selenium_error

install npm http-server to create a simple file server

`npm install http-server -g`


start it in this directory

`cd chrome_connection_refused`

`http-server`


replace the adress in `driver.get("http://10.65.194.148:8082")` with for example the first address displayed in http-server


start chrome with
`docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.8.2-20230325`


run `main.py`