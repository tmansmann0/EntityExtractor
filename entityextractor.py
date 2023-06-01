import re
import datetime

class EntityExtractor:
    def __init__(self, text):
        self.text = text

    def extract_date(self):
        regex = r"(?:\b(?:(?:January|February|March|April|May|June|July|August|September|October|November|December)\b\s+(?:(?:first|1st|second|2nd|third|3rd|fourth|4th|fifth|5th|sixth|6th|seventh|7th|eighth|8th|ninth|9th|tenth|10th|eleventh|11th|twelfth|12th|thirteenth|13th|fourteenth|14th|fifteenth|15th|sixteenth|16th|seventeenth|17th|eighteenth|18th|nineteenth|19th|twentieth|20th|twenty-first|21st|twenty-second|22nd|twenty-third|23rd|twenty-fourth|24th|twenty-fifth|25th|twenty-sixth|26th|twenty-seventh|27th|twenty-eighth|28th|twenty-ninth|29th|thirtieth|30th|thirty-first|31st)\b))|(?:\b(?:(?:(?:0?[1-9]|1[0-2])/(?:0?[1-9]|1\d|2[0-8]))|(?:(?:0?[13-9]|1[0-2])/29)|(?:(?:0?[13578]|1[02])/29|30|31)))\b(?:/\d{2,4})?\b)|(?:\bthe\b\s+first\s+of\b\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\b)"
        match = re.search(regex, self.text, re.IGNORECASE)
        if match:
            date_str = match.group(0)
            return date_str
        return None

    def convert_date(self, date_str, format_option="dd/mm/yyyy"):
        current_year = datetime.datetime.now().year
        current_month = datetime.datetime.now().month
        date_obj = None

        if re.match(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\b", date_str, re.IGNORECASE):
            date_obj = datetime.datetime.strptime(date_str, "%B %d")
        elif re.match(r"\b(?:(?:0?[1-9]|1[0-2])/(?:0?[1-9]|1\d|2[0-8]))|(?:(?:0?[13-9]|1[0-2])/29)|(?:(?:0?[13578]|1[02])/29|30|31)\b(?:/\d{2,4})?\b", date_str):
            date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y" if len(date_str) > 5 else "%m/%d")
        elif re.match(r"\bthe\b\s+first\s+of\b\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\b", date_str, re.IGNORECASE):
            date_obj = datetime.datetime.strptime(date_str, "the first of %B")
        
        if date_obj:
            if date_obj.month < current_month:
                date_obj = date_obj.replace(year=current_year + 1)
            else:
                date_obj = date_obj.replace(year=current_year)

            if format_option == "dd/mm/yyyy":
                return date_obj.strftime("%d/%m/%Y")
            elif format_option == "mm/dd/yyyy":
                return date_obj.strftime("%m/%d/%Y")
            elif format_option == "dd/mm/yy":
                return date_obj.strftime("%d/%m/%y")
            elif format_option == "mm/dd/yy":
                return date_obj.strftime("%m/%d/%y")
        return None
        
    def extract_time(self):
        regex = r'\b((?:0?[1-9]|1[0-2]):[0-5][0-9]\s?[ap]m)\b|\b(?:(?:midnight|noon)\b)'
        matches = re.findall(regex, self.text, re.IGNORECASE)
        return matches

    def convert_time(self, time_str, format_option="12-hour"):
        time_obj = None

        if re.match(r"\b(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?[ap]m\b", time_str, re.IGNORECASE):
            time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
        elif re.match(r"\b(?:midnight)\b", time_str, re.IGNORECASE):
            time_obj = datetime.datetime.strptime("12:00 AM", "%I:%M %p")
        elif re.match(r"\b(?:noon)\b", time_str, re.IGNORECASE):
            time_obj = datetime.datetime.strptime("12:00 PM", "%I:%M %p")
        
        if time_obj:
            if format_option == "12-hour":
                return time_obj.strftime("%I:%M %p")
            elif format_option == "24-hour":
                return time_obj.strftime("%H:%M")
        
        return None

    def extract_url(self):
        link_regex = r'(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\/[^\s]*)?'  # Extract URL
        matches = re.findall(link_regex, self.text)
        return matches
