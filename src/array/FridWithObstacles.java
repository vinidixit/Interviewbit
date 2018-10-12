package array;
import java.util.*;

public class FridWithObstacles {
	public static void main(String args[])
	{
		FridWithObstacles obj = new FridWithObstacles();
		int[] arr[] = {
		  {0,0,0},
		  {0,1,0},
		  {0,0,0}
		};
		
		List<List<Integer>> a = new ArrayList<List<Integer>>();
		for(int i = 0; i < 3; ++i)
		{
			ArrayList<Integer> l = new ArrayList<Integer>();
			l.add(arr[i][0]);l.add(arr[i][1]);l.add(arr[i][2]);
			a.add(l);
		}
		
		System.out.println(a);
		obj.uniquePathsWithObstacles(a);
		
		
	}
	
	public int uniquePathsWithObstacles(List<List<Integer>> a) {
	    
	    int ROW = a.size();
	    if(ROW == 0 || a.get(0).get(0)==1)
	        return 0;
	        
	    int COL = a.get(0).size();
	    
	    int wayMatrix[][] = new int[ROW][COL];
	   
	    for(int i = 0;i < ROW; ++i)
	    {
	        if(a.get(i).get(0) == 0)
	            wayMatrix[i][0] = 1;
	        else
	            wayMatrix[i][0] = 0;
	    }
	        
	    for(int j =1; j < COL; ++j)
	    {
	        if(a.get(0).get(j)==0)
	            wayMatrix[0][j] = 1;
	        else
	            wayMatrix[0][j] = 0;
	    }
	   
	   for(int i = 1;i<ROW;++i)
	   {
	       for(int j = 1;j < COL; ++j)
	       {
	           if(a.get(i).get(j)==0)
	            wayMatrix[i][j] = wayMatrix[i][j-1]+ wayMatrix[i-1][j];
	        else
	            wayMatrix[i][j] = 0;
	       }
	   }
	   
	   for( int i =0; i <ROW; ++i)
	   {
		   for(int j = 0; j < COL; ++j)
			   System.out.print(wayMatrix[i][j] + " ");
		   System.out.println();
	   }
		   
	   return wayMatrix[ROW-1][COL-1];
	}
}
