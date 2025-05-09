# Ex.05 Design a Website for Server Side Processing
# Date: 12.04.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
I --> Intensity
R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
views.py 

from django.shortcuts import render
def power(request):
	if request.method=="POST":
		intensity_value=int(request.POST.get("intensity"))
		resistance_value=int(request.POST.get("resistance"))
		power=(intensity_value**2)*resistance_value
		return render(request,'power.html',{"output":power})
	return render(request,'power.html')

```
```
power.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            color:rgb(20, 126, 219);
        }
        label {
            color: rgb(8, 6, 3);
            font-size: 150%;
            }
        input {
            font-size: 150%;
        }
        button {
            font-size: 150%;
        }
        p {
            color: rgb(21, 16, 2);
            font-size: 200%;
            }
        body {
            background-color: #cccccc;
        }

        h1{
            border: 2px solid black;
            padding: 20px;
            margin: 10px;
            border-radius: 5px;
            position: fixed;
            top: 200px;
            right: 500px;
            font-size: xx-large;
            font-weight: bolder;
            font-variant: small-caps;
            background: linear-gradient(to bottom,rgb(176, 203, 54),white,rgb(103, 109, 35));
            font-family: Georgia, 'Times New Roman', Times, serif;
            color: grey;
        }
        form{
            border: 2px solid black;
            background-color: rgba(128, 128, 128, 0.064) ;
            padding: 30px;
            margin: 10px;
            border-radius: 10px;
            width: 425px;
            position: fixed;
            top: 300px;
            left: 527px;
        
            background-size: 60%;
            background-repeat: no-repeat;
            background-position: left;
            
        }


    </style>
</head>
<body>
    <h1 align="center">CALCULATION OF POWER</h1>
    <form action="{% url 'power' %}" method="POST">
        {% csrf_token %}
        <label>Intensity: </label>
        <input type="number" name="intensity">
        <br>
        <br>

        <label>Resistance: </label>
        <input type="number" name="resistance">

        <br>
        <br>
        <br>


        <button type="submit">Calculate</button>
        <p align="center">The Power of the lamp is: {{ output }}</p>
    </form>
</body>
</html>

```
```
urls.py

from django.contrib import admin
from django.urls import path
from powerapp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.power,name='power'),
]
```
# OUTPUT:
![alt text](<Screenshot 2025-04-21 160747.png>)
![alt text](<Screenshot 2025-04-21 160720.png>)


# RESULT:
The program for performing server side processing is completed successfully.
