<div align=center>
<img align=center src=images/logo.png>
<h1 align=center>SMART - RADIO </h1>
<p align=center> Play online radios from terminal (on RaspBerry Pi too) and save songs information to check them later </p>

</div>

### Why use?

1. Play radio from the terminal! why not?
2. Save songs information as a text file so that you don't have to open the shazam app every time to recognize unknows songs :tada:
3. Play radio from invisible browser 
4. Can be run on a CLI based OS like RaspBerry Pi :cool:

### Sources

#### 1. [**Gaana.com**](https://gaana.com/radio/)

<p align=center>
<img src=./images/pehla_nasha.jpg height=120px>
<img src=./images/meethi_mirchi.jpg height=120px>
<img src=./images/english_love.jpg height=120px>
<img src=./images/english_retro.jpg height=120px>
<img src=./images/mirchi_90s.jpg height=120px>
<img src=./images/toota_dil.jpg height=120px>
<img src=./images/rabindra_sangeet.jpg height=120px>

</p>

#### Stations

| Name                      | ID                 | Provider |
| ------------------------- | ------------------ | -------- |
| Mirchi Pehla Nasha        | pehla_nasha        | Gaana    |
| Meethi Mirchi             | meethi_mirchi      | Gaana    |
| Mirchi English Love       | english_love       | Gaana    |
| Mirchi English Retro Hits | english_retro_hits | Gaana    |
| Mirchi Toota Dil          | toota_dil          | Gaana    |
| Mirchi 90s Bollywood Hits | mirchi_90s         | Gaana    |
| Mirchi Rabindra Sangeet   | rabindra_sangeet   | Gaana    |
|                           |                    |          |

More coming soon .....

### Example

``` bash
(.venv) deep@lubuntu:~/Desktop/smart-radio$ python smart-radio.py --station mirchi_90s
      i     | Starting radio: Mirchi 90s
      i     | Playing now
      i     | Song => title: Jane De,jane De,mujhe Jane De, artist(s)/album: Shola Aur Shabnam
      i     | Song => title: Pehli Baar Mile Hain, artist(s)/album: Saajan
      i     | Song => title: Chalte Chalte, artist(s)/album: Mohabbatein
      i     | Song => title: Hum Aapke Dil Mein Rehte Hain, artist(s)/album: Hum Aapke Dil Mein Rehte Hain
      i     | Song => title: Odh Li Chunariya Tere Naam Ki, artist(s)/album: Pyaar Kiya To Darna Kya
      i     | Song => title: Rimjhim Rimjhim, artist(s)/album: 1942 A Love Story
      i     | Song => title: Deewane To Deewane Hain, artist(s)/album: Deewane To Deewane Hain
```

### Install

#### Linux

1. Clone this repository `git clone https://github.com/deep5050/smart-radio.git && cd smart-radio`
2. (Optional) Create a virtual python environment `python3 -m venv .venv` and activate it `source .venv/bin/activate`
3. Install Dependencies `pip install -r requirements`
4. Install latest chrome and chromedriver `bash chrome.sh`
5. Add to ENV PATH `source sourcefile`
6. Run `python smart-radio --station [STATION_ID]`

#### Windows

1. Clone this repository `git clone https://github.com/deep5050/smart-radio.git && cd smart-radio`
2. (Optional) Create a virtual python environment `python3 -m venv .venv` and activate it `source .venv/bin/activate`
3. Install Dependencies `pip install -r requirements`
4. Make sure you have chrome installed and download chromedriver from [here](http://chromedriver.chromium.org/downloads) , unzip  and place chromedriver.exe  under `driver/`
5. Add driver path to system ENV
5.  Run `python smart-radio --station [STATION_ID]`

#### MAC

I'm not that rich LOL :smile:  
Must be same !

### License

MIT License

Copyright (c) 2021 Dipankar Pal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Acknowledgements
### Icons
<div>Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
</div>
<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

<div align=center>
<img src=images/footer.png>
<p align=center> Happy Listening </p>
</div>
