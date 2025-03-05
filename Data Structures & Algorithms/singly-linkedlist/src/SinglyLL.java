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
            System.out.println("Singly Linkedlist: { NULL }");
        } else if (isEmpty()) {
            System.out.println("Singly Linkedlist: { HEAD -> NULL }");
        } else {
            System.out.print("Singly Linkedlist: { HEAD -> ");
            Node currentNode = head;
            while (currentNode != null) {
                System.out.print(currentNode.getData() + " -> ");
                currentNode = currentNode.getNext();
            }
            System.out.println("NULL }");
        }
        printSinglyLLStats();
    }

    public void insertHead(int data) {
        System.out.println("\nSinglyLL.insertHead(" + data + ") called...");
        if (isNull()) {
            head = new Node(data, null);
            size = 1;
        } else if (isEmpty()) {
            head.setData(data);
            size = 1;
        } else {
            Node currentHead = head;
            Node newHead = new Node(data, currentHead);
            head = newHead;
            size++;
        }
        printSinglyLL();
    }

    public void removeHead() {
        System.out.println("\nSinglyLL.removeHead() called...");
        if (isNull() || isEmpty()) {
            System.out.println("\n***ERROR***: Cannot remove from NULL or empty list.");
        } else if (size == 1) {
            head = null;
            size = 0;
        } else {
            head = head.getNext();
            size--;
        }
        printSinglyLL();
    }

    public void insertTail(int data) {
        System.out.println("\nSinglyLL.insertTail(" + data + ") called...");
        if (isNull()) {
            head = new Node(data, null);
            size = 1;
        } else if (isEmpty()) {
            head.setData(data);
            head.setNext(null);
            size = 1;
        } else if (size == 1) {
            head.setNext(new Node(data, null));
            size = 2;
        } else {
            Node currentNode = head;
            while (currentNode != null) {
                if (currentNode.getNext() == null) {
                    currentNode.setNext(new Node(data, null));
                    size++;
                    break;
                }
                currentNode = currentNode.getNext();
            }
        }
        printSinglyLL();
    }

    public void removeTail() {
        System.out.println("\nSinglyLL.removeTail() called...");
        if (isNull() || isEmpty()) {
            System.out.println("\n***ERROR***: Cannot remove from NULL or empty list.");
        } else if (size == 1) {
            head = null;
            size = 0;
        } else {
            Node currentNode = head;
            while (currentNode != null) {
                if (currentNode.getNext().getNext() == null) {
                    break;
                }
                currentNode = currentNode.getNext();
            }
            currentNode.setNext(null);
            size--;
        }
        printSinglyLL();
    }

    public void insertAtIndex(int index, int data) {
        System.out.println("\nSinglyLL.insertAtIndex(" + index + ", " + data + ") called...");
        if (index <= 0 || index >= size) {
            System.out.println("\t***ERROR***: Invalid index. Use insertHead() or insertTail() instead...");
        } else if (index == 1) {
            Node currentHead = head;
            Node nextHead = currentHead.getNext();
            Node newNode = new Node(data, nextHead);
            currentHead.setNext(newNode);
            head = currentHead;
            size++;
        } else {
            Node tempHead = head;
            int i = 0;
            Node currentNode = tempHead;
            while (currentNode != null) {
                if (i == index - 1) {
                    break;
                }
                currentNode = currentNode.getNext();
                i++;
            }
            Node nextNode = currentNode.getNext();
            Node newNode = new Node(data, nextNode);
            currentNode.setNext(newNode);
            head = tempHead;
            size++;
        }
        printSinglyLL();
    }

    public void removeAtIndex(int index) {
        System.out.println("\nSinglyLL.removeAtIndex(" + index + ") called...");
        if (index <= 0 || index >= size) {
            System.out.println("\t***ERROR***: Invalid index. Use removeHead() or removeTail() instead...");
        } else if (index == 1) {
            Node tempHead = head;
            Node currentHead = tempHead;
            Node nodeToDelete = currentHead.getNext();
            Node nextNode = nodeToDelete.getNext();
            currentHead.setNext(nextNode);
            head = tempHead;
            size--;
        } else {
            Node tempHead = head;
            int i = 0;
            Node currentNode = tempHead;
            while (currentNode != null) {
                if (i == index - 1) {
                    break;
                }
                currentNode = currentNode.getNext();
                i++;
            }
            Node nodeToDelete = currentNode.getNext();
            Node nextNode = nodeToDelete.getNext();
            currentNode.setNext(nextNode);
            head = tempHead;
            size--;
        }
        printSinglyLL();
    }

    /*
    @Override
    public String toString() {}
    */
}