# Hobbies
## Creation of a restAPI by Flask (createAPI)

### Description  
Creation a simple restAPI in which a GET request to the below URL returns some data points coordinates (in JSON format) that changes over time.


http://127.0.0.1:5300/api/points


### Getting Started

#### Prerequisites
Install python 2.7 and pip

```
   sudo apt install python2.7 python-pip
```
Install the python libraries flask and flask-cors

```
   pip install flask=0.12.2
   pip install flask-cors
```
Additional python libraries needed 
```
   pip install json
   pip install numpy
```

#### Running

```
   cd {path_to_directory}/createAPI
   export FLASK_APP=restapi.py
   flask run --port 5300
```


## Web page to visualize data points from restAPI (data_vis_webpage)

### Description  
A simple chart to show the coordinates of three points read by an API.

### Getting Started

#### Prerequisites
Launch API by Flask (See createAPI) before opening the web page. 

#### Running

```
firefox visualize_points.html
```
#### Screenshot
![Alt text](/data_vis_webpage/screenshot/1.jpg?raw=true "Optional Title")


## License
[MIT licence](https://choosealicense.com/licenses/mit/)
