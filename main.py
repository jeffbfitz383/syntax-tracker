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
    bundling
    data structures
    HTML
    CSS
    DOM
    Events
    Git
    Project
phase1
phase2
phase3
phase4
phase5
algo