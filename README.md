# lyrics-processor
Automated Lyrics processor for your mp3 files.  This process will update your locally stored mp3 files ID3 tags with the lyrics of the song.

## Architecture:
The system is built with the following components:
- Python
- BeautifulSoup
- mutagen.id3
- Regular Expressions

The system uses a Factory to load the particular lyric website you want to use.
New lyric websites can be added independantly.

The state of the system is POC.

Lyrics are shown in iTunes, on iPhone while playing.

### How to Use:
Songs must be stored with the following naming convention:

`Artist Name - Song Title With-Dashes or Spaces`

![Example Album with Naming Convention](https://storage.matiboux.com/imgshot/DGKdoiSMYXo4.png)


Currently using NameChanger application for Mac OS X to help rename mass amounts of files:
[NameChanger](https://mrrsoftware.com/namechanger/)

Update `test_lyrics_processor.py` and update variable `path_to_music` and place the path to the local mp3 files in the test case.
Run the test case.

### Requirements:
- MP3 file(s)
- Python3
- ID3 Program to view/verify the lyrics (iTunes, MPFreaker, Sound Studio etc.)

### Optional Requirements:
- PyCharm
- NameChanger

### Future Enhancements:
- Plumb the main process to check all lyric websites
- Add nightly build process to test the lyric websites
- Support more lyric websites
- Error handling for song lyrics that were unable to be found

### Currently Supported Lyric Websites:
- [AZLyrics](http://www.azlyrics.com)
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

Song File: /Users/user/Downloads/New Music/The Bouncing Souls - Crucial Moments (2019)/Bouncing Souls - Favorite Everything.mp3
```

### Issues
- DarkLyrics has organized the lyrics by album

#### Tested Full Albums and Songs
##### Songs:
- Chevelle - Joyride (Omen)
- Dandy Warhols - Everyday should be a holiday
- Badflower - Ghost


##### Albums:
- Every Time I Die - From Parts Unknown
- Haste the Day - Coward
- Foo Fighters - Concrete Gold
- Brand New - 3 Demos, Reworked EP
- A Tribe Called Quest - We Got It From Here... Thank you 4 Your Service
- Propagandhi - Victory Lap
- Killswitch Engage - Incarnate
- Hatebreed - The Concrete Confessional
- Avenged Sevenfold - The Stage
- Transplants - Take Cover EP
- Sam Roberts Band - Lo-Fantasy
- Face to Face - Protection
- Foo Fighters - Sonic Highways
- Green Day - Revolution Radio
- Eminem - Revival
- In Flames - Battles
- In Flames - Siren Charms
- Babymetal - Babymetal _(contained Japanese characters in filenames and lyrics)_
- Weezer - Everything Will Be Alright In The End
- Silverstein - I Am Alive In Everything I Touch
- Lagwagon - Hang
- Hellyeah - Blood for Blood
- Megadeth - Dystopia
- Refused - Freedom
- Korn - Serenity of Suffering
- Nine Inch Nails - Not the Actual Events
- NOFX - First Ditch Effort
- NOFX - Backstage Passport Soundtrack
- NOFX - I Heard They Suck Live!!
- NOFX - Stoke Extinguisher
- Ghost BC - Popestar EP
- Protest The Hero - Pacific Myth EP
- Parkway Drive - Reverence
- Our Last Night - Younger Dreams
- Our Last Night - Selective Hearing EP
- A Perfect Circle - Eat the Elephant
- Nine Inch Nails - Bad Witch
- Drake - Scorpion
- Between the Buried and Me - Automata II
- Eminem - Kamikaze
- Lil Wayne - Tha Block Is Hot
- Lil Wayne - Lights Out
- Lil Wayne - 500 Degreez
- Lil Wayne - Tha Carter I
- Lil Wayne - Tha Carter II
- Lil Wayne - Tha Carter III
- Lil Wayne - Tha Carter IV Deluxe Edition
- Lil Wayne - Tha Carter V
- Atreyu - In Our Wake
- Alice In Chains - Rainer Fog
- Alkaline Trio - Is this thing cursed?
- Nicki Minaj - Pink Friday
- Nicki Minaj - Pinkprint
- Weezer - The Teal Album
- The Flatliners - Dead Language
- The Flatliners - Mass Candescence EP
- The Flatliners - Division of Spoils
- The Flatliners - Cynics EP
- New Found Glory - From The Screen To Your Stereo Part I
- New Found Glory - From The Screen To Your Stereo Part II
- NOFX - Hepatitis Bathtub 7 inch
- Architects - Hollow Crown
- Architects - Lost Forever Lost Together
- Architects - Nightmares
- Architects - Ruin
- Architects - The Here And Now
- In Flames - I, The Mask
- Children of Bodom - Hexed (Deluxe Version)
- Descendents - SpazzHazard
- Faith No More - Sol Invictus
- New Found Glory - Makes Me Sick Again
- Jimmy Eat World - Integrity Blues
- Pennywise - Yesterdays
- The Offspring - Days Go By
- Refused - Servants of Death EP
- Violent Soho - Hungry Ghost
- Violent Soho - Waco
- Propagandhi - The Recovered EP
- Propagandhi - Sacrifice Split 7"
- Propagandhi - FYP Split 7"
- Weezer - The White Album
- Weezer - The Black Album
- Weezer - Pacific Daydream
- Hellyeah - 333
- Hellyeah - Band of Brothers
- Hellyeah - Unden!Able
- Hot Water Music/The Bouncing Souls - Tour Split EP
- The Bouncing Souls - Menzingers Split EP
- Our Last Night - Let Light Overcome EP
- The Bouncing Souls - Crucial Moments EP
- Cancer Bats - Searching for Zero
- Killswitch Engage - Incarnate
- Wu-Tang Clan - The Saga Continues
- Finch - Back to Oblivion
- Germs - The Complete Anthology (MIA)
- Kanye West - 808's & Heartbreak
- Kanye West - Graduation
- Devil You Know - The Beauty Of Destruction
- Kanye West - Late Registration
- Kanye West - The College Dropout
- Kanye West - My Beautiful Dark Twisted Fantasy
- Kanye West - Yeezus
- Kanye West – The Life Of Pablo
- Between The Buried And Me - Automata I
- Dandy Warhols - Distortland _(2 songs missing)_
- Descendents - Hypercaffium Spazzinate
- I Killed the Prom Queen - Beloved
- Ministry - AmeriKKKant
- Pennywise - Never Gonna Die
- Jay-Z - Reasonable Doubt
- Jay-Z - In My Lifetime, Volume 1
- Soulfly - Ritual
- Soulfly - Arcangel
- Drake - Views
- Architects - All Our Gods Have Abandoned Us
- Architects - Daybreaker
- Architects - Holy Hell
- Drake - More Life
- Cardi B - Invasion of Privacy
- Papa Roach - Crooked Teeth
- Papa Roach - Who Do You Trust
- The Used - The Canyon
- POD - Circles
- The Roots - ...and then you shoot your cousin
- Foo Fighters - Concrete and Gold
- A Day To Remember - Bad Vibrations
- Descendents - Who We Are 7 inch
- Faith No More - Sol Invictus
- The Distillers - Man Vs. Magnet, Blood In Gutters
- The Bouncing Souls - Simplicity
- Linkin Park - The Hunting Party
- New Found Glory - Resurrection
- Screeching Weasel - Carnival Of Schadenfreude
- Rancid - Honor is all we know
- NOFX - They've Actually Gotten Worse Live!