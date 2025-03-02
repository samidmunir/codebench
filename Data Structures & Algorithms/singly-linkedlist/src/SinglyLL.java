public class SinglyLL {

    private Node head;
    private short size = 0;
    private short NODE_MEM = 4;

    private boolean isNull() {
        return head == null;
    }

    private boolean isEmpty() {
        return !isNull() && size == 0;
    }

    private void printSinglyLLStats() {
        System.out.println("\tsize: " + size);
        System.out.println("\tmemory usage: " + (size * NODE_MEM) + " bytes");
    }

    private void printSinglyLL() {
        if (isNull()) {
            System.out.println("Singly Linkedlist: NULL");
        } else if (isEmpty()) {
            System.out.println("Singly Linkedlist: HEAD -> NULL");
        } else {
            System.out.print("Singly Linkedlist: HEAD ");
            Node currentNode = head;
            while (currentNode != null) {
                System.out.print(" -> " + currentNode.getData());
                currentNode = currentNode.getNext();
            }
            System.out.println("NULL");
        }
        printSinglyLLStats();
    }

    public void insertHead(int data) {}

    public void removeHead() {}

    public void insertTail(int data) {}

    public void removeTail() {}

    public void insertAtIndex(int index, int data) {}

    /*
    @Override
    public String toString() {}
    */
}