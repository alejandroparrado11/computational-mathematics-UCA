#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VECTOR_SIZE 10

void fill_random_vector(int v[], int n);
int verify_descending_order(int v[], int n);

int main() {
    srand((unsigned int)time(NULL));
    int vector[VECTOR_SIZE];

    fill_random_vector(vector, VECTOR_SIZE);

    printf("Generated Random Vector:\n");
    for (int i = 0; i < VECTOR_SIZE; i++) {
        printf("%d ", vector[i]);
    }
    printf("\n");

    if (verify_descending_order(vector, VECTOR_SIZE - 1)) {
        printf("Analysis Result: The vector is strictly ordered in descending magnitude.\n");
    } else {
        printf("Analysis Result: The vector is unsorted or out of sequence.\n");
    }

    return 0;
}

void fill_random_vector(int v[], int n) {
    for (int i = 0; i < n; i++) {
        // Limit random bounds for better visibility
        v[i] = rand() % 100;
    }
}

int verify_descending_order(int v[], int n) {
    if (n <= 0) {
        return 1;
    }
    if (v[n] > v[n - 1]) {
        return 0;
    }
    return verify_descending_order(v, n - 1);
}
