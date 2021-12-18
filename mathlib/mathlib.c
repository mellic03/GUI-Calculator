int factorial(int x) {
    if (x <= 1) {
        return (1);
    }
    else {
        return (x * factorial(x-1));
    }
}

float getEuler() {

    float eulersNum = 0;

    for (int i = 0; i < 20; i++) {
        eulersNum += (float)1 / (float)factorial(i);
    }

    return eulersNum;
}

float exponent(float x) {

    float eulersNumber = 2.71828;
    float workingVal = 1;

    for (int i = 0; i < x; i++) {
        workingVal *= eulersNumber;
    }

    return workingVal;
}