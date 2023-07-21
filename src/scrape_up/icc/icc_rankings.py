from bs4 import BeautifulSoup
import requests

class ICC:
    """
    Create an instance of `ICC` class.
    ```python
    scraper = ICC()
    ```
    | Method                       | Details                                                             |
    | ---------------------------- | ------------------------------------------------------------------- |
    | `.team_rankings(format)`     | Returns the list of rankings of teams of desired format             |
    |`.player_ranking(type,format)`| Returns the list of player ranking of desired type and format       |
    """

    def __init__(self):
        self.url = "https://www.icc-cricket.com/rankings/mens/"
    
    def team_rankings(self,format):
        try:
            teams_list={}
            url=self.url+"team-rankings/"+format
            response=requests.get(url)
            soup=BeautifulSoup(response.content,'html.parser')
            teams=soup.find_all('span',class_="u-hide-phablet")
            for rank, team in enumerate(teams, 1):
                teams_list[rank] = team.get_text()
                
            return teams_list
        except:
            return "No such format exists"
        
    def player_ranking(self,type,format):
        try:
            url=self.url+f"/player-rankings/{format}/{type}"
            response=requests.get(url)
            soup=BeautifulSoup(response.content,'html.parser')
            top_player=soup.find('div',class_="rankings-block__banner--name-large").get_text()
            rest_players=soup.find_all('td',class_="table-body__cell rankings-table__name name")
            players_list={}
            players_list[1]=top_player
            for rank, player in enumerate(rest_players, 2):
                players_list[rank] = player.get_text().replace('\n','')
                
            return players_list
        except:
            return "Enter correct type and format"