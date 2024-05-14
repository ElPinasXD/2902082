public class Main {

    static int plusMethod(int x, int y){

        return x + y;
        
    }

    static double plusMethod(double x, double y){
        return x + y;
    }

    public static void main(String[] args) {
        int Num1 = plusMethod(4, 6);
        double Num2 = plusMethod(4.2, 3.2);
        System.out.println("Primera operacion " + Num1);
        System.out.println("Segunda operacion " + Num2);
    }
    

}



/*
3. 
public class Main{

    public static void main(String[] args) {
    
        //System.out.println("Hello World");
        checkAge(12);
    
    }
    
    static void checkAge(int age) { // Para mirar la edad
        if (age < 18) {
            System.out.println("Menor de edad");
        } else {
            System.out.println("Mayor edad");
        }
    }
    
}

2.

public class Main{

    public static void main(String[] args) {
    
        //System.out.println("Hello World");
        System.out.println(myMethod(5,2));
    
    }
    
    static int myMethod(int x, int y) {
        return x + y;
    }
    
}

1.

public class Main{

public static void main(String[] args) {

    //System.out.println("Hello World");
    myMethod("Esteban", 12);

}

private static void myMethod(String fname , int age) {
    System.out.println("Your name is " + fname + " you are " + age );
}

} */


/* 

Sobrecarga de metodo (Method overloading): Mismo nombre de una variable con diferentes parametros 
private static void myMethod(Tipo de dato  funcion)

Metodo: nombre en minuscula, () 
regla: CamelCase
debe hacer para lo que se creo 

static = no necesita a nadie
void = Tipo de retorno

Firma = Conjunto de Parametros
Parametros(Crea) = Cuando se crea o define la funcion
Argumentos(Llama) = Cuando se llama la funcion

*/