class Clothes: 
    cost=0   
    def calc(self,price=10):
        print(" The width is 15 meters, It is not customizable !!")        
        length = int(input("\nEnter length of cloth required: "))
        self.cost = length * price
        print("Price without adding color is: ",self.cost)
        return self.cost        

    def colors(self):
        c =int(input("If you want to add colors, select 1 or 0: "))
        if c==1:
            print(" 1)Blue \n 2)Green \n 3)Yellow \n 4)Violet \n 5)Black \n 6)Purple")
            co=int(input("Enter the color you want: "))
            if co==1:
                totalcost=self.cost*20
                print("Your total cost is: ", totalcost)
            elif co==2:
                totalcost=self.cost*30
                print("Your total cost is: ", totalcost)
            elif co==3:
                totalcost=self.cost*40
                print("Your total cost is: ", totalcost)
            elif co==4:
                totalcost=self.cost*50
                print("Your total cost is: ", totalcost)
            elif co==5:
                totalcost=self.cost*10
                print("Your total cost is: ", totalcost)
            elif co==6:
                totalcost=self.cost*25
                print("Your total cost is: ", totalcost)
            else:
                print("No colors selected")
        else:
            print("Your total cost is: ",self.cost)

    def cloth_type(self):
        print("Please choose the type of cloth you want to buy:\n1) Cotton\n2) Nylon\n3) Linen\n4) Silk")
        t = int(input("Enter the type of cloth: "))
        if t == 1:
            print("\nCotton Info:\n \n Cotton is known for its versatility,\n performance and natural comfort.\n Cotton's strength and absorbency\n makes it an ideal fabric to make clothes and homewares,\n and industrial products like tarpaulins, \n tents, hotel sheets, army uniforms. \n\n 60 rupees for 2 meters of cloth.")
            c = Cotton()
            c.calc()
            c.colors()
        elif t == 2:
            print("\nNylon Info:\n \n Nylon is the commercial name for a group of polyamides that are thermoplastic polymers.\n Because of their durability and stretchiness \n Nylon is the first fully synthetic fibre prepared from coal,\n water and air. Nylon fibres are strong, \n elastic and light. It is lustrous and easy to wash.\n\n 80 rupees for 2 meters of cloth.")
            n = Nylon()
            n.calc()
            n.colors()
        elif t == 3:
            print("\nLinen Info:\n\nLinen clothing is worn mostly in summers \n because the fabric absorbs moisture and skin perspirations.\n When it comes to heat and summer, \n linen is the only material that suits andprovides with a cooling sensations.\n\n 100 rupees for 2 meters of cloth.")
            l = Linen()
            l.calc()
            l.colors()
        elif t == 4:
            print("\nSilk Info:\n\nSilk is a natural fiber known for its luster,\n shine, strength, and durability,and \n it has a long trading history across the world.\n Silk is the epitome of luxury due to its\n high cost to produce, soft feel, and elegant appearance,\n and it is thus a popular textile in high-end and couture fashion design.\n\n 120 rupees for 2 meters of cloth.")
            s = Silk()
            s.calc()
            s.colors()
        else:
            print("Invalid input")

class Cotton(Clothes):
    def calc(self,price=30):
        print(" The width is 15 meters, It is not customizable !!")
        length = int(input("\nEnter length of cloth required: "))
        self.cost = length * price
        print("Price without adding color is: ",self.cost)
        return self.cost

class Nylon(Clothes):
    def calc(self,price=40):
        print(" The width is 15 meters, It is not customizable !!")
        length = int(input("\nEnter length of cloth required: "))
        self.cost = length * price
        print("\nTotal cost:", self.cost)
        return self.cost

class Linen(Clothes):
    def calc(self,price=50):
        print(" The width is 15 meters, It is not customizable !!")
        length = int(input("\nEnter length of cloth required: "))
        self.cost = length * price
        print("\nTotal cost:", self.cost)
        return self.cost

class Silk(Clothes):
    def calc(self,price=60):
        print("The width is 15 meters, It is not customizable !!")
        length = int(input("\nEnter length of cloth required: "))
        self.cost = length * price
        print("\nTotal cost:", self.cost)
        return self.cost

o = Clothes()
o.cloth_type()