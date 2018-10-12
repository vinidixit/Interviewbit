package array;
import java.util.*;

public class MaxNonNegativeArray {

	public static ArrayList<Integer> maxset(ArrayList<Integer> a) {
	    
	    ArrayList<Integer> res = new ArrayList<Integer>();
	    
	    int n = a.size();
	    if(n == 0)
	        return res;
	        
	    int L = -1, R = -1;
	    int max_L = -1, max_R = -1;
	    
	    long cur_sum = 0, max_sum = -1;
	    
	    for(int i = 0; i < n; ++i)
	    {
	        if(a.get(i) >= 0)
	        {
	           if(L == -1)
	                L = i;
	            
	            R = i;
	            cur_sum += a.get(i); 
	            
	            if((cur_sum > max_sum) || (cur_sum == max_sum && R-L > max_R-max_L))
		        {
		            max_L = L; max_R = R;
		            max_sum = cur_sum;
		        }
	        }
	        else
	        {
	            L = -1;
	            cur_sum = 0;
	        }
	        
	       
	    }
	    System.out.println(max_L + " " + max_R);
	    
	    for(int i = max_L; (i <= max_R)&&(max_R!=-1); ++i)
	    {
	        res.add(a.get(i));
	    }
	    return res;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int A[]  = { 1967513926, 1540383426, -1303455736, -521595368 };
		ArrayList<Integer> l = new ArrayList<Integer>();
		//System.out.println(A[1]+A[0]);
		for(int num : A)
		{
			l.add(num);
		}
		
		System.out.println(MaxNonNegativeArray.maxset(l));
	}

}
