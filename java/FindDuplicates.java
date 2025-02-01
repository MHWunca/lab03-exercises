import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FindDuplicates {

    private static final boolean DEBUG = false;

    public static List<Integer> findDuplicatesNestedLoops(List<Integer> l) {
        List<Integer> s = new ArrayList<Integer>(l);
        List<Integer> ds = new ArrayList<Integer>();
        for (int i = 0; i < s.size()-1; i++) for (int j = i+1; j < s.size(); j++) {
            if (DEBUG) System.out.println(i+" "+j+"    "+s+" "+ds);
            if (s.get(i) == s.get(j)) {
                if (DEBUG) System.out.println("Duplicate found!");
                ds.add(s.remove(j));
                for (int ii = j; ii < s.size(); ii++) {
                    if (DEBUG) System.out.println(i+" "+j+" "+ii+"  "+s+" "+ds);
                    while (ds.get(ds.size()-1) == s.get(ii)) {
                        if (DEBUG) System.out.println("Another duplicate found!");
                        s.remove(ii);
                        if (!(ii < s.size())) break;
                    }
                }
                break;
            }
        }
        return ds;
    }

    public static List<Integer> findAllDuplicatesNestedLoops(List<Integer> l) {
        List<Integer> s = new ArrayList<Integer>(l);
        List<Integer> d = new ArrayList<Integer>();
        for (int i = 0; i < s.size()-1; i++) for (int j = i+1; j < s.size(); j++) {
            if (DEBUG) System.out.println(i+" "+j+"    "+s+" "+d);
            boolean b = false;
            while (s.get(i) == s.get(j)) {
                if (DEBUG) System.out.println("Duplicate found!");
                d.add(s.remove(j));
                if (j == s.size()) break;
            }
        }
        return d;
    }

    public static void main(String[] args) {
        // some test strings:
        List<Integer> sample1 = new ArrayList<Integer>(Arrays.asList(3, 7, 5, 6, 7, 4, 8, 5, 7, 66));
        List<Integer> sample2 = new ArrayList<Integer>(Arrays.asList(3, 5, 6, 4, 4, 5, 66, 6, 7, 6));
        List<Integer> sample3 = new ArrayList<Integer>(Arrays.asList(3, 0, 5, 1, 0));
        List<Integer> sample4 = new ArrayList<Integer>(Arrays.asList(3));
        System.out.println("Sample 1: " + findDuplicatesNestedLoops(sample1));
        System.out.println("Sample 2: " + findDuplicatesNestedLoops(sample2));
        System.out.println("Sample 3: " + findDuplicatesNestedLoops(sample3));
        System.out.println("Sample 4: " + findDuplicatesNestedLoops(sample4));
        /*
        System.out.println("Sample 1: " + findAllDuplicatesNestedLoops(sample1));
        System.out.println("Sample 2: " + findAllDuplicatesNestedLoops(sample2));
        System.out.println("Sample 3: " + findAllDuplicatesNestedLoops(sample3));
        System.out.println("Sample 4: " + findAllDuplicatesNestedLoops(sample4));
        */
    }

}