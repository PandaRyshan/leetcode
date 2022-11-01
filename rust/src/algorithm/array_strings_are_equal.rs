#[allow(dead_code)]
pub fn array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
    if word1.join("").eq(&word2.join("")) {
        return true;
    } else {
        return false;
    }
}


#[cfg(test)]
mod test {
    use super::array_strings_are_equal;

//    #[test_case( ["ab", "c"], ["a", "bc"] ; "")]
    use test_case::test_case;

    #[test_case(Vec::from(["ab".to_string(), "c".to_string()]), Vec::from(["c".to_string(), "ab".to_string()]) => false ; "ne")]
    #[test_case(Vec::from(["ab".to_string(), "c".to_string()]), Vec::from(["a".to_string(), "bc".to_string()]) => true; "eq")]
    fn test_array_strings_are_equal(word1: Vec<String>, word2: Vec<String>) -> bool {
        //assert_eq!(true, array_strings_are_equal(word1, word2));
        array_strings_are_equal(word1, word2)
    }
}