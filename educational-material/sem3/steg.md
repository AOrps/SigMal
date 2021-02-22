# Sig Mal, Week 5

## Steganography


**What is Stegonagraphy?** 
In essence, Steg is hiding things inside images. This can vary from text, files, or even running code.

Exhibit A: The untouched image
==================================

![](img/thestart.png)

This is the unaltered image. I made a copy of it called purewillick, this is mainly for the next step.

Exhibit B: Hiding a message in the image, and comparing the pure images and the edited images.
==================================
![](img/themiddle.png)

Notice when comparing the hex from the pure image and the altered image. Of course, when we use something like xxd, it will display something like this. 

![](img/stringsnhex.png)

Of course, after playing around with some syntax and forgetting strings is a beautiful thing; we can actually get the hidden text.

###**Naturally, this works for hiding files too.**
Let's say that I have some data I want to hide, bank account details, passwords, the works. While I could keep that stuff on something like a usb, I could also be very noided and decide to hide it an image.

![](img/jocko.png)

So, I ended up hiding my secret file into this new png. I simply catted everything together. Now, I have the graphics for the image. Someone can view and thing "Wow, this guy has a funny Jocko meme, though me personally I'm more of a fan of Goggins." Which is fair, I love Goggins too. Anyway, what said person won't know, unless they want to dig a bit, is that there is a text in there. So what if said individual was smart and wanted to dig, or alternatively you just want your files. You can actually unzip it, or view it.

Do note, I acccidentally overwrote one of the Jocko files, so I made a Jocko2. Pardon my innaneness.
![](img/oddity.png)

The above image displays not only that there is a file inside the image, but also the contents of said image. The reason? It's becauses already compress their data, so shoving a compressed item in there won't cause any *extra compression*, it'll just treat it as readable content. Anyways, the next image, and unfortunate last of this psuedo demo, is me unzipping my jpg's contents, as well as using strings to see the contents of my png. Thought it'd be cool.

![](img/theend.png)

===================================
## Extra Credit, embedding code.

Of course, one can also embed some nasty stuff, or cool code in an image. I left out my experimentation with that, but I can tell you it works. Some malware attacks actually involved using images. There was a brazilian made malware that actually hid some nasty nasty code inside a jpg. Would recommend trying to embed some kind of bash script in the image, and see what happens if you try stuff with it. 
