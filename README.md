# Hobbies
## Creation of an API by Flask (createAPI)

### Description  
A simple chart to show the coordinates of three points read by an API.

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




## License
MIT licence
