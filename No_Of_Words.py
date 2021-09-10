a="""Android is a mobile operating system based on a modified version of the Linux kernel and other open source software, designed primarily for touchscreen mobile devices such as smartphones and tablets. Android is developed by a consortium of developers known as the Open Handset Alliance and commercially sponsored by Google. It was unveiled in November 2007, with the first commercial Android device, the HTC Dream, being launched in September 2008. """
b = " "
n = a.count(b)
print("Number of words : ",n+1)
a = a.lower();  
w = a.split(" ");  
print("Duplicate words in a given string : ");  
for i in range(0, len(w)):
    count = 1;  
    for j in range(i+1, len(w)):  
        if(w[i] == (w[j])):  
            count = count + 1;  
            w[j] = "0";                
    if(count > 1 and w[i] != "0"):  
        print(w[i]);  
