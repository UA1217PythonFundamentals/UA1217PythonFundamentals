import re
string = "Academy SoftServe"

# pattern = r"Acade"
# result = re.match(pattern, string)
# print(result)

# pattern = r"Soft"
# result = re.match(pattern, string)
# print(result)

# pattern = "e"
# result = re.search(pattern, string)
# print(result)
# print(result.group(0))

string = """In the year 2023, the global population reached approximately 8 billion. Among these, around 1.4 billion people live in China, and about 1.3 billion reside in India. The world's largest cities, such as Tokyo with over 37 million residents and Delhi with 31 million, continue to grow rapidly.

In the tech industry, Apple's revenue for the fiscal year 2022 was $394.3 billion, while Samsung reported earnings of $244.3 billion. The latest iPhone model, the iPhone 14, sold over 10 million units within the first month of its release.

On the environmental front, the average global temperature increased by 1.2°C since pre-industrial times, highlighting the urgency of climate action. Renewable energy sources contributed 28% of the world's electricity in 2022, a significant increase from the 21% reported in 2018.

In sports, the 2024 Summer Olympics, set to be held in Paris, are expected to feature 10,500 athletes competing in 329 events across 32 sports. The previous Olympics in Tokyo saw the USA top the medal table with 39 golds, followed by China with 38 and Japan with 27.



For any inquiries about our products, please contact our customer support team at support@company.com. If you have questions related to billing, reach out to billing@company.com. For job opportunities, you can send your resume to careers@company.com.

Our marketing department can be contacted via marketing@company.com, and for media inquiries, please email press@company.com. If you encounter technical issues, our IT support team is available at it_support@company.com.

For feedback and suggestions, feel free to email feedback@company.com. Additionally, our CEO, John Doe, can be reached directly at john.doe@company.com."""

# pattern = "e"
# pattern = "[eaS]"
# pattern = "[a-z]"
# pattern = "\d"
# pattern = "e.e"
# pattern = "\d{4}"
# pattern = "\d{2,4}"
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


result = re.findall(pattern, string)
print(result)




# import re
# pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# string = """
# For any inquiries about our products, please contact our customer support team at support@company.com. If you have questions related to billing, reach out to billing@company.com. For job opportunities, you can send your resume to careers@company.com.

# Our marketing department can be contacted via marketing@company.com, and for media inquiries, please email press@company.com. If you encounter technical issues, our IT support team is available at it_support@company.com.

# For feedback and suggestions, feel free to email feedback@company.com. Additionally, our CEO, John Doe, can be reached directly at john.doe@company.com.

# For international inquiries, please contact our regional offices:
# - Europe: europe@company.com
# - Asia: asia@company.com
# - Americas: americas@company.com
# - Africa: africa@company.com

# For partnership opportunities, please email partnerships@company.com. If you need assistance with anything else, you can always reach us at info@company.com.
# """

# result = re.findall(pattern, string)
# print(result)
