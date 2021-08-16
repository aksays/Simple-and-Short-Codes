Our goal is to trim the youtube video online while downloading

This can be achieved using Python and few other tools

1.Install the latest version of Python from https://www.python.org/downloads/

2. Set the environment path for the Python, and pip. 
  For Python :  https://datatofish.com/add-python-to-windows-path/
  For PIP : https://medium.com/swlh/solved-windows-pip-command-not-found-or-pip-is-not-recognized-as-an-internal-or-external-command-dd34f8b2938f

3. Download FFMPEG from https://www.ffmpeg.org/download.html
  Follow these steps: https://www.wikihow.com/Install-FFmpeg-on-Windows

4. Install youtube-dl using this command-> pip install youtube-dl

5. make a excel sheet with column names as follows: 
  	Title, youtube video link,	start time stamp,	end time stamp,	Rough formula,	Original Formula	

Title - Title you wish to give to the dowloaded file. Title should not have space between words. ex: python_tutorials_dictionaries
youtube video link - Youtube video link
Make sure start time stamp,	end time stamp column cells are Text Format 
Rough formula - 'youtube-dl --external-downloader ffmpeg --external-downloader-args "-ss'
Original formula - '=CONCATENATE(E2," ",C2," -to ",D2,CHAR(34)," -f best ",CHAR(34),B2,CHAR(34)," -o ",A2,".mp4")'

open the destination folder, where you want the video files to be downloaded - open cmd in that folder
Copy the original formula cell and paste it in cmd.
