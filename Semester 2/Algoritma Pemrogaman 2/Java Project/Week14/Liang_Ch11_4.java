package 
Week14;

import java.util.ArrayList;

public class Liang_Ch11_4 {
    public static Integer max ( ArrayList < Integer > list ) {
        if ( list == null || list . size () == 0) return null ;
        Integer max = list . get (0) ;
        for ( int i = 1; i < list . size () ; i ++) {
        if ( list . get ( i ) > max ) max = list . get ( i );
        }
        return max;
    }
}
