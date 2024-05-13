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
        array
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


        array-Methods
            const superheroes = ["Catwoman", "Storm", "Jessica Jones"];

            superheroes.push("Wonder Woman");
            // => 4

            superheroes;
            // => ["Catwoman", "Storm", "Jessica Jones", "Wonder Woman"]

            const cities = ["New York", "San Francisco"];

            cities.unshift("Boston", "Chicago");
            // => 4

            cities;
            // => ["Boston", "Chicago", "New York", "San Francisco"]



            const coolCities = ["New York", "San Francisco"];

            const copyOfCoolCities = [...coolCities];

            copyOfCoolCities;
            //=> ["New York", "San Francisco"]

            const coolCities = ["New York", "San Francisco"];

            const allCities = ["Los Angeles", ...coolCities];

            coolCities;
            // => ["New York", "San Francisco"]

            allCities;
            // => ["Los Angeles", "New York", "San Francisco"]

            const coolCats = ["Hobbes", "Felix", "Tom"];

            const allCats = [...coolCats, "Garfield"];

            coolCats;
            // => ["Hobbes", "Felix", "Tom"]

            allCats;
            // => ["Hobbes", "Felix", "Tom", "Garfield"]

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.pop();
            // => "Sun"

            days;
            // => ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.shift();
            // => "Mon"

            days;
            // => [Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            const primes = [2, 3, 5, 7];

            const copyOfPrimes = primes.slice();

            primes;
            // => [2, 3, 5, 7]

            copyOfPrimes;
            // => [2, 3, 5, 7]

            const primes = [2, 3, 5, 7];

            const copyOfPrimesUsingSlice = primes.slice();

            const copyOfPrimesUsingSpreadOperator = [...primes];

            primes.push(11);
            // => 5

            primes;
            // => [2, 3, 5, 7, 11]

            copyOfPrimesUsingSlice;
            // => [2, 3, 5, 7]

            copyOfPrimesUsingSpreadOperator;
            // => [2, 3, 5, 7]


            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.slice(2, 5);
            // => ["Wed", "Thu", "Fri"]

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.slice(5);
            // => ["Sat", "Sun"]

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.slice(1);
            // => ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.slice(0, days.length - 1);
            // => ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.slice(-1);
            // => ["Sun"]

            days.slice(-3);
            // => ["Fri", "Sat", "Sun"]

            days.slice(0, -1);
            // => ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

            array.splice(start);

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

            days.splice(2);
            // => ["Wed", "Thu", "Fri", "Sat", "Sun"]

            days;
            // => ["Mon", "Tue"]


            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
            // => ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            days.splice(-2);
            // => ["Sat", "Sun"]

            days;
            // => ["Mon", "Tue", "Wed", "Thu", "Fri"]

            array.splice(start, deleteCount);

            const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
            // => ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

            days.splice(2, 3);
            // => ["Wed", "Thu", "Fri"]

            days;
            // => ["Mon", "Tue", "Sat", "Sun"]

            array.splice(start, deleteCount, item1, item2, ...)

            const cards = [
            "Ace of Spades",
            "Jack of Clubs",
            "Nine of Clubs",
            "Nine of Diamonds",
            "Three of Hearts",
            ];

            cards.splice(2, 1, "Ace of Clubs");
            // => ["Nine of Clubs"]

            cards;
            // => ["Ace of Spades", "Jack of Clubs", "Ace of Clubs", "Nine of Diamonds", "Three of Hearts"]

            const menu = [
            "Jalapeno Poppers",
            "Cheeseburger",
            "Fish and Chips",
            "French Fries",
            "Onion Rings",
            ];

            menu.splice(1, 2, "Veggie Burger", "House Salad", "Teriyaki Tofu");
            // => ["Cheeseburger", "Fish and Chips"]

            menu;
            // => ["Jalapeno Poppers", "Veggie Burger", "House Salad", "Teriyaki Tofu", "French Fries", "Onion Rings"]

            const books = ["Beloved", "Giovanni’s Room", "The Color Purple", "The Grass Dancer"];

            books.splice(2, 0,  "Kindred", "Love Medicine");
            // => []

            books;
            // => ['Beloved', 'Giovanni’s Room', 'Kindred', 'Love Medicine', 'The Color Purple', 'The Grass Dancer']

            const cards = [
            "Ace of Spades",
            "Jack of Clubs",
            "Nine of Clubs",
            "Nine of Diamonds",
            "Three of Hearts",
            ];

            cards[2] = "Ace of Clubs";
            // => "Ace of Clubs"

            cards;
            // => ["Ace of Spades", "Jack of Clubs", "Ace of Clubs", "Nine of Diamonds", "Three of Hearts"]

            const menu = [
            "Jalapeno Poppers",
            "Cheeseburger",
            "Fish and Chips",
            "French Fries",
            "Onion Rings",
            ];

            const newMenu = [
            ...menu.slice(0, 1),
            "Veggie Burger",
            "House Salad",
            "Teriyaki Tofu",
            ...menu.slice(3),
            ];

            menu;
            // => ["Jalapeno Poppers", "Cheeseburger", "Fish and Chips", "French Fries", "Onion Rings"]

            newMenu;
            // => ["Jalapeno Poppers", "Veggie Burger", "House Salad", "Teriyaki Tofu", "French Fries", "Onion Rings"]
                            
        array-lab

            const cats = ["Milo", "Otis", "Garfield"];

            function destructivelyAppendCat (name) {
            cats.push(name);
            }

            function destructivelyPrependCat (name) {
            cats.unshift(name);
            }

            function destructivelyRemoveLastCat () {
            cats.pop();
            }

            function destructivelyRemoveFirstCat () {
            cats.shift();
            }

            function appendCat (name) {
            return [...cats, name];
            }

            function prependCat (name) {
            return [name, ...cats];
            }

            function removeFirstCat () {
            return cats.slice(1);
            }

            function removeLastCat () {
            return cats.slice(0, cats.length - 1);



            

        objects

            const address = "11 Broadway, 2nd Floor, New York, NY 10004";

            const address = ["11 Broadway", "2nd Floor", "New York", "NY", "10004"];

            address[1] = "3rd Floor";

            address;
            //=> ["11 Broadway", "3rd Floor", "New York", "NY", "10004"]

            const street1 = "11 Broadway";
            const street2 = "2nd Floor";
            const city = "New York";
            const state = "NY";
            const zipCode = "10004";

            const obj = {};

            const obj = { key: value };

            const obj = {
            key1: value1,
            key2: value2,
            };

            const obj = {
            key1: value1,
            key2: {
                innerKey1: innerValue1,
                innerKey2: innerValue2,
            },
            };

            const address = {
            street: {
                line1: "11 Broadway",
                line2: "2nd Floor",
            },
            city: "New York",
            state: "NY",
            zipCode: "10004",
            };

            const meals = {
            breakfast: "Avocado toast",
            lunch: "Avocado toast",
            dinner: "Avocado toast",
            };

            meals.breakfast;
            // => "Avocado toast"

            meals.dinner;
            // => "Avocado toast"

            const meals = {
            breakfast: "Avocado toast",
            breakfast: "Oatmeal",
            breakfast: "Scrambled eggs",
            };

            meals;
            // => { breakfast: "Scrambled eggs" }

            //=> { line1: "11 Broadway", line2: "2nd Floor" }

            address.city;
            //=> "New York"

            address.state;
            //=> "NY"

            address.zipCode;
            //=> "10004"

            address.street.line1;
            //=> "11 Broadway"

            address.street.line2;
            //=> "2nd Floor"

            address.country;
            //=> undefined

            address["street"];
            //=> { line1: "11 Broadway", line2: "2nd Floor" }

            address["street"]["line1"];
            //=> "11 Broadway"

            address["street"]["line2"];
            //=> "2nd Floor"

            address["city"];
            //=> "New York"

            address["state"];
            //=> "NY"

            address["zipCode"];
            //=> "10004"

            const wildKeys = {
            "Cash rules everything around me.": "Wu",
            "C.R.E.A.M.": "Tang",
            "Get the money.": "For",
            "$ $ bill, y'all!": "Ever",
            };

            wildKeys.'Cash rules everything around me.';
            // ERROR: Uncaught SyntaxError: Unexpected string

            wildKeys["$ $ bill, y'all!"];
            //=> "Ever"

            address["zip" + "Code"];
            //=> "10004"

            const meals = {
            breakfast: "Oatmeal",
            lunch: "Caesar salad",
            dinner: "Chimichangas",
            };

            let mealName = "lunch";

            meals[mealName];
            //=> "Caesar salad"

            mealName = "dinner";
            //=> "dinner"

            meals.mealName;
            //=> undefined
             
            const morningMeal = "breakfast";
            const middayMeal = "lunch";
            const eveningMeal = "dinner";

            const meals = {
            [morningMeal]: "French toast",
            [middayMeal]: "Personal pizza",
            [eveningMeal]: "Fish and chips",
            };

            meals;
            //=> { breakfast: "French toast", lunch: "Personal pizza", dinner: "Fish and chips" } 

            const morningMeal = "breakfast";
            const middayMeal = "lunch";
            const eveningMeal = "dinner";

            const meals = {
            morningMeal: "French toast",
            middayMeal: "Personal pizza",
            eveningMeal: "Fish and chips",
            };

            meals;
            //=> { morningMeal: "French toast", middayMeal: "Personal pizza", eveningMeal: "Fish and chips" }

            const wednesdayMenu = {
            cheesePlate: {
                soft: "Brie",
                semiSoft: "Fontina",
                hard: "Provolone",
            },
            fries: "Sweet potato",
            salad: "Southwestern",
            };

            Object.keys(wednesdayMenu);
            //=> ["cheesePlate", "fries", "salad"]

        
        mod-objects

            



            const city = "New York";


            const circle = {}; // Create `circle` and set it to an empty Object

            circle;
            //=> {}

            circle.radius = 5; // Create the key inside `circle` and set its value to 5

            circle;
            //=> { radius: 5 }


            const circle = {};

            circle.radius = 5;

            circle["diameter"] = 10;

            circle.circumference = circle.diameter * Math.PI;
            //=> 31.41592653589793

            circle["area"] = Math.PI * circle.radius ** 2;
            //=> 78.53981633974483

            circle;
            //=> { radius: 5, diameter: 10, circumference: 31.41592653589793, area: 78.53981633974483 }
            .



            const mondayMenu = {
            cheesePlate: {
                soft: "Chèvre",
                semiSoft: "Gruyère",
                hard: "Manchego",
            },
            fries: "Curly",
            salad: "Cobb",
            };

            mondayMenu.fries = "Sweet potato";

            mondayMenu;
            //=> { cheesePlate: { soft: "Chèvre", semiSoft: "Gruyère", hard: "Manchego" }, fries: "Sweet potato", salad: "Cobb" }
            Note that modifying an Object's properties in the way we did above is destructive. This means that we're making changes directly to the original Object.



            function destructivelyUpdateObject(obj, key, value) {
            obj[key] = value; //Why are we using bracket notation here?

            return obj;
            }


            const mondayMenu = {
            cheesePlate: {
                soft: "Chèvre",
                semiSoft: "Gruyère",
                hard: "Manchego",
            },
            fries: "Sweet potato",
            salad: "Cobb",
            };

            const tuesdayMenu = destructivelyUpdateObject(mondayMenu, "salad", "Caesar");

            tuesdayMenu;
            //=> { cheesePlate: { soft: "Chèvre", semiSoft: "Gruyère", hard: "Manchego" }, fries: "Sweet potato", salad: "Caesar" }

            tuesdayMenu.salad;
            //=> "Caesar"
            Looks like our tuesdayMenu came out perfectly. But what about mondayMenu?

            mondayMenu.salad;
            //=> "Caesar"




            function nondestructivelyUpdateObject(obj, key, value) {
            // Code to return new, updated menu object
            }


            function nondestructivelyUpdateObject(obj, key, value) {
            const newObj = { ...obj };

            // Code to return new, updated menu object goes here
            }


            function nondestructivelyUpdateObject(obj, key, value) {
            const newObj = { ...obj };

            newObj[key] = value;

            return newObj;
            }

            const sundayMenu = nondestructivelyUpdateObject(
            tuesdayMenu,
            "fries",
            "Shoestring"
            );

            tuesdayMenu.fries;
            //=> "Sweet potato"

            sundayMenu.fries;
            //=> "Shoestring"




            function nondestructivelyUpdateObject(obj, key, value) {
            return {
                ...obj,
                [key]: value,
            };
            }

            const sundayMenu = nondestructivelyUpdateObject(
            tuesdayMenu,
            "fries",
            "Shoestring"
            );

            tuesdayMenu.fries;
            //=> "Sweet potato"

            sundayMenu.fries;
            //=> "Shoestring"





            s:

            const wednesdayMenu = {
            cheesePlate: {
                soft: "Brie",
                semiSoft: "Fontina",
                hard: "Provolone",
            },
            fries: "Sweet potato",
            salad: "Southwestern",
            };

            delete wednesdayMenu.salad;
            //=> true

            wednesdayMenu;
            //=> { cheesePlate: { soft: "Brie", semiSoft: "Fontina", hard: "Provolone" }, fries: "Sweet potato" }






            typeof [];
            //=> "object"


            const myArray = [];

            myArray.summary = "Empty array!";

            myArray;
            //=> [summary: "Empty array!"]


            myArray["summary"] = "This array is totally empty.";

            myArray;
            //=> [summary: "This array is totally empty."]

            myArray.summary;
            //=> "This array is totally empty."


            myArray.push(2, 3, 5, 7);
            //=> 4

            myArray;
            //=> [2, 3, 5, 7, summary: "This array is totally empty."]


            myArray.length;
            //=> 4
            .

            myArray[0];
            //=> 2
            ?

            myArray[myArray.length - 1];
            //=> 7




            const myArray = [];

            myArray[0] = "Will this be an `Object` property or an `Array` element?";
            //=> "Will this be an `Object` property or an `Array` element?"

            // Moment of truth...
            myArray.length;
            //=> 1

            myArray;
            //=> ["Will this be an `Object` property or an `Array` element?"]
            ?

            myArray["0"] = "What about this one?";
            //=> "What about this one?"

            myArray.length;
            //=> 1

            myArray;
            //=> ["What about this one?"]


            const myArray = [2, 3, 5, 7];

            myArray["1"] = "Hi";
            //=> "Hi"

            myArray;
            //=> [2, "Hi", 5, 7]

            myArray["01"] = "Ho";
            //=> "Ho"

            myArray;
            //=> [2, "Hi", 5, 7, 01: "Ho"]

            myArray[01];
            //=> "Hi"

            myArray["01"];
            //=> "Ho"


            myArray.length;
            //=> 4


            Object.keys(myArray);
            //=> ["0", "1", "2", "3", "01"]

        object-lab.

            const employee = {
            name: "Max",
            streetAddress: "5 Main Street",
            };

            function updateEmployeeWithKeyAndValue(employee, key, value) {
            // Alternate using ES6 Spread operators:
            // return { ...employee, ...{ [key]: value } }
            return Object.assign({}, employee, { [key]: value });
            }

            function destructivelyUpdateEmployeeWithKeyAndValue(employee, key, value) {
            employee[key] = value;

            return employee;
            }

            function deleteFromEmployeeByKey(employee, key) {
            // Alternate using ES6 Spread operators:
            // const newObj = { ...employee }
            const newObj = Object.assign({}, employee);

            delete newObj[key];

            return newObj;
            }

            function destructivelyDeleteFromEmployeeByKey(employee, key) {
            delete employee[key];

            return employee;
            }




        .
        debugging in node


        stack-to
        looping lab

            const gifts = ["teddy bear", "drone", "doll"];

            function wrapGift(gift) {
            console.log(`Wrapped ${gift} and added a bow!`);
            }

            wrapGift(gifts[0]);
            wrapGift(gifts[1]);
            wrapGift(gifts[2]);

            for ([initialization]; [condition]; [iteration]) {
            [loop body]
            }

            for (let age = 30; age < 40; age++) {
            console.log(`I'm ${age} years old. Happy birthday to me!`);
            debugger;
            }

            const gifts = ["teddy bear", "drone", "doll"];

            function wrapGifts(gifts) {
            for (let i = 0; i < gifts.length; i++) {
                console.log(`Wrapped ${gifts[i]} and added a bow!`);
                debugger;
            }

            return gifts;
            }

            wrapGifts(gifts);

            writeCards(["Charlie", "Samip", "Ali"], "birthday");

            [
            "Thank you, Charlie, for the wonderful birthday gift!",
            "Thank you, Samip, for the wonderful birthday gift!",
            "Thank you, Ali, for the wonderful birthday gift!",
            ];

            while ([condition]) {
            [loop body]
            }

            const gifts = ["teddy bear", "drone", "doll"];

            function wrapGifts(gifts) {
            let i = 0; // the initialization moves OUTSIDE the body of the loop!
            while (i < gifts.length) {
                console.log(`Wrapped ${gifts[i]} and added a bow!`);
                i++; // the iteration moves INSIDE the body of the loop!
            }

            return gifts;
            }

            wrapGifts(gifts);
            // LOG: Wrapped teddy bear and added a bow!
            // LOG: Wrapped drone and added a bow!
            // LOG: Wrapped doll and added a bow!
            // => ["teddy bear", "drone", "doll"]

            function plantGarden() {
            let keepWorking = true;
            while (keepWorking) {
                chooseSeedLocation();
                plantSeed();
                waterSeed();
                keepWorking = checkForMoreSeeds();
            }
            }

            let countup = 0;
            while (countup < 10) {
            console.log(countup++);
            }

            for (let countup = 0; countup < 10; countup++) {
            console.log(countup);
            }

            //;lab


            function writeCards( namesArray, event ) {
            let thankYouCards = []
            for ( let i = 0; i < namesArray.length; i++ ) {
            thankYouCards.push( `Thank you, ${namesArray[i]}, for the wonderful ${event} gift!` )
            }
            return thankYouCards
            }

            function countDown( startingNumber ) {
            while ( startingNumber > 0 ) {
                console.log( startingNumber );
                startingNumber -= 1;
            }
            console.log( startingNumber );
            }
        object iteration
        
            const userInfo = {
            firstName: "Avi",
            lastName: "Flombaum",
            companyName: "Flatbook Labs",
            jobTitle: "Developer Apprentice",
            friend1firstName: "Nancy",
            friend1lastName: "Burgess",
            friend1companyName: "Flatbook Labs",
            friend1jobTitle: "Developer Apprentice",
            friend2firstName: "Corinna",
            friend2lastName: "Jackson",
            friend2companyName: "Flatbook Labs",
            friend2jobTitle: "Senior Developer",
            project1title: "Flatbook",
            project1description:
                "The premier Flatiron School-based social network in the world.",
            project2title: "Scuber",
            project2description:
                "A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.",
            };

            const userInfo = {
            firstName: "Avi",
            lastName: "Flombaum",
            company: {
                name: "Flatbook Labs",
                jobTitle: "Developer Apprentice",
            },
            friends: [
                {
                firstName: "Nancy",
                lastName: "Burgess",
                company: {
                    name: "Flatbook Labs",
                    jobTitle: "Developer Apprentice",
                },
                },
                {
                firstName: "Corinna",
                lastName: "Jackson",
                company: {
                    name: "Flatbook Labs",
                    jobTitle: "Lead Developer",
                },
                },
            ],
            projects: [
                {
                title: "Flatbook",
                description:
                    "The premier Flatiron School-based social network in the world.",
                },
                {
                title: "Scuber",
                description:
                    "A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.",
                },
            ],
            };

            userInfo.lastName;
            //=> "Flombaum"

            userInfo.company.jobTitle;
            //=> "Developer Apprentice"

            userInfo.friends[0].firstName;
            //=> "Nancy"

            userInfo.projects[1].title;
            //=> "Scuber"
            
            const letters = ["a", ["b", ["c", ["d", ["e"]], "f"]]];

            
            letters[1];
            //=> ["b", ["c", ["d", ["e"]], "f"]]

            letters[1][1];
            //=> ["c", ["d", ["e"]],


            letters[1][1][1][1];
            //=> ["e"]

            letters[1][1][1][1][0];
            //=> "e"


            const userInfo = {
            firstName: "Avi",
            lastName: "Flombaum",
            companyName: "Flatbook Labs",
            jobTitle: "Developer Apprentice",
            friend1firstName: "Nancy",
            friend1lastName: "Burgess",
            friend1companyName: "Flatbook Labs",
            friend1jobTitle: "Developer Apprentice",
            friend2firstName: "Corinna",
            friend2lastName: "Jackson",
            friend2companyName: "Flatbook Labs",
            friend2jobTitle: "Senior Developer",
            project1title: "Flatbook",
            project1description:
                "The premier Flatiron School-based social network in the world.",
            project2title: "Scuber",
            project2description:
                "A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.",
            };

            function shallowIterator(target) {
            for (const key in target) {
                console.log(target[key]);
            }
            }

            shallowIterator(userInfo);
            // LOG: Avi
            // LOG: Flombaum
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Nancy
            // LOG: Burgess
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Corinna
            // LOG: Jackson
            // LOG: Flatbook Labs
            // LOG: Senior Developer
            // LOG: Flatbook
            // LOG: The premier Flatiron School-based social network in the world.
            // LOG: Scuber
            // LOG: A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.

            const primes = [2, 3, 5, 7, 11];

            shallowIterator(primes);
            // LOG: 2
            // LOG: 3
            // LOG: 5
            // LOG: 7
            // LOG: 11

            const numbers = [1, [2, [4, [5, [6]], 3]]];

            shallowIterator(numbers);
            // LOG: 1
            // LOG: [2, [4, [5, [6]], 3]]

            function shallowIterator(target) {
            for (const key in target) {
                if (typeof target[key] === "object") {
                for (const nestedKey in target[key]) {
                    console.log(target[key][nestedKey]);
                }
                } else {
                console.log(target[key]);
                }
            }
            }

            shallowIterator(numbers);
            // LOG: 1
            // LOG: 2
            // LOG: [4, [5, [6]], 3]

            function deepIterator(target) {
            if (typeof target === "object") {
                for (const key in target) {
                deepIterator(target[key]);
                }
            } else {
                console.log(target);
            }
            }

            const numbers = [1, [2, [4, [5, [6]], 3]]];

            deepIterator(numbers);
            // LOG: 1
            // LOG: 2
            // LOG: 4
            // LOG: 5
            // LOG: 6
            // LOG: 3

            function deepIterator(target) {
            console.log("Argument: ", target);
            if (typeof target === 'object') {
            for (const key in target) {
                deepIterator(target[key]);
            }
            } else {
            console.log("Logged value: ", target);
            }
                }
            const numbers = [1, [2, [4, [5, [6]], 3]]];

            deepIterator(numbers);


            function deepIterator(target) {
            if (typeof target === 'object') {
            for (const key in target) {
                deepIterator(target[key]);
            }
            } else {
            console.log(target);
            }
            }

            const userInfo = {
            firstName: "Avi",
            lastName: "Flombaum",
            company: {
                name: "Flatbook Labs",
                jobTitle: "Developer Apprentice",
            },
            friends: [
                {
                firstName: "Nancy",
                lastName: "Burgess",
                company: {
                    name: "Flatbook Labs",
                    jobTitle: "Developer Apprentice",
                },
                },
                {
                firstName: "Corinna",
                lastName: "Jackson",
                company: {
                    name: "Flatbook Labs",
                    jobTitle: "Lead Developer",
                },
                },
            ],
            projects: [
                {
                title: "Flatbook",
                description:
                    "The premier Flatiron School-based social network in the world.",
                },
                {
                title: "Scuber",
                description:
                    "A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.",
                },
            ],
            };

            deepIterator(userInfo);
            // LOG: Avi
            // LOG: Flombaum
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Nancy
            // LOG: Burgess
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Corinna
            // LOG: Jackson
            // LOG: Flatbook Labs
            // LOG: Lead Developer
            // LOG: Flatbook
            // LOG: The premier Flatiron School-based social network in the world.
            // LOG: Scuber
            // LOG: A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.

            let counter = 0;

            function deepIterator(target) {
            counter++;

            if (typeof target === "object") {
                for (const key in target) {
                deepIterator(target[key]);
                }
            } else {
                console.log(target);
            }
            }

            deepIterator(userInfo);
            // LOG: Avi
            // LOG: Flombaum
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Nancy
            // LOG: Burgess
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Corinna
            // LOG: Jackson
            // LOG: Flatbook Labs
            // LOG: Lead Developer
            // LOG: Flatbook
            // LOG: The premier Flatiron School-based social network in the world.
            // LOG: Scuber
            // LOG: A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters.

            function deepIterator(target) {
            if (typeof target === "object") {
                for (const key in target) {
                deepIterator(target[key]);
                }
            } else if (Array.isArray(target)) {
                console.log("We found an array");
                // iterate through the array
            } else {
                // console.log(target);
            }
            }

            deepIterator(userInfo);


            function deepIterator(target) {
            if (Array.isArray(target)) {
                // iterate through the array
                console.log("We found an array");
            } else if (typeof target === "object") {
                for (const key in target) {
                deepIterator(target[key]);
                }
            } else {
                console.log(target);
            }
            }

            deepIterator(userInfo);
            // LOG: Avi
            // LOG: Flombaum
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: We found an array
            // LOG: We found an array

            function deepIterator(target) {
            if (Array.isArray(target)) {
                for (const element of target) {
                deepIterator(element);
                }
            } else if (typeof target === "object") {
                for (const key in target) {
                deepIterator(target[key]);
                }
            } else {
                console.log(target);
            }
            }

            deepIterator(userInfo);
            // LOG: Avi
            // LOG: Flombaum
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Nancy
            // LOG: Burgess
            // LOG: Flatbook Labs
            // LOG: Developer Apprentice
            // LOG: Corinna
            // LOG: Jackson
            // LOG: Flatbook Labs
            // LOG: Lead Developer
            // LOG: Flatbook
            // LOG: The premier Flatiron School-based social network in the world.
            // LOG: Scuber
            // LOG: A burgeoning startup helping busy parents transport their children to and from all of their activities on scooters





    HTML

        
        A Quick Tour Of The Web

            <!DOCTYPE html>
            <html lang="">
            <head>
                <title>Home | The Metropolitan Museum of Art</title>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <meta name="title" content="Home" />
                <meta
                name="keywords"
                content="Metropolitan Museum, Met, Metropolitan Museum of Art, Met Museum, Metropolitan"
                />
                <meta name="description" content="The Metropolitan Museum of Art is a..." />
                ...
            </head>
            </html>


            Welcome to HTML
            Files and File Types
            Experiencing HTML Lab
        
            <li>"Monstera deliciosa"</li>
            <li>"Fiddle Leaf Fig"</li>
            <li>"Pilea"</li>
            <li>"Golden Pothos"</li>
            <li>"Peace Lily"</li>

            <ol>
            <li>"Monstera deliciosa"</li>
            <li>"Fiddle Leaf Fig"</li>
            <li>"Pilea"</li>
            <li>"Golden Pothos"</li>
            <li>"Peace Lily"</li>
            </ol>

            <ol>
                  <li>"Monstera deliciosa"</li>
                <li>"Fiddle Leaf Fig"</li>
                <li>"Pilea"</li>
                <li>"Golden Pothos"</li>
                <li>"Peace Lily"</li>
            </ol>

            <p>Some of my favorite plants!</p>
            <ul>
                <li>"Monstera deliciosa"</li>
                <li>"Fiddle Leaf Fig"</li>
                <li>"Pilea"</li>
                <li>"Golden Pothos"</li>
                <li>"Peace Lily"</li>
            </ul>

            <h1>My Plant List</h1>


            <h1>My Plant List</h1>
            <p>Some of my favorite plants!</p>
            <ul>
                <li>"Monstera deliciosa"</li>
                <li>"Fiddle Leaf Fig"</li>
                <li>"Pilea"</li>
                <li>"Golden Pothos"</li>
                <li>"Peace Lily"</li>
            </ul>





        Document Structure Continued



            <html lang="en"></html>
            <!-- This is a comment! -->

            <link rel="stylesheet" type="text/css" href="style.css" />
            
            <link
                rel="stylesheet"
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"
            />
            <link rel="stylesheet" type="text/css" href="company.css" />
            <link rel="stylesheet" type="text/css" href="engineering-department.css" />
            <link rel="stylesheet" type="text/css" href="project-x-launch.css" />
            <link rel="stylesheet" type="text/css" href="typography.css" />

            <title>My Site Title</title>

        my first html lab  

            <!-- Write your HTML in this file -->
            <h1>Hello, World!</h1>
            explorer.exe index.html

        Nested HTML Tags And Attributes00

            <!DOCTYPE html>
            <html>
            <head>
                <title>Web development course</title>
            </head>
            <body>
                <header>
                <!-- header element documentation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header -->

                <nav id="main-navigation">
                <!-- nav element documentation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav -->

                    <ul>
                    <!-- ul element documentation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul -->

                    <li><a href="/web">Introduction to the web</a></li>
                    <!-- li element documentation: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li -->

                    <li><a href="/html">Learn HTML</a></li>
                    </ul>
                </nav>
                </header>
            </body>
            </html>

            <element attribute_name="attribute_value" another_attribute_name="another_attribute_value"></element>

            <p id='main_paragraph'>This element can be uniquely identified  using the 'main_paragraph' id HTML attribute</p>

            <p class='other_paragraphs'>This element belongs to a group of elements who share the 'other_paragraphs' HTML class attribute</p>
            <p class='other_paragraphs'>This element also belongs to a group of elements who share the 'other_paragraphs' HTML class attribute</p>


            <a href="https://flatironschool.com/">Flatiron School</a>

        create href lab 

            <!-- Write your HTML in this file -->

            <a href="https://flatironschool.com">Flatiron School</a>

        HTML Elements

            <ul>
            <li>One item</li>
            <li>Another item</li>
            </ul>

            <ol>
            <li>First item</li>
            <li>Second item</li>
            </ol>

            <dl>
            <dt>First term</dt>
            <dd>Term definition</dd>
            </dl>

            <img
            src="https://via.placeholder.com/800x600.png"
            alt="Alternative Text"
            title="Display Title"
            width="800"
            height="600"
            />

            <a href="http://example.com/">This is a link</a>

            <a href="http://example.com/">
            <img src="https://via.placeholder.com/800x600.png" alt="Alternative Text" />
            </a>
    

            <a href="mailto:webmaster@example.com">Send an email</a>

            <p id="tips">Useful Tips Section</p>
            <a href="#tips">Jump to the Useful Tips Section</a>

            <a href="about.html">This is a relative URL link</a>

            <a href="http://example.com/">This is an absolute URL link</a>


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