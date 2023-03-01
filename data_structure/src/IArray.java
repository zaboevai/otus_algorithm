public interface IArray<T> {
    void put(T item);

    T get(int index);

    int size();

    void add(int index, T item);

    T remove(int index);
}
