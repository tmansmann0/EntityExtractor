# EntityExtractor
Entity Extractor Python Module for basic Natural Language Computing Tasks

  <p>
    This is a simple Python class, <code>EntityExtractor</code>, that provides methods to extract and convert entities from text. It currently supports extracting and converting dates, times, and URLs.
  </p>
  <h3>Why does this exist?</h3>
  <p>
    The <code>EntityExtractor</code> class aims to simplify the extraction and conversion of common entities from text. It can be useful in various natural language processing (NLP) tasks where extracting specific information such as dates, times, or URLs is required.
  </p>
  <h3>License</h3>
  <p>
    This code is open source and available under the <a href="https://opensource.org/licenses/MIT">MIT License</a>. You are free to use, modify, and distribute it, as long as the original license is included and proper attribution is given.
  </p>
  <h3>Example Usage</h3>
  <pre><code>
    # Instantiate the EntityExtractor with some text
    text = "I have an appointment on January 15th at 2:30 PM. Visit my website at https://example.com"
    extractor = EntityExtractor(text)

    # Extract and convert the date
    date = extractor.extract_date()
    if date:
        formatted_date = extractor.convert_date(date)
        print("Date:", formatted_date)
    else:
        print("No date found")

    # Extract and convert the time
    times = extractor.extract_time()
    if times:
        for time in times:
            formatted_time = extractor.convert_time(time)
            print("Time:", formatted_time)
    else:
        print("No time found")

    # Extract URLs
    urls = extractor.extract_url()
    if urls:
        print("URLs:")
        for url in urls:
            print(url)
    else:
        print("No URLs found")
  </code></pre>
  <p>Output:</p>
  <pre><code>
  Date: 15/01/2023
  Time: 2:30 PM
  URLs: https://example.com
  </code></pre>
  <p>
    Note: The above example assumes that you have already imported the necessary modules and instantiated the <code>EntityExtractor</code> class.
  </p>
</details>
