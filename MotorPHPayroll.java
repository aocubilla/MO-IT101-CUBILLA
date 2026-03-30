import java.util.*;

class Employee {
    String id;
    String name;
    double rate;

    Employee(String id, String name, double rate) {
        this.id = id;
        this.name = name;
        this.rate = rate;
    }
}

public class Main {
    static HashMap<String, Employee> employees = new HashMap<>();
    static Scanner sc = new Scanner(System.in);

    public static void addEmployee() {
        System.out.print("Enter Employee ID: ");
        String id = sc.nextLine();

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Hourly Rate: ");
        double rate = sc.nextDouble();
        sc.nextLine();

        employees.put(id, new Employee(id, name, rate));
        System.out.println("Employee added!");
    }

    public static void viewEmployees() {
        if (employees.isEmpty()) {
            System.out.println("No employees found.");
            return;
        }

        for (Employee e : employees.values()) {
            System.out.println("ID: " + e.id + ", Name: " + e.name + ", Rate: " + e.rate);
        }
    }

    public static void computeSalary() {
        System.out.print("Enter Employee ID: ");
        String id = sc.nextLine();

        if (!employees.containsKey(id)) {
            System.out.println("Employee not found.");
            return;
        }

        System.out.print("Enter hours worked: ");
        double hours = sc.nextDouble();
        sc.nextLine();

        Employee e = employees.get(id);
        double salary = hours * e.rate;

        System.out.println("Salary of " + e.name + ": " + salary);
    }

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n1. Add Employee");
            System.out.println("2. View Employees");
            System.out.println("3. Compute Salary");
            System.out.println("4. Exit");

            System.out.print("Enter choice: ");
            String choice = sc.nextLine();

            if (choice.equals("1")) {
                addEmployee();
            } else if (choice.equals("2")) {
                viewEmployees();
            } else if (choice.equals("3")) {
                computeSalary();
            } else if (choice.equals("4")) {
                break;
            } else {
                System.out.println("Invalid choice");
            }
        }
    }
}