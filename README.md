<div align=center>
<h1 align=center>SMART - RADIO </h1>
<p align=center> Play online radios from terminal (on RaspBerry Pi too) and save songs information to check them later </p>


</div>

### Why use?
1. Play radio from the terminal! why not?
2. Save songs information as a text file so that you don't have to open the shazam app every time to recognize unknows songs :tada:
3. Play radio from invisible browser 
4. Can be run on a CLI based OS like RaspBerry Pi :cool:

### Stations
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



### Example

```bash
(.venv) deep@lubuntu:~/Desktop/smart-radio$ python smart-radio.py --station mirchi_90s
      i     | Starting radio: Mirchi 90s
      i     | Playing now
      i     | Song => title: Mohabbat Ho Na Jaye (Dekha Jo Tumko), artist(s)/album: Kasoor
      i     | Song => title: Filhaal, artist(s)/album: Filhaal

```
### Note

To run this on a Windows machine skip the `chrome.sh` step and follow windows section