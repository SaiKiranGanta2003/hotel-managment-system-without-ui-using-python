import datetime
temp=(str(datetime.datetime.now()).split())[1]
time=temp[:8]
date=(str(datetime.datetime.now()).split())[0]

def show_items():
    print()
    for i in range(len(list1)):
        print(f'{i+1} . {list1[i]}  {amount[i]}rs' )
    print()
    print()

def  item_number():
    show_items()
    try:
        items=int(input('Enter the items code using above text - '))
        print()
    except:
        print('print enter correct item number - ')
        item_number()
    if items<10:
        return items
    else:
        item_number()
        
def quant():
    try:
        quantity=int(input('enter the qunatity you want - '))
        print()
    except:
        print('enter numbers only')
        quant()
    return quantity

def add_item(list_items,order_cost,count1):
    item=item_number()
    quantity=quant()
    list_items.append(list1[item-1])
    order_cost.append(amount[item-1]*quantity)
    count1.append(quantity)

def remove_item(list_items,order_cost,count1):
    for i in range(len(list_items)):
        print(f'{i+1} . {list_items[i]} - qunatity : {count1[i]}')
    remove_items=int(input('enter the items number which you want to delete - '))
    if remove_items>len(list_items):
        print('item number doesnot exsit')
        remove_item()
    else:
        list_items.pop(remove_items-1)
        order_cost.pop(remove_items-1)
        count1.pop(remove_items-1)

def place_order(list_items,order_cost,count1):
    print()
    print('your order is')
    for i in range(len(list_items)):
        print(f'{i+1}. {list_items[i-1]} - qunatity {count1[i]}')
    print('Total amount',sum(order_cost))
    filename=date+'.txt'
    with (open(filename,'a') as f):
        f.write('****************************************************************************\n')
        for i in range(len(list_items)):
            f.write(str(i+1)+'. '+ list_items[i-1] +' quantity ' +str(count1[i-1])+'\n')
        f.write('total amount of order'+str(sum(order_cost))+'\n')
        f.write('****************************************************************************'+'\n')
    total_amounts_of_order.append(sum(order_cost))

def show_order_details(list_items,order_cost,count1):
    print('the order details are')
    for i in range(len(list_items)):
        print(f'{i+1} . {list_items[i]} - quantity {count1[i]}')
    print('total price of this order ',sum(order_cost))

def new_order():
    list_items=[]
    order_cost=[]
    count1=[]
    while True:
        print('================================================')
        print()
        print('1.Add item')
        print('2.Remove Item')
        print('3.Place Order')
        print('4. show order details')
        print('5.Clear the order')
        print()
        print()
        try:
            choice1=int(input('which Operation you want to do - '))
            print()
        except:
            print('invalid number')
            new_order()
        if choice1==1:
            add_item(list_items,order_cost,count1)
        elif choice1==2:
            remove_item(list_items,order_cost,count1)
        elif choice1==3:
            place_order(list_items,order_cost,count1)
            break
        elif choice1==4:
            show_order_details(list_items,order_cost,count1)
        elif choice1==5:
            new_order()
        else:
            print('invalid input try again')
            new_order()

def closing_time():
    filename=date+'.txt'
    with (open(filename,'a') as f):
        f.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        f.write('this is the end of day\n')
        sum_of_prodct=sum(total_amounts_of_order)
        count_of_order=len(total_amounts_of_order)
        f.write('The total number of orders is '+str(count_of_order)+'\n')
        f.write('Today total collection is '+str(sum_of_prodct)+'\n')
        f.write('\n')
        f.write('Good night! \n')
        f.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
def print_data():
    sum_of_prodct=sum(total_amounts_of_order)
    count_of_order=len(total_amounts_of_order)
    print('The total number of orders is '+str(count_of_order))
    print('Today total collection is '+str(sum_of_prodct))
        
list1=['Briyani','Chicken kabab','Noodles','Chicken wings', 'Chicken 65','sprit','fanta','chicken briyani','fried rice']
amount=[200,150,100,180,150,50,50,180,120]
total_amounts_of_order=[]

def main():
    while True:
        print()
        print()
        print('welcome to the hotel')
        print('-----------------------------------------')
        print('1.New Order')
        print('2.closing time')
        print('3.today count of orders and the total amount')
        print('4.close the program')
        print()
        print()
        try:
            choice=int(input('enter your input - '))
            print()
        except: 
            print('invalid input! try again')
            main()
        if choice == 1:
            new_order()
        elif choice==2:
            closing_time()
        elif choice==3:
            print_data()
        elif choice==4:
            print('The program is terminating good bye')
            break
        else:
            print('invalid input try again')
            main()
main()
print()
print('gud night broo!!!!!!!!')
print('-----------------------------------------')
print()
total_amounts_of_order=[]