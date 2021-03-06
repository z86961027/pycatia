# Changelog

## 0.1.6
* Added feature to get position matrix of product. See new example 9.

## 0.1.5.1
* Attempt to fix pip installation error.

## 0.1.5
* Added unit requirement to create_points function. 
  Previously it was assumed all inputs were millimeters.
* Added missing macros file to pypi package.

## 0.1.4
* Added CATDrawing methods

## 0.1.3

* Added in_work_object method to class Part().
* Moved create_reference method to class Part(). It's proper home.
* Added find_object_by_name method to class Part().
* Added methods activate, deactivate and is_inactive to class Part().

## 0.1.2

* Added support to export files along with example.
* Updated example_3.py to show how to export the data to a csv file.

## 0.1.1

* Removed reference to CATIA V6 pre-requisite.

## 0.1.0

* Expanded tests.
* Added documentation.
* Added context manager.
* Many more changes ...

## 0.0.3

* Added ability to parse csv and create points in a CATIA part.
* Added methods to open, save, save as and close CATIA files.
* Test coverage now covers all CATMeasurable methods.
