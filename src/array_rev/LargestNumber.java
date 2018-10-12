package array_rev;

import java.util.Arrays;
import java.util.Comparator;

public class LargestNumber {

	public String largestNumber(final int[] A) {
		String A_str[] = new String[A.length];
		for(int i=0;i<A.length;++i)
			A_str[i]=A[i]+"";
		
        Arrays.sort(A_str, new Comparator<String>(){
           @Override
           public int compare(String num1_str,String num2_str)
           {
               int n1=num1_str.length();
               int n2=num2_str.length();
               int i=0,j=0;
               while(i<n1 && j < n2 && num1_str.charAt(i)==num2_str.charAt(j))
               {
                   ++i;
                   ++j;
               }
               if(i==n1 && j==n2)
                 return 1; // both are equal, send anything
                
                if(i==n1) // compare next digit of second number
                {	if((int)num2_str.charAt(j)==(int)num1_str.charAt(0))
                		return (int)num2_str.charAt(j)-(int)num1_str.charAt(i-1);
                				
                    return (int)num2_str.charAt(j)-(int)num1_str.charAt(0);
                }
                if(j==n2) // compare next digit of first number
                    return (int)num2_str.charAt(0)-(int)num1_str.charAt(i);
                
                return (int)num2_str.charAt(j)-(int)num1_str.charAt(i);
           }
        });
        
        int i = 0, n = A_str.length;
        while(i<n && A_str[i].equals("0"))
            ++i;
        if(i == n)
            return "0";
        
        StringBuffer sb= new StringBuffer();    
        for(; i<n; ++i)
            sb.append(A_str[i]+" ");
        return sb.toString();
    }
	
	
	public static void main(String[] args) {
		
		LargestNumber obj =new LargestNumber();
		int A[] = {170, 480, 735, 896, 634, 844, 1, 610, 446, 591, 935, 802, 383, 8, 443, 247, 124, 461, 317, 457, 48, 886, 420, 473, 973, 464, 203, 288, 785, 703, 935, 7, 987, 48, 692, 633, 597, 857, 139, 733, 692, 68, 434, 587, 489, 517, 305, 432, 577, 335, 586, 34, 659, 491, 310, 857, 256, 856, 257, 877, 209, 979, 653, 646, 2, 65, 858, 779, 372, 116, 404, 268, 364, 351, 866, 824, 947, 960, 91, 691, 492, 312, 609, 915, 579, 476, 248, 192 };
			//987 979 973 960 947 935 935 91 915 896 8 886 877 866 858 857 857 856 844 824 802 785 779 7 735 733 703 692 692 691 686 596565364663463361060959759158758657957751749249148948484804764734644614574464434344324204043833723643513433531731231030528826825725624824722092031921701391241161
		
				
				//{ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 };
 
		//991 974 940 930 905 895 877 872 868 825 799 798 791 782 780 772 735 709 686 686 678 675 6 646 533
		// 502 470 409 395 366 363 357 337 298 29 27126124019124113
		
		
			//{472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412};
		System.out.println(obj.largestNumber(A));
		
		//964852722676663635 485472 4 412368319
	}

}
