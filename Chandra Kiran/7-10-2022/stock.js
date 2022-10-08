var maxProfit = function (prices) {
    let currentPrice = Infinity, profit = 0, pastProfit = 0;

    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < currentPrice) {
            currentPrice = prices[i];
        }
        profit = prices[i] - currentPrice;
        if (pastProfit < profit)
            pastProfit = profit;
    }
    return pastProfit;
};