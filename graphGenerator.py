import matplotlib.pyplot as plt
from fpdf import FPDF
import data_utils

def generate_graph(obj):
    # file_path = r'/Users/shripad/Documents/Developer/Projects/Project-1-Email Report Generator/test.xlsx'
    # obj = data_utils.get_excelData(file_path)
    x = []
    y = []

    ##################Overall Graph##################
    # x = obj.categories
    # y = obj.amounts

    # plt.plot(x, y, marker = 'o')
    # plt.title("Overall Graph")
    # plt.xlabel('Categories')
    # plt.xlabel('Amount(in $)')
    # plt.grid(True)
    # plt.show()


    ##################Income Graph##################
    # for i in range(len(obj.categories)):
    #     if (obj.categoryType[obj.categories[i]]).lower() == 'income':
    #         x.append(obj.categories[i])
    #         y.append(obj.amounts[i])

    # plt.plot(x, y, marker = 'o')
    # plt.title("Incomes Graph")
    # plt.xlabel("Category")
    # plt.ylabel("Amount(in $)")
    # plt.grid(True)
    # plt.show()


    ##################Expenses Graph##################
    # for i in range(len(obj.categories)):
    #     if (obj.categoryType[obj.categories[i]]).lower() == 'expense':
    #         x.append(obj.categories[i])
    #         y.append(obj.amounts[i])

    # plt.plot(x, y, marker = 'o')
    # plt.title("Expenses Graph")
    # plt.xlabel("Category")
    # plt.ylabel("Amount(in $)")
    # plt.grid(True)
    # plt.xticks(rotation = 45)
    # plt.tight_layout()
    # plt.savefig('Expenses_Graph.png')
    # plt.show()


    ##################Expenses Pie Chart##################
    # for i in range(len(obj.categories)):
    #     if (obj.categoryType[obj.categories[i]]).lower() == 'expense':
    #         x.append(obj.categories[i])
    #         y.append(obj.amounts[i])
    # print(x)
    # print(y)
    # plt.pie(
    #     y,
    #     labels=x,
    #     autopct='%1.1f%%',
    #     startangle=140,
    #     shadow=True
    # )
    # plt.title("Expenses Chart")
    # plt.axis('equal')
    # plt.show()



    income_labels = []
    income_values = []
    expense_labels = []
    expense_values = []

    # Separate incomes and expenses
    for i in range(len(obj.categories)):
        category = obj.categories[i]
        amount = obj.amounts[i]
        type_ = obj.categoryType[category].lower()

        if type_ == 'income':
            income_labels.append(category)
            income_values.append(amount)
        elif type_ == 'expense':
            expense_labels.append(category)
            expense_values.append(amount)

    # Create subplots: 1 row, 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Income Pie
    ax1.pie(income_values, labels=income_labels, autopct='%1.1f%%', startangle=140, shadow=True)
    ax1.set_title('Income Distribution')
    ax1.axis('equal')

    # Expense Pie
    ax2.pie(expense_values, labels=expense_labels, autopct='%1.1f%%', startangle=140, shadow=True)
    ax2.set_title('Expense Distribution')
    ax2.axis('equal')

    # Add a main title
    plt.suptitle("Income vs Expense Breakdown", fontsize=16)
    plt.tight_layout()
    plt.savefig('monthly_report.png', format='png', dpi=300, bbox_inches = 'tight')
    # plt.show()
