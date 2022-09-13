int minimumOperations(int * nums, int numsSize){
    int i, j, count = 0, flag = 0, signal = 1;
    for (i = 0; i < numsSize; i++) {
        signal = 1;
        for (j = 0; j <= i; j++) {
            if (nums[i] == 0) {
                signal = 0;
                break;
            }
            if (nums[i] == nums[j] && i != j) {
                signal = 0;
                break;
            }

        }
        if (signal)
            count++;
    }

    return count;
}