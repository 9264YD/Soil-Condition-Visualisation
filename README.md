This is a project for soil condition inversion calculation based on pygimli and pybert, includes the source code and program documentation for the project development.

## Environment Configuration
Instructions for configuring the environment for Soil Condition Visualization:

### Install Python 3
First, make sure Python 3 is installed on your system. If it's not installed, you can download the latest version of Python 3 from the [official Python website](https://www.python.org/downloads/) and follow the installation guide.

### Install Anaconda
Anaconda is a powerful distribution of Python and other scientific computing tools. You can download and install Anaconda from the [official Anaconda website](https://www.anaconda.com/download/). Follow the installation instructions provided on the website for your specific operating system.

### Install packages in a terminal or command prompt
Below are the packages that need to be installed and the corresponding commands for environment configuration. Users can also download the  environment_config.py file from the project's GitHub repository and run the following command in the terminal or command prompt: 

```console
python3 environment_config.py
```

| Package  | Command                               |
|----------|---------------------------------------|
| Pygimli  | `conda install -c gimli pygimli`      |
|          |                                       |
| Create Virtual Environment | `conda create -n pg -c gimli -c conda-forge pygimli=1.4.3` |
| Activate Virtual Environment | `conda activate pg` |
| Pybert   | `conda install -c gimli pybert`       |
| Pip      | `apt-get update`                      |
|          | `apt-get upgrade`                     |
|          | `apt-get install python3-pip`          |
| PyQt5    | `pip install pyqt5`                   |
| Matplotlib | `pip install matplotlib`            |
| Numpy    | `pip install numpy`                   |
| Imageio  | `pip install imageio`                 |

## Features
There are 5 steps in this project:
1. Import Raw Data files and Data Preprocessing
2. Domain Selection and meshing
3. Parameters Selection and Inverse Model Computing
4. Water Content Computing
5. Results Visualization

