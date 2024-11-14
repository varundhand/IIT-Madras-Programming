//* Data Types

// Primitive Data Types
// byte, short, int, long, float, double, boolean, char

// Non-Primitive Data Types
// String, Array, Class

// 1. int
int myNum = 5;

// integer has sub types i.e. byte, short, long
// int is 4 bytes long (1 byte = 8 bits)
// byte is 1 byte long
// short is 2 bytes long
// long is 8 bytes long
long myLongNum = 15000000000L; 
// long needs to followed by L at the end

// 2. float
float myFloatNum = 5.98f;
//! by default java interprets decimal numbers as double so we need to declare float with f at the end

// float is 4 bytles long
// double is 8 bytes long

double myDoubleNum = 5.99d;

// 3. char
char myLetter = 'D'; 
// '' is used to represent char and "" is used to represent string
//! Jvaa uses unicode to represent characters instead of ASCII so it has a wider range of characters

// char is 2 bytes long

// 4. boolean
boolean isJavaFun = true;
// boolean is used for true or false values
// boolean is 1 bit long

//* Non-Primitive Data Types
//* 5. String
String greeting = "Hello World";
// String is a sequence of characters
// String is a class in java and not a data type
// String is immutable i.e. once created it cannot be changed

//* String methods
// concatenate 
String firstName = "Varun"
String lastName = "Dhand"

String fullName = firstName + " " + lastName;
String fullName = firstName.concat(" ").concat(lastName);

// charAt() - returns the character at a specified index
char myChar = firstName.charAt(0); // retuns V

// lenght() - returns the length of a string
int len = firstName.length(); // returns 5

// replace() - replaces a character with another character
String newString = firstName.replace('V', 'S'); // returns Sarun // the original string is not changed

// substring() - extracts a part of a string
String subString = firstName.substring(1, 3); // returns ar

// toLowerCase() - converts a string to lower case
String lowerCase = firstName.toLowerCase(); // returns varun

//* 6. Arrays 
// Arrays are used to store multiple values in a single variable
// Arrays are of fixed size
// Arrays are of same data type

int[] marks = new int[3];// creates an array of size 3
int[] marks = {97, 98, 95} // creates an array of size 3 with values 10, 20, 30
system.out.println(marks); //! prints the memory address of the array but not the array
system.out.println(marks[0]); // prints 97

//! Java by default initializes the array with 0 for int, 0.0 for float, false for boolean, null for string

import Java.util.Arrays; //! use this import stament to use array methods
// import Java.util.*; // this imports all the classes in the util package

//* Array methods 
// length - returns the length of the array
int len = marks.length; // returns 3

// sort - sorts the array in ascending order
Arrays.sort(marks);

// copyOf - copies the array to a new array
int[] newMarks = Arrays.copyOf(marks, 3); // newMarks = {97, 98, 95}

// copyOfRange - copies the array to a new array from a specified range
int[] newMarks = Arrays.copyOfRange(marks, 1, 3); // newMarks = {98, 95}

// fill - fills the array with a specified value
Arrays.fill(marks, 10); // marks = {10, 10, 10}

// toString - converts the array to a string
String str = Arrays.toString(marks); // str = [10, 10, 10]

// equals - compares two arrays
boolean isEqual = Arrays.equals(marks, newMarks); // returns false

// binarySearch - searches for an element in the array
int index = Arrays.binarySearch(marks, 10); // returns 0

// asList - converts an array to a list
List<int> list = Arrays.asList(marks); // list = [10, 10, 10]

// Array of Arrays (2D arrays)
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
int x = myNumbers[1][2]; // returns 7

//! casting 