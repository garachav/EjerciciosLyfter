#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_vehicles=["Kia","Suzuki","Toyota","Nissan"]
temporal= my_vehicles[0]
my_vehicles[0]= my_vehicles [len(my_vehicles)-1]
my_vehicles[len(my_vehicles)-1]=temporal 
print (my_vehicles)
