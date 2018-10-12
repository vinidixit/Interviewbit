package array;
import java.util.*;

public class Flip {

public static ArrayList<Integer> flip(String A) {
        
        int n = A.length();
        
        int cur_A = 0;int cur_B = 0; int cur_diff = 0;
        int max_L = -1, max_R = -1, max_diff = 0;
        int L = -1;
        ArrayList<Integer> res = new ArrayList<Integer>();
        
        for(int i = 0; i < n; ++i)
        {
        	if(L == -1)
                L = i+1;
            
            if(A.charAt(i)=='0')
            {
                cur_A++;
            }
            else 
            {
                cur_B++;
            }
                
            if(cur_A-cur_B < 0)
            {
                cur_A = 0; cur_B = 0;
                L=-1;
            }
            
            cur_diff = cur_A-cur_B;
            if(cur_diff > max_diff)
            {
                max_diff = cur_diff; 
                max_L = L;
                max_R = i+1;
            }
        }
        
        if(max_L!=-1 && max_L!=-1)
        {    
            res.add(max_L);
            res.add(max_R);
        }
        
        System.out.println(max_L + " " + max_L);
        return res;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String A = "011";
		
		System.out.println(Flip.flip(A));
	}

}
