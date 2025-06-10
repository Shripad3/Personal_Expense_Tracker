import pandas as pd
import openpyxl
from dataclasses import dataclass

@dataclass
class ReturnVars:
    dates: list
    categories: list
    amounts: list
    types: list
    cat_amt: dict
    categoryType: dict
    totalIncome: float
    totalExpenses: float
    netBalance: float

#if the uploaded file is excel.
def get_excelData(file_path):
    # Load workbook and sheet
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Determine max number of rows
    max_rows = sheet.max_row

    columns = ['A', 'B', 'C', 'D']
    dates = []
    categories = []
    amounts = []
    types = []
    cat_amt = {}
    categoryType = {}
    for row in range(2, max_rows + 1):  # row 1 has headers
        #storing cell values as we iterate through the excel
        date_cell = sheet[f"A{row}"].value
        category_cell = sheet[f"B{row}"].value
        amount_cell = sheet[f"C{row}"].value
        type_cell = sheet[f"D{row}"].value
        #appending cell values to their respective lists
        dates.append(date_cell)
        categories.append(category_cell)
        amounts.append(amount_cell)
        types.append(type_cell)
        
    for i in range(len(amounts)):
        cat_amt[categories[i]] = amounts[i]
        categoryType[categories[i]] = types[i]

    totalIncome = 0
    totalExpenses = 0
    netBalance = 0
    for category in categories:
        if (categoryType[category]).lower() == 'income':
            totalIncome += cat_amt[category]
        elif (categoryType[category]).lower() == 'expense':
            totalExpenses += cat_amt[category]
    netBalance = totalIncome - totalExpenses

    return ReturnVars(
        dates = dates,
        categories = categories,
        amounts = amounts,
        types = types,
        cat_amt = cat_amt,
        categoryType = categoryType,
        totalIncome = totalIncome,
        totalExpenses = totalExpenses,
        netBalance = netBalance
    )

    # print("Total Income: ", totalIncome)
    # print("Total Expenses: ", totalExpenses)
    # print("Net Balance: ", netBalance)
    # print("Dates: ", dates)
    # print("Categories: ", categories)
    # print("Amounts: ", amounts)
    # print("Mappings1: ", cat_amt)
    # print("Mappings2: ", categoryType)


#if the uploaded file is csv.
def get_csvData(file_path):
    df = pd.read_csv(file_path)
    dates = list(df['Date'])
    categories = list(df['Category'])
    amounts = list(df['Amount'])
    types = list(df['Type'])
    cat_amt = {}
    categoryType = {}

    for i in range(len(categories)):
        cat_amt[categories[i]] = amounts[i]
        categoryType[categories[i]] = types[i]

    totalIncome = 0
    totalExpenses = 0
    netBalance = 0
    for category in categories:
        if (categoryType[category]).lower() == 'income':
            totalIncome += cat_amt[category]
        elif (categoryType[category]).lower() == 'expense':
            totalExpenses += cat_amt[category]
    netBalance = totalIncome - totalExpenses

    return ReturnVars(
        dates = dates,
        categories = categories,
        amounts = amounts,
        types = types,
        cat_amt = cat_amt,
        categoryType = categoryType,
        totalIncome = totalIncome,
        totalExpenses = totalExpenses,
        netBalance = netBalance
    )
