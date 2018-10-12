package array;

import java.util.ArrayList;

public class AntiDiagonals {

	ArrayList<ArrayList<Integer>> matrix;
    int ROW = 0, COL=0;
    
    ArrayList<Integer> printReverseDiagonal(int curRow, int curCol)
    {
    	ArrayList<Integer> result = new ArrayList<Integer>();
        
        for(;curRow < ROW && curCol >= 0;++curRow,--curCol)
        {
            result.add(matrix.get(curRow).get(curCol));
        }
        return result;
    }
    
	public ArrayList<ArrayList<Integer>> diagonal(ArrayList<ArrayList<Integer>> a) {
	
	    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
	    
	    ROW = a.size();
	    if(ROW == 0)
	        return result;
	    
	    matrix = a;
	    
	    COL = a.get(0).size();
	    
	    for(int j = 0; j < COL; ++j)
	    {
	        result.add(printReverseDiagonal(0, j));
	    }
	    for(int i = 1; i < ROW; ++i)
	    {
	        result.add(printReverseDiagonal(i, COL-1));
	    }
	    
	    return result;
	}
	public static void main(String[] args) {
		ArrayList<ArrayList<Integer>> matrix = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> row = new ArrayList<Integer>();
		
		for(int i = 1; i <= 9; ++i)
		{
			row.add(i);
			
			if(i%3 == 0)
			{
				ArrayList<Integer> temp = new ArrayList<Integer>();
				temp.addAll(row);
				matrix.add(temp);
				row.clear();
			}
		}
		System.out.println(matrix);
		
		AntiDiagonals obj = new AntiDiagonals();
		System.out.println(obj.diagonal(matrix));
	}

}
