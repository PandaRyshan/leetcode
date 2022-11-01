package algorithm;

public class ArrayStringsAreEqual {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {

        if (String.join("", word1).equals(String.join("", word2))) {
            return true;
        } else {
            return false;
        }
    }
    
}
