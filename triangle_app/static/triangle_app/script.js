// function to check if the inputs are valid integer values
function checkParameter(a, b, c) {
    // check condition
    if (Number.isInteger(a) && Number.isInteger(b) && Number.isInteger(c)){
        return true
    }
    return false
}
     
// function to check if any of the inputs are zero
function checkZero(a, b, c) {
    // check condition
    if ((a === 0) || (b === 0) || (c === 0)){
        return true
    }
    return false
}

// function to check if any of the inputs are negative
function checkNegative(a, b, c) {
    // check condition
    if ((a < 0) || (b < 0) || (c < 0)){
        return true
    }
    return false
}
     
// function to check if the three sides form a triangle or not
function checkValidTriangle(a, b, c) {
    // check condition
    if ((a + b > c) && (a + c > b) && (b + c > a)) {
        return true
    }
    return false
}

function isScalene(a, b, c) {
    if ((a !== b) && (b !== c) && (a !== c)) {
        return true
    }
    return false
}

function isIsosceles(a, b, c) {
    if ((a === b) || (b === c) || (a === c)) {
        return true
    }
    return false
}

function isEquilateral(a, b, c) {
    if ((a === b) && (b === c) && (a === c)){
        return true
    }
    return false
}

/*
A scalene triangle is one where no two sides are equal.
An isosceles triangle has two equal sides.
An equilateral triangle has three sides of equal length.
*/

function myFunction() {
    var a = Number(document.querySelector("#id_a").value);
    var b = Number(document.querySelector("#id_b").value);
    var c = Number(document.querySelector("#id_c").value);
    if (a && b && c) {
        if (checkParameter(a, b, c)) {
            if (!checkZero(a, b, c)) {
                if (!checkNegative(a, b, c)) {
                    if (checkValidTriangle(a, b, c)){
                        if (isEquilateral(a, b, c)){
                            document.getElementById('message').innerHTML = "An equilateral triangle";
                        } else if (isIsosceles(a, b, c)) {
                            document.getElementById('message').innerHTML = "An isosceles triangle";
                        } else if (isScalene(a, b, c)) {
                            document.getElementById('message').innerHTML = "A scalene triangle";
                        }
                    } else {
                        document.getElementById('message').innerHTML = "Error: The sum of the lengths of any two sides of a triangle has to be greater than the length of the third side.";
                    }
                } else {
                    document.getElementById('message').innerHTML = "Error: Negative integer is invalid";
                }
            } else {
                document.getElementById('message').innerHTML = "Error: 0 is not a valid length";
            }
        } else {
            document.getElementById('message').innerHTML = "Error: Please enter integer value";
        }
    } else {
        document.getElementById('message').innerHTML = "";
    }
}
