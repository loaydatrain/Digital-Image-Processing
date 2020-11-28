# project-haripraveen_subramanian_cool_boss

This is our code for manga colourization as a part of DIP Monsoon 2020 course project. The paper that we have used is 
http://www.cse.cuhk.edu.hk/~ttwong/papers/manga/manga.pdf


### Instructions on how to run the code

#### Dependencies
There are a variety of python packages used in this project. The major ones if you already have the latest version of python and pip installed.
all other dependencies have been listed below.
```
numpy , matplotlib.pyplot , opencv-contrib-python , cv2 , webcolors , scikit-image , scipy 
```
These can be installed in the below manner if you are on a pip environment
```
pip3 install <package name>

```
We have added a install.sh file to help install packages of python required to run this project. Use this using the following snippet
```
chmod +x install.sh
./install.sh
```

#### Procedure
- Make sure that you have ```main.py``` , ```pattern_continuous.py```, ```levelset.py``` , and the image that you want it to colour in the same folder.
USAGE:
    ```python main.py <filename>```

- Two windows will show up, one for input and one for output.At first, in input window, scribble around the object using
mouse left button. Then select the trackbar window and press one of two numbers '0' or '1'.
  - Key '0' - To do intensity continuous colorization
  - Key '1' - To do pattern continuous colorization
  -  Key ctrl + 'c' - To stop level set method.
- After you press ctrl + 'c' the process will stop and you will see the output on the output window.Also the output will get stored in the same folder 
with the name ```res.png```. 
- If you want to colour the same image again then run ```python main.py res.png``` after exiting the current session ,you can't
 colour multiple regions in one execution of the code. 
