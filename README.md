# bodegaDiscount

In November 2021, Bodega, an online sneaker/fashion shop [tweeted a picture containing a crambled discount code worth $200](https://twitter.com/bodega/status/1455624553418403844). It was 8 random letters and whoever could figure out the correct order by trying different combinations during checkout would get $200 off their order. Bodega has lots of cools shoes and clothing, so I started guessing random codes. After realizing that I'm not nearly lucky enough to guess the code in a few tries, I decided to write a script that would help me through this process. I didn't want to spend too long on it as everyone who saw the tweet was already trying codes and, well, it was for only $200 after all. 

## Approach
To work as quickly as possible, I wanted to rely on existing tools to handle most of the work for me. The given characters in the picture appeared to be CGQYTHZL. I googled 'string shuffler' and used an online tool to get all the possible combinations of those letters. I took those combinations and put them into a text file called [list.txt](list.txt) with each combination on a new line. 

Then I went to Bodega.com in my browser and added something over $200 to my cart. I went to the checkout page where the code would be entered. I then grabbed this URL and added `&discount=' to the end of it. Using the search and replace feature in VS Code, I was able to quickly add this URL to the beginning of each line in list.txt. 

I then wrote [discountOpener.py](discountOpener.py) which opens one of the links in a google chrome broswer every 5 seconds. This gave me ample time to watch the page load and see if the discount applied succesfully. I could have written code to make the HTTP request in Python directly, but with the limited time I had, I figured I might as well try this approach and hope I got lucky. Since the string shuffler already essentially randomized the codes, I had at least as good of a chance as anyone guessing randomly. 

One issue I ran into along the way was that Bodega was limiting my IP after 5 attempts or so. To get around this, I used the BP Proxy Switcher Chrome extension with some proxies I had from sneaker botting to change the IP every 30 seconds. This worked well, but with 40,320 combinations, it would still take 56 hours of staring at my screen to hit all the combinations.

After about an hour of watching the links open while doing other things, I realized luck was not on my side, and terminated the script. I had expected someone to surely have guessed it by now. I looked at Bodega's Twitter again and saw that it still had not been claimed and they gave a hint that the first letter was "C". Of course, that significantly lessened the number of combinations. I removed any combinations from list.txt that did not start with C and started running the script again. Surely I could get lucky out of 5040 codes, right? Alas, Lady Luck was again nowhere to be found and I terminated the script wishing I was familiar enough with writing HTTP requests in Python to write something that could brute force the codes more quickly.

Nonetheless, it was a fun experience and it inspired me to learn more about web development. Hopefully I can revisit this in the future and make it not only run faster by handling the requests directly, but offer a more generic way to run as well so that it is not tied only to Bodega's website. 
