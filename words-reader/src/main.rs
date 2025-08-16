use std::time::SystemTime;
use std::fs;

fn main() {
    let mut rdr = csv::Reader::from_path("data.csv").expect("wher file");
    let starttime = SystemTime::now();
    let mut inputword = fs::read_to_string("user_text.txt").expect("Failed to read user_text.txt");
    inputword = inputword.trim().to_lowercase();

    let mut countvec: Vec<String> = Vec::new();
    let mut countvecint: Vec<i32> = Vec::new();
    let mut counthelper: Vec<i32> = Vec::new();
    let mut index = 0;

    //println!("Input word: {}", inputword.trim());

    for result in rdr.records() {
        let record = result.expect("wher record");

        //add the users
        if !countvec.contains(&record[1].to_string()){
            countvec.push(record[1].to_string());
            countvecint.push(0);
            counthelper.push(0);
        }

        if record[3].split_whitespace().any(|word| word.to_lowercase() == inputword) {
            index = countvec.iter().position(|x| x == &record[1]).unwrap();
            countvecint[index] += 1;
        }
        index = countvec.iter().position(|x| x == &record[1]).unwrap();
        counthelper[index] += 1;

    }
    println!("{:?}", countvec);
    println!("{:?}", countvecint);
    println!("{:?}", counthelper);

    println!("Time Elapsed: {:?}", starttime.elapsed());
}
