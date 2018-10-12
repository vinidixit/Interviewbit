package array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Number implements Comparable<Number>
{
    int num, ind;
    Number(int num, int ind)
    {
        this.num = num;
        this.ind = ind;
    }
    
    @Override
    public int compareTo(Number o)
    {
        return this.num-o.num;
    }
}

public class MaximumGap {
	// DO NOT MODIFY THE LIST
	public static int maximumGap(final List<Integer> a) {
	    
	    int n = a.size();
	    Number nums[] = new Number[n];
	    
	    for(int i = 0; i < n; ++i)
	        nums[i] = new Number(a.get(i), i);
	    
	    Arrays.sort(nums);
	    
	    // suffix array for max index
	    int[] maxIndexes = new int[n];
	    int maxIndex = Integer.MIN_VALUE;
	    
	    for(int i = n-1;i >=0; --i)
	    {
	        maxIndex = Math.max(maxIndex, nums[i].ind);
	        maxIndexes[i] = maxIndex;
	    }
	    
	    int maxGap = 0;
	    for(int i = 0;i < n; ++i)
	    {
	        if(maxIndexes[i] != nums[i].ind)
	        {
	            maxGap = Math.max(maxGap, maxIndexes[i]-nums[i].ind);
	        }
	    }
	    
	    // bruteforce
	    /*for(int l = 0; l < n-1; ++l)
	    {
	        for(int r = n-1; r > l; --r)
	        {
	            if(a.get(l) <= a.get(r))
	            {
	                max_gap = Math.max(max_gap, r-l);
	                break;
	            }
	        }
	    }*/
	    return maxGap;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int A[] = {3 ,5, 4, 2};
		
		ArrayList<Integer> l = new ArrayList<Integer>();
		for(int n : A)
			l.add(n);
		
		System.out.println(l.size());
		System.out.println(MaximumGap.maximumGap(l));
	}

}

