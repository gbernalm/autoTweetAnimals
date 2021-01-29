


<br />
<p align="center">
  <a href="https://github.com/gbernalm/cuteAnimaux">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">cuteAnimaux</h3>

  <p align="center">
    Set of scripts that download images from google search. Categorizes them using openCV and with with a set of pre-configured comments, manages to tweet the pictures along with a proper caption that matches the animal in the posted picture.
    <br />
    <a href="https://github.com/gbernalm/cuteAnimaux"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project uses google's speech to text platform to pick up what the user is saying. Once it is converted from speech to text, the command is then parsed with a set of preprogrammed events.

### Built With

* `openCV`
* `Tweepy`
* `google_images_search`



<!-- GETTING STARTED -->
## Getting Started

Download and setup `OpenCV` modules along with the YOLO classifier.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gbernalm/cuteAnimaux.git
   ```




<!-- USAGE EXAMPLES -->
## Usage
1. Setup credentials for the autoTweet.py,Img_Classifier.py and Google_Image_Downloader.py (Will need a Google project account)

2. Run the Google_Image_Downloader.py to download the pictures
3. Run the Img_Classifier.py to classify the pictures
4. Run AutoTweet.py to post to the account.



<!-- LICENSE -->
## License

Distributed under the MIT License.



<!-- CONTACT -->
## Contact

Gonzalo BM - [@gbm05](https://twitter.com/gbm05) - gbernalmorhaim@ucdavis.edu

Project Link: [https://github.com/gbernalm/cuteAnimaux](https://github.com/gbernalm/cuteAnimaux)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* <b>Built using the YOLO Classifier </b>



