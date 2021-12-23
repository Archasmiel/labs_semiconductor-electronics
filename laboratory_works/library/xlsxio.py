import openpyxl


def read_sheet_to_array(sheet, rows, columns, swap):
    if swap:
        rows, columns = columns, rows

    sheet_data = []
    for i in columns:
        temp = []
        for j in range(rows[0], rows[1] + 1):
            temp.append(sheet[i + str(j)].value)
        sheet_data.append(temp)
    return sheet_data


def get_all_sheets_from_file(path, columns, rows):
    wb_obj = openpyxl.load_workbook(path, data_only=True)
    sheets = [wb_obj[i] for i in wb_obj.sheetnames]
    all_sheets = []
    for k in range(len(sheets)):
        cur_sheet = read_sheet_to_array(sheets[k], columns[k], rows[k], True)
        all_sheets.append(cur_sheet)
    return all_sheets
