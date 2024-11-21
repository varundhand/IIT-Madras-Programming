 // primitive types
byte age = 30;
int phone = 281982189;
long phone2 = 2819821892891892L;
float pi = 3.14F;
char letter = 'A';
boolean isAdult = false;


 // non-primitive types
String name = "varun";
System.out.println(name.length());

int[] marks = {12,23,21,45};
Arrays.sort(marks); 

System.out.println(marks[1]);

// adding gst using float 
float amount = 100f;
float finalAmount = amount + amount * 0.18f;
System.out.println(finalAmount);

// Math class
System.out.println(Math.max(10, 20)); // 20
System.out.println(Math.min(10, 20)); // 10
System.out.println((int)(Math.random()*100)); 

//! taking input from user 
Scanner sc = new Scanner(System.in);
System.out.println("Please Enter Your Age: ");
int age = sc.nextInt(); // takes integer input 

//! Consume the newline left by nextInt()
sc.nextLine();

float floatNumber = sc.nextFloat(); // takes float input 
System.out.println("you are " + age + (age == 1 ? " year old." : " years old."));

String name = sc.next(); // takes string input

//  if/else
boolean isSunUp = true;
if (isSunUp)
    System.out.println("Its day");
else 
    System.out.println("Its night");

int age = 17;
if (isSunUp && age >= 18) // and 
// if (isSunUp || age >= 18) // or 
    System.out.println("Good to go");
else
    System.out.println("Nopeeee");


// we can use curly braces if we have more than one statments in the if block
if (isSunUp) {
    System.out.println("Its day");
    System.out.println("Good to go");
} else {
    System.out.println("Its night");
    System.out.println("Nopeeee");
}

// switch case

int day = 1;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Invalid day");
}

// loops
// for loop
for (int i = 0; i<100; i++){
    System.out.println(i);

}

// do while loop
int inputNumber = sc.nextInt();
do {
    System.out.println("Enter the number:");
    // int inputNumber = sc.nextInt();
    System.out.println("The number is " + inputNumber);

} while (inputNumber != 100);
System.out.println("The end");

//! Exception handling
// try-catch
int[] marks = {21,32,24};
    try {
      System.out.println(marks[5]);
    }catch (Exception exception){
      // do something
    }

//! declaring functions
public static void printJava(){
    (int )
};

public static void helloName(String name){
    System.out.println("Hello " + name);
}

 public static int sum(int a, int b){
    return a + b;
};
  
for (int m : marks){
    if (m %2 == 0){
    System.out.println(m);
    }
}

helloName("Varun");
int sumOfNumbers = sum(10, 20);

