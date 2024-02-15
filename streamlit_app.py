import streamlit

import pandas as pd
import numpy


# ENSURE YOUR CSV FILE are CAPITILsed including Column to make it easy to match , = UPPER(A1)
# forced the  USER INPUT to capitalise   Str.upper()
# Ensure your CSV HAS NO WHITESAPCE N COL NAME -GIVES KEY ERROR
# REMOVE WHITE SPACE FROM ALL VALUES IN CSV  = strip(A1)
# remove white space from user entry str.strip()
# create function to handle button

def salesRecords(sales_details):
     try:
        if sales_details[0] == 0:
            return 'Enter Sales ID.  '
        elif sales_details[1] == '':
            return 'Enter Sales item '
        elif sales_details[2] == 0.00:
            return 'Enter unit price '
        elif sales_details[3] == 0:
            return 'Enter quantity '
        # elif sales_details[4] == 0.00: zero value is allowed as no dsicount
        #     return 'Enter Discount'
        elif sales_details[5] == 0 : #automatically calclated
             return 'Enter price'
        elif sales_details:  # is not empty
            # check for double sales id
            df_sale = pd.read_csv('simpleSalesRecord.csv')
            check_salesid = df_sale['SALES_ID'].values.tolist()  # if does work with pandas convert to list
            if sales_details[0] in check_salesid:
                return 'This sales has been registered. choose another sales id!!!'
            else:
                Input_array = numpy.asarray(sales_details)
                Input_array_reshaped = Input_array.reshape(1, -1)  # one row ,as many cols
                df= pd.DataFrame(Input_array_reshaped)
                df.to_csv('simpleSalesRecord.csv',mode='a',index= False,header=False)

                return 'Sales entry was sucessful'
        else: # if everrything failed
            return 'Sales entry  failed '
     except:  # capture bug and error
          return 'code error '

def fetchSale(see_records):
    # try:
        if see_records[0] == 'ADMIN':  #for security purpose create a file to hold this password
        # if  password is Admin
            df_fetch = pd.read_csv('simpleSalesRecord.csv')
        # dispay the file to user
            streamlit.write(df_fetch)
            count = len(df_fetch)
        # calculate the sum  to user
            total_sales = df_fetch['PRICE'].sum()
            return f'Your total amount is {total_sales} for  {count} sales'
        else:
            return 'wrong password'
    # except:  # capture bug and error
    #     return 'error in Registration'


#delete sales record
def deleteSalesRecords(sales_delete):  #delet error in sales records
    try:
        if sales_delete[0] == 'ADMIN':
            #proceed if password is admin
            if sales_delete[1]: # if entry for row to delete is not empty
                df_fetch2 = pd.read_csv('simpleSalesRecord.csv')
                if sales_delete[1] < len(df_fetch2.index) : # row mut not be greater than length
                #drop the row df.index[-1]
                    df_update_sales = df_fetch2.drop(df_fetch2.index[sales_delete[1]])
                    df_update_sales.to_csv('simpleSalesRecord.csv',index =False)  #do not add new index to update file
                    return f'Row {sales_delete[1]}  is successfully deleted '
                else:
                    return 'Row of record doesnt exist. Enter proper row number  '
            else:
                return ' you have not entered row number to delete'
        else:
            return " wrong password"
    except:  # capture bug and error do not show it to ende user
         return 'code error'


#deleteAllSalesRecords
#to drop all rows in dataframe keeper the header/cols
#update the new file csv with no index
def deleteAllSalesRecords(Allsales_delete):
    try:
        if Allsales_delete[0] == 'ADMIN':
            df_fetch3 = pd.read_csv('simpleSalesRecord.csv')
            #drop all row apart from row 1 reserved
            df_update_all_sales = df_fetch3.drop(df_fetch3.index[1:])
            df_update_all_sales.to_csv('simpleSalesRecord.csv',index =False)  #do not add new index to update file
            streamlit.write(df_update_all_sales)
            return f' all sales records is successfully deleted '
        else:
            return " wrong password"
    except:
        return 'error in code'

#df.at[index,col label] = new value
def editing(usersupdate):
    if usersupdate[0] == 'ADMIN':
        #proceed if password is admin
        if usersupdate[1] == 0:  #2
            return ' enter index or row  number to edit '
        elif usersupdate[2] == '': #desc
            return ' enter column name to edit'
        elif usersupdate[3] == '':
            return ' enter new values '
        elif usersupdate: # not empy

            df_update = pd.read_csv('simpleSalesRecord.csv')
            df_update.at[usersupdate[1], usersupdate[2]] = usersupdate[3]
            df_update.to_csv('simpleSalesRecord.csv',index = False)

            return ' file has been update '
        else:
            return 'no entry found'
    else:
        return 'wrong password'

def fetchStock(stockdetails):
    try:
        return 'option not activated in this package'
    except:
        return 'option not activated in this package'
def fetchliveStock(livestockdetails):
    try:
        return 'option not available in this package'
    except:
        return 'option not activated in this package'
def stckRecords(stockuploader):
    try:
        return 'option not available in this package'
    except:
        return 'option not activated in this package'

##### build interface
def main():
    # # sales inteface
    # # give a title
    streamlit.title('MY SHOPPING MALL, LAGOS-Sales Records')

    streamlit.image('blogo.png', caption='Shop Logo')  # copy image to pain resize 100 pixel
    streamlit.title('Enter Sales')

    # fect last sales id for tracking
    dflast_sales_id= pd.read_csv('simpleSalesRecord.csv')
    last_sales_id = dflast_sales_id['SALES_ID'].iloc[-1]
    Next_sales_ID = last_sales_id + 1
    streamlit.write('sales id is:',Next_sales_ID)

    with streamlit.form("Salesform", clear_on_submit=True):

        Enter_sale_id = streamlit.number_input('enter sales id', min_value=0, max_value=1000000, value=Next_sales_ID, step=1, key='sid')
        Enter_sale_id = int(Enter_sale_id)

        Enter_items = streamlit.text_input('ENTER SALES ITEMS', value="",key= 'sitems')
        Enter_items_cl = Enter_items.upper().strip() # # convert when fetching from file or user


        Enter_unit_price = streamlit.number_input('ENTER UNIT PRICE', min_value=0.00, max_value=1000000.00, value=0.00, step=1.00, key='uprice')
        Enter_unit_price =float(Enter_unit_price) # convert when fetching from file or user
        Enter_qty = streamlit.number_input('ENTER QTY', min_value=0, max_value=1000000, value=0, step=1,key='uqty')
        Enter_qty = int(Enter_qty) # convert when fetching from file or user

        Enter_Discount = streamlit.number_input('ENTER DISCOUNT', min_value=0.00, max_value=1000000.00, value=0.00, step=1.00, key='dis')
        Enter_Discount = float(Enter_Discount) # convert when fetching from file or user

        Enter_price2 = (Enter_unit_price * Enter_qty) - Enter_Discount
        Enter_price1= float(Enter_price2) # convert when fetching from file or user
        Enter_price = streamlit.number_input('PRICE IS', min_value=0.00, max_value=1000000000.00, value=0.00, step=1.00, key='price')


        Enter_notes = streamlit.text_input('Observation', value="", key='ob')

        current_time = pd.Timestamp.now()
        time = streamlit.text_input('Timer', value=current_time, key='tim')

        submit = streamlit.form_submit_button(label="Upload Sales")

    salesrecords = ""  # declare this variable to hold result like empty list
    if submit:          #
    # if streamlit.button('Upload Sales',key = 'upsal'):
        # Reg ...call the function to process input
        salesrecords = salesRecords([Enter_sale_id,Enter_items_cl,Enter_unit_price,Enter_qty ,Enter_Discount,Enter_price,Enter_notes,time])
    streamlit.success(salesrecords)



#sales record viewer
#  ----- fetch all sales records
    # give a title

    streamlit.title('Display My Sales Record')

    admin_password = streamlit.text_input('enter password', value="", key='salpass')
    admin_password_upper = admin_password.upper().strip()
    fetchsale = ""  # declare this variable to hold result like empty list

    if streamlit.button('See all Sales', key='fetsale'):
        # fetchRecords ...call the function to process input
        fetchsale = fetchSale([admin_password_upper])
    streamlit.success(fetchsale)


    streamlit.subheader('Admins only')
    # DELeTING wrong sales RECORDS
    admin_del = streamlit.number_input('enter row number of record to delete', min_value=0, max_value=1000000, value=0,
                                           step=1, key='delrows')

    delectesal = ""
    if streamlit.button('Delete one Sales Record', key='delsal'):
        delectesal = deleteSalesRecords([admin_password_upper, int(admin_del)])
    streamlit.success(delectesal)  # return the result

    col1, col2 = streamlit.columns((1,2))
    with col1:
        # DELeTING all sales RECORDS fro new business day
        delecteallsal = ""
        if streamlit.button('Delete All Sales Record', key='delallsal'):
            delecteallsal = deleteAllSalesRecords([admin_password_upper])
        streamlit.success(delecteallsal)  # return the result

    #### edit button of a file
    col1, col2, col3 = streamlit.columns((1, 1, 1))  # layout element
    with col1:
        Enter_row_number = streamlit.number_input('Enter_row_number ', min_value=0, max_value=10000, value=0, step=1,
                                                  key='rowno')
        Enter_row_number = int(Enter_row_number)
    with col2:
        Enter_col_title = streamlit.text_input('Enter_title of column', value="", key='colabel')
        Enter_col_title_cl = Enter_col_title.upper().strip()  # col must match the document
    with col3:
        Enter_new_value = streamlit.text_input('Enter_new_value', value="", key='newval')
        Enter_new_value_cl = Enter_new_value.strip()

    edit = ""  # declare this variable to hold result like empty list

    if streamlit.button('edit file', key='ed'):
        # Reg ...call the function to process input
        edit = editing([admin_password_upper, Enter_row_number, Enter_col_title_cl, Enter_new_value_cl])

    streamlit.success(edit)

