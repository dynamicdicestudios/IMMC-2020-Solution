def get_excel_info():
    loc = (r"C:\Users\Josiah\Desktop\IMMC 2020\StoreData_IMMC.xlsx") 
      
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
      
    sheet.cell_value(0, 0)
    items = []

    for i in range(2, sheet.nrows):
        if sheet.row_values(i)[4] == "":
            break
        items.append(sheet.row_values(i)[4:9])

    return items

def deal_sort(bad, good):
    popular = []
    
    items = get_excel_info()
    
    for item in items:
        discount = 1.0 - (float(item[2])/float(item[1]))
        quantity = item[3]
        rating = item[4]
        temp = item[0], discount, quantity, rating
        temp = list(temp)
        
        if discount > good:
            average = (rating + quantity) / 2.0

    return front, mid, back
