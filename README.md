<h1 align="center"> Squirrel-Tracker 

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDmxds7w_jy3_ZUSU7n9mxwqa-EwfldIOv0kIfusMwLYt7OYeY&s.jpg)
</h1>
<h4 align="center">Squirrel Tracker is a web based application, built with the Django framework, designed to track squirrel sightings in Central Park, New York. The web application imported data from the  <a href="https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw">2018 Central Park Squirrel Census</a> and allows a user to add, update, and view squirrel data. 
</h4>

## Project Features:
### Management commands:
    * Import: A command that can be used to import the data from the 2018 census file.
    * Export: A command that can be used to export the data in CSV format.
### Supported fields for the sightings:
    * Latitude
      - Integer Field
    * Longitude
      - Integer Field
    * Unique Squirrel ID
      - Character Field
    * Shift
      - Character Field
    * Date
      - DateTime Field
    * Age
      - Like: 'Adult', Juvenile'
    * Primary Fur Color
      - Like: 'Black', 'Cinnamon', 'Gray'
    * Location
      -  Like: 'Ground Plane', 'Above Ground'
    * Specific Location
      - Like: 'under a tree', 'on tree root', 'Branch', 'tree', etc.  
    * Running
      - Boolean Field
    * Chasing
      - Boolean Field
    * Climbing
      - Boolean Field
    * Eating
      - Boolean Field
    * Foraging
      - Boolean Field
    * Other Activities
       - Like: 'Wrestling With Mother', 'Moving Slowly', 'Gathering Acorns', etc.
    * Kuks
      - Boolean Field
    * Quaas
      - Boolean Field
    * Moans
      - Boolean Field
    * Tail flags
      - Boolean Field
    * Tail twitches
      - Boolean Field
    * Approaches
      - Boolean Field
    * Indifferent
      - Boolean Field
    * Runs from
      - Boolean Field

## Web Application Features
- [x] All
    + A view where a user can select between viewing the maps, stats or adding/updating a squirrel sighting
    + Location: */squirrel_sightings/*
- [x] Edit
    + A view to update a particular sighting. 
    + Location: */sightings/<unique_squirrel_id>/edit*
- [x] Add
    + A view to create a new sighting. 
    + Location: */sightings/add*
- [x] Stats
    + A view with general stats about the sightings.
    + Location: */squirrel_sightings/stats*
- [x] Map
    + A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map
    + Location: */map*
    
## Web Application Demo 
### The main page
![Screenshot](5.png)
### Edit page
![Screenshot](4.png)
### Add page
![Screenshot](3.png)
### Stats page
![Screenshot](2.png)
### Map View page
![Screenshot](1.png)

### Project Group and UNI
    * Project Group 14, Section 1
    * UNI: adj2141, rv2428

