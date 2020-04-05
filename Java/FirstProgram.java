import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;

class FirstProgram {

    public static void main(String args[]) {
        
        //working with variables
        int age = 30;
        System.out.println(age);

        //primitive types: byte (1 byte) | short (2) | int (4) | long (8)
        //float (4) | double (8) | char (2) | boolean (1)
        int viewsCount = 123_456_123;
        long viewsCountBig = 3_456_123_123L;
        float price = 19.88F;

        //reference types: complex types
        Date now = new Date(); //allocate memory
        now.getTime();
        System.out.println(now);

        //arrays        
        int[][] numbers = new int[3][3]; //two rows, three columns
        numbers[0][1] = 1;
        numbers[1][2] = 2;
        numbers[2][0] = 3;
        numbers[2][1] = 3;

        int[] x = {1, 2, 3}; //after created, we had a fixed length

        System.out.println(x);
        System.out.println(Arrays.toString(x));
        System.out.println(Arrays.deepToString(numbers));

        //constant
        final float PI = 3.14F;

        //prefix and postfix
        int xx = 1;
        int yy = xx++; //if it's ++xx the result will be 2, insted of 1
        System.out.println(xx); //2
        System.out.println(yy); //1

        //order of operands: () * / + -

        //casting
        short sho = 1;
        int inte = sho + 2; //implicit casting 
        //byte > short > int > long > float > double

        double db = 1.1;
        int int2 = (int)db + 2; //3 - explicit casting: with compatible types

        Integer.parseInt("123"); //

        //format numbers
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String result = currency.format(1234567.891);
        System.out.println(result); //$1,234,567.89

        Scanner scanner = new Scanner(System.in);

        System.out.print("Age:");
        byte age2 = scanner.nextByte();
        System.out.println("you are " + age2 + " years old.");
    }
}