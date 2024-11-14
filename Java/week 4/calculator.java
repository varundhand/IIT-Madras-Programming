public class Calculator {

    // Static variable to keep track of total operations
    private static int operationCount = 0;

    // Static method for addition
    public static int add(int a, int b) {
        operationCount++;
        return a + b;
    }

    // Static method for subtraction
    public static int subtract(int a, int b) {
        operationCount++;
        return a - b;
    }

    // Static method for multiplication
    public static int multiply(int a, int b) {
        operationCount++;
        return a * b;
    }

    // Static method for division
    public static double divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        operationCount++;
        return (double) a / b;
    }

    // Static method to get the total number of operations
    public static int getOperationCount() {
        return operationCount;
    }

    public static void main(String[] args) {
        System.out.println("Addition: " + Calculator.add(10, 5));
        System.out.println("Subtraction: " + Calculator.subtract(10, 5));
        System.out.println("Multiplication: " + Calculator.multiply(10, 5));
        System.out.println("Division: " + Calculator.divide(10, 5));
        System.out.println("Total operations: " + Calculator.getOperationCount());
    }
}


