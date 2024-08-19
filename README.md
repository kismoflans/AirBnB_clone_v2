# Project: AirBnB Clone

<p align='center'>
  <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*IEHW7v6g0-yeFJie" width=auto height=auto />
</p>

- This repository covers AirBnB Clone project in Python/Flask.

### Expected web static for the final product:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>

### Web Stack for building the product:

<p align="center">
  <img src="https://i.imgur.com/lgZnZrz.png">
</p>

### Schemas:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg">
</p>

---
### Files

File Name | Description
--- | ---
`README.md` | A description of the AirBnB Project
`AUTHORS` | A listing of the project contributors
`console.py` | The program to launch the HBNB console
`basemodel.py` | Defines the BaseModel Class
`file_storage.py` | Defines the FileStorage Class & handles the database
`user.py` | Defines the User Class, a subclass of BaseModel
`city.py` | Defines the City Class, a subclass of BaseModel
`state.py` | Defines the User Class, a subclass of BaseModel
`amenity.py` | Defines the Amenity Class, a subclass of BaseModel
`review.py` | Defines the Review Class, a subclass of BaseModel
`place.py` | Defines the Place Class, a subclass of BaseModel
`tests/` | The test directory containing the unittest files for each Class


#### Tasks

#### 0. README, AUTHORS 
Writing a README.md and highlighting the authors
#### 1. Be pycodestyle compliant!
Write beautiful code that passes the pycodestyle checks.
#### 2. Unittests
All your files, classes, functions must be tested with unit tests
#### 3. BaseModel
Write a class BaseModel that defines all common attributes/methods for other classes:
models/base_model.py
- Public instance attributes:
  - id: string - assign with an uuid when an instance is created:
      you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
      the goal is to have unique id for each BaseModel
  - created_at: datetime - assign with the current datetime when an instance is created
  - updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time   
    you change your object
-  __str__: should print: [<class name>] (<self.id>) <self.__dict__>
- Public instance methods:
    - save(self): updates the public instance attribute updated_at with the current datetime
    -  to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
        - by using self.__dict__, only instance attributes set will be returned
        - a key __class__ must be added to this dictionary with the class name of the object
        - created_at and updated_at must be converted to string object in ISO format:
            -  format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
            -  you can use isoformat() of datetime object
        - This method will be the first piece of the serialization/deserialization process: create a dictionary   
           representation with “simple object type” of our BaseModel

#### 4. Create BaseModel from dictionary
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

```class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>```


