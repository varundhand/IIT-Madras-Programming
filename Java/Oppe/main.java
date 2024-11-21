import java.util.Scanner;
class Faculty{
   private String name;
   private double salary;
   public Faculty(String name, double salary) {
       this.name = name;
       this.salary = salary;
   }
   public double bonus(float percent){
       return (percent/100.0)*salary;
   }
    // Define method getDetails()
    public String getDetails(){
        return this.name + ", "+ this.salary; //! used this 
    }
    
    // Override method getDetails(float percent)
    public String getDetails(float percent){
        return this.name + ", " + this.salary + ", bonus = " + bonus(percent); 
    }
    
}
class Hod extends Faculty{
    private String personalAssistant;
    public Hod(String name, double salary, String pa) {
        super(name, salary);
        this.personalAssistant = pa;
    }
    // Override method bonus(float percent)
    public double bonus(float percent){
        return super.bonus(percent)*0.5; // this is the bonus of faculty 
    }
    // Override method getDetails()
    public String getDetails(){
        String s = super.getDetails();
        return s +  ", " + this.personalAssistant;
    }
    // Override method getDetails(float percent)
    public String getDetails(float percent){
        return getDetails() + ", " + bonus(percent); // this is the bonus of hod
    }

}
public class InheritanceTest{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        Faculty obj1 = new Faculty(sc.next(), sc.nextDouble());
        Faculty obj2 = new Hod(sc.next(), sc.nextDouble(), sc.next());
        System.out.println(obj1.getDetails());
        System.out.println(obj1.getDetails(10));
        System.out.println(obj2.getDetails());
        System.out.println(obj2.getDetails(10));
    }
}