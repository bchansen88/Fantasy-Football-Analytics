import pandas as pd


year = '2017'
pos = 'RB'



class DefenseFP:
    
    def __init__(self, year, position):
        
        self.year = year
        self.position = position
        
    def getData(self):
        url = 'https://www.pro-football-reference.com/years/' + year + \
              '/fantasy-points-against-' + pos + '.htm'
              
        df = pd.read_html(url)
        
        #converts pandas list into dataframe
        df = df[0].dropna(axis=0, thresh=4)
        #drops the top level that isn't needed
        df.columns = df.columns.droplevel(0)
        #sets the index to teams
        df.set_index(['Tm'])
        #Rename columns
        df.columns = ['Tm', 'G', 'Att', 'Ru-Yds', 'Ru-TD', 'Tgt', 'Rec', 'Rec-yds', 
              'Rec-TD', 'FantPt', 'DKPt', 'FDPt', 'FantPt', 'DKPt', 'DFPt']
        df.to_csv('C:\\Users\\Ben\\env\\football.analytics\\defense' + \
                  year + '.csv')
        return df
        
    
        
rb = DefenseFP(year, pos)
print(rb.getData())