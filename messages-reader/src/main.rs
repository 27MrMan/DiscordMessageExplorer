use std::collections::HashMap;
use std::time::SystemTime;

fn main() {
    let mut rdr = csv::Reader::from_path("data.csv").expect("wher file");
    let mut word_count: HashMap<String, u64> = HashMap::new();

    let starttime = SystemTime::now();

    for result in rdr.records() {
        let record = result.expect("wher record");
        let message = &record[3]; // Change index if message is in a different column

        for word in message.split_whitespace() {
            let word = word.to_lowercase();
            *word_count.entry(word).or_insert(0) += 1;
        }
    }

    // Find the top 10 most common words
    let mut word_vec: Vec<(&String, &u64)> = word_count.iter().collect();
    word_vec.sort_by(|a, b| b.1.cmp(a.1)); // Sort descending by count

    let mut words: Vec<String> = Vec::new();
    let mut counts: Vec<u64> = Vec::new();

    for (_i, (word, count)) in word_vec.iter().take(10).enumerate() {
        words.push(String::from(*word));
        counts.push(u64::from(**count));
    }
    println!("{:?}", words);
    println!("{:?}", counts);

    println!("Time Elapsed: {:?}", starttime.elapsed());
}
