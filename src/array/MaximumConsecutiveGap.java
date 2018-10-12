package array;

import java.util.*;

public class MaximumConsecutiveGap {

	public static int maximumGap(final List<Integer> a) {
	    
		int maxGap = 0;
	    int n = a.size();
	    
	    if(n <= 2)
	        return maxGap;
	        
	    int max = Collections.max(a);
	    int min = Collections.min(a);
	    
	    int gap = (max-min)/(n-1);
	    
	    Map<Integer,ArrayList<Integer>> buckets = new HashMap<Integer,ArrayList<Integer>>();
	    
	    for(int i = 0; i < n; ++i)
	    {
	    	int bucketInd = (a.get(i)-min)/gap;
	    
	    	if(buckets.get(bucketInd) == null)
	    		buckets.put(bucketInd, new ArrayList<Integer>());
	    	
	    	ArrayList<Integer> indices = buckets.get(bucketInd);
	    	indices.add(a.get(i));
	    }
	    
	    System.out.println(buckets);
	    
	    int prevInd = -1;
	    for(int i = 0; i < n; ++i)
	    {
	    	if(buckets.get(i) != null)
	    	{
	    		if(prevInd==-1)
	    		{
	    			prevInd = i;
	    			continue;
	    		}
	    		
	    		List<Integer> curIndices = buckets.get(i);
	    		int prevMin = Collections.min(buckets.get(prevInd));
	    		int curMax = Collections.max(curIndices);
	    		maxGap = Math.max(maxGap, curMax-prevMin);
	    		
	    		prevInd = i;
	    	}
	    }
	   
	    return maxGap;
	}

	public static void main(String[] args) {
		
		int arr[] = {10, 1, 5};
		List<Integer> a = new ArrayList<Integer>();
		for(int num : arr)
			a.add(num);
		
		System.out.println(MaximumConsecutiveGap.maximumGap(a));

	}

}
