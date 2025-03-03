public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Singly Linkedlist (Java implementation)");
        System.out.println("---------------------------------------\n");

        SinglyLL singlyLL = new SinglyLL();

        // Testing function insertHead()
        singlyLL.insertHead(0);
        singlyLL.insertHead(2);
        singlyLL.insertHead(11);
        singlyLL.insertHead(7);

        // Testing function removeHead()
        singlyLL.removeHead();
        singlyLL.removeHead();
        singlyLL.removeHead();
        singlyLL.removeHead();
        singlyLL.removeHead(); // REMOVAL ERROR

        // Testing function insertTail()
        singlyLL.insertTail(1);
        singlyLL.insertTail(3);
        singlyLL.insertTail(5);
        singlyLL.insertTail(7);
    }
}