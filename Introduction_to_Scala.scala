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

