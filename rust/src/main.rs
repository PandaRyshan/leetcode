fn print_type<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
}

struct Example {
    number: i32,
}

impl Example {
    fn boo() {
        println!("boo! Example::boo() was called")
    }

    fn answer(&mut self) {
        self.number += 42;
    }

    fn get_number(&self) -> i32 {
        self.number
    }
}

trait Thingy {
    fn do_thingy(&self);
}

impl Thingy for Example {
    fn do_thingy(&self) {
        println!("doing a thing! also, number is {}!", self.number);
    }
}

struct Val {
    val: f64,
}

struct GenVal<T> {
    gen_val: T,
}

impl Val {
    fn value(&self) -> &f64 {
        &self.val
    }
}

struct A;

struct Single(A);

struct SingleGen<T>(T);

trait Bird {
    fn call(&self) -> String;
}

struct Chicken {}

struct Duck {}

impl Bird for Chicken {
    fn call(&self) -> String {
        String::from("cluck cluck")
    }
}

impl Bird for Duck {
    fn call(&self) -> String {
        String::from("quack quack")
    }
}

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

    let _s = Single(A);

    let _char: SingleGen<char> = SingleGen('a');

    let _t = SingleGen(A);
    let _i32 = SingleGen(6);
    let _char = SingleGen('a');

    let chicken = Chicken {};
    let duck = Duck {};
    println!("{}", chicken.call());
    println!("{}", duck.call());
}