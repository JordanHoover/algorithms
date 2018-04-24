// return nth fibonacci number
let fib = n => {
    if(n === 0) return 0;
    if(n === 1) return 1;
    else return fib(n -1) + fib(n - 2);
}

//console.log(fib(3));

// print list of fibonacci numbers from 0 to nth fibonacci number
// * 1 is considered 1st fibonacci number
let printFib = n => {
    for( i=1; i <=n; i++){
        console.log(fib(i));
    }
}
//printFib(6);


// memoize the program to improve runtime to O(n)
let print_fib_memo = n => {
    let memo = new Array(n+1);
    for(let i=1; i <= n; i++){
        console.log(fib_memo(i, memo));
    }
}

let fib_memo = (n, memo) => {
    if(n <= 0) return 0;
    if(n === 1) return 1;
    if(! memo[n]) {
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo);
    }
    return memo[n];
}

print_fib_memo(6); // outputs first 6 fibonacci numbers