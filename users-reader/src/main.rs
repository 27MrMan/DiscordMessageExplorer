use std::time::{SystemTime};

fn main() {
    let mut rdr = csv::Reader::from_path("data_copy.csv").expect("wher file");
    //let mut limit = 150;
    //let mut print:bool = true;
    //let mut lentest = 0;
    let mut users: Vec<String> = Vec::new();
    let mut usercount: Vec<u64> = Vec::new();

    let starttime = SystemTime::now();
    /* 
    for i in rdr.records() {
        let line = i.expect("wher record");
        if print{
        println!("{:?}", line);
        println!(" ");}

        limit -=1;
        lentest += 1;

        if limit == 0 {
            print = false;
        }


    } */

    for i in rdr.records() {
        let line = i.expect("wher record");
        let cuser = &line[1].to_string();
        if !users.contains(cuser) {
            users.push(String::from(cuser));
            usercount.push(0);
        }
        for i in users.iter() {
            if i == cuser {
                let index = users.iter().position(|x| x == cuser).unwrap();
                usercount[index] += 1;
            }
        }

    }
    //println!("Total records processed: {}", lentest);
    println!("{:?}", users);
    println!("{:?}", usercount);
    println!("Time Elapsed: {:?}", starttime.elapsed());
}
