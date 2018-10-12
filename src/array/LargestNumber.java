package array;

import java.util.Arrays;
import java.util.*;

class Node implements Comparable<Node>
{
	int number;
	Node(int num)
	{
		this.number = num;
	}
	
	@Override
	public int compareTo(Node o) {
		String numStr1 = this.number + ""+ o.number;
		String numStr2 = o.number + "" + this.number;
		
		return numStr2.compareTo(numStr1);
	}
}

public class LargestNumber {

public static String largestNumber(final List<Integer> a) {
	    
	    int n = a.size();
	    
	    Node[] nums = new Node[n];
		
		for(int i = 0; i < n; ++i)
			nums[i] = new Node(a.get(i));
		
		Arrays.sort(nums);
		
		StringBuffer res = new StringBuffer();
		
		int start = 0;
		if(nums[start].number==0)
		{
		    while(start < n && nums[start].number == 0)start++;
		    start--;
		}
		
		for(;start < n; ++start)
			res.append(nums[start].number);
		
		return res.toString();
	}

	public static void main(String[] args) {
		
		int arr[] = {0, 0, 0, 0, 0 };
		List<Integer> l = new ArrayList<Integer>();
		
		for(int num : arr)
			l.add(num);
		
		System.out.println(LargestNumber.largestNumber(l));

	}

}
