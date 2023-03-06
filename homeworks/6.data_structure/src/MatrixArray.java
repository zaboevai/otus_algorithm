public class MatrixArray<T> implements IArray<T> {
    public T[][] matrix_array;
    int matrix_size;
    public T[] array;
    int array_size;
    int MAX_ARRAY_SIZE = 10;

    int cur_step;

    public MatrixArray() {
        matrix_size = 0;
        matrix_array = (T[][]) new Object[matrix_size][];

        array = createArray(MAX_ARRAY_SIZE);
        array_size = 0;
    }

    public int size() {
        return matrix_size;
    }
    // optimized getting
    public T get(int index) {
        set_array_to_matrix();
        for (int i = 0; i < matrix_array.length; i++) {

            int min_index = i * MAX_ARRAY_SIZE;
            int max_index = min_index + MAX_ARRAY_SIZE;

            if ((min_index <= index) && (index < max_index)) {
                int real_index = index - min_index;
                return matrix_array[i][real_index];
            }
        }
        return null;
    }
    // trivial getting
    public T get2(int index) {
        set_array_to_matrix();
        cur_step = 0;

        for (int i = size() - 1; i >= 0; i--) {
            for (int j = MAX_ARRAY_SIZE - 1; j >= 0; j--) {
                int cur_index = (size() * MAX_ARRAY_SIZE) - 1 - cur_step;
                if (cur_index == index) {
                    return matrix_array[i][j];
                }
                cur_step++;
            }
        }
        return null;
    }

    public void put(T item) {
        if (array_size == array.length) {
            resize_matrix_array();
            matrix_array[size()] = array;
            matrix_size++;
            array = createArray(MAX_ARRAY_SIZE);
            array_size = 0;
        }
        array[array_size] = item;
        array_size++;
    }

    @Override
    public void add(int index, T item) {
        set_array_to_matrix();
        cur_step = 0;

        for (int i = size() - 1; i >= 0; i--) {
            for (int j = MAX_ARRAY_SIZE - 1; j >= 0; j--) {
                int cur_index = (size() * MAX_ARRAY_SIZE) -1 - cur_step;
                if (cur_index == index) {
                    matrix_array[i][j] = item;
                    return;
                }
                if (j != 0) {
                    matrix_array[i][j] =  matrix_array[i][j - 1];
                }
                cur_step++;
            }
            if (i != 0)
                matrix_array[i][0] = matrix_array[i - 1][MAX_ARRAY_SIZE - 1];
        }
    }

    @Override
    public T remove(int index) {
        set_array_to_matrix();
        cur_step = 0;
        T prev_value = null;
        for (int i = size() - 1; i >= 0; i--) {
            for (int j = MAX_ARRAY_SIZE - 1; j >= 0; j--) {

                int cur_index = (size() * MAX_ARRAY_SIZE) - cur_step;
                if (cur_index == index)
                    return prev_value;

                T curr_value = matrix_array[i][j];
                matrix_array[i][j] = prev_value;
                prev_value = curr_value;
                cur_step++;
            }

        }
        return null;
    }

    private void resize_matrix_array() {
        T[][] newArray = (T[][]) new Object[(size() + 1)][];
        for (int i = 0; i < size(); i++)
            newArray[i] = matrix_array[i];
        matrix_array = newArray;
    }

    private void set_array_to_matrix() {
        if (matrix_array[size() - 1] != array) {
            resize_matrix_array();
            matrix_array[size()] = array;
            matrix_size++;
        }
    }

    private T[] createArray(int max_size) {
        return (T[]) new Object[max_size];
    }

}
