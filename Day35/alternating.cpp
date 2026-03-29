int countDigits(int n) {
            if (n == 0) return 1;
                return log10(n) + 1;
            }
class Solution {
public:
    int alternateDigitSum(int n) {
        int temp=n;
        int ans=0;
        
        int counter=countDigits(n);
        while(temp){
            int digit=temp%10;
            if(counter%2==0){
                ans+=digit;
                
            }
            else{
                digit=digit*-1;
                ans+=digit;
                
            }
            temp=temp/10;
            counter--;
        }
    return ans*-1;
    }
};
