# Encapsulation is a way to restrict the direct access to some components of an object
class AccessExample:
    def __init__(self):
        self.public_var = 'i am public variable'
        self._prot_var = 'i am protected variable'
        self.__private_var = 'i am private varibale'

    def public_method(self):
        print('this is public method')
    def _prot_method(self):
        print('this is protected method')
    def __private_method(self):
        print('this is private method')
        
    def access_all_vars_and_method(self):
        print(self.public_var)
        print(self._prot_var)
        print(self.__private_var)
        self.public_method()
        self._prot_method()
        self.__private_method()

example = AccessExample()


#Accessing the public members
print('Accessing Public memebers:')
print(example.public_var)
example.public_method()

#Accessing the protectec memebers(Not enforced but a conventuon)
print('Accesing the Protected members:')
print(example._prot_var)
example._prot_method()

#Accessing private members 
print('Accessing the private members')
# print(example.__private_var) # this would raise a AttributeError
# example.__private_method() # this would raise a AttributeError

#Accessing all memebers
print("Accessing all memebers")
example.access_all_vars_and_method()