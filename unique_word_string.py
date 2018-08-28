#this code will convert string to list and then list to string
#also this will get unique letters from string

def main(inp_string):

   #convert string to list
   l = list(inp_string)
   print(l)
   #convert list to string
   str = ''.join(l)
   print(str)

   #define empty set:
   uniq_Str = set()

   for i in range(len(inp_string)):
       if inp_string[i] not in uniq_Str:
           uniq_Str.add(inp_string[i])

   print(''.join(uniq_Str))

if __name__ == "__main__":
    main("adasdsaasdpqpa")
    
#output would be apdsq
