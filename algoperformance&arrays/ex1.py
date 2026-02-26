"""Implementing insert method
Here you have a class named IntArray with an implementation of an Array that can store integer values. It uses another class ReservedMemory (also provided) to store the integer values in memory as bytes (you can convert values to byte type or you can just use integer values between 0 and 255. Both are fine. In the code provided the latter form is used).

When instantiating an IntArray variable, the size of the array elements can be defined. By default this value is 2 bytes, that gives room to store values from -32768 to 32767 (65536 different values in total, i.e. 16 bit range)

Some internal methods and some public methods have been already implemented. Your job is to implement a new method "insert". The definition of the method is already present. Just replace the placeholder code provided with your own code.

This new insert method has to be able to insert a new element at whatever position/index of the array. For that a new array has to be created and the old content has to be copied making room for the new value

You will have to study a little bit the provided code to understand how it works. And you can use the already implemented methods as an example on what can be done.

Notice that ReservedMemory has a copy function you can use to copy the content of an old array to a new one.
"""