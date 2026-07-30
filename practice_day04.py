class product:
    def __init__(self,name,code,price,quantity,discount):
        self.name=name
        self.product_code=code
        self.price=price
        self.quantity=quantity
        self.discount=discount
        self.Total=(self.quantity*self.price)-((self.quantity*self.price)*self.discount/100)
    @classmethod
    def display(cls,lists):
        print("           ---Shoping Cart Bill---")
        print("item name    price    quantity    discount    total")    
        for items in lists:
            print(items.name,"  ",items.price,"  ",items.quantity,"  ",items.discount,"  ",items.Total)
        net_total=product.grand_total(lists)
        print(net_total)
    @staticmethod
    def grand_total(lists):
        grand_total=0
        for items in lists:
            grand_total=grand_total+items.Total
        return grand_total

p1=product("mouse ",1123  ,230.0,2,8) 
p2=product("monitor",1313,2999.0,1,0)
lists=[p1,p2]
product.display(lists)
