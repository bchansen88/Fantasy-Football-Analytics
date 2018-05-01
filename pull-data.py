import pandas as pd
import os



year = '2017'

class DefVsPos:

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
        #df = df.set_index(['Tm'])
        #Rename columns
        #df.columns = ['Tm', 'G', 'Att', 'Ru-Yds', 'Ru-TD', 'Tgt', 'Rec', 'Rec-yds', 
        #      'Rec-TD', 'FantPt', 'DKPt', 'FDPt', 'FantPt', 'DKPt', 'DFPt']
        '''
        if not os.path.exists(file):
            
            df.to_csv(file)
        '''
        return df
#function to save to csv file if file does not already exist 
def saveToFile(df):
        
    if not os.path.exists(file):
        df.to_csv(file, index = False)
        
#initialize position variable
#pos = ''
#list to grab all positions
all_pos = ['RB', 'TE', 'QB', 'WR']
#file name structure for def vs pos csv files
file = os.getcwd() + '\\collection\\defense_' + pos + '_' + year + '.csv'

def selectPosition(pos):
    
    print('Select a position to pull: \n\
                    1. Running Back \n\
                    2. Tight End \n\
                    3. Quarterback \n\
                    4. Wide Receiver\n\
                    5. All')
    
    pos = input()
    
    if pos == 1:
        pos = 'RB'
        
    elif pos == 2:
        pos = 'TE'
    
    elif pos == 3:
        pos = 'QB'
        
    elif pos == 4:
        pos = 'WR'

selectPosition(pos)           
p = DefVsPos(year, pos)
p = p.getData()
saveToFile(p)
print(p.head())
