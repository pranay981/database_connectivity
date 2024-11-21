import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",     
        user="root",           
        password="your_password",  
        database="quiz_db"     
    )


def insert_questions(cursor, questions):
    for category, question_list in questions.items():
        for question_data in question_list:
            question = question_data["question"]
            options = ', '.join(question_data["options"])  
            answer = question_data["answer"]
            cursor.execute("""
                INSERT INTO questions (category, question, options, answer)
                VALUES (%s, %s, %s, %s)
            """, (category, question, options, answer))


def fetch_questions(cursor):
    cursor.execute("SELECT * FROM questions")
    return cursor.fetchall()


def display_questions(questions):
    for question in questions:
        print(f"Category: {question[1]}")
        print(f"Question: {question[2]}")
        print(f"Options: {question[3]}")
        print(f"Answer: {question[4]}")
        print()


questions = {
    "General Knowledge": [
        {"question": "Who was the first President of India?", "options": ["A) Dr. Rajendra Prasad", "B) Sarvepalli Radhakrishnan", "C) Zakir Husain", "D) V. V. Giri"], "answer": "A"},
        {"question": "Which is the smallest state in India by area?", "options": ["A) Kerala", "B) Goa", "C) Sikkim", "D) Nagaland"], "answer": "B"},
        {"question": "Which is the official language of the Indian state of Karnataka?", "options": ["A) Telugu", "B) Kannada", "C) Tamil", "D) Malayalam"], "answer": "B"},
        {"question": "Who is the founder of the Maurya Empire in India?", "options": ["A) Chandragupta Maurya", "B) Ashoka", "C) Bindusara", "D) Harsha"], "answer": "A"},
        {"question": "In which year was the Indian Constitution adopted?", "options": ["A) 1947", "B) 1949", "C) 1950", "D) 1952"], "answer": "C"},
        {"question": "Which of the following cities is known as the 'City of Joy'?", "options": ["A) Kolkata", "B) Mumbai", "C) Delhi", "D) Chennai"], "answer": "A"},
        {"question": "Which state in India is known for the Sun Temple at Konark?", "options": ["A) Odisha", "B) Bihar", "C) Rajasthan", "D) Gujarat"], "answer": "A"},
        {"question": "Who is the current Chief Justice of India (as of 2024)?", "options": ["A) D.Y. Chandrachud", "B) N.V. Ramana", "C) Sharad Arvind Bobde", "D) Ranjan Gogoi"], "answer": "A"},
        {"question": "Which festival is celebrated in Punjab as a harvest festival?", "options": ["A) Holi", "B) Baisakhi", "C) Diwali", "D) Onam"], "answer": "B"},
        {"question": "Which of the following is the largest desert in India?", "options": ["A) Thar Desert", "B) Rann of Kutch", "C) Ladakh", "D) Deccan Plateau"], "answer": "A"},
        {"question": "Who is the author of the famous book 'Discovery of India'?", "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Sardar Vallabhbhai Patel", "D) B.R. Ambedkar"], "answer": "A"},
        {"question": "Which Indian state is known as the 'Land of Five Rivers'?", "options": ["A) Punjab", "B) Haryana", "C) Rajasthan", "D) Uttar Pradesh"], "answer": "A"},
        {"question": "Which city is home to the Golden Temple?", "options": ["A) New Delhi", "B) Chandigarh", "C) Amritsar", "D) Patiala"], "answer": "C"},
        {"question": "Which Mughal emperor built the Taj Mahal?", "options": ["A) Akbar", "B) Shah Jahan", "C) Aurangzeb", "D) Humayun"], "answer": "B"},
        {"question": "Which freedom fighter gave the slogan 'Inquilab Zindabad'?", "options": ["A) Bhagat Singh", "B) Subhash Chandra Bose", "C) Jawaharlal Nehru", "D) Mahatma Gandhi"], "answer": "A"},
        {"question": "Which of the following is the national tree of India?", "options": ["A) Neem", "B) Peepal", "C) Banyan", "D) Mango"], "answer": "C"},
        {"question": "Who was the first woman Chief Minister of an Indian state?", "options": ["A) Sucheta Kriplani", "B) Indira Gandhi", "C) Sarojini Naidu", "D) Pratibha Patil"], "answer": "A"},
        {"question": "Which state is known for the Kathakali dance form?", "options": ["A) Tamil Nadu", "B) Kerala", "C) Andhra Pradesh", "D) Karnataka"], "answer": "B"},
        {"question": "Who is known as the 'Iron Man of India'?", "options": ["A) Sardar Vallabhbhai Patel", "B) Lal Bahadur Shastri", "C) Bal Gangadhar Tilak", "D) B.R. Ambedkar"], "answer": "A"},
        {"question": "Which Indian city is known as the 'City of Lakes'?", "options": ["A) Udaipur", "B) Bhopal", "C) Jaipur", "D) Srinagar"], "answer": "A"},
        {"question": "Which state in India has the longest coastline?", "options": ["A) Gujarat", "B) Maharashtra", "C) Tamil Nadu", "D) Kerala"], "answer": "A"},
        {"question": "Who was the first Indian to win the Nobel Prize?", "options": ["A) C.V. Raman", "B) Rabindranath Tagore", "C) Amartya Sen", "D) Kailash Satyarthi"], "answer": "B"},
        {"question": "What is the currency of India?", "options": ["A) Dollar", "B) Rupee", "C) Yen", "D) Pound"], "answer": "B"},
        {"question": "Which city is the capital of Andhra Pradesh (as of 2024)?", "options": ["A) Amaravati", "B) Visakhapatnam", "C) Vijayawada", "D) Tirupati"], "answer": "A"},
        {"question": "Which Indian state is famous for the classical dance form Bharatnatyam?", "options": ["A) Kerala", "B) Tamil Nadu", "C) Karnataka", "D) Andhra Pradesh"], "answer": "B"}
    ],
    "Technology": [
        {"question": "Which company is India's largest IT services provider?", "options": ["A) Infosys", "B) Wipro", "C) TCS", "D) HCL"], "answer": "C"},
        {"question": "What is the name of India's indigenous operating system?", "options": ["A) BharatOS", "B) IndOS", "C) HindOS", "D) IndiaOS"], "answer": "A"},
        {"question": "In which year did ISRO launch its first satellite, Aryabhata?", "options": ["A) 1972", "B) 1975", "C) 1980", "D) 1984"], "answer": "B"},
        {"question": "Which Indian scientist is known as the 'Missile Man of India'?", "options": ["A) Dr. A.P.J. Abdul Kalam", "B) Homi Bhabha", "C) Vikram Sarabhai", "D) Satish Dhawan"], "answer": "A"},
        {"question": "What is the full form of UPI in India’s digital payment system?", "options": ["A) Unified Payments Interface", "B) Universal Payment Identity", "C) Unified Personal Interface", "D) Unified Process Infrastructure"], "answer": "A"},
        {"question": "Which Indian company developed the Aakash tablet?", "options": ["A) Infosys", "B) Reliance", "C) DataWind", "D) HCL"], "answer": "C"},
        {"question": "Which of the following is a major IT park in India?", "options": ["A) Hinjewadi", "B) Electronic City", "C) Cybercity", "D) All of the above"], "answer": "D"},
        {"question": "Who is the CEO of Google as of 2024?", "options": ["A) Satya Nadella", "B) Sundar Pichai", "C) Shantanu Narayen", "D) Parag Agrawal"], "answer": "B"},
        {"question": "Which Indian mobile brand was the first to develop a 5G smartphone?", "options": ["A) Micromax", "B) Intex", "C) Karbonn", "D) Reliance Jio"], "answer": "D"},
        {"question": "Which is the highest civilian award given for contributions to science and technology in India?", "options": ["A) Padma Shri", "B) Padma Bhushan", "C) Shanti Swarup Bhatnagar Prize", "D) Padma Vibhushan"], "answer": "C"},
        {"question": "Which of the following organizations is responsible for India's defense research?", "options": ["A) ISRO", "B) DRDO", "C) HAL", "D) BHEL"], "answer": "B"},
        {"question": "Which of these was India's first nuclear reactor?", "options": ["A) Cirus", "B) Apsara", "C) Dhruva", "D) Pokhran"], "answer": "B"},
        {"question": "What is the name of the digital identity system used in India?", "options": ["A) Aadhaar", "B) DigiID", "C) BharatID", "D) DigitalIndia"], "answer": "A"},
        {"question": "Which company introduced ChatGPT?", "options": ["A) Google", "B) OpenAI", "C) Microsoft", "D) IBM"], "answer": "B"},
        {"question": "Which programming language is widely used in data science?", "options": ["A) Python", "B) Java", "C) C++", "D) Ruby"], "answer": "A"},
        {"question": "What does AI stand for?", "options": ["A) Artificial Intelligence", "B) Automated Input", "C) Automatic Intelligence", "D) None of the above"], "answer": "A"},
        {"question": "Which technology is used for cryptocurrency transactions?", "options": ["A) Blockchain", "B) Cloud Computing", "C) Internet of Things", "D) Big Data"], "answer": "A"},
        {"question": "Which software is primarily used for photo editing?", "options": ["A) Adobe Photoshop", "B) MS Paint", "C) CorelDRAW", "D) Blender"], "answer": "A"},
        {"question": "What is the full form of IoT?", "options": ["A) Internet of Things", "B) Internet on Technology", "C) Information of Things", "D) Internet Operation Technology"], "answer": "A"},
        {"question": "Which Indian scientist led the Mars Orbiter Mission (Mangalyaan)?", "options": ["A) Ritu Karidhal", "B) K. Radhakrishnan", "C) Tessy Thomas", "D) A.S. Kiran Kumar"], "answer": "A"},
        {"question": "What does VPN stand for?", "options": ["A) Virtual Private Network", "B) Very Private Network", "C) Virtual Protection Network", "D) Visual Protocol Network"], "answer": "A"},
        {"question": "Which Indian company launched the supercomputer 'Param'?", "options": ["A) C-DAC", "B) DRDO", "C) Infosys", "D) ISRO"], "answer": "A"},
        {"question": "Which database is used in large-scale websites like Facebook?", "options": ["A) MySQL", "B) MongoDB", "C) Oracle", "D) Cassandra"], "answer": "B"},
        {"question": "Which is the primary programming language for Android development?", "options": ["A) Java", "B) Python", "C) C++", "D) Swift"], "answer": "A"},
        {"question": "What is the name of India's ambitious digital payment system?", "options": ["A) BharatPay", "B) Paytm", "C) BHIM", "D) GPay"], "answer": "C"}
    ],
    "Sports": [
        {"question": "Who won the 2019 ICC Cricket World Cup?", "options": ["A) England", "B) Australia", "C) India", "D) New Zealand"], "answer": "A"},
        {"question": "Which country hosted the 2020 Summer Olympics?", "options": ["A) Japan", "B) China", "C) Brazil", "D) Russia"], "answer": "A"},
        {"question": "Who is known as the 'Flying Sikh'?", "options": ["A) Milkha Singh", "B) P.T. Usha", "C) Sardar Singh", "D) Vijay Kumar"], "answer": "A"},
        {"question": "Which country won the 2018 FIFA World Cup?", "options": ["A) France", "B) Croatia", "C) Germany", "D) Argentina"], "answer": "A"},
        {"question": "Who holds the record for the most number of goals in international football?", "options": ["A) Cristiano Ronaldo", "B) Lionel Messi", "C) Pele", "D) Miroslav Klose"], "answer": "A"},
        {"question": "Which tennis player has won the most Grand Slam singles titles?", "options": ["A) Roger Federer", "B) Rafael Nadal", "C) Novak Djokovic", "D) Serena Williams"], "answer": "C"},
        {"question": "In which year did India win its first hockey Olympic gold?", "options": ["A) 1928", "B) 1936", "C) 1948", "D) 1952"], "answer": "A"},
        {"question": "Which athlete has won the most Olympic gold medals?", "options": ["A) Michael Phelps", "B) Usain Bolt", "C) Carl Lewis", "D) Simone Biles"], "answer": "A"},
        {"question": "Who was the first female athlete to win an Olympic gold medal for India?", "options": ["A) P.T. Usha", "B) Mary Kom", "C) Saina Nehwal", "D) Karnam Malleswari"], "answer": "D"},
        {"question": "In which sport would you perform a slam dunk?", "options": ["A) Tennis", "B) Basketball", "C) Football", "D) Hockey"], "answer": "B"},
        {"question": "Who is the fastest cricketer to score 1000 runs in ODIs?", "options": ["A) Virat Kohli", "B) AB de Villiers", "C) Shane Watson", "D) Fakhar Zaman"], "answer": "A"},
        {"question": "Which country won the 2016 Rio Olympics overall medal tally?", "options": ["A) USA", "B) China", "C) Russia", "D) Germany"], "answer": "A"},
        {"question": "Who is the all-time top scorer in the history of the IPL?", "options": ["A) Virat Kohli", "B) Chris Gayle", "C) Suresh Raina", "D) David Warner"], "answer": "A"},
        {"question": "Who won the 2017 FIFA Confederations Cup?", "options": ["A) Germany", "B) Chile", "C) Portugal", "D) Brazil"], "answer": "A"},
        {"question": "Which country has won the most Rugby World Cup titles?", "options": ["A) New Zealand", "B) Australia", "C) South Africa", "D) England"], "answer": "A"},
        {"question": "Which cricketer has the record for the highest individual score in a Test match?", "options": ["A) Brian Lara", "B) Don Bradman", "C) Virender Sehwag", "D) Ricky Ponting"], "answer": "A"},
        {"question": "Who won the 2020 UEFA Champions League?", "options": ["A) Paris Saint-Germain", "B) Bayern Munich", "C) Liverpool", "D) Real Madrid"], "answer": "B"},
        {"question": "Which famous boxer has the nickname 'The Greatest'?", "options": ["A) Mike Tyson", "B) Muhammad Ali", "C) Floyd Mayweather", "D) George Foreman"], "answer": "B"},
        {"question": "Who holds the record for the most career points in NBA history?", "options": ["A) LeBron James", "B) Michael Jordan", "C) Kareem Abdul-Jabbar", "D) Kobe Bryant"], "answer": "C"},
        {"question": "Which country won the 2014 FIFA World Cup?", "options": ["A) Brazil", "B) Germany", "C) Argentina", "D) Netherlands"], "answer": "B"},
        {"question": "Which country has won the most number of Olympic gold medals?", "options": ["A) USA", "B) Russia", "C) Germany", "D) China"], "answer": "A"},
        {"question": "Which city hosted the 2008 Summer Olympics?", "options": ["A) Beijing", "B) London", "C) Sydney", "D) Athens"], "answer": "A"},
        {"question": "In which sport is the Ashes series contested?", "options": ["A) Tennis", "B) Cricket", "C) Rugby", "D) Golf"], "answer": "B"}
    ]
}



def main():
    
    connection = create_connection()
    cursor = connection.cursor()

    
    insert_questions(cursor, questions)

    
    connection.commit()

   
    fetched_questions = fetch_questions(cursor)
    display_questions(fetched_questions)

   
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
