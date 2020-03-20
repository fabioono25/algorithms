/**
 * 5– Given a chessboard, how would you find whether the king is threatened by the queen? 
 * Consider that you’ll have coordinates for the king (Kx, and Ky) and the queen (Qx and Qy). 
 */

function checkMate(kX, kY, qX, qY) {

    /*in this case, I have three scenarios to consider
    1 - queen is in the same row as the king
    2 - queen is in the same column as the king
    2 - queen is in the same diagonal position as the king
    */

    //first, it's possible to verify if the arguments and positions are correct
    if (!validInput(kX, kY, qX, qY)) {
        throw "Some invalid parameter";
    }

    return (kX === qX || kY === qY || Math.abs(kX - qX) === Math.abs(kY - qY));
}

function validInput(kX, kY, qX, qY) {

    if (kX === qX && kY === qY) return false; //same position

    if (!Number.isInteger(kX) || !Number.isInteger(kY) || !Number.isInteger(qX) || !Number.isInteger(qY)) return false; //invalid numeric

    if (kX > 7 || kX < 0 || kY > 7 || kY < 0 || qX > 7 || qX < 0 || qY > 7 || qY < 0) return false; //invalid boundaries

    return true;
}

console.log(checkMate(1,1, 3,1)); //same column
console.log(checkMate(1,1, 1,4)); //same row
console.log(checkMate(3,2, 6,5)); //same diagonal
console.log(checkMate(4,1, 2,3)); //king is dead
console.log(checkMate(4,1, 2,5)); //king is safe!
