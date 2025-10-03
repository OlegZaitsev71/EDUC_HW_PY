class CustomerDataClass:  # noqa: D100
    """_summary_."""
    def __init__(self,customerid,customername):
        """_summary_.

        Args:
            customerid (_type_): _description_
            customername (_type_): _description_
        """        
        self.customerId=customerid
        self.CustomerName=customername 
        self.Orders=[]

    def addorder(self,orderobject):
        """_summary_.

        Args:
            orderobject (_type_): _description_
        """        
        self.Orders.append(orderobject)

    def getotalamount(self):
        """_summary_.

        Returns:
            _type_: _description_
        """        
        total=0
        for o in self.Orders:
            total = total + o.amount
        return total
    
    def calculatediscount(self):
        """_summary_.

        Args:
            customerobj (_type_): _description_

        Returns:
            _type_: _description_
        """        
        totalamount = self.getotalamount()
        discount = totalamount * 0.1 if totalamount > 1000 else 0
        return discount
    
    def printcustomerreport(self, orderobject):
        """_summary_.

        Args:
            customerobj (_type_): _description_
        """        
        print('Customer Report for:', self.CustomerName)
        print('Total Orders:', len(self.Orders))
        print('Total Amount:', self.getotalamount()) 
        print('Discount:', self.calculatediscount())
        print('Average Order:',self.getotalamount()/len(self.Orders))


class OrderDataClass:
    """_summary_."""
    def __init__(self,orderid,amount):
        """_summary_.

        Args:
            orderid (_type_): _description_
            amount (_type_): _description_
        """        
        self.orderId=orderid
        self.amount=amount



def mainprogram():
    """_summary_."""        
    c1=CustomerDataClass(1,'SAP Customer')
    o1=OrderDataClass(101,500)
    c1.addorder(o1) 
    c1.printcustomerreport(o1) 
            
    c2=CustomerDataClass(2,'Empty Customer')
    o2=OrderDataClass(102,1800)
    c2.addorder(o2)
    c2.printcustomerreport(o2) 

    o3=OrderDataClass(103,800)
    c2.addorder(o3)
    c2.printcustomerreport(o3)


mainprogram()




