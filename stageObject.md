



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




