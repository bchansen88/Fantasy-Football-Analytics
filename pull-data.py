import pandas as pd
import os




class DefVsPos:

    def __init__(self, year, position):
        
        self.year = year
        self.position = position
        
    def getData(self):
        

        url = 'https://www.pro-football-reference.com/years/' + year + \
              '/fantasy-points-against-' + pos + '.htm'
        print(url)
              
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
    
#organizes the structure of the main program to scrape data
def main():
    
    print('What do you want to do? \n\
          1. Pull current season\'s stats \n\
          2. Pull previous season\'s stats \n\
          3. Pull stats for previous 5 seasons \n\
          4. Pull stats for previous 10 seasons \n\
          5. Pull stats for another amount of seasons \n\
          6. Quit Program')
    
#function to save to csv file if file does not already exist 
def saveToFile(df):
        
    if not os.path.exists(file):
        df.to_csv(file, index = False)
        
#range for specified duration (5 or 10 years)
def yearDuration():
    
    i = int(year) + 1
    x = i - dur
    
    for i in range(x, i):
        i = str(i)
        
    

#initialize position variable
#pos = ''
#list to grab all positions
all_pos = ['RB', 'TE', 'QB', 'WR']

    
print('Select a position to pull: \n\
      1. Running Back \n\
      2. Tight End \n\
      3. Quarterback \n\
      4. Wide Receiver\n\
      5. All')



pos = input()
year = '2017'

print(type(pos))


 
if pos == '1':
    pos = 'RB'
        
elif pos == '2':
    pos = 'TE'
    
elif pos == '3':
    pos = 'QB'
        
elif pos == '4':
    pos = 'WR'
   
    

#file name structure for def vs pos csv files
#file = os.getcwd() + '\\collection\\defense_' + pos + '_' + year + '.csv'
file = os.path.dirname(os.path.realpath('__file__'))
folder = 'collection\defense_' + pos + '_' + year + '.csv'
file = os.path.join(file, folder)
print(file)
    
     
p = DefVsPos(year, pos)
p = p.getData()
saveToFile(p)
print(p.head())



