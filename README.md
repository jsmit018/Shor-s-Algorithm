# Shor's-Algorithm
Shor’s algorithm routine that will allow the factoring of large and complex numbers. Although there are a few restrictions to the algorithm: that numbers cannot be prime, shouldn’t be an even number and not in exponent notation. 

## The Algorithm
1. The first step in the algorithm is to take a number that you want to factor and designate that as N.  In the source code, this is represented by user input to allow the user to choose which number they want input that can be factored. The source code doesn't contain checks for the general rules of thumb for the algorithm, but it is likely that if a number is inserted that won't work it will just return to user input.
2. The next step is to then declare a second number K which is a number between 1 and N. In the source code represents this through random number generation given a range between 1 and the number input by the user. Random Number Generation is used to increase execution speed, otherwise the user would have to have another input to manage.
3. The next step is to then find the GCD(N,K) – If GCD is not equal to one then the GCD is a factor of N else if it is one you move on. If one, then you will need to find the smallest positive integer, r, such that f(x) = (k^x)mod N then f(a) = (a+r). 
4. Now you will need to define another variable q, now you will need to find (qxk)mod N. If the remainder is not one, then se the value of q to the value of the remainder that was calculated and repeat this step until the remainder is one; keeping track of the iterations of the recursion. The number of transformations that you calculated 1…N will be the r use in the equation. If r is an odd number go back to the second step, choosing a random number K.
5. Otherwise, define p = remainder in (r/2)th transformation – If p + 1 = N then go back to step two otherwise move on to the final step of the algorithm.
6.  Now you will be able to generate the factors of N by sampling doing f1 = GCD(p+1, N) and f2 = GCD(p-1, N).

## Why Python?
For the purposes of completing this assignment I chose to utilize Python, because it was familiar to me, but is also a language that is frequently used in Quantum Computing. Due to Travel and an impending Hurricane I didn't want to attempt to learn a language that was unfamliar to me at the moment. Before starting the programming I did look into Shor's Algorithm for Paper 1, as it was an extension of the Fourier Transformation, and actually includes the Fourier Transformation as one of its steps in the algorithm. In Paper 1 I do go into detail a little more about the background but I lay the groundwork for the algorithm that I implemented. Before deciding to utilize Python I did some research into Silq as it was touted as a language that was easy to use and took the more difficult aspects of other quantum programming languages, and fixed them, by automating them essentially. When looking into the language, it was found that the syntax, to me at least was a little confusing because there are a lot of nuiances that are unique to the language that don't exist in other languages. For that reason I chose to use Pythong, and because of that it is also a little easier to follow along with the algorithm as it implements and executes code. 

## Choosing new Programming Languages
For the purposing of completing the final assignment, I took the approach of simply redoing Shor's algorithm in 3 different coding languages, as it fell under one of the algorithms we discussed in class. However the only interesting interpretation that I was not sure of was whether or not the coding languages needed to be a quantum language or a non-quantum language that much was uncertain - but for selecting the languages I decided to use 2 languages that I was familiar with, and then I learned Ruby in order to complete the third language.

The reason that I chose to continue shor's algorithm was to see how the difficulty would scale from using a language that doesn't require direct typecasting to 2 languages that did and how that would impact the implemntation of the algorithm. For my languages I selected C++, Java, and Ruby all of which are Object Oriented Programing languages, but each of their own unique way of approaching the problem and I will talk about the subtle differences from the original algorithm done in python. 

## Why C++, Java, and Ruby?
C++, Java and Python are what I consider a tri-fecta of programming languages as they generally are conisdered the big 3 of the programming languages as most common/easy to use/learn languages. C++ was my first language, but I haven't had to use it in a while due to school/work not using it as a default language. However, C++ syntax, to me, is very different than the syntax of a lot of other languages but it provides the user with a lot more control over what it is that they are trying to accomplish. Given the way that Python is structured it allowed the intilization, flow and implementation of the program a lot easier.

Java was a secondary language for me as I had to learn the ins and outs of the language when I joined the Computer Science Master's Program and Vanderbilt, and this allowed me to actually start looking into code base related things at my previous job. To me implementing Shor's algorithm in java structure wise was the easiest of the four languages, however with that being said Java iteracts with Primitives and Primitive classes. So without directly implementing the GCD function as an algorithm of its own and deriving it from a built in Java library I had to add in a few extra lines that converted BigIntegers which are a class of integers to convert the data into a primitive integer type in order to get an integer value that could be interperated by the rest of the program in order to execute the algorithm. 

Lastly, Ruby - After selecting to the use the other 2 languages that I was comfortable with I had to find a third language that I was unfamliar with in order to utilize it for the project. I spent some time googling popular programming langauges to see if I could find another language that would peak my interest that was also widely used to see if there was a benefit I could gain in understanding it. So I landed on ruby because it seems to be a versitle language and resembles Python in a sense. I watched a brief half hour youtube video explaining the basic syntatical things related to ruby and was quicklya ble to translate Shor's algorithm into a .rb file.  

## Differences between the Languages
There weren't too many massive differences when implementing the algorithm in different langauges, there were a few slight changes that had to made from language to language in terms of direct typing of variables. The biggest difference was how each language handled the use of its librariers and the GCD function - this required some slight modification in order to receive the values that it needed in order to actually execute appropriately. Another difference was that some languages can hanlde a do while loop while other languages cannot. This didn't change my approach to impelementation as I still impelmented it in each langauge as if the do while loops didn't exist in the main algorithm. The only other real difference between all the languages were how things were outputting to the terminal/screen as each language has their own way of appropaching that. 

