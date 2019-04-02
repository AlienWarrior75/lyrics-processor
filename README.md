# lyrics-processor
Automated Lyrics processor for your mp3 files.  This process will update your locally stored mp3 files ID3 tags with the lyrics of the song.

## Architecture
The system is built with:
- Python
- BeautifulSoup
- mutagen.id3
- Regular Expressions

The system uses a Factory to load the particular lyric website you want to use.
New lyric websites can be added independantly.

### How to Use
Songs must be stored with the following naming convention:

```Artist Name - Song Title With-Dashes or Spaces```

Currently depending on NameChanger application for Mac OS X to help rename mass amounts of files:
[NameChanger](https://mrrsoftware.com/namechanger/)

Update Test_lyrics_processor.py and update ```path_to_music``` and place the path to the mp3 files in the test case.
Run the test case.

### Requirements:
- MP3 file(s)
- Python3
- ID3 Program to view/verify the lyrics (iTunes, MPFreaker, etc.)

### Future Enhancements
- Plumb the main process to check all lyric websites
- Add nightly build process to test the lyric websites
- Support more lyric websites
- Error handling for song lyrics that were unable to be found

### Supported Lyric Websites
- [AZLyrics](http://www.azlyrics/com)
- [PLyrics](http://www.plyrics.com)
- [LyricsOnDemand](http://lyricsondemand.com)
- [DarkLyrics](http://www.darklyrics.com)
- [GeniusLyrics](http://www.genius.com)

##### Licensed Under the GPL 3.0 license


### Sample Output:
```5 Bouncing Souls - Favorite Everything.mp3
Song With Dash: Bouncing Souls - Favorite Everything
Artist: Bouncing Souls Song:Favorite Everything Song For HTML: Favorite Everything
URL Artist: bouncingsouls
URL Song: favoriteeverything
URL: http://www.azlyrics.com/lyrics/bouncingsouls/favoriteeverything.html
Lyrics Retrieved: 

You have this certain something
You're my blues and my swing
No exaggeration
You're the greatest compilation
You are disintegration
My girl, my temptation

You're my rock steady beat
Maybelline in the drivers seat
You're the songs that bring a tear
Embrace the love, embrace the fear
Don't run to search for your heart
Love will tear us apart
You inspire devotion
Every emotion

You're my favorite everything
You're my favorite everything
You're my favorite everything
You're my favorite everything

You're the reason that I sing
You're my favorite everything
You're the reason that I sing
You're my favorite everything

No I won't waste my time
Trying to find
Another reason to love
Time after time

You're my favorite everything
You're my favorite everything
You're my favorite everything
You're my favorite everything

Song File: /Users/user/Downloads/New Music/The Bouncing Souls - Crucial Moments (2019)/Bouncing Souls - Favorite Everything.mp3```