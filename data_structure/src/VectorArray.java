public class VectorArray<T> implements IArray<T> {
    public T[] array;
    int size;
    int vector = 100;

    public VectorArray() {
        size = 0;
        array = (T[]) new Object[size];
    }

    @Override
    public int size() {
        return size;
    }

    public void put(T item) {
        if (size == array.length) {
            resize();
        }
        array[size] = item;
        size++;
    }

    public T get(int index) {
        return array[index];
    }

    @Override
    public T remove(int index) {
        T[] newArray = (T[]) new Object[size() - 1];
        T delItem = array[index];
        for (int i = 0; (i < size() - 1); i++) {
            if (i < index) {
                newArray[i] = array[i];
            }
            if (i >= index) {
                newArray[i] = array[i + 1];
            }
        }
        array = newArray;
        size--;
        return delItem;
    }

    @Override
    public void add(int index, T item) {
        resize();
        for (int i = size() - 1; (i > index); i--) {
            array[i] = array[i - 1];
        }
        array[index] = item;
    }

    public void resize() {
        T[] newArray = (T[]) new Object[(size() + vector)];
        for (int i = 0; i < size(); i++)
            newArray[i] = array[i];
        array = newArray;
    }

}


