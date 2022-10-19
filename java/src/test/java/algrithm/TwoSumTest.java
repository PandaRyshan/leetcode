package algrithm;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;


public class TwoSumTest {

    @Test
    @DisplayName("Two Array Should Be Equal")
    void testTwoSum() {
        TwoSum twoSum = new TwoSum();

        assertArrayEquals(new int[]{0, 1},
            twoSum.twoSum(new int[]{2, 7, 11, 15}, 9));

        assertArrayEquals(new int[]{3, 4},
            twoSum.twoSum(new int[]{6, 9, 6, 1, 3, 2, 2}, 4));
    }
    
}