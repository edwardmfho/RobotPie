[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=plastic)

<br />
<p align="center">
  <a href="https://github.com/edwardmfho/RobotPie">
    <img src="https://cdn.onlinewebfonts.com/svg/img_504359.png" height="100">
  </a>

  <h3 align="center">RobotPie - The next generation simple robot companion</h3>

  </p>
</p>

<p align="center">
  Classify web pages with NLP
    <br />
    <a href="https://github.com/edwardmfho/RobotPie"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/edwardmfho/RobotPie">View Demo</a>
    ·
    <a href="https://github.com/edwardmfho/RobotPie/issues">Report Bug</a>
    ·
    <a href="https://github.com/edwardmfho/RobotPie/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contact](#contact)
* [Known Issues](#known-issues)

<!-- ABOUT THE PROJECT -->

## About the Project

It could be a lonely world, so why don't we build ourselves a robotic friend? This is an on-going robotic project built using Raspberry Pi and Python. By leveraging computer vision, nlp and robotic techniques, we would able to create a cost-effecitve, and interactive robot for everyone.
<!-- GETTING STARTED -->

## Getting Started
To get started, please follow the below guidelines on prerequisites and installation.

<!-- PREREQUISITES -->

### Prerequisites
* OpenCV==4.4.0
* Numpy==1.18.2
* WebCam
* RaspberryPi (Optional at this stage)

<!-- INSTALLATION -->

### Installation
1. First fork and star this repo
2. Create a folder on your machine for your project
2. Inside the folder right-click and select Git Bash Here
3. Git clone this repo into the folder by running the below command
```sh
git clone https://github.com/edwardmfho/RobotPie.git
```

<!-- USAGE -->

## Usage
1. If you haven't done so before, download the [YOLOv3 weights](https://pjreddie.com/media/files/yolov3.weights) and the [cfg file](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg), and modify its corresponding path using a config.py file. 
2. Make sure your web cam is connected and in console enter the following
```sh
python obj_detection.py
```

<!-- TO DO -->
## To-Do or New Release:

1. I would be looking to start adding integration of Raspberry Pi, implementing actuators (wheels) and a person-following function.



<!-- CONTRIBUTING -->

## Contributing
I welcome anyone to contribute to this project so if you are interested, feel free to add your code.
Alternatively, if you are not a programmer but would still like to contribute to this project, please click on the request feature button at the top of the page and provide your valuable feedback.

<!-- CONTACT -->

## Contact
* [Edward Ho](https://github.com/edwardmfho)

<!-- KNOWN ISSUES -->

## Known Issues
* TinyYOLO, a lighter model cannot detect objects due to possible issue with parameters settings. 

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/edwardmfho/RobotPie.svg?style=flat-square
[contributors-url]: https://github.com/edwardmfho/RobotPie/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/edwardmfho/RobotPie.svg?style=flat-square
[forks-url]: https://github.com/edwardmfho/RobotPie/network/members
[stars-shield]: https://img.shields.io/github/stars/edwardmfho/RobotPie.svg?style=flat-square
[stars-url]: https://github.com/edwardmfho/RobotPie/stargazers
[issues-shield]: https://img.shields.io/github/issues/edwardmfho/RobotPie.svg?style=flat-square
[issues-url]: https://github.com/edwardmfho/RobotPie/issues
