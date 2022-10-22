pub fn main() {
    let mut hashtable = std::collections::HashMap::<i32, i32>::new();
    hashtable.insert(0, 7);
    hashtable.insert(1, 9);

    println!("{}", hashtable[&1]);
    println!("{}", &match hashtable.get(&1) {
        Some(val) => {val},
        None => {&1},
    });
    print_type(&hashtable.get(&1));

    let l1 = vec![1, 2, 3];
    let l2 = vec![1, 2, 3];
    println!("{}", l1.eq(&l2));

}

fn print_type<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
}