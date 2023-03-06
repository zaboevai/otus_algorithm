import java.util.Random;

public class Main {
    static int put_total = 1000;
    static int get_total = put_total;
    static int to_index = put_total / 2;
    static int value = 999;

    public static void main(String[] args) {
        IArray<Integer> single = new SingleArray<>();
        IArray<Integer> vector = new VectorArray<>();
        IArray<Integer> factor = new FactorArray<>();
        IArray<Integer> matrix = new MatrixArray<>();


        testPut(single, put_total);
        testGet(single, get_total);
        testAddByIndex(single, to_index, value );
        testRemoveByIndex(single, to_index);
        System.out.println("----");

        testPut(vector, put_total);
        testGet(vector, get_total);
        testAddByIndex(vector, to_index, value );
        testRemoveByIndex(vector, to_index);
        System.out.println("----");

        testPut(factor, put_total);
        testGet(factor, get_total);
        testAddByIndex(factor, to_index, value );
        testRemoveByIndex(factor, to_index);
        System.out.println("----");

        testPut(matrix, put_total);
        testGet(matrix, get_total);
        testAddByIndex(matrix,  to_index, value );
        testRemoveByIndex(matrix,  to_index );
        System.out.println("----");
    }

    public static void testAddByIndex(IArray<Integer> array, int index, int value) {
        long start = System.currentTimeMillis();
        array.add(index, value);
        System.out.println(array.getClass().getName() + " testPutByIndex: " + index + "=" + value + " " + (System.currentTimeMillis() - start));

    }
    public static void testRemoveByIndex(IArray<Integer> array, int index) {
        long start = System.currentTimeMillis();
        int result = array.remove(index);
        System.out.println(array.getClass().getName() + " testDelByIndex: " + index + " " + (System.currentTimeMillis() - start));

    }
    public static void testPut(IArray<Integer> array, int total) {
        long start = System.currentTimeMillis();
        for (int j = 0; j < total; j++)
            array.put(j);
        System.out.println(array.getClass().getName() + " TestPut: " + total + " " + (System.currentTimeMillis() - start));
    }

    public static void testGet(IArray<Integer> array, int total) {
        Random rn = new Random();
        long start = System.currentTimeMillis();
        for (int j = 0; j < total; j++) {
            int next_index = rn.nextInt(put_total);
            Integer value = array.get(next_index);
        }

        System.out.println(array.getClass().getName() + " TestGet: " + total + " " + (System.currentTimeMillis() - start));
    }
}