#### Ormuco and VanHack Code Challenge

> The Question
> The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

#### My Solution

Get Started:

- Clone this repository:
```sh
$ git@github.com:jattoabdul/ABDULQAHHAR_AMINUJATTO_PythonDev.git
```
- Change into the `compare_version_strings` directory:
```sh
$ cd ABDULQAHHAR_AMINUJATTO_PythonDev
```
- Install all dependencies:
```sh
$ pip install -r requirements.txt
```
Run Test:
```sh
$ pytest
```

Run as Packaged Library:
- Install:
```sh
$ pip install jatto_compare_version_strings
```

- Usage:

````
from compare_version_strings.compare_version_strings import compare_versions, prepare_comparison_result

comparison_result = compare_versions('1.0.1', '1.0.3')

# It will return:
#     A positive number: If the first version is greater than the second  
#     A negative number: If the first version is smaller than the second
#     Zero: If the versions are equals

formated_result = prepare_comparison_result('1.0.1', '1.0.3')

# It will return:
#     '{version1}' is equal to '{version2}': If the comparison returns 0
#     '{version1}' is smaller than '{version2}': If the comparison returns -1
#     '{version1}' is greater than '{version2}': If the comparison returns 1
````

#### LICENSE

>- [MIT License](https://github.com/jattoabdul/andela-bootcamp-postit/blob/master/LICENSE)

#### Author(s)
>- [Aminujatto Abdulqahhar](https://github.com/jattoabdul)
