# Intro

A tool for creating custom filters for your webcam to be used with video conferencing tools. 

# Setup

I can't be bothered to figure out why the library and Mac M1 aren't playing nicely beyond this solution. 
If you're not using an Mac M1, ignore the aliasing part and just use `python` and `pip`. 

Setup Virtual Env 
Install `virtualenvwrapper`
`mkvirtualenv cv2-in-the-middle`
`workon cv2-in-the-middle`

Add the following two lines to .zshrc
`alias pytel="arch -x86_64 python"`
`alias piptel="arch -x86_64 pip"`

Install Dependencies
`piptel install -r requirements.txt`

Setup Virtual Camera
https://pypi.org/project/pyvirtualcam/

Execute Script
`pytel main.py`

Start Test Server
`pytel -m http.server` 
Navigate to http://localhost:8000/sandbox.html