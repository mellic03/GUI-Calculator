int factorial(int x) {
    if (x <= 1) {
        return (1);
    }
    else {
        return (x * factorial(x-1));
    }
}


float exponent(float x) {

    float eulersNumber = 2.71828;
    float workingVal = 1;

    for (int i = 0; i < x; i++) {
        workingVal *= eulersNumber;
    }

    return workingVal;
}