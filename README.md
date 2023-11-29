# Security / Python Homework - SBOM
The main file of the repository is the sbom.py file, the rest of the files are files that are used to run the program or are produced by sbom.py file. The sbom file is used to find the different dependencies of a system. The different dependencies are found in the requirement.txt and package.json files that are found in the subdirectories of the specified directory—the specified directory is specified is specified when running the file. The sbom.py is run with
```console
python3 sbom.py path_to_directories
```
Where the path_to_directories is the path to the directory that contains the subdirectories with the packages. The program than produces a csv file with the format
| name      | version | command | absolute path |
| ----------- | ----------- | ----------- | ----------- |
| mender-gui/home/hkonyehaugmoe/Work_Nortech/gui/package.json      | 1.0.0 | npm | /home/hkonyehaugmoe/Work_Nortech/gui/package.json |
|apache-libcloud|3.3.1|pip|/home/hkonyehaugmoe/Work_Nortech/cf-remote/requirements.txt|

And for each of the subdirectories there are made sbom.json files that contains the the information for the corresponding row.