use std::time::SystemTime;
use std::fs;

fn main(){
    let mut rdr = csv::Reader::from_path("data.csv").expect("wher file");
    let starttime = SystemTime::now();
    let mut inputword = fs::read_to_string("compare_user_text1.txt").expect("Failed to read compare_user_text1.txt");
    let mut inputuser = fs::read_to_string("compare_user_text2.txt").expect("Failed to read compare_user_text2.txt");

    inputword = inputword.trim().to_lowercase();
    inputuser = inputuser.trim().to_lowercase();

    let mut dates: Vec<String> = Vec::new();
    let mut dateusagecounter = 0;
    let mut datecounter1: Vec<u32> = Vec::new();
    let mut datecounter2: Vec<u32> = Vec::new();
    let mut datecounter3: Vec<u32> = Vec::new();
    let mut futureadd:bool = false;

    let mut index:usize = 0;
    let mut starting:bool = true;
    let mut added:bool = false;
    let mut tmpstr = String::new();


    for result in rdr.records() {
        let record = result.expect("wher record");
        added = false;
        //println!("{}",index);

        tmpstr = record[2].to_string()[..10].to_string();
        if !dates.contains(&tmpstr) {
            //println!("{}",index);
            //println!("{:?}", dates);
            dates.push(tmpstr);
            datecounter1.push(0);
            datecounter3.push(0);
            if !starting {
                index += 1;
            }
            if starting {
                starting = false;
            }
            added = true;
        }

        if added && index >0{
            dateusagecounter += datecounter3[index-1];
            datecounter2.push(dateusagecounter);
        }

        if futureadd {
            datecounter1[index] += 1;
            futureadd = false;
        }

        if (record[1].to_string() == inputuser) && record[3].split_whitespace().any(|word| word.to_lowercase() == inputword){
            datecounter3[index]+=1;
            datecounter1[index]+=1;

            if index>0 {
                datecounter1[index-1]+=1;
            }

            futureadd = true;
        }


    }
    println!("{:?}", datecounter1);
    println!("{:?}", datecounter2);
    println!("{:?}", dates);
    //println!("{:?}", datecounter3);
    println!("Time Elapsed: {:?}", starttime.elapsed());

}