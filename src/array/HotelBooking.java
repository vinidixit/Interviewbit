package array;

import java.util.Arrays;

class Time implements Comparable<Time>
{
    int s, e;
    Time(int s, int e)
    {
        this.s = s;this.e = e;
    }
    
    @Override
	public int compareTo(Time o) {
	
	    return this.s-o.s;
	}
}

public class HotelBooking {

	public static void main(String[] args) {
		
		int s[] = {3, 1, 5};
		int e[] = {2,6,8};
		
		Time time[] = new Time[s.length];
		
		for(int i=0;i<s.length;++i)
			time[i] = new Time(s[i], e[i]);
		
		Arrays.sort(time);
		
		for(Time t : time)
			System.out.println(t.s + " " + t.e);
			

	}

}