# option not avialble   for this package
    #  ----- fetch all stock records
    # give a title
    streamlit.header('This option is not available in this package')
    streamlit.subheader ('Check Inventory & stock taking ')

    admin_stk_password = streamlit.text_input('enter password', value="", key='stkpass')
    admin_stk_password_upper = admin_stk_password.upper().strip()
    fetchstk = ""  # declare this variable to hold result like empty list

    if streamlit.button('See last inventory', key='fetstck'):
        # fetchRecords ...call the function to process input
        fetchstk = fetchStock([admin_stk_password_upper])
    streamlit.success(fetchstk)

    #### getting live inventory
    fetchstklive = ""  # declare this variable to hold result like empty list

    if streamlit.button('See live inventory', key='fetlivstck'):
        # fetchRecords ...call the function to process input
        fetchstklive = fetchliveStock([admin_stk_password_upper])
    streamlit.success(fetchstklive)

    # upload stock

    streamlit.subheader(' upload new stock')
    with streamlit.form("myform", clear_on_submit=True):
        Enter_stk_id = streamlit.number_input('enter stock category id', min_value=0, max_value=1000000, value=0,
                                              step=1, key='sitemid')
        Enter_stk_id = int(Enter_stk_id)
        # fect curent stock id
        dflast_stcok_id = pd.read_csv('Stock.csv')
        dflast_stcok_id = dflast_stcok_id['Stock_id'].iloc[-1]
        Next_stcok_id = dflast_stcok_id + 1
        streamlit.write('the next stock id is:', Next_stcok_id)

        Enter_stk_items = streamlit.text_input('enter stock category name', value="", key='stckitems')
        Enter_stk_items_cl = Enter_stk_items.upper().strip()  # pass an upper

        Enter_stk_Desc = streamlit.text_input('stock item description', value="", key='stkdesc')
        Enter_stk_Desc_cl = Enter_stk_Desc.upper().strip()  # pass an upper

        Enter_stk_oty = streamlit.number_input('enter quantity ', min_value=0, max_value=1000000, value=0, step=1,
                                               key='stkqty')
        Enter_stk_oty = int(Enter_stk_oty)

        Enter_stk_price = streamlit.number_input('enter cost price of stock', min_value=0.00, max_value=1000000000.00,
                                                 value=0.00, step=1.00, key='stkprice')
        Enter_stk_price = int(Enter_stk_price)
        Enter_amount_made = 0
        Enter_profit_made = 0
        Enter_stk_uprice = streamlit.number_input('enter selling unit price of stock', min_value=0.00,
                                                  max_value=1000000000.00,
                                                  value=0.00, step=1.00, key='unstkprice')
        Enter_stk_uprice = int(Enter_stk_uprice)

        Enter_stk_notes = streamlit.text_input('enter  observation about product if any', value="", key='stkob')

        current_time = pd.Timestamp.now()
        time_stk = streamlit.text_input('date and Time of stock', value=current_time, key='stktim')
        submit = streamlit.form_submit_button(label="Upload stock")
    stockrecords = ""  # declare this variable to hold result like empty list

    if submit:  # streamlit.button('Upload stock',key = 'upstck'):
        # Reg ...call the function to process input
        stockrecords = stckRecords(
            [Enter_stk_id, Enter_stk_items_cl, Enter_stk_Desc_cl, Enter_stk_oty, Enter_stk_price, Enter_amount_made,
             Enter_profit_made, Enter_stk_uprice, Enter_stk_notes, time_stk])

    streamlit.success(stockrecords)

    streamlit.write('aPP for every shop developers')

if __name__ == '__main__':
    main()

# web app  on your desktop local host
#run  on your pycharm terminal ' streamlit run simpleSales.py '
########
