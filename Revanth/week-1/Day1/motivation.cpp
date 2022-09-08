#include <iostream>
using namespace std;

int main() {

    int test, n, x;

    cin>>test;
    while(test--){
        std::cin>>n>>x;
        int size[n], rate[n];
        for(int i=0;i<n;i++){
            std::cin>>size[i]>>rate[i];
        }
        int msize = x, mrate = 0;
        for(int i=0;i<n;i++){
            if(size[i]<=msize && rate[i]>mrate){
                    mrate = rate[i];
            }
        }
        std::cout << mrate <<endl;
    }
    return 0;
}