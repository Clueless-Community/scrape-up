```python
from scrape_up import twitch
```

### Scrape 

First, create an object of class `Twitch_Scraper`

```python
twitch_scraper = Twitch_Scraper()
```

| Methods                    | Details                                       |
| -------------------------- | --------------------------------------------- |
| `.scrape_title_description(channel)`     | Returns: Stream Title (if Live) or Channel Description (if Offline). |


---

    Example: using KaiCenat's twitch channel
```python
    scraper = Twitch_Scraper()
    title = scraper.scrape_title_description("kaicenat")
    print(title)
```
    
Output (if Live): ⚔️100+ HOUR STREAM⚔️ELDEN RING DLC MARATHON⚔️CLICK HERE⚔️LORD DWARF⚔️ELITE GAMER⚔️FOCUS⚔️

 
    **WARNING!**
    Smaller twitch channels with low stream time results is generic return value: 
    "Twitch is the world's leading video platform and community for gamers."
