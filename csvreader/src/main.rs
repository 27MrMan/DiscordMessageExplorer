use std::time::{SystemTime};

fn main() {
    let mut rdr = csv::Reader::from_path("data_copy.csv").expect("wher file");
    let mut limit = 150;
    let mut print:bool = true;
    let mut lentest = 0;

    let starttime = SystemTime::now();
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


    }
    println!("Total records processed: {}", lentest);
    println!("Time Elapsed: {:?}", starttime.elapsed());
}
