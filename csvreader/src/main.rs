fn main() {
    let mut rdr = csv::Reader::from_path("data_copy.csv").expect("wher file");
    let mut limit = 150;

    for i in rdr.records() {
        let line = i.expect("wher record");
        println!("{:?}", line);
        println!(" ");
        limit -=1;
        if limit == 0 {
            break;
        }
    }
}
