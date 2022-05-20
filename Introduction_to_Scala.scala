/////////////////////////
// A Scalable Language //
/////////////////////////


////// Scala is object-oriented

// Calculate the difference between 8 and 5
val difference = 8-5

// Print the difference
println(difference)


////// Define immutable variables (val)

// Define immutable variables for clubs 2♣ through 4♣
val twoClubs: Int = 2
val threeClubs: Int = 3
val fourClubs: Int = 4


////// Don't try to change me

// Define immutable variables for player names
val playerA: String = "Alex"
val playerB: String = "Chen"
val playerC: String = "Umberto"


////// Define mutable variables (var)

// Define mutable variables for all aces
var aceClubs = 1
var aceDiamonds = 1
var aceHearts = 1
var aceSpades = 1


////// You can change me

// Create a mutable variable for Alex as player A
var playerA = "Alex"

// Change the point value of A♦ from 1 to 11
var aceDiamonds = 11

// Calculate hand value for J♣ and A♦
println(aceDiamonds+jackClubs)




///////////////////////////////////////
// Workflows, Functions, Collections //
///////////////////////////////////////

////// Call a function

// Calculate hand values
var handPlayerA: Int = queenDiamonds+threeClubs+aceHearts+fiveSpades
var handPlayerB: Int = kingHearts+jackHearts

// Find and print the maximum hand value
println(maxHand(handPlayerA, handPlayerB))


////// Create and parameterize an array

// Create and parameterize an array for a round of Twenty-One
val hands: Array[Int] = new Array[Int](3)


////// Initialize an array

// Create and parameterize an array for a round of Twenty-One
val hands: Array[Int] = new Array[Int](3)

// Initialize the first player's hand in the array
hands(0) = tenClubs + fourDiamonds

// Initialize the second player's hand in the array
hands(1) = nineSpades + nineHearts

// Initialize the third player's hand in the array
hands(2) = twoClubs + threeSpades


////// An array, all at once

// Create, parameterize, and initialize an array for a round of Twenty-One
val hands = Array(tenClubs + fourDiamonds,
              nineSpades + nineHearts,
              twoClubs + threeSpades)


////// Updating arrays

// Initialize player's hand and print out hands before each player hits
hands(0) = tenClubs + fourDiamonds
hands(1) = nineSpades + nineHearts
hands(2) = twoClubs + threeSpades
hands.foreach(println)

// Add 5♣ to the first player's hand
hands(0) = hands(0) + fiveClubs

// Add Q♠ to the second player's hand
hands(1)  = hands(1) + queenSpades

// Add K♣ to the third player's hand
hands(2) = hands(2) + kingClubs

// Print out hands after each player hits
hands.foreach(println)


////// Initialize and prepend to a list

// Initialize a list with an element for each round's prize
val prizes = List(10,15,20,25,30)
println(prizes)

// Prepend to prizes to add another round and prize
val newPrizes = 5 :: prizes
println(newPrizes)


////// Initialize a list using cons and Nil

// Initialize a list with an element each round's prize
val prizes = 10 :: 15 :: 20 :: 25 :: 30 :: Nil
println(prizes)


////// Concatenate Lists

// The original NTOA and EuroTO venue lists
val venuesNTOA = List("The Grand Ballroom", "Atlantis Casino", "Doug's House")
val venuesEuroTO = "Five Seasons Hotel" :: "The Electric Unicorn" :: Nil

// Concatenate the North American and European venues
val venuesTOWorld = venuesNTOA ::: venuesEuroTO