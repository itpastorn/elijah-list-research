# Elijah List Research Archive

This project aims to create a **local, researchable archive** of alleged prophetic messages published on *The Elijah List*.  
The project is designed for **theological analysis, historical documentation, and critical research**, with particular focus on the New Apostolic Reformation (NAR) and related prophetic movements.

The archive is built by programmatically fetching, extracting, and structuring content from publicly available pages on *elijahlist.com*.

This project is in its infancy. It is developed on my spare time. And altough I have written lots and lots of code before in other languages, I am Python newbie.

---

## Purpose

The project has three main objectives:

1. **Documentation**  
   To create a comprehensive (as complete as possible) local archive of Elijah List messages, including messages that have later been removed.

2. **Research and Analysis**  
   To enable long-term analysis of:
   - recurring themes,
   - eschatological patterns,
   - political prophecies,
   - language use and theology over time.

3. **Transparency and Reuse**  
   To provide open-source code so that other researchers, journalists, and theologians can:
   - reproduce the dataset,
   - build upon the tools,
   - examine and evaluate the methodology and sources.

---

## Scope

- Each Elijah List message is identified by a numeric ID, for example:  
  `https://www.elijahlist.com/words/display_word.html?ID=16950`
- The highest known ID at the start of the project is **33684**.
- The project does **not**:
  - bypass access controls,
  - fetch content from archive.org,
  - attempt to reconstruct removed content from third-party sources.

Pages that no longer exist are logged as *missing*.

Re-use: Do the same for the so-called prophecies by Kim Clement
They are published using the same format:
https://www.houseofdestiny.org/prophecy/word/?trid=ID

---

## Technical Overview

- **Language:** Python 3  
- **Environment:** Ubuntu (WSL)  
- **Code editing:** Windows (editor/IDE), execution in WSL  
- **Version control:** Git (CLI in WSL)  
- **License:** Permissive open-source license (see LICENSE) TODO

### Design Principles

- Restartable execution (interruptions should not require starting over)
- Low load on the target server (rate limiting)
- Tolerant HTML parsing (legacy, table-based layout)
- Separate storage of:
  - raw HTML
  - extracted content
  - per-ID logs and status information

---

## Extracted Data

For each message, the script attempts to extract:

- ID
- URL
- HTTP status
- Fetch timestamp
- **Title**
- **Publication date**
- **Message body**
- (optional) raw HTML for future re-parsing

---

## Legal and Ethical Notice

This project:
- archives **publicly available content**,
- is intended for **research and analysis**,
- makes no claim of ownership over the original texts.

All content remains the property of its respective authors.  
The project provides structure, metadata, and tooling—not copyright.

---

## Project Status

The project is in an **active development phase**.

Planned steps:
1. Basic fetcher with logging
2. Stable HTML extraction
3. Scaling to the full ID range
4. Export formats suitable for analysis
5. Extended documentation for research use

---

## Intended Audience

- Theologians
- Scholars of religion
- Journalists
- Church leaders
- Researchers of charismatic movements
- Anyone interested in empirically examining prophetic claims

---

## Contributing

Pull requests, issues, and methodological critique will be welcome, once this project is off the ground.   
The project aims for **clarity, transparency, and reproducibility**.

---

## Author

Lars Gunther  
https://github.com/itpastorn
