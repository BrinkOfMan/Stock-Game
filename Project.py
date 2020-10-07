import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import random
import time
from copy import copy
import string


##############################################################################
#What's left to do?                                                          #
                                                                             #
#Key: ✓(complete), ♻(working on it), ✗(gave up), Ø(unclaimed)               #
                                                                             #
##A finished group project                          ✓ — Everyone             #
##Core gameplay features                            ✓ — Ethan                #
##GUI features for core gameplay                    ✓ — Ethan                #
##Clear entry boxes when hitting enter              ✓ — Ethan                #
##Special life events                               ✓ — Sam                  #
##Incorporate multiplayer functionality             ✗                        #
##Save-load game functionality                      ✗	                     #   
##More buttons and labels                           ✓ — Noah                 #
##Actions will update player label                  ✓ — Noah                 #
##Make enter key pressed event update player frame  ✓ — Noah/Ethan           #
##Output dialog (in the GUI) for investing amount   ✓ — Noah/Ethan           #
##Output dialog (in the GUI) for yearly returns     ✓ — Noah/Ethan           #
##Periods of good/bad returns for specific stocks   ✓ — Sam                  #
##############################################################################



#=======================================Player class: has states of name, balance, and  invested amount, methods for gaining/losing money=======================================
class Player:
    def __init__(self, n, b, s):
        self.name = n
        self.bal = b
        self.stocks = s

    def getName(self):
        return self.name
    
    def getBal(self):
        return self.bal

    def getStock(self,n):
        if n == 0:
            return self.stocks[0]
        elif n == 1:
            return self.stocks[1]
        elif n == 2:
            return self.stocks[2]
        elif n == 3:
            return self.stocks[3]
        else:
            return None

    def moreMoney(self, amt):
        self.bal += amt

    def lessMoney(self, amt):
        self.bal -= amt

    def __str__(self):
        listStocks = [str(self.stocks[i].getName()) + ': $'+ str(round(self.stocks[i].getInvested(),2)) for i in range (4)]
        return str(self.name)+"'s current balance is: $"+str(self.bal)+". Here's how much they have invested in each stock: "  +str(listStocks)
    
#============================================================================End of the player class============================================================================
################################################################################################################################################################################
################################################################################################################################################################################
#====================================Stock class: has states of name and invested amount, methods for investing/withdrawing, change in year=====================================
class Stock:

    def __init__(self, n, i):
        self.name = n
        self.invested = i

    def getName(self):
        return self.name
    
    def getInvested(self):
        return round(self.invested,2)

    def invest(self, p, amt):

        if amt > p.getBal():
            return("You don't have enough in your balance to invest any more!")
        
        else:
            self.invested += amt
            p.lessMoney(amt)
            return('You have successfully invested $'+str(amt)+' into '+str(self.name))

    def withdraw(self, p, amt):
        if amt*-1 > self.invested:
            return("you don't have enough money invested to withdraw that amount!")
            
        else:
            self.invested += amt
            #This will add a negative amount to the invested total
            p.moreMoney(amt*-1)
            #This will add a positive amount to the player balance
            strVer = str(amt)
            return('You have successfully withdrawn $'+str(strVer[1:])+' from '+str(self.name))


    def nextYear(self, p, year):

        makeDecision = random.randrange(1,101) #100 random outcomes

        #Here is the framework for "good" and "bad" years
        if self.name == 'QMAG' and (year >= 5 and year <=7):
            makeDecision = random.randrange(1,8)

        elif self.name == 'QMAG' and (year >= 17 and year <=19):
            makeDecision = random.randrange(92,101)
            
        if self.name == 'PIPI' and (year >= 1 and year <=3):
            makeDecision = random.randrange(1,8)

        elif self.name == 'PIPI' and (year >= 10 and year <=13):
            makeDecision = random.randrange(92,101)
            
        if self.name == 'ORLY' and (year >= 12 and year <=16):
            makeDecision = random.randrange(1,8)
            
        elif self.name == 'ORLY' and (year >= 3 and year <=5):
            makeDecision = random.randrange(92,101)
            
        if self.name == 'TREZ' and (year >= 16 and year <=18):
            makeDecision = random.randrange(1,8)
            
        elif self.name == 'TREZ' and (year >= 9 and year <=11):
            makeDecision = random.randrange(92,101)
            #For some reason, TREZ is not affected by this method, but all others are


        #1% chance for a large loss
        elif makeDecision == 100:
            randChange = random.randrange(-200, -99)/10
            output = randChange
            randChange = 1 + randChange/100
            self.invested *= randChange
            return('Ouch! '+str(self.name)+' fell by a whopping '+str(output).replace("-", "")+'% this year.')

        #5% chance for a loss
        elif makeDecision >= 95 and makeDecision < 100:
            randChange = random.randrange(-50,-9)/10
            output = randChange
            randChange = 1 + randChange/100
            self.invested *= randChange
            return(str(self.name)+' fell by '+str(output).replace("-", "")+'% this year. Bummer.')

        #5% chance for a large increase
        if makeDecision <= 5:
            randChange = random.randrange(100, 201)/10
            output = randChange
            randChange = 1 + randChange/10
            self.invested *= randChange
            return('Woah! '+str(self.name)+' had a great yearly return of '+str(output)+'%')

        #89% chance for an average increase
        else:
            randChange = random.randrange(10,51)/10
            output = randChange
            randChange = 1 + randChange/100
            self.invested *= randChange
            return(str(self.name)+' had an average yearly return rate of '+str(output)+'%')

      
    def __str__(self):
        return 'You currently have $'+str(self.getInvested())+' invested in '+str(self.name)

#============================================================================End of the Stock class=============================================================================
################################################################################################################################################################################
################################################################################################################################################################################
#======================================================================Start of the Lifetime events class=======================================================================


class LifeEvents:
    def __init__(self):
        pass
    
        
    
    def nextYear2(self,p,game):
        makeDecisionTwo=random.randrange(1,101)
        makeDecisionThree = random.randrange(1,11)

       
       #5% chance for big, negative event
       
        if makeDecisionTwo<=95 and makeDecisionTwo > 90:
            self.medical=random.randint(800,5000)
            p.lessMoney(self.medical)
            return("You slipped on some cash a more successful investor dropped. Your medical bill was $"+str(self.medical))
    
        #10% chance for a positive event
        
        elif makeDecisionTwo <= 90 and makeDecisionTwo > 80:
            self.windfall=random.randint(50,250)
            p.moreMoney(self.windfall)
            return("Congratulations, you've found $"+str(self.windfall)+" on the street. Spend it wisely!")
        
        #1% chance for very big, very positive event
        
        elif makeDecisionTwo == 50:
            self.inherit=random.randint(20000,100000)
            p.moreMoney(self.inherit)
            return("You've inherited $"+str(self.inherit)+" from a distant relative. Invest wisely!")
        
        
        
        #1% chance for a very big, very negative event.
        
        elif makeDecisionTwo == 10:
            self.bill=random.randint(10000,20000)
            p.lessMoney(self.bill)
            return("You have been fined by the IRS for tax fraud. You must pay $"+str(self.bill))

        #0.1% chance to win the lottery

        elif makeDecisionTwo == 1 and makeDecisionThree == 1:
            self.lotterywin=random.randint(50000,200000000)
            p.moreMoney(self.lotterywin)
            return("You won the lottery. After taxes, your winnings are "+str(self.lotterywin)+" congratulations.")

        else:
            return('Nothing extra special this year')



#============================================END of Lifetime Events Class============================================#


#============================================GUI class: has states of a whole buncha things, methods for doing a ton of stuff, I bet============================================

class StockGame:
    def __init__(self, p):
        self.player = p
        self.window = tk.Tk()
        self.window.title('Stock Market Game')
        self.tutWin = tk.Tk()
        self.tutWin.title('Tutorial')
        self.year = 0
        self.tutCounter = 0
        self.window.withdraw()
        self.tutorial()

    def tutorial(self):
        self.counter = 0
        self.tutWin['padx'] = 5
        self.tutWin['pady'] = 5
        self.tutWin.geometry("900x200")
        self.tutWin.focus_force()

        self.buffLabel = ttk.Label(self.tutWin, text='\n')
        self.buffLabel.pack()
        self.tutLabel = ttk.Label(self.tutWin, text = 'Welcome to the game! Click the "Next" button to read through the tutorial. Click the "Skip" button if you know how to play already')
        self.tutLabel.pack()

        self.buffLabel1 = ttk.Label(self.tutWin, text='\n\n')
        self.buffLabel1.pack()
        self.nextButton = tk.Button(self.tutWin, text='Next', command=self.next)
        self.nextButton.pack()

        self.buffLabel2 = ttk.Label(self.tutWin, text='\n')
        self.buffLabel2.pack()
        self.skipButton = tk.Button(self.tutWin, text='Skip', command=self.createEverythingElse)
        self.skipButton.pack()

    def next(self):
        if self.tutCounter == 0:
            self.tutLabel.configure(text="You are Stock Man, who recently decided to invest in stocks for the next 20 years.")
            self.tutCounter += 1

        elif self.tutCounter == 1:
            self.tutLabel.configure(text="Four stocks have caught your eye")
            self.tutCounter += 1

        elif self.tutCounter == 2:
            self.tutLabel.configure(text="Quality Magnets: devliering quality magnets without knowing how they work for over 20 years!")
            self.tutCounter += 1

        elif self.tutCounter == 3:
            self.tutLabel.configure(text="Pi & Pie Math & Café: Pie almost as beautiful as the similar-sounding mathematical constant.")
            self.tutCounter += 1

        elif self.tutCounter == 4:
            self.tutLabel.configure(text="""Oh, Really? Auto Parts: Our prices are so low, you'll be saying "oh, really?" every time.""")
            self.tutCounter += 1

        elif self.tutCounter == 5:
            self.tutLabel.configure(text="Treez Incorporated: We plant trees. Please invest in us.")
            self.tutCounter += 1
            
        elif self.tutCounter == 6:
            self.tutLabel.configure(text="Every year you can invest or withdraw money by entering the amount next to the stock label.")
            self.buffLabel1.configure(text='Positive integers will deposit money into a stock; negative integers will withdraw money from a stock.\n\n')
            self.tutCounter += 1

        elif self.tutCounter == 7:
            self.tutLabel.configure(text='When you are done for that year, click the "Proceed to next year" button.')
            self.buffLabel1.configure(text='\n\n')
            self.tutCounter += 1

        elif self.tutCounter == 8:
            self.tutLabel.configure(text="After 20 years, the game will end, and you can walk away with your earnings.")
            self.tutCounter += 1

        elif self.tutCounter == 9:
            self.tutLabel.configure(text="Make sure to keep an eye out for stock news. It will let you know what stocks will do good/bad in the coming years.")
            self.buffLabel1.configure(text='Also, you have a life. Stuff may happen in your life that benefits or damages your financial status.\n\n')
            self.tutCounter += 1

        elif self.tutCounter == 10:
            self.tutLabel.configure(text="Good luck, and happy investing!")
            self.buffLabel1.configure(text='\n\n')
            self.tutCounter += 1

        else:
            self.createEverythingElse()

    def createEverythingElse(self):
        self.tutWin.destroy()
        self.window.update()
        self.window.deiconify()
        self.window['padx'] = 5
        self.window['pady'] = 5
        self.window.geometry("900x400")

        
        #================================Beginning of stock entry frame================================

        entryFrame = ttk.LabelFrame(self.window, text='Enter how much you want to invest in/withdraw from each stock')
        entryFrame.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        #Player will enter how much to invest in/withdraw from each stock

        #QMAG
        self.investInQMAGEntry = ttk.Label(entryFrame, text='QMAG:')
        self.investInQMAGEntry.grid(row=0,column=0)
        investAmtQMAG = self.investInQMAGEntry = ttk.Entry(entryFrame, width=10)
        investAmtQMAG.bind('<Return>',self.investWithdrawQMAG)
        self.investInQMAGEntry.grid(row=0, column=1)

        #PIPI
        self.investInPIPIEntry = ttk.Label(entryFrame, text='PIPI:')
        self.investInPIPIEntry.grid(row=1,column=0)
        investAmtPIPI = self.investInPIPIEntry = ttk.Entry(entryFrame, width=10)
        investAmtPIPI.bind('<Return>',self.investWithdrawPIPI)
        self.investInPIPIEntry.grid(row=1, column=1)

        #ORLY
        self.investInORLYEntry = ttk.Label(entryFrame, text='ORLY:')
        self.investInORLYEntry.grid(row=2,column=0)
        investAmtORLY = self.investInORLYEntry = ttk.Entry(entryFrame, width=10)
        investAmtORLY.bind('<Return>',self.investWithdrawORLY)
        self.investInORLYEntry.grid(row=2, column=1)

        #TREZ
        self.investInTREZEntry = ttk.Label(entryFrame, text='TREZ:')
        self.investInTREZEntry.grid(row=3,column=0)
        investAmtTREZ = self.investInTREZEntry = ttk.Entry(entryFrame, width=10)
        investAmtTREZ.bind('<Return>',self.investWithdrawTREZ)
        self.investInTREZEntry.grid(row=3, column=1)

    #====================End of stock entry frame, beginning of control buttons====================

        buttonFrame = ttk.LabelFrame(self.window, text='Control buttons')
        buttonFrame.grid(row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S)

        self.nextYrButton = tk.Button(buttonFrame, text='Proceed to next year', command=self.nextYearUpdate)
        self.nextYrButton.grid(row=4, column=0)
        
        self.quitButton = tk.Button(buttonFrame,text='Quit',command = self.window.destroy)
        self.quitButton.grid(row=5, column=0)

    #====================End of buttons frame, beginning of player stats frame=====================

        self.playerStatsFrame = ttk.LabelFrame(self.window, text= 'Player Stats')
        self.playerStatsFrame.grid(row = 2, column = 0,sticky=tk.E + tk.W + tk.N + tk.S)
                
        self.nameLabel = ttk.Label(self.playerStatsFrame, text = "Player Name: " + self.player.name)
        self.nameLabel.grid(row = 1, column = 0)

        self.balanceLabel = ttk.Label(self.playerStatsFrame, text = "Current Balance: $" + str(self.player.getBal()))
        self.balanceLabel.grid(row = 2, column = 0)

        self.stockLabel_1 = ttk.Label(self.playerStatsFrame, text = str(self.player.getStock(0)))
        self.stockLabel_1.grid(row = 3, column = 0)

        self.stockLabel_2 = ttk.Label(self.playerStatsFrame, text = str(self.player.getStock(1)))
        self.stockLabel_2.grid(row = 4, column = 0)

        self.stockLabel_3 = ttk.Label(self.playerStatsFrame, text = str(self.player.getStock(2)))
        self.stockLabel_3.grid(row = 5, column = 0)

        self.stockLabel_4 = ttk.Label(self.playerStatsFrame, text = str(self.player.getStock(3)))
        self.stockLabel_4.grid(row = 6, column = 0)

        self.yearLabel = ttk.Label(self.playerStatsFrame, text = "Number of years passed : " + str(int(self.year)))
        self.yearLabel.grid(row = 7, column = 0)

    #====================End of player stats frame, beginning of last year stats frame=====================
        self.lastYearStatsFrame = ttk.LabelFrame(self.window, text= "Previous Year's stats")
        self.lastYearStatsFrame.grid(row = 2, column = 2,sticky=tk.E + tk.W + tk.N + tk.S)

    #====================End of last year stats frame, beginning of dialog box frame=====================
        self.dialogBoxFrame = ttk.LabelFrame(self.window, text= 'Dialog Box')
        self.dialogBoxFrame.grid(row = 0, column = 2, sticky=tk.E + tk.W + tk.N + tk.S)

        #Investment label
        self.dialogLabel = ttk.Label(self.dialogBoxFrame, text = "\t\t\t")
        self.dialogLabel.grid(row = 0, column = 1)

        #Previous year's stock change
        self.dialogLabel1 = ttk.Label(self.dialogBoxFrame, text = "")
        self.dialogLabel1.grid(row = 1, column = 1)
        
        self.dialogLabel2 = ttk.Label(self.dialogBoxFrame, text = "")
        self.dialogLabel2.grid(row = 2, column = 1)
        
        self.dialogLabel3 = ttk.Label(self.dialogBoxFrame, text = "")
        self.dialogLabel3.grid(row = 3, column = 1)
        
        self.dialogLabel4 = ttk.Label(self.dialogBoxFrame, text = "")
        self.dialogLabel4.grid(row = 4, column = 1)

        #Life events
        self.dialogLabel5 = ttk.Label(self.dialogBoxFrame, text = "")
        self.dialogLabel5.grid(row = 5, column = 1)
        
    #================End of dialog box frame, beginning of the stock news frame==================

        self.newsBoxFrame = ttk.LabelFrame(self.window, text= 'News regarding your stocks')
        self.newsBoxFrame.grid(row = 1, column = 2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.newsLabel = ttk.Label(self.newsBoxFrame, text='\t\t\t')
        self.newsLabel.grid(row=0,column=0)

    #================End of stock news frame, beginning of controller functions==================

    #Function to clear every entry box after hitting enter
    def clear_text(self):
        self.investInQMAGEntry.delete(0, 'end')
        self.investInPIPIEntry.delete(0, 'end')
        self.investInORLYEntry.delete(0, 'end')
        self.investInTREZEntry.delete(0, 'end')

    #All the investment and withdraw entry functions
    
    def investWithdrawQMAG(self,event):
        try:
            enteredAmt = int(self.investInQMAGEntry.get())
            if enteredAmt >= 0:
                change=self.player.getStock(0).invest(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
            else:
                change=self.player.getStock(0).withdraw(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
        except:
            self.clear_text()
            self.dialogLabel.configure(text="That didn't work. Please try re-entering the amount you want to invest.")

    def investWithdrawPIPI(self,event):
        try:
            enteredAmt = int(self.investInPIPIEntry.get())
            if enteredAmt >= 0:
                change=self.player.getStock(1).invest(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
            else:
                change=self.player.getStock(1).withdraw(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
        except:
            self.clear_text()
            self.dialogLabel.configure(text="That didn't work. Please try re-entering the amount you want to invest.")

    def investWithdrawORLY(self,event):
        try:
            enteredAmt = int(self.investInORLYEntry.get())
            if enteredAmt >= 0:
                change=self.player.getStock(2).invest(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
            else:
                change=self.player.getStock(2).withdraw(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
        except:
            self.clear_text()
            self.dialogLabel.configure(text="That didn't work. Please try re-entering the amount you want to invest.")

    def investWithdrawTREZ(self,event):
        try:
            enteredAmt = int(self.investInTREZEntry.get())
            if enteredAmt >= 0:
                change=self.player.getStock(3).invest(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
            else:
                change=self.player.getStock(3).withdraw(self.player, enteredAmt)
                self.dialogLabel.configure(text=change)
                self.clear_text()
                self.checkPlayerStats()
        except:
            self.clear_text()
            self.dialogLabel.configure(text="That didn't work. Please try re-entering the amount you want to invest.")


    #All the button click funtions (besides quit)
    def checkPlayerStats(self):
        global year
        self.playerStatsFrame.grid()
        self.nameLabel.configure(text = "Player Name: " + self.player.name)
        self.nameLabel.grid(row = 1, column = 0)
    
        self.balanceLabel.configure(text = "Current Balance: $" + str(self.player.getBal()))

        self.stockLabel_1.configure(text = str(self.player.getStock(0)))

        self.stockLabel_2.configure(text = str(self.player.getStock(1)))

        self.stockLabel_3.configure(text = str(self.player.getStock(2)))

        self.stockLabel_4.configure(text = str(self.player.getStock(3)))

        self.yearLabel.configure(text = "Number of years passed : " + str(int(self.year)))

    def nextYearUpdate(self):
        global year
        
        StockGame.lastYearStats(self)
        for i in range(4):
            text = (self.player.getStock(i).nextYear(self.player, self.year))
            if i == 0:
                self.dialogLabel1.configure(text = text)

            if i == 1:
                self.dialogLabel2.configure(text = text)
                
            if i == 2:    
                self.dialogLabel3.configure(text = text)

            if i == 3:   
                self.dialogLabel4.configure(text = text)
        
        self.year += 1
        l=LifeEvents()
        l.nextYear2(self.player, self)
        self.dialogLabel5.configure(text = l.nextYear2(self.player, self))

        self.balanceLabel.configure(text = "Current Balance: $" + str(self.player.getBal()))
            
        self.stockLabel_1.configure(text = str(self.player.getStock(0)))

        self.stockLabel_2.configure(text = str(self.player.getStock(1)))

        self.stockLabel_3.configure(text = str(self.player.getStock(2)))

        self.stockLabel_4.configure(text = str(self.player.getStock(3)))

        self.yearLabel.configure(text = "Number of years passed : " + str(int(self.year)))

        if(int(self.player.getBal())) < 0:
            self.youLose()

        if self.year == 5:
            self.newsLabel.configure(text="Quality Magnets has found a new, super-magnetic substance!\nThey expect to roll out new, super-strong magnets by next year.")

        elif self.year == 17:
            self.newsLabel.configure(text='Quality Magents has been caught using child labor.\nHuman rights groups protest the heinous action.')

        elif self.year == 1:
            self.newsLabel.configure(text='Math enthusiasts across the globe rejoice at the new Pi & Pie Café.\nA line that extends beyond the sidewalk appears on opening day.')

        elif self.year == 10:
            self.newsLabel.configure(text='Pi & Pie Café owner disagrees with world-renowned mathemeticians.\nMath enthusiasts boycott the store.')

        elif self.year == 14:
            self.newsLabel.configure(text='Pi & Pie Café owner apologizes for disagreeing with mathemeticians.\nThey realized that they forgot to carry a 0 when making their formula.')

        elif self.year == 12:
            self.newsLabel.configure(text='ORLY has made enough money to astronomically lower its prices.\nThis draws customers away from their competitors.')

        elif self.year == 3:
            self.newsLabel.configure(text='ORLY customers say "not actually a low price", absolutely furious.')

        elif self.year == 6:
            self.newsLabel.configure(text="ORLY's PR team has curbed the outrage against the business and is back to normal.")

        elif self.year == 16:
            self.newsLabel.configure(text='The trees that Treez Incorporated planted 15 years ago are growing well.\nPeople want to help out by buying more shares.')


        
        elif self.year == 20:
            self.youWin()
            self.window.destroy()

        else:
            self.newsLabel.configure(text='No special news regarding your stocks')

    def lastYearStats(self):
        
        global year

        if self.year == 0:
            
            self.lastYearLabel = ttk.Label(self.lastYearStatsFrame, text = "These are from year: " + str(int(self.year)))
            self.lastYearLabel.grid(row = 0, column = 0)

            self.previousBalanceLabel = ttk.Label(self.lastYearStatsFrame, text = "Current Balance: $" + str(self.player.getBal()))
            self.previousBalanceLabel.grid(row = 1, column = 0)

            self.previousStockLabel_1 = ttk.Label(self.lastYearStatsFrame, text = str(self.player.getStock(0)).replace("currently have", "had"))
            self.previousStockLabel_1.grid(row = 3, column = 0)

            self.previousStockLabel_2 = ttk.Label(self.lastYearStatsFrame, text = str(self.player.getStock(1)).replace("currently have", "had"))
            self.previousStockLabel_2.grid(row = 4, column = 0)

            self.previousStockLabel_3 = ttk.Label(self.lastYearStatsFrame,text = str(self.player.getStock(2)).replace("currently have", "had"))
            self.previousStockLabel_3.grid(row = 5, column = 0)

            self.previousStockLabel_4 = ttk.Label(self.lastYearStatsFrame, text = str(self.player.getStock(3)).replace("currently have", "had"))
            self.previousStockLabel_4.grid(row = 6, column = 0)

        else:
            self.lastYearLabel = ttk.Label(self.lastYearStatsFrame, text = "These are from year: " + str(int(self.year)))
            self.lastYearLabel.grid(row = 0, column = 0)

            self.nameLabel.configure(text = "Player Name: " + self.player.name)
            self.nameLabel.grid(row = 1, column = 0)

            self.previousBalanceLabel.configure(text = "Current Balance: $" + str(self.player.getBal()))

            self.previousStockLabel_1.configure(text = str(self.player.getStock(0)).replace("currently have", "had"))

            self.previousStockLabel_2.configure(text = str(self.player.getStock(1)).replace("currently have", "had"))

            self.previousStockLabel_3.configure(text = str(self.player.getStock(2)).replace("currently have", "had"))

            self.previousStockLabel_4.configure(text = str(self.player.getStock(3)).replace("currently have", "had"))

    def youWin(self):
        self.window2 = tk.Tk()
        self.window2.title('The End')
        self.window2.geometry("900x200")
        self.endLabel = ttk.Label(self.window2,text="\nAfter 20 years of investment, you ended with these stats\n\n\n")
        self.endLabel.pack()
        self.endLabel2 = ttk.Label(self.window2,text=str(self.player)+'\n\n')
        self.endLabel2.pack()
        self.quitButton = tk.Button(self.window2,text='Quit',command = self.window2.destroy)
        self.quitButton.pack()

    def youLose(self):
        self.window2 = tk.Tk()
        self.window2.title('Game Over')
        self.window2.geometry("900x150")
        self.endLabel = ttk.Label(self.window2,text="\nSomething happened to put you in debt, but those who you are indebted to agree to forgive your debt in exchange for all your stocks.")
        self.endLabel.pack()
        self.endLabel2 = ttk.Label(self.window2,text="\nRemember to keep some money around in case something bad happens next time!\n\n\n")
        self.endLabel2.pack()
        self.quitButton = tk.Button(self.window2,text='Quit',command = self.window2.destroy)
        self.quitButton.pack()
        self.window.destroy()
        
   
#==============================================================================End of the GUI class=============================================================================
################################################################################################################################################################################
################################################################################################################################################################################
#===========================================================================Start of main() function============================================================================


def main():
    
    #Creating four stocks to play with: QualityMagnets, Pi and Pie Math and Food Company, O'Really Auto Parts, and Trees Incorporated
    QMAG = Stock('QMAG', 1000)
    PIPI = Stock('PIPI', 1000)
    ORLY = Stock('ORLY', 1000)
    TREZ = Stock('TREZ', 1000)

    #Creating a player class with a name, balance, and the stocks they are invested in
    player1 = Player('StockMan', 50000, [copy(QMAG), copy(PIPI), copy(ORLY), copy(TREZ)])


    #Create the game
    #NOTE: POSSIBLY ADD A MULTIPLAYER FUNCTIONALITY USING A LIST OF PLAYERS
    program = StockGame(player1)
    #Play the game
    program.window.mainloop()

if __name__ == '__main__':
    main()
