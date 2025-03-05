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

        // Testing function removeTail()
        singlyLL.removeTail();
        singlyLL.removeTail();
        singlyLL.removeTail();
        singlyLL.removeTail();
        singlyLL.removeTail(); // REMOVAL ERROR

        // Testing function insertAtIndex() (simultaneously)
        singlyLL.insertHead(0);
        singlyLL.insertTail(2);
        singlyLL.insertHead(11);
        singlyLL.insertTail(7);
        singlyLL.insertHead(34);
        singlyLL.insertAtIndex(0, 100); // INSERTION AT BEGINNING ERROR
        singlyLL.insertAtIndex(5, 100); // INSERTION AT END ERROR
        singlyLL.insertAtIndex(1, 35);
        singlyLL.insertAtIndex(2, 36);
        singlyLL.insertAtIndex(6, 3);
        singlyLL.insertAtIndex(7, 4);

        // Testing function removeAtIndex()
        singlyLL.removeAtIndex(0); // REMOVAL AT BEGINNING ERROR
        singlyLL.removeAtIndex(10); // REMOVAL AT END ERROR
        singlyLL.removeAtIndex(1); // REMOVAL AT INDEX 1
        singlyLL.removeAtIndex(4);
        singlyLL.removeAtIndex(2);
        singlyLL.removeAtIndex(3);

        System.out.println("\n---------------------------------------\n");
    }
}