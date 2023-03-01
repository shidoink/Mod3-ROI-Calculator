class ROICalc():

    def __init__(self,cashonCashROI):
        '''initiates class'''
        self.cashonCashROI= cashonCashROI

    def calcPropertyValue(self):
        '''gathers user input for property value'''
        self.propertyValue= input(" What is the value of your property? $")

    def calcIncome(self):
        '''gathers user input for montly rental income '''
        self.income= input(" What will be your rental income per month? $")
    
    def calcExpenses(self):
        '''calculates expense from income, property value, and assorted user inputs'''
        tax= (float(self.income)* 0.075)
        insurance= (float(self.propertyValue)* 0.0005)
        vacancy =input("How much per month are you going to budget for vacancies? $")
        repairs= input("How much per month are you going to budget for repairs? $")
        capex= input("How much per month are you going to budget for capital expenses? $")
        prop_man= input("How much per month are you going to budget for property management? $")
        mortgage= input("What will be your monthly mortgage payment? $")
        self.expenses= (float(tax) + float(insurance) +float(vacancy) +
                        float(repairs) + float(capex) + float(prop_man) + float(mortgage))
        
        print(f'TAX:{tax}\nINSURANCE: {insurance} \nREPAIRS: {repairs} \nCAPITAL EXPENSES: {capex}')
        print(f'PROPERTY MANAGEMENT: {prop_man}\nMORGAGE: {mortgage} \nTotal Expenses = {self.expenses}')
    
    def calcCashFlow(self):
        '''calculates cash flow'''
        self.cashFlow= float(self.income) - float(self.expenses)
        print(f'Expected monthly cashflow= {self.cashFlow}')
    
    def calcCoCROI(self):
        '''calculates Cash on Cash ROI'''
        down_payment= input("What will be your down payment?(typical 20% property value) $")
        closing_costs= input("What will be your closing costs? $")
        rehab_budget= input("What will you spend on rehab? $")
        annual_cash_flow= float(self.cashFlow*12)
        total_investment= float(down_payment) + float(closing_costs) + float(rehab_budget)
        print(f'\nExpected annual cash flow: {annual_cash_flow}')
        print(f'Expected total investment: {total_investment} ')
        self.cashonCashROI= (float(annual_cash_flow) / float(total_investment))*100
        print(f'\nCalculated Cash on Cash Return on investment = % {self.cashonCashROI}')



my_prop=ROICalc(0)
my_prop.calcPropertyValue()
my_prop.calcIncome()
my_prop.calcExpenses()
my_prop.calcCashFlow()
my_prop.calcCoCROI()