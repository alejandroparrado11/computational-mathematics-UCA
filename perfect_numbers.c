#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int check_perfect(int num, int sum);
int calculate_divisors_sum(int num, int divisor, int sum);

int main() {
    srand((unsigned int)time(NULL));

    // Genérate a random target or test a fixed sample
    int number = 6;
    printf("Testing integer: %d\n", number);

    int divisors_sum = calculate_divisors_sum(number, 1, 0);
    int is_perfect = check_perfect(number, divisors_sum);

    if (is_perfect) {
        printf("The number %d IS a perfect number.\n", number);
    } else {
        printf("The number %d IS NOT a perfect number.\n", number);
    }

    return 0;
}

int check_perfect(int num, int sum) {
    return (sum == num) ? 1 : 0;
}

int calculate_divisors_sum(int num, int divisor, int sum) {
    if (divisor > num / 2) {
        return sum;
    }

    if (num % divisor == 0) {
        sum += divisor;
    }

    return calculate_divisors_sum(num, divisor + 1, sum);
}
