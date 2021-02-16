# FamilyFeud

### Option #1: Let me help you

1. Edit the "input.txt" file with your data, keeping the same format.
    * Note: You can create fewer or more questions if you'd like.
    * Note: You can create fewer or more than 5 answers, but 5 looks really nice on the screen.
2. Send it to me.
3. I'll send you the html file that was generated based on your input.
4. Double click on the familyFeud.html file to open it and play.

### Option #2: Do it yourself

Download Prerequisites:
1. Install Python 3 [`https://www.python.org/downloads/`] and ensure it is added to PATH during installation. If it is not you --can-- do it afterwards, but it is a big pain in the butt. Note: on Linux it is preinstalled!
2. [Optional] Install Git [`https://git-scm.com/downloads`]. Follow the instructions carefully during installation, especially on Windows. Note: again on Linux it is preinstalled!

To download the files:
1. Click on the green "Code" dropdown button.
2. Click "Download zip".

Or if you want to be a real computer nerd, you can download the files using Git:
1. Type in your terminal `git clone https://www.github.com/patrick-girard/FamilyFeud`

Note: Windows users can use WSL, GitBash, or the Command Prompt/PowerShell.

2. Change into that directory `cd FamilyFeud`

To create your input file with questions and answers:
1. Edit the "input.txt" file with your data, keeping the same format.

To generate the webpage:
1. Access the command line (Terminal on Mac, or probably Putty on Windows).
2. Switch into the directory with these files. (cd is the command for change directory).
3. Enter: `python3 writeFamilyFeud.py input.txt`

To access the webpage:
1. Double click on the newly generated familyFeud.html file. If on Linux typing into your terminal `xdg-open familyFeud.html` in the current directory will open the webpage in your default web browser.

### To play the game:
* You can flip each answer to reveal it by clicking on that answer.
* To award points, 
    * Reveal the answers that the winning team got correct and hide the answers that were not guessed correctly.
    * Then, click their team's score button at the bottom to add that amount to their total score.
* Have fun!


### Customization
* To change the colors of the buttons, edit them in the styles.css file.
* To change the background image, replace the "background.jpeg" image with image called "background.jpeg".
   * If your image is not a jpeg, either make it a jpeg or edit the filetype for the background image in the styles.css file.
