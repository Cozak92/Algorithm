public class ArraysStack<E> {

    public class ArrayStack {
        private E[] elements;
        private int size;

        public ArrayStack() {
            this.elements = new E[10];
        }

        public void push(E obj) {
            elements[size++] = obj;
        }

        public E pop() {
            if (size == 0) {
                throw new IllegalArgumentException("스택에 아무것도 없습니다");
            }
            E result = elements[--size];
            elements[size] = null;
            return result;
        }

    }
}
