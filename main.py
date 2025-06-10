import os
import data_utils
import report_generator
import graphGenerator
import email_sender


file_path = r'/Users/shripad/Documents/Developer/Projects/Project-1-Email Report Generator/test.xlsx'
file_extension = os.path.splitext(file_path)[1].lower()

if file_extension == ".xlsx":
    print("Excel file inputted")
    obj = data_utils.get_excelData(file_path)
    graphGenerator.generate_graph(obj)
    report_generator.generate_pdf(obj)
    email_sender.send_mail()
elif file_extension == ".csv":
    print("CSV file inputted")
    obj = data_utils.get_csvData(file_path)
    graphGenerator.generate_graph(obj)
    report_generator.generate_pdf(obj)
    email_sender.send_mail()
else:
    print("Invalid file type")


