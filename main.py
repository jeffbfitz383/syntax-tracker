##### this page is not to have function python code.  It is merely used as a syntax reference.

<break code>


#testing collapsable arrows
first layer a
    second layer aa
    second layer ab
first layer b
    second layer ba 
    second layer bb


phase0
    setup
    cli
    expressions
        intro
            1 + 1
        expressions
            1 + 2
            10 + (3 * ( (-1) ** 3) + 2) / 18

            order of expression 

            +	Addition	
            -	Subtraction	
            *	Multiplication	We use * instead of × because it looks like x-the-letter
            /	Division	We use / instead of ÷ because that's not on a keyboard
            **	Exponentiation	We use ** instead of ^ because ^ means something else in programming languages
            ()	Association	Expressions inside of () get evaluated earlier
        constant
        assignment
            aFunNumber = 3 * (10 - 4);
            myBirthYear = 1989;
            maximumSpeed;
            maximumSpeed = 9000;
            heightInCentimeters = 50;
            heightInCentimeters = 180;
            recurringExpressionValue = 3 * (10 - 4);
            // => 18
        Variable 
            // Assignment expression that returns 32
            age = 32;

            // Type in the assigned name
            age;
        js variables
            let pi;
            //=> undefined
            pi = 3.14159;
            //=> 3.14159

            let pi = 3.14159;
            const pi = 3.14159;
        javaScript Data Types

            typeof 42;
            //=> "number"
            typeof "I am a string.";
            //=> "string"
            typeof true;
            //=> "boolean"

            const js = {
            name: "JavaScript",
            createdBy: {
                firstName: "Brendan",
                lastName: "Eich",
            },
            firstReleased: 1995,
            isAwesome: true,
            };

            typeof js;
            //=> "object

            const dogs = ["Byron", "Cubby", "Boo Radley", "Luca", "Spinach"];
            typeof dogs;
            //=> "object"

            typeof null;
            //=> "object"

            typeof undefined;
            //=> "undefined"

            let unassignedVariable;
            typeof unassignedVariable;
            //=> "undefined"

            unassignedVariable = "";
            typeof unassignedVariable;
            //=> "string"

            3 - 2;
            //=> 1

            "Hello" + ", " + `world!`;
            //=> "Hello, world!"

            1 + 2 + 3 + 4 + 5;
            //=> 15

            "1" + 2 + 3 + 4 + 5;
            //=> "12345"

            1 + "2" + 3 + 4 + 5;
            //=> "12345"

            1 + 2 + "3" + 4 + 5;
            //=> "3345"

            1 + 2 + 3 + "4" + 5;
            //=> "645"

            1 + 2 + 3 + 4 + "5";
            //=> "105"

            1 + 2 + "3" + 4 + 5;
            //=> "3345"
        strings

            const greeting = "Hello, folks";

            const barkCount = 3;
            const backtick = `Spinach barks ${barkCount} times`; //=> "Spinach barks 3 times"
            const singleQuote = 'Spinach barks ${barkCount} times'; //=> "Spinach barks ${barkCount} times"
            const doubleQuote = "Spinach barks ${barkCount} times"; //=> "Spinach barks ${barkCount} times"

            const spinach = `Spinach is ${2 + 3} years old`; //=> "Spinach is 5 years old"
            const littleWomanEsque = '"Wait," said Jo, "Do not go without me!"';
            const littleWomanEsque = '"Wait," said Jo, "Don\'t go without me!"';

            const firstName = "Spinachius";
            const clanName = "Karbitus";
            const commonName = "Maris";
            let fullName;

            // With +
            fullName = firstName + " " + clanName + " " + commonName; //=> "Spinachius Karbitus Maris"

            // Or, with interpolation
            fullName = `${firstName} ${clanName} ${commonName}`; //=> "Spinachius Karbitus Maris"

            // Keep in mind it returns a _new_ String; therefore:
            firstName; //=> "Spinachius"
            clanName; //=> "Karbitus"
            commonName; //=> "Maris"
            fullName; //=> "Spinachius Karbitus Maris"

            const fact = "Spinach is "; // fact is of type `String`
            const tail = " years old"; // tail is of type `String`
            const age = 5; // age is of type `Number`

            fact + age + tail; //=> "Spinach is 5 years old"

            const fact = "Spinach is";
            const tail = "years old";
            const age = 5;

            `${fact} ${age} ${tail}`; //=> "Spinach is 5 years old"

            const fact = "Spinach is "; // fact is of type `String`
            const tail = " years old"; // tail is of type `String`
            const age = 5; // age is of type `Number`

            fact + age.toString() + tail; //=> "Spinach is 5 years old"
        boolean
            Boolean(false);
            // => false

            Boolean(null);
            // => false

            Boolean(undefined);
            // => false

            Boolean(0);
            // => false

            Boolean(NaN);
            // => false

            Boolean("");
            // => false

            Boolean(true);
            // => true

            Boolean(42);
            // => true

            Boolean("Hello, world!");
            // => true
        comparisons
            42 === 42;
            // => true

            42 === "42";
            // => false

            true === 1;
            // => false

            "0" === false;
            // => false

            null === undefined;
            // => false

            " " === 0;
            // => false

            9000 !== 9001
            // => true

            9001 !== '9001'
            // => true

            [] !== ''
            // => true

            42 == 42;
            // => true

            42 == "42";
            // => true

            true == 1;
            // => true

            "0" == false;
            // => true

            null == undefined;
            // => true

            " " == 0;
            // => true

            9000 != 9001
            // => true

            9001 != '9001'
            // => false

            [] != ''
            // => false

            88 > 9;
            // => true

            88 >= 88;
            // => true

            88 < 9;
            // => false

            88 > "9";
            // => true

            88 >= "hello";
            // => false

            88 <= "hello";
            // => false

            "88" > "9";
            // => false
        logical
            const truthyValue = 'This value is truthy.';
            const falseyValue = 0;

            !truthyValue;
            false && "Anything";
            // => false

            // 4 * 0 returns 0, which is falsey
            4 * 0 && "Anything";
            // => 0

            true && false;
            // => false

            1 + 1 && "Whatever";
            // => "Whatever"

            "The truthiest of truthy strings" && 9 * 9;
            // => 81

            true || "Whatever";
            // => true

            1 + 1 || "Whatever";
            // => 2

            false || "Whatever";
            // => "Whatever"

            1 === 2 || 8 * 8;
            // => 64

            "" || "Not " + "an " + "empty " + "string";
            // => "Not an empty string"

            0 && false;

            0 && true;

            true && NaN;

            true && !1;

            !0 && "This is a string";

            !0 && "";

            !0 && !!"";

            // Practice with OR
            0 || false;

            true || false;

            true || 1;

            !true || !false

            !1 || !0
        programmong with-expresion
            console.log('Hello, world!')
            const sum = 1 + 1;

            console.log(sum);
            const difference = 10 - 5;

            booleanExpression ? "thingToReturnIfTrue" : "thingToReturnIfFalse";
            const likelyToRain = true;
            const clothingChoice = likelyToRain ? "rain boots" : "sun hat";

            console.log(clothingChoice);
            const rainPercentage = 0.2;
            const clothingChoice = rainPercentage > 0.3 ? "rain boots" : "sun hat";

            console.log(clothingChoice);

            const name = "Your name here";
            const probabilityOfRain = 0.2;
            const temperatureInC = 26;

            // Create our message
            const message = `Hello, ${name}, with a rain chance of ${probabilityOfRain * 100}% and a temperature of ${temperatureInC}C we recommend that you ` + (probabilityOfRain > 0.3 ? "take an umbrella" : "enjoy this rain-free day") +
            `${temperatureInC >= 26 ? ' and watch out for heatstroke.' : ' and bask in this fine weather.'}`;

            console.log(message);

            const name = "Spinach the Shiba";
            const rainPercentage = 0.2 * 100;

            const probabilityOfRain = 0.2;
            const rainPercentage = probabilityOfRain * 100;

            const name = "Spinach the Shiba";
            const probabilityOfRain = 0.2;
            const temperatureInC = 26;

            const likelyToRain = probabilityOfRain > 0.3;
            const sunIsDangerous = temperatureInC >= 26;
            const rainPercentage = probabilityOfRain * 100;

            const message = `Hello, ${name}, with a rain chance of ${rainPercentage}% and a temperature of ${temperatureInC}C we recommend that you ` +
            (likelyToRain ? "take an umbrella" : "enjoy this rain-free day") +
            `${
                sunIsDangerous
                ? " and watch out for heatstroke!"
                : " and bask in this fine weather."
            }`;

            console.log(message);

            const advice = raining ? "take an umbrella" : "enjoy this rain-free day";

            const rainAdvice = likelyToRain
                ? "take an umbrella"
                : "enjoy this rain-free day";

            const name = "Spinach the Shiba";
            const probabilityOfRain = 0.2;
            const temperatureInC = 26;

            const likelyToRain = probabilityOfRain > 0.3;
            const sunIsDangerous = temperatureInC >= 26;
            const rainPercentage = probabilityOfRain * 100;

            const rainAdvice = likelyToRain
            ? "take an umbrella"
            : "enjoy this rain-free day";
            const sunAdvice = sunIsDangerous
            ? " and watch out for heatstroke"
            : " and bask in this fine weather";

            const message = `Hello, ${name}, with a rain chance of ${rainPercentage}% and a temperature of ${temperatureInC}C we recommend that you ` + rainAdvice + sunAdvice;

            console.log(message);

            const name = "Spinach the Shiba";
            const probabilityOfRain = 0.2;
            const temperatureInC = 26;

            const likelyToRain = probabilityOfRain > 0.3;
            const sunIsDangerous = temperatureInC >= 26;

            const rainPercentage = probabilityOfRain * 100;
            const rainAdvice = likelyToRain ? "take an umbrella" : "enjoy this rain-free day";
            const sunAdvice = sunIsDangerous ? "watch out for heatstroke" : "bask in this fine weather";

            const message = `Hello, ${name}, with a rain chance of ${rainPercentage}% and a temperature of ${temperatureInC}C we recommend that you ${rainAdvice} and ${sunAdvice}.`;

            console.log(message);

            const first = 2;
            const second = 1;
            const problem = 99;
            const luckyNumber = first > second ? (problem - 1) / 2 : problem / 3;
            luckyNumber; //=> ??? (Test it out yourself!)
    statements
        intro

            let favoriteNumber = 32;
            if (favoriteNumber >= 10) { // evaluating favoriteNumber >= 10 returns true
            favoriteNumber = favoriteNumber + 10
            } 
            console.log(favoriteNumber);

            let favoriteNumber = 0;
            while (favoriteNumber < 10) {
            favoriteNumber = favoriteNumber + 1;
            }
            console.log(favoriteNumber);
        comment

            // From the Three Dog Night song: "Joy to the World (Jeremiah was a Bullfrog)"
            const lineOne = "Joy to the world";
            const lineTwo = "All the boys and girls";
            const lineThree = "Joy to the fishes in the deep blue sea";
            const lineFour = "Joy to you and me";

            // The '\n' inserts a new line into the string
            const chorus = `${lineOne}\n${lineTwo}\n${lineThree}\n${lineFour}`;

            const lineOne = "Joy to the world";
            const lineTwo = "All the boys and girls";
            const lineThree = "Joy to the fishes in the deep blue sea";
            const lineFour = "Joy to you and me";

            const chorus = `${lineOne}\n${lineTwo}\n${lineThree}\n${lineFour}`;

            const lineOne = "Joy to the world";
            const lineTwo = "All the boys and girls";
            //const lineThree = "Joy to the fishes in the deep blue sea";
            const lineFour = "Joy to you and me";

            // const chorus = `${lineOne}\n${lineTwo}\n${lineThree}\n${lineFour}`;
            const chorus = `${lineOne}\n${lineTwo}\n${lineFour}`;

            const lineOne = "Joy to the world";
            const lineTwo = "All the boys and girls";
            const lineThree = "Joy to the fishes in the deep blue sea"; 
            */
            const lineFour = "Joy to you and me";

            lineFour; // => "Joy to you and me"
        selection with conditionals 

            const name = "Alice";
            let greeting;

            if (name === "Alice") {
            greeting = "Hello, Alice!";
            } else if (name === "The White Rabbit") {
            greeting = "Don't be late, White Rabbit";
            } else if (name === "The Mad Hatter") {
            greeting = "Welcome to the tea party, Mad Hatter";
            } else if (name === "The Queen of Hearts") {
            greeting = "Please don't chop off my head!";
            } else {
            greeting = "Whoooo are you?";
            }

            greeting;
            //=> "Hello, Alice!"

            const name = "Alice";
            let greeting;

            switch (name) {
            case "Alice":
                greeting = "Hello, Alice!";
                break;
            case "The White Rabbit":
                greeting = "Don't be late, White Rabbit";
                break;
            case "The Mad Hatter":
                greeting = "Welcome to the tea party, Mad Hatter";
                break;
            case "The Queen of Hearts":
                greeting = "Please don't chop off my head!";
                break;
            default:
                greeting = "Whoooo are you?";
            }

            console.log(greeting);

            let characterType;

            const name = "Grumpy";
          

            switch (name) {
            case "Sleepy":
            case "Sneezy":
            case "Happy":
            case "Grumpy":
            case "Bashful":
            case "Dopey":
            case "Doc":
                characterType = "dwarf";
                break;
            case "Handsome Prince":
                characterType = "hero";
                break;
            case "Evil Queen":
                characterType = "villain";
                break;
            case "Snow White":
                characterType = "heroine";
                break;
            default:
                characterType = "minor character";
            }

            console.log(characterType);

            const age = 20;
            let isAdult, canWork, canEnlist, canDrink;

            if (age >= 21) {
            isAdult = true;
            canWork = true;
            canEnlist = true;
            canDrink = true;
            } else if (age >= 18) {
            isAdult = true;
            canWork = true;
            canEnlist = true;
            } else if (age >= 16) {
            canWork = true;
            }
            // => true

            isAdult;
            // => true

            canWork;
            // => true

            canEnlist;
            // => true

            canDrink;
            // => undefined

            const age = 21;
            let isAdult, canWork, canEnlist, canDrink;

            switch (true) {
            case age >= 21:
                canDrink = true;
            case age >= 18:
                isAdult = true;
                canEnlist = true;
            case age >= 16:
                canWork = true;
            }
            console.log(canWork);
            console.log(canEnlist);
            console.log(isAdult);
            console.log(canDrink);
        logging

            console.log("Hello, world!");
            console.log("one", "two", "three");
            console.log("I must have logged", 1000, "times today.");

            const name = "Spinach the Shiba";
            console.log("Hello,", name);

            const age = 20;

            let isAdult=false, canWork=false, canEnlist=false, canDrink=false;

            if (age >= 21) {
            canWork = true;
            canEnlist = true;
            isAdult = true;
            canDrink = true;
            } else if (age >= 18) {
            canWork = true;
            canEnlist = true;
            isAdult = true;
            } else if (age >= 16) {
            canWork = true;
            }

            console.log(canWork, canEnlist, isAdult, canDrink);
            true false false false

            console.log(
            "Age:",
            age,
            "Can work:",
            canWork,
            "Can enlist:",
            canEnlist,
            "Is a legal adult:",
            isAdult,
            "Can drink:",
            canDrink
            );

            console.log(
            `Age: ${age}, Can work: ${canWork}, Can enlist: ${canEnlist}, Is a legal adult: ${isAdult}, Can drink: ${canDrink}`
            );

            const age = 18;

            let isAdult=false, canWork=false, canEnlist=false, canDrink=false;

            if (age >= 21) {
            canWork = true;
            canEnlist = true;
            isAdult = true;
            canDrink = true;
            } else if (age > 18) {
            canWork = true;
            canEnlist = true;
            isAdult = true;
            } else if (age >= 16) {
            canWork = true;
            }

            console.log(`Age: ${age}\nCan work: ${canWork}\nCan enlist: ${canEnlist}\nIs a legal adult: ${isAdult}\nCan drink: ${canDrink}`);

            const age = 18;

            let isAdult=false, canWork=false, canEnlist=false, canDrink=false;

            if (age >= 21) {
            canWork = true;
            canEnlist = true;
            isAdult = true;
            canDrink = true;
            } else if (age > 18) {
            console.log("The condition returned true")
            canWork = true;
            canEnlist = true;
            isAdult = true;
            } else if (age >= 16) {
            canWork = true;
            }

            console.log(`Age: ${age}\nCan work: ${canWork}\nCan enlist: ${canEnlist}\nIs a legal adult: ${isAdult}\nCan drink: ${canDrink}`);
            
            if (condition1) {
            console.log("Condition 1 returned true");
            } else if (condition2) {
            console.log("Condition 2 returned true");
        while

            while (condition expression) {
            // stuff to do
            }

            while (true) {
            console.log("say this forever...");
            }

            while (-1) {
            // -1 is truthy....
            console.log("say this forever...");
            }

            while (null) {
            console.log("I will never run");
            }

            let count = 0; // Initialize a counter variable; note that we need to use `let` here
            while (count < 3) {
            //A Boolean expression that uses the counter to decide whether to keep looping
            console.log(`I am the ${count}, I love to count!`); // The work the loop does
            count = count + 1; // Update the counter variable; this keeps track of how many times the loop has executed
            }

            count = count + 1;

            // take the value of count, add 1 to it and then assign that result to count
            count += 1;

            let count = 0; 
            while (count < 3) { 
            console.log(`I am the ${count}, I love to count!`); 
            count++; 
            }

            do {
            console.log(`I will execute once`);
            } while (false);
    bundling
        intro
        testing

            const name = "Joe";
            const height = 74;
            const message = `${name} is ${height} inches tall`;

            module.exports = { name, height, message };

            const message = `${name} is ${height} inches tall`;
            node index.js

            const { name, height, message } = require("../index.js");

            describe("Name", () => {
            it('returns "Susan"', () => {
                expect(name).toEqual("Susan");
            });
            });

            describe("Height", () => {
            it("is less than 40", () => {
                expect(height).toBeLessThan(40);
            });
            });

            describe("Message", () => {
            it("gives the name and height", () => {
                expect(message).toInclude(name);
                expect(message).toInclude(height);
            });
            });
        intro-functions

            function sayHello() {
            console.log("Hello!");
            }

            sayHello();

            function sayHelloToGuadalupe() {
            console.log("Hello, Guadalupe!");
            }

            function sayHelloToLiz() {
            console.log("Hello, Liz!");
            }

            function sayHelloToSamip() {
            console.log("Hello, Samip!");
            }

            sayHelloToGuadalupe();
            sayHelloToLiz();
            sayHelloToSamip();

            function doSomething(thing) {
            console.log(thing);
            }

            doSomething("anything"); // passing the argument 'anything' into our function

            function sayHelloTo(firstName) {
            console.log(`Hello, ${firstName}!`);
            }

            sayHelloTo("Guadalupe"); // "Hello, Guadalupe!"
            sayHelloTo("Jane"); // "Hello, Jane!"
            sayHelloTo("R2-D2"); // "Hello, R2-D2!"
            sayHelloTo(1); // "Hello, 1!"

            // ^ Note that in the above, JavaScript coerces the number 1 to the string "1"

            function say(greeting, firstName) {
            console.log(`${greeting}, ${firstName}!`);
            }

            say("Julio", "hello");

            function say(greeting, firstName) {
            console.log("firstName: ", firstName);
            console.log("greeting: ", greeting);
            console.log(`${greeting}, ${firstName}!`);
            }

            function add(x, y) {
            return x + y;
            }

            console.log(add(1, 2));

            function say(greeting, firstName) {
            return `${greeting}, ${firstName}!`;
            }

            function say(greeting, firstName) {
            console.log(`${greeting}, ${firstName}!`);
            }

            function add(x, y) {
            x + y;
            }

            console.log(add(1, 2));

            const sum = add(num1, num2);
            const message = `The sum of your numbers is: ${sum}.`;

            const message = `The sum of your numbers is: ${add(num1, num2)}.`;

            function say(greeting, firstName) {
            return `${greeting}, ${firstName}!`;
            console.log("I was called!");
            }

            console.log(say("Howdy", "partner"));

            function say(greeting, firstName) {
            console.log("I was called!");
            return `${greeting}, ${firstName}!`;
            }
        functions-lab

            function shout(string) {
            return string.toUpperCase()
            }

            function whisper(string) {
            return string.toLowerCase()
            }

            function logShout(string) {
            console.log(string.toUpperCase())
            }

            function logWhisper(string) {
            console.log(string.toLowerCase())
            }

            function sayHiToHeadphonedRoommate(string) {
            if (string.toLowerCase() === string) {
                return "I can't hear you!"
            }

            if (string.toUpperCase() === string) {
                return "YES INDEED!"
            }

            if (string === "Let's have dinner together!") {
                return "I would love to!"
            }
            }
        parameters-lab

            function introduction(name) {
            return `Hi, my name is ${name}.`;
            }

            function introductionWithLanguage(name, language) {
            return `Hi, my name is ${name} and I am learning to program in ${language}.`;
            }

            function introductionWithLanguageOptional(name, language = "JavaScript") {
            return `Hi, my name is ${name} and I am learning to program in ${language}.`;
            }
                    calculator
        calculator
            function add(a,b) {
            return a + b
            }

            function subtract(a,b) {
            return a - b
            }

            function divide(a,b) {
            return a / b
            }

            function multiply(a,b) {
            return a * b
            }

            function increment(n) {
            return n += 1
            }

            function decrement(n) {
            return n -= 1
            }

            function makeInt(string) {
            return parseInt(string, 10)
            }

            function preserveDecimal(string) {
            return parseFloat(string)
            }


    data structures

        intro
            const theBeatles = [
            "John Lennon",
            "Paul McCartney",
            "Ringo Starr",
            "George Harrison",
            ];

            const englishBandsByCity = {
                liverpool: "The Beatles",
                manchester: "The Smiths",
                coventry: "Delia Derbyshire and the BBC Radiophonic Band",
                london: "Ziggy Stardust and the Spiders from Mars",
                };

            const englishMusicByCity = {
            manchester: [
                {
                bandName: "The Smiths",
                memberNames: ["Morrissey", "Johnny", "Andy", "Mike"],
                },
                {
                bandName: "Joy Division",
                memberNames: ["Peter", "Stephen", "Bernard", "Ian"],
                },
            ],

            };

            englishMusicByCity["manchester"][0]["bandName"]; //=> "The Smiths"
                englishMusicByCity["manchester"][0]["memberNames"]; //=> ["Morrissey", "Johnny", "Andy", "Mike"]

                console.log(
                `There were ${englishMusicByCity["manchester"][0]["memberNames"].length} members in ${englishMusicByCity["manchester"][0]["bandName"]}`
                );
                //=> "There were 4 members in The Smiths"
                        arrays
        array-method
            const firstNumber = 32;
            const secondNumber = 9;
            const thirdNumber = 14;
            const fourthNumber = 33;
            const fifthNumber = 48;
            const powerBall = 5;

            const firstNumber = 32;
            const secondNumber = 9;
            const thirdNumber = 14;
            const fourthNumber = 33;
            const fifthNumber = 48;
            const powerBall = 5;

            function logWinningNumbers(first, second, third, fourth, fifth, power) {
            console.log("Winning numbers:", first, second, third, fourth, fifth, power);
            }

            logWinningNumbers(
            firstNumber,
            secondNumber,
            thirdNumber,
            fourthNumber,
            fifthNumber,
            powerBall
            );
            // LOG: Winning numbers: 32 9 14 33 48 5
            // => undefined

            ["This", "is", "an", "array", "of", "strings."];
            // => ["This", "is", "an", "array", "of", "strings."]

            ["Hello, world!", 42, null, NaN];
            // => ["Hello, world!", 42, null, NaN]

            const primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37];

            const flowers = ["Rose", "Tulip", "Orchid", "Lily"];

            const myArray = ["This", "array", "has", 5, "elements"];

            myArray.length;
            // => 5

            const winningNumbers = [32, 9, 14, 33, 48, 5];

            function logWinningNumbers(numbers) {
            console.log("Winning numbers:", numbers);
            }

            logWinningNumbers(winningNumbers);
            // LOG: Winning numbers: [32, 9, 14, 33, 48, 5]
            // => undefined

            const winningNumbers = [32, 9, 14, 33, 48, 5];
            // => undefined

            winningNumbers[0];
            // => 32

            winningNumbers[3];
            // => 33

            const alphabet = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            ];
            // => undefined

            alphabet.length;
            // => 26

            alphabet[alphabet.length - 1];
            // => "z"

            const planets = [
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Juptier",
            "Saturn",
            "Uranus",
            "Neptune",
            ];
            //=> undefined

            planets[4] = "Jupiter";
            //=> "Jupiter"

            planets;
            //=> ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

            planets = ["new", "array"];
            //=> Uncaught TypeError: Assignment to constant variable.

            const egregiouslyNestedArray = [
            "How",
            ["deep", ["can", ["we", ["go", ["?"], "Pretty"], "dang"], "deep,"], "it"],
            "seems.",
            ];

            egregiouslyNestedArray[0];
            //=> 'How'

            egregiouslyNestedArray[1];
            //=> [ 'deep', [ 'can', [ 'we', [Array], 'dang' ], 'deep,' ], 'it' ]

            egregiouslyNestedArray[2];
            //=> 'seems.'
            egregiouslyNestedArray[1][0];
            //=> 'deep'

            egregiouslyNestedArray[1][1];
            //=> [ 'can', [ 'we', [ 'go', [Array], 'Pretty' ], 'dang' ], 'deep,' ]

            egregiouslyNestedArray[1][2];
            //=> 'it'

            egregiouslyNestedArray[1][1][1][1][1];
            //=> ['?']

            egregiouslyNestedArray[1][1][1][1][1][0];
            //=> '?'

            const board = [
            ["X", "O", " "],
            [" ", "X", "O"],
            ["X", " ", "O"],
            ];

            board;
            // => [["X", "O", " "], [" ", "X", "O"], ["X", " ", "O"]]

            board[1];
            // => [" ", "X", "O"]

            board[0][0];
            // => "X"

            board[0][2];
            // => " "

            board[2][2];
            // => "O"

            const string = "Hello";

            string.toUpperCase();
            //=> "HELLO"

            const string = "Hello";

            string.toUpperCase();
            //=> "HELLO"

            string;
            //=> "Hello"


        array-lab
        objects
        mod-objects
        object-lab
        debugging in node
        stack-to
        looping lab
        object interpolation(interaction)
        traversing nested objects



    HTML

        
        A Quick Tour Of The Web
        Welcome to HTML
        Files and File Types
        Experiencing HTML Lab
        Document Structure Continued
        Your First HTML Tag Lab
        Nested HTML Tags And Attributes
        Create a Link Using the href Attribute
        HTML Elements
        HTML Lists
        HTML Tables
        HTML Images
        HTML Validation
        Expanding Your HTML Vocabulary via MDN
        Researching HTML Elements
        HTML Issue Bot 9000
        Using Your Browser's Developer Tools
        HTML Album Cover
        BONUS: Riyadh Blog


    CSS

        
        Intro to CSS
        Introduction to CSS Lab
        CSS Fundamentals
        CSS Fundamentals Lab
        CSS Validation Lab: Issue Bot 9000
        My Little Rainbow
        BONUS: CSS Kitten Wheelbarrow
        BONUS: CSS Graffiti Override Lab


    DOM

        
        Introduction to the DOM
        DOM Editing Lab
        Changing The DOM with DevTools and JavaScript
        The DOM Is a Tree
        JavaScript Query Selector Methods
        Creating and Inserting DOM Nodes Lab
        Survey - Manipulating the DOM

    Events

    
        JavaScript Events
        JavaScript Event Listeners Lab
        Moving Things with JavaScript by Acting on Events


    Git

        
        Intro to Version Control
        Git Basics
        Getting Code with Git
        Pushing Code with Git

    Project

        
        Software Engineering Prep Final Project Setup Part I: Setting Up Your Repo
        Software Engineering Prep Final Project Setup Part II: Hosting a Website on GitHub Pages
        Project: Build a Personal Website



phase1
phase2
phase3
phase4
phase5
algo