package array;
import java.util.*;

public class LargestRectangle {

	public static int largestRectangleArea(ArrayList<Integer> a) {
	    int n = a.size();    
	    if(n==0)
	        return 0;
	   
	    int maxArea = 0;
	    Stack<Integer> st = new Stack<Integer>();
	    
	    for(int i = 0; i < n; ++i)
	    {
	        if(st.isEmpty())
	        	st.push(i);
	        else if(a.get(st.peek()) <= a.get(i))
	        	st.push(i);
	        else 
	        {
	        	int rightInd = st.peek();
	        	while(!st.isEmpty() && a.get(i)<a.get(st.peek()))
	        	{
	        		int curInd = st.pop();
	        		int leftInd = st.isEmpty()?0:st.peek();
	        		int curArea = a.get(curInd)*(rightInd-leftInd);
	        		maxArea = Math.max(maxArea, curArea);
	        		
	        	}
	        	st.push(i);
	        }
	    }
	    
	    if(!st.isEmpty())
	    {
	    	int rightInd = st.peek();
	    	
	    	while(!st.isEmpty())
		    {
		    	int curInd = st.pop();
		    	int leftInd = st.isEmpty()?0:st.peek();
		    	int curArea = a.get(curInd)*(rightInd-leftInd);
		    	maxArea = Math.max(maxArea, curArea);
		    }
	    }
	    
	    return maxArea;
	}
	
	public static void main(String[] args) {
		
		ArrayList<Integer> a = new ArrayList<Integer>();
		//[2,1,5,6,2,3]
		a.add(2);a.add(1);a.add(5);a.add(6);a.add(2);a.add(3);
		System.out.println(LargestRectangle.largestRectangleArea(a));
	}

}
