with entry{
    age: int = 30;

    if age <= 12{
        print("Child");
    } elif age <= 19 {
        print("Teenager");
    } elif age <= 64 {
        print("Adult");
    } else {
        print("Senior");
    }
}