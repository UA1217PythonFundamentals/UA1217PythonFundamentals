from mylog import logging
def parse_to_int(text):
    try:
        result = int(text)
        logging.info(f"{text}=>{result}")
        return result
    except:
        logging.error(f"{text} is not number")