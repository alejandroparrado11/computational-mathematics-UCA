#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[20];
    char lastname[30];
    float cs_grade;
    float physics_grade;
    float stats_grade;
} Student;

int display_menu();
void initialize_student(Student *s);
void modify_student(Student *s);
float get_highest_grade(const Student *s);

int main() {
    int choice;
    Student active_student;
    int is_initialized = 0;

    do {
        choice = display_menu();
        switch (choice) {
            case 1:
                initialize_student(&active_student);
                is_initialized = 1;
                break;
            case 2:
                if (is_initialized) {
                    modify_student(&active_student);
                } else {
                    printf("Error: Student record must be initialized first.\n");
                }
                break;
            case 3:
                if (is_initialized) {
                    printf("Highest registered grade: %.2f\n", get_highest_grade(&active_student));
                } else {
                    printf("Error: No data available.\n");
                }
                break;
            case 4:
                printf("Exiting system.\n");
                break;
            default:
                printf("Invalid selection.\n");
        }
    } while (choice != 4);

    return 0;
}

int display_menu() {
    int option;
    printf("\n--- STUDENT MANAGEMENT SYSTEM ---\n");
    printf("1. Initialize Record\n");
    printf("2. Modify Parameters\n");
    printf("3. Compute Highest Grade\n");
    printf("4. Exit\n");
    printf("Select option: ");
    if (scanf("%d", &option) != 1) {
        return 4; // Safely exit on bad inputs
    }
    return option;
}

void initialize_student(Student *s) {
    printf("Enter First Name: ");
    scanf("%19s", s->name);
    printf("Enter Last Name: ");
    scanf("%29s", s->lastname);
    printf("Enter Computer Science Grade: ");
    scanf("%f", &s->cs_grade);
    printf("Enter Physics Grade: ");
    scanf("%f", &s->physics_grade);
    printf("Enter Statistics Grade: ");
    scanf("%f", &s->stats_grade);
}

void modify_student(Student *s) {
    int target;
    printf("Modify Field: 1.Name | 2.Last Name | 3.CS Grade | 4.Physics Grade | 5.Stats Grade: ");
    scanf("%d", &target);

    switch (target) {
        case 1: printf("New Name: "); scanf("%19s", s->name); break;
        case 2: printf("New Last Name: "); scanf("%29s", s->lastname); break;
        case 3: printf("New CS Grade: "); scanf("%f", &s->cs_grade); break;
        case 4: printf("New Physics Grade: "); scanf("%f", &s->physics_grade); break;
        case 5: printf("New Stats Grade: "); scanf("%f", &s->stats_grade); break;
        default: printf("Modification aborted.\n");
    }
}

float get_highest_grade(const Student *s) {
    float max = s->cs_grade;
    if (s->physics_grade > max) max = s->physics_grade;
    if (s->stats_grade > max) max = s->stats_grade;
    return max;
}
