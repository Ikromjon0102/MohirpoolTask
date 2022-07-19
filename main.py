from student import Unversity,Undergraduate,Postgraduate

student1 = Undergraduate('001',"Hakimov Salim","Uzbek",'erkak','KIF','2020','Home')
student2 = Postgraduate('0001',"Aliyev Vali","Uzbek",'erkak','KIF','2020',"Ergashev Ikromjon",'AI in the Market')
student3 = Undergraduate('00001',"Valiyev Ali","Uzbek",'erkak','KIF','2020',"Residential Hall" )

univer1 = Unversity("TATU",'Yunusobod')

univer1.add_(student3)
univer1.add_(student2)
univer1.add_(student1)
print(univer1.display_all())
print(univer1.find_one("0001"))
print(univer1.remove_one('00001'))