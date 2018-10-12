package array;

import java.util.ArrayList;
import java.util.Collections;

public class MaximumUnsortedSubarray {

	public static ArrayList<Integer> subUnsort(ArrayList<Integer> A) {
        
        ArrayList<Integer> res = new ArrayList<Integer>();
        
        int n = A.size();
        if(n <= 1)
        {
            res.add(-1);
            return res;
        }
        
        int l = -1, r = -1;
        
        for(int i = 0; i < n-1; ++i)
        {
            if(A.get(i) > A.get(i+1))
            {
                l = i;
                break;
            }
        }
        
        for(int i = n-1; i>=1; --i)
        {
            if(A.get(i) < A.get(i-1))
            {
                r = i;
                break;
            }
        }
        
        if(l != -1 && r != -1)
        {
        	// check boundary elements
        	int subarray_min = Collections.min(A.subList(l, r+1));
        	int subarray_max = Collections.max(A.subList(l, r+1));
        	
        	System.out.println(l + " " + r + " " + subarray_min + " " + subarray_max);
        	while(l-1 >= 0 && A.get(l-1) > subarray_min)
        		l--;

        	while(r+1 < n && A.get(r+1) < subarray_max)
        		r++;

            res.add(l);
            res.add(r);
        }
        else
            res.add(-1);
            
        return res;
        
    }
	public static void main(String[] args) {
	
		int arr[] = { 1, 2, 3, 5, 6, 13, 15, 16, 17, 13, 13, 15, 17, 17, 17, 17, 17, 19, 19};//{1, 3, 2, 4, 5};
		
		ArrayList<Integer> l = new ArrayList<Integer>();
		
		for(int num : arr)
			l.add(num);
		
		System.out.println(MaximumUnsortedSubarray.subUnsort(l));
		
		
	}

}
