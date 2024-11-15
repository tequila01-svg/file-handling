#open file
file=open('sample.txt')
#read file
print(file.read())
file.close()


#open in write mode
file_write=open('sample.txt','w')
file_write.write("hello, my name is Ayobami")
#print|file_write.read()
file_write.close()