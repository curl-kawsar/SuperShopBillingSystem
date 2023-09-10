from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        #product_category_list
        self.Category=["Select Option","Clothing","LifeStyle","Grocery"]    
        
        
        #SubCloth
            
        self.SubCatClothing=["Pant","T_Shirt","Shirt"]
        self.pant=["Levis","Mufti","Dior"]
        self.price_Levis=500
        self.price_Mufti=700
        self.price_Dior=1000
        
        self.T_Shirt=["Polo","Half","Full"]
        self.price_Polo=500
        self.price_Half=700
        self.price_Full=1000
        
        self.Shirt=["Full","Half","Formal"]
        self.price_Full=500
        self.price_Half=700
        self.price_Formal=1000
        
        
        #subLifeStyle
        
        self.SubCatLifeStyle=["Soap","Cream","FaceWash","Oil"]
        self.soap=["Lux","Lifeboy","Pearl","Detol"]
        self.price_Lux=float(20)
        self.price_Lifeboy=20
        self.price_Pearl=(20)
        self.price_Detol=(20)
        
        self.Cream=["Ponds","Fair and Lovely","Nevia","Xstudio"]
        self.price_Ponds=(20)
        self.price_Fair=20
        self.price_Nevia=(20)
        self.price_Xstudio=(20)
        
        self.FaceWash=["Ponds","Fair and Lovely","Nevia","Xstudio"]
        self.price_Ponds=(20)
        self.price_Fair=20
        self.price_Nevia=(20)
        self.price_Xstudio=(20)
        
        self.Oil=["Parachute","Jasmin","Nevia","Thanda"]
        self.price_Parachute=(20)
        self.price_Jasmin=20
        self.price_Thanda=(20)
        
        #SubGrocery
        self.SubCatGrocery=["Fish","Beef","Chicken"]
        self.Fish=["Katla","Ilish","Betrongi"]
        self.price_Katla=350
        self.price_Ilish=350
        self.price_Betrongi=350
        
        self.Fish=["Katla","Ilish","Betrongi"]
        self.price_Katla=350
        self.price_Ilish=350
        self.price_Betrongi=350
        
        self.Fish=["Katla","Ilish","Betrongi"]
        self.price_Katla=350
        self.price_Ilish=350
        self.price_Betrongi=350
        
        
        
        
        #img1
        img=Image.open("img/s1.jpg")
        img=img.resize((500,170),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=500,y=0,width=500,height=130)
        
        #img2
        img_1=Image.open("img/s1.jpg")
        img_1=img_1.resize((500,170),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=0,y=0,width=500,height=130)
        
        #img3
        img_2=Image.open("img/s1.jpg")
        img_2=img_2.resize((540,170),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=540,height=130)
        
        
        
        lbl_title=Label(self.root,text="BILLING SOFTWARE BY FOLDCURL",font=("times new roman",35,"bold"),bg="white",fg="green")
        lbl_title.place(x=0,y=130,width=1530,height=45)
        
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        #customer_Lebel
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)
        
        self.lbl_mob=Label(Cust_Frame,text="Phone No",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        
        self.lblCustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
        
        self.txtCustName=ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        self.lblCustemail=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Email",bd=4)
        self.lblCustemail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        
        self.txtCustemail=ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width=24)
        self.txtCustemail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        
        #Product_Lebel
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",15,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=670,height=140)
        
        #category
        
        self.lblcategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblcategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",12,"bold"),width=24,state="readonly")
        self.Combo_category.current(0)
        self.Combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_category.bind("<<ComboboxSelected>>",self.Categories)
        
        #Subcategory
        self.lblsubcategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Sub Categories",bd=4)
        self.lblsubcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_subcategory=ttk.Combobox(Product_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        self.Combo_subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        #Product Name
        self.lblproduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Product",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.Combo_product=ttk.Combobox(Product_Frame,font=("arial",12,"bold"),width=24,state="readonly")
        self.Combo_product.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
        #Price
        self.lblPrice=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        
        self.Combo_Price=Entry(Product_Frame,font=("arial",12,"bold"),width=15)
        self.Combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        #Qty
        self.lblQuantity=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Quantity",bd=4)
        self.lblQuantity.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        
        self.Combo_Quantity=ttk.Entry(Product_Frame,font=("arial",12,"bold"),width=15)
        self.Combo_Quantity.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        
        
        #middleFrame
        
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=1028,height=340)
        
        img19=Image.open("img/s2.jpg")
        img19=img19.resize((490,340),Image.ANTIALIAS)
        self.photoimg19=ImageTk.PhotoImage(img19)
        
        lbl_img19=Label(MiddleFrame,image=self.photoimg19)
        lbl_img19.place(x=0,y=0,width=490,height=340)
        
        img190=Image.open("img/s3.jpg")
        img190=img190.resize((490,340),Image.ANTIALIAS)
        self.photoimg190=ImageTk.PhotoImage(img190)
        
        lbl_img190=Label(MiddleFrame,image=self.photoimg190)
        lbl_img190.place(x=490,y=0,width=500,height=340)
  
        #Srch
        src_Frame=Frame(Main_Frame,bd=2,bg="white")
        src_Frame.place(x=1040,y=15,width=500,height=40)
        
        self.lbBill=Label(src_Frame,font=("arial",12,"bold"),bg="red",fg="white",text="BILL NUMBER",bd=4)
        self.lbBill.grid(row=0,column=0,sticky=W,padx=1)
        
        self.src=ttk.Entry(src_Frame,font=("arial",12,"bold"),width=15)
        self.src.grid(row=0,column=1,sticky=W,padx=2)
        
        self.Btnsrc=Button(src_Frame,text="Search",font=("arial",10,"bold"),bg="Orangered",fg="white",width=18)
        self.Btnsrc.grid(row=0,column=2)
        
        #Right
        
        RightLabelFrame=Label(Main_Frame,text="BILL AREA",font=("times new roman",15,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1040,y=45,width=480,height=443)
        
        Scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=Scroll_y.set,bg="white",fg="blue",font=("times new roman",15,"bold"))
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        
        #BillCounter_Lebel
        Bottom_Frame=LabelFrame(Main_Frame,text="BILL COUNTER",font=("times new roman",15,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=486,width=1520,height=125)
        
        #Subtotal
        self.lbSubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lbSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        
        self.SubTotal=ttk.Entry(Bottom_Frame,font=("arial",12,"bold"),width=15)
        self.SubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        #Tax
        self.lbtax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Tax",bd=4)
        self.lbtax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        
        self.tax=ttk.Entry(Bottom_Frame,font=("arial",12,"bold"),width=15)
        self.tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        
        #AmountToBePay
        self.lbTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lbTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        
        self.Total=ttk.Entry(Bottom_Frame,font=("arial",12,"bold"),width=15)
        self.Total.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        
      
        #ButtonFrame
        btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        btn_Frame.place(x=320,y=0)
        
        self.BtnAddToCard=Button(btn_Frame,height=2,text="Add to Cart",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15)
        self.BtnAddToCard.grid(row=0,column=0)
        
        
        self.BtnGB=Button(btn_Frame,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15)
        self.BtnGB.grid(row=0,column=1)
        
        
        self.BtnSave=Button(btn_Frame,height=2,text="Save",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15)
        self.BtnSave.grid(row=0,column=2)
        
        
        self.BtnPrint=Button(btn_Frame,height=2,text="Print",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15)
        self.BtnPrint.grid(row=0,column=3)
        
        
        self.BtnClear=Button(btn_Frame,height=2,text="Clear",font=("arial",15,"bold"),bg="Orangered",fg="white",width=15)
        self.BtnClear.grid(row=0,column=4)
        
        
        self.BtnExit=Button(btn_Frame,height=2,text="Exit",font=("arial",15,"bold"),bg="Orangered",fg="white",width=18)
        self.BtnExit.grid(row=0,column=5)
        


    def Categories(self,event=""):
        if self.Combo_category.get()=="Clothing":
            self.Combo_subcategory.config(value=Combo_subcategory)
            self.Combo_subcategory.current(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    root=Tk() 
    obj=Bill_App(root)   
    root.mainloop()    