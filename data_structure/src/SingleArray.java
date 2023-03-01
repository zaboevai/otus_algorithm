public class SingleArray<T> implements IArray<T> {
    public T[] array;

    public SingleArray() {
        array = (T[]) new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void put(T item) {
        resize();
        array[size() - 1] = item;
    }

    @Override
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
        T[] newArray = (T[]) new Object[size() + 1];
        for (int i = 0; i < size(); i++)
            newArray[i] = array[i];
        array = newArray;
    }

}
