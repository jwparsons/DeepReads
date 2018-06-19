Deep Reads Source Code
=========================

![alt text](https://jwparsons.bitbucket.io/style/images/projects/deepreads/title.png "DeepReads Title")

## Introduction
This repository contains the source code for DeepReads, a collection of machine learning models for generating book descriptions by genre. 


## Requirements
* DeepReads was created with [Python 3.6.5](https://www.python.org/downloads/release/python-365/).
* Training requires [textgenrnn](https://github.com/minimaxir/textgenrnn) and [TensorFlow](https://www.tensorflow.org/install/).


## Dataset
The dataset in this repository is comprised of 5 files containing 1000 book descriptions each, separated by genre.
There is a file for **Fantasy**, **Mystery**, **Philosophy**, **Romance**, and **Science Fiction**.
Each file contains a book description on each line.


For example, the Fantasy file contains the book description:

"Taran wanted to be a hero, and looking after a pig wasn't exactly heroic, even though Hen Wen was an oracular pig. But the day that Hen Wen vanished, Taran was led into an enchanting and perilous world. With his band of followers, he confronted the Horned King and his terrible Cauldron-Born. These were the forces of evil, and only Hen Wen knew the secret of keeping the kingdom of Prydain safe from them. But who would find her first?"


## Motivation
The motivation behind this application of NLG is to create models which can perhaps inspire people in the realm of creative writing.
Many writers sometimes have trouble generating ideas for what they would like to writ eabout.
Furthermore, writers sometimes practice their abilities using prompts.
If a particular Fantasy author would like to practice writing Fantasy or is in need of ideas for their next novel, DeepReads could potentially be of help.


## Instructions
### Training
1. Install [textgenrnn](https://github.com/minimaxir/textgenrnn) and [TensorFlow](https://www.tensorflow.org/install/).
1. Navigate to the directory **training**.
1. Run any of the files corresponding to each genre.
    * The training parameters can be customized according to the [textgenrnn](https://github.com/minimaxir/textgenrnn/blob/master/docs/textgenrnn-demo.ipynb) documentation.

### Generation
1. Install [textgenrnn](https://github.com/minimaxir/textgenrnn) and [TensorFlow](https://www.tensorflow.org/install/).
1. Navigate to the directory **generation**.
1. Run any of the files corresponding to each genre.
    * The variable **training_path** can be modified to point towards a new model or any of the existing ones in the **models** folder.


## Results
### Fantasy
* "Barnes Penguin from the fairy tales in the dark hand of destruction. His difference was about to rule the first Standy that he leaves the children of a terrible creature."
* "The master of the terrible prince of light. The real family of the moon search of the dead. Leviday, the dreaded Farmer s rules on the most published injured King and everything Morgoth? As Inferno of the World Bomb is a way to save why she has been such a prophecy of war and enchanted."
* "The novel that has come to help begin to change the world of the demonic interest of the Guide of the Holy 's Grey Brothers comes to find a book in a fire, the blood of the empire that seems to take the inner secret of the power by the most powerful boy from the secret of the warrior."

### Mystery
\<to be added\>

### Philosophy
\<to be added\>

### Romance
\<to be added\>

### Science Fiction
\<to be added\>

## Contribution
This project was created entirely by me for the class Social Network Mining at FSU.

Enjoy!