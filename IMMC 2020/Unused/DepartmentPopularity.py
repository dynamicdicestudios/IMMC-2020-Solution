def get_excel_info():
    loc = (r"C:\Users\Josiah\Desktop\IMMC 2020\StoreData_IMMC.xlsx") 
      
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)

    return sheet

def get_department_ratings():
    sheet = get_excel_info()
    sheet.cell_value(0, 0)
    departments = {}

    for i in range(2, sheet.nrows):
        name = sheet.row_values(i)[0]
        rating = sheet.row_values(i)[8]
        
        if sheet.row_values(i)[4] == "":
            break
        
        departments[name] += rating

    return departments

def 
