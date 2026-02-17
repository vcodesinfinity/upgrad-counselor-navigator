# =================================================================
# PROJECT: upGrad AC Navigator (DS/AI/ML Portfolio)
# VERSION: 1.0.0 (Production Stable)
# AUTHOR:  Vinay Kumar T N
# LICENSE: MIT (Open Source)
# DATE:    February 17, 2026
# =================================================================
def upgrad_ultimate_counselor_assistant():
    # Finalized Database: Synced with MD, CSV, and User Directives
    db = {
        1: {
            "Program": "Professional Certificate Program in Data Science with GenAI", "Abbr": "PCP-DS",
            "Course Type": "Certification", "Duration": "6 Months", 
            "Eligibility": "Bachelor's / Final Year Students. No prior coding required.",
            "Learning Mode": "Blended: 20+ Live Sessions (Masterclasses + Workshops)",
            "Counselor Pitch": "Fastest ROI: Quick entry with Microsoft GenAI badge. Ideal for freshers.",
            "Total Cost": "INR 99,000 (Inclusive of Taxes)", "Block Amount": "N/A",
            "Certificates": "IIITB Cert + Microsoft (GenAI Professional Programme)",
            "Academic Faculty": "Dr. V. Sridhar & Dr. Chandrashekhar Ramanathan",
            "Industry Experts": "Shailesh Kumar(Chief Data Scientist - Jio),Deependra Singh, Sajan Kedia, Mirza Rahim Baig",
            "Top Projects": "Exploratory Data Analysis using Python, GenAI Prompting for Developers",
            "Relevant Tools": "Python, MySQL, Excel, ChatGPT, DALL-E, Midjourney"
        },
        2: {
            "Program": "Executive PG Certificate in Data Science & AI", "Abbr": "EPGC-DS",
            "Course Type": "Executive PG Certification", "Duration": "6 Months", 
            "Eligibility": "Bachelors or Master’s Degree or its equivalent in any discipline with minimum 50% aggregate mark or equivalent CGPA.",
            "Learning Mode": "Online: Weekly Doubt Hangouts",
            "Counselor Pitch": "Career Pivot: Includes 3-mo Math/Python bootcamp. Best for non-tech switches.",
            "Total Cost": "INR 1,80,000 (No Taxes Applicable)", "Block Amount": "INR 15,000",
            "Certificates": "IIITB Exec PG Cert + Microsoft(GenAI Professional Programme)",
            "Academic Faculty": "Tricha Anjali, Debabrata Das, Prof. G. Srinivasaraghavan, Dr.Chandrashekhar Ramanathan",
            "Industry Experts": "Abhishek Vijayvargia(Sr.Data Scientist), Deependra Singh(VP & Head of DSc), Mirza Rahim Baig (Lead Analyst)",
            "Top Projects": "Exploratory Data Analysis (Analyse NYC Taxi operations), Linear Regression (Predict parcel delivery time for Porter)",
            "Relevant Tools": "Python, MySQL, Excel, NumPy, Pandas, Matplotlib, Seaborn"
        },
        3: {
            "Program": "Executive Diploma in Data Science & AI", "Abbr": "ED-DS",
            "Course Type": "Executive PG Program", "Duration": "12 Months", 
            "Eligibility": "Bachelor's Degree with minimum 50% marks. No prior coding experience required.",
            "Learning Mode": "Online: 1-2 Live Sessions/Week (50+ Live Learning Sessions)",
            "Counselor Pitch": "Dual Alumni Edge: Choose from 5 specializations; 60+ industry projects, Complimentary fundamentals bootcamp (3Months,Pass to Skip)",
            "Total Cost": "INR 3,15,000 (Inclusive of Taxes)", "Block Amount": "INR 15,000",
            "Certificates": "IIITB Exec Diploma + Microsoft (GenAI Professional Programme)",
            "Academic Faculty": "Dr.C.Ramanathan, Dr.G.Srinivasaraghavan, Dr.Debabrata Das, Dr.Tricha Anjali",
            "Industry Experts": "Abhishek Vijayvargia, Deependra Singh, S. Anand, Manish Shukla",
            "Pi": "π Pack (+₹50k): Adds 3 months and grants Exec Diploma in ML & AI.",
            "Specializations": "1.Data Analysis, 2.Data Engineering, 3.Business Analytics, 4.NLP, 5.Deep Learning",
            "Top Projects": "Advanced GenAI for Analytics: Analyse Amazon customer reviews, Analyse NYC taxi operations etc",
            "Relevant Tools": "Python, SQL, Tableau, Power BI, Spark, AWS EMR, Kafka"
        },
        4: {
            "Program": "MS in Data Science (LJMU + IIITB)", "Abbr": "MS-DS",
            "Course Type": "Master's Degree", "Duration": "18 Months", 
            "Eligibility": "Bachelor's Degree with minimum 50% marks. No coding experience required.",
            "Learning Mode": "Hybrid: 100+ Live Sessions (57 IIITB + 49 LJMU)",
            "Counselor Pitch": "Global Mobility: WES-recognized UK degree at 1/10th cost. Complimentary fundamentals bootcamp (3Months,Pass to Skip)",
            "Total Cost": "INR 5,20,000 (Inclusive of Taxes)", "Block Amount": "INR 15,000",
            "Certificates": "MSc Degree (LJMU) + IIITB Executive Diploma",
            "Academic Faculty": "Prof.Diya Al-Jumeily (LJMU), Dr.Chandrashekar Ramanathan, Dr.Debabrata Das, Dr.Tricha Anjali (IIITB)",
            "Industry Experts": "S.Anand, Sajan Kedia, Mirza Rahim Baig, Abhishek Vijayvargia",
            "Pi": "π Pack (+₹50k): Adds 3 months and grants Exec Diploma in ML & AI.",
            "Immersion": "On-Campus Immersion in LJMU(UK) +₹2,00,000",
            "Top Projects": "6-Month Master's Thesis/Dissertation, NYC Taxi Data Analysis",
            "Relevant Tools": "Python, MySQL, Tableau, Power BI, Hadoop, Spark, Airflow, AWS"
        },
        5: {
            "Program": "MS in AI and Data Science (O.P. Jindal)", "Abbr": "MS-AI",
            "Course Type": "Master's Degree", "Duration": "12 Months", 
            "Eligibility": "Bachelor's degree with 50% or equivalent passing marks. No work experience required.",
            "Learning Mode": "Online: Weekly Weekend Faculty-Led Sessions",
            "Counselor Pitch": "Academic Prestige: Ranked #1 Private Univ. Full Indian Master's in 12 months.",
            "Total Cost": "INR 2,75,000 (Inclusive of Taxes)", "Block Amount": "INR 10,000",
            "Certificates": "MSc Degree (JGU) + Microsoft Certification",
            "Academic Faculty": "Prof.Akshay Agrawal, Prof.Jitendra Prakash, Prof.Jatin Anand",
            "Industry Experts": "Mirza Rahim Baig, S Anand, Sajan Kedia",
            "Top Projects": "Retail Category Optimization, MRI Data Enhancement for Healthcare",
            "Relevant Tools": "Python, TensorFlow, Keras, Power BI, Tableau, SQL"
        },
        6: {
            "Program": "Executive Diploma in ML & AI with MLOps, Gen AI & Agentic AI", "Abbr": "ED-ML",
            "Course Type": "Executive PG Program", "Duration": "12 Months", 
            "Eligibility": "Bachelor's Degree with 50% marks. Proficiency in Python/Programming is recommended.",
            "Learning Mode": "Online: Fortnightly Mentorship + Weekly Hangouts",
            "Counselor Pitch": "Production Mastery: Master MLOps & Agentic AI deployment on AWS/Azure.",
            "Total Cost": "INR 3,40,000 (Inclusive of Taxes)", "Block Amount": "INR 15,000",
            "Certificates": "IIITB Exec Diploma + Microsoft (GenAI Professional Programme)",
            "Academic Faculty": "Dr.C.Ramanathan, Dr.G.Srinivasaraghavan, Dr.Debabrata Das, Dr.Tricha Anjali",
            "Industry Experts": "S.Anand, Sajan Kedia, Deependra Singh, Mirza Rahim Baig, Abhishek Vijayvargia",
            "Pi": "π Pack (+₹50k): Adds 3 months and grants Exec Diploma in DS.",
            "Top Projects": "Neural Machine Translation, Gesture Recognition, Autonomous Driving Sim",
            "Relevant Tools": "Python, Scikit-learn, Statsmodels, OpenAI APIs, LangChain, Vector DBs"
        },
        7: {
            "Program": "MS in ML & AI (LJMU + IIITB)", "Abbr": "MS-ML",
            "Course Type": "Master's Degree", "Duration": "18 Months", 
            "Eligibility": "Bachelor's Degree (min 50%) + Minimum 1 Year of Work Experience.",
            "Learning Mode": "Hybrid: 70+ Industry-Led Sessions",
            "Counselor Pitch": "Top-Tier Hikes: Highest salary hike potential (52%+). For Architect roles.",
            "Total Cost": "INR 5,65,000 (Inclusive of Taxes)", "Block Amount": "INR 15,000",
            "Certificates": "MSc Degree (LJMU) + IIITB Executive Diploma",
            "Academic Faculty": "Prof.Diya Al-Jumeily (LJMU), Dr.Chandrashekar Ramanathan, Dr.Debabrata Das, Dr.Tricha Anjali (IIITB)",
            "Industry Experts": "S.Anand, Sajan Kedia, Deependra Singh, Mirza Rahim Baig, Abhishek Vijayvargia",
            "Pi": "π Pack (+₹50k): Adds 3 months and grants Exec Diploma in DS.",
            "Immersion": "On-Campus Immersion in LJMU(UK) +₹2,0,000",
            "Top Projects": "Reinforcement Learning (Tic-Tac-Toe), Object Detection (YOLO), Thesis",
            "Relevant Tools": "Python, TensorFlow, PyTorch, Keras, OpenCV, LangChain"
        },
        8: {
            "Program": "EPGC in GenAI & Agentic AI (IIT Kharagpur)", "Abbr": "EPGC-GenAI",
            "Course Type": "Executive PG Certification", "Duration": "8 Months (32 Weeks)", 
            "Eligibility": "Bachelor's or Master's in STEM with 50% in each or 2 years of work experience in a technical role.",
            "Learning Mode": "100% Live: Sat 10AM-1PM",
            "Counselor Pitch": "Elite Branding: 100% Faculty-led by IIT-K. Physical Convocation Ceremony. India’s Strongest Academic Bench in AI & Data Science",
            "Total Cost": "INR 1,77,000 (Inclusive of Taxes)", "Block Amount": "INR 10,000",
            "Certificates": "IIT Kharagpur Executive PG Certificate",
            "Academic Faculty": "Prof.S.Bhattacharya, Prof.Niloy Ganguly, Prof.Pawan Goyal, Prof.Sudeshna Sarkar",
            "Industry Experts": "N/A (This is a 100% Faculty-Led Academic Certification)",
            "Top Projects": "Enterprise RAG Systems, Advanced LLM Fine-tuning (LoRA/PEFT), Multi Agent System",
            "Relevant Tools": "Transformers, LangChain, PyTorch, LoRA/QLoRA, RAG Frameworks"
        },
        9: {
            "Program": "EPGP in Applied AI and Agentic AI (IIITB)", "Abbr": "EPGP-AA",
            "Course Type": "Executive PG Program", "Duration": "7 Months", 
            "Eligibility": "Bachelor's or master's Degree or its equivalent in any discipline from UGC recognized University with minimum 50% aggregate marks.",
            "Learning Mode": "Online: Weekly weekend sessions + 10+ Masterclasses",
            "Counselor Pitch": "Agent Specialist: First program for Multi-Agent RAG with Microsoft Garage access.",
            "Total Cost": "INR 1,40,000 (No Tax Applicable)", "Block Amount": "INR 10,000",
            "Certificates": "IIITB EPGP + Microsoft (GenAI Professional Programme)",
            "Academic Faculty": "Dr.C.Ramanathan, Dr.G.Srinivasaraghavan, Dr.Debabrata Das, Dr.Tricha Anjali",
            "Industry Experts": "S.Anand, Sajan Kedia, Deependra Singh, Mirza Rahim Baig, Abhishek Vijayvargia, Ujjyaini Mitra, Ankit Jain, Rajesh Sabapathy, Kautuk Pandey",
            "Top Projects": "Production Agentic Systems, RAG Enterprise Assistant Bots",
            "Relevant Tools": "LangChain, LlamaIndex, LangGraph, AutoGen, CrewAI, Docker, FastAPI"
        },
        10: {
            "Program": "Executive Programme in GenAI for Leaders", "Abbr": "EP-GenAL",
            "Course Type": "Certification", "Duration": "5 Months", 
            "Eligibility": "Bachelor's degree with a minimum of 4 years of work experience.",
            "Learning Mode": "Online: 25+ Strategy-Focused Live Sessions",
            "Counselor Pitch": "C-Suite Advantage: Focus on AI ROI, Governance, & A.D.A.P.T framework.",
            "Total Cost": "INR 2,25,000 (Inclusive of Taxes)", "Block Amount": "N/A",
            "Certificates": "IIITB Cert + Microsoft (GenAI Professional Programme)",
            "Academic Faculty": "Dr.V.Sridhar, Dr.Chandrashekhar Ramanathan",
            "Industry Experts": "Rajesh Sabapathy, Hindol Basu, Mukesh Jain, Shailesh Kumar",
            "Work Shops": "Exploring GenAI Potential, Developing and Executing an AI strategy for your business",
            "Relevant Tools": "ChatGPT, DALL-E 2, LangChain, LlamaIndex, Midjourney"
        },
        11: {
            "Program": "CTO & AI Leadership Programme", "Abbr": "CTO-AI",
            "Course Type": "C-suite Certification", "Duration": "6 Months", 
            "Eligibility": "Bachelor’s degree with a minimum of 8 years of work experience.",
            "Learning Mode": "Online: Exclusive Masterclasses + Peer Coaching",
            "Counselor Pitch": "Leadership Hub: Dual Alumni (IIITB & IIM Udaipur). Board-Ready Dossier.",
            "Total Cost": "INR 3,50,000 (Taxes Additional)", "Block Amount": "N/A",
            "Certificates": "Chief Technology Officer & AI Leadership Programme by IIITB",
            "Academic Faculty": "Prof.Kunal Kamal Kumar(IIMU), Prof.Shankar Prakash, Prof.C.Ramanathan, Prof.Gopalakrishnan S.(IIITB)",
            "Industry Experts": "Global CTOs from Fortune 500 Network",
            "Top Projects": "Strategic CTO Dossier for Enterprise AI Transformation",
            "Relevant Tools": "ChatGPT, DALL-E, Pinecone, Enterprise Architecture Frameworks"
        },
        12: {
            "Program": "DBA in Emerging Technologies with concentration in Gen AI from GGU",
            "Abbr": "DBA-GenAI",
            "Course Type": "Doctorate",
            "Duration": "36 Months",
            "Eligibility": "A Bachelor's degree with a minimum of 55% marks and 10 years of full-time work experience after graduation. (See script for Masters/Diploma equivalency rules).",
            "Learning Mode": "500 Hours of Live Learning",
            "Counselor Pitch": "Golden Gate University (GGU), San Francisco. 120+ years of excellence. Accredited by WSCUC. 68,000+ global alumni network.",
            "Total Cost": "INR 18,00,000 (No Taxes Applicable)",
            "Block Amount": "₹ 44,999",
            "Certificates": "Doctorate from GGU + PwC Directorship Certificate (at INR 10,000/-)",
            "Academic Faculty": "GGU Global Faculty",
            "Industry Experts": "Global AI Experts",
            "Immersion": "Immersion 1: Singapore (5 days), Immersion 2: San Francisco (5 days)",
            "Immersion Costs": "Learner bears: Airport transfers, flights, logistics to hotel & Univ, Accommodation, Visa, Travel Insurance, Breakfast & Dinner. upGrad provides Lunch.",
            "Relevant Tools": "Python, Tableau, Research Methodologies (Qualitative/Quantitative Tools)",
            "Program Link": "https://www.upgrad.com/dba-emerging-technologies-specialization-in-gen-ai-ggu/"
        }
    }

    while True:
        print("\n" + "="*95)
        print("   upGrad 2026 OFFICIAL AC NAVIGATOR (Working Professionals) (BETA 7 STABLE)   ")
        print("="*95)
        for k, v in db.items():
            print(f"[{k:02d}] {v['Program']} ({v['Abbr']})")
        print("[00] Exit")
        
        choice = input("\nEnter Sl No for All Details: ")
        if choice == '0' or choice == '00': break
        if not choice.isdigit() or int(choice) not in db: continue
            
        p = db[int(choice)]
        print("\n" + "-"*95)
        print(f"| {'FIELD':<20} | {'DETAILS':<70} |")
        print("-" * 95)
        for field, detail in p.items():
            detail_str = str(detail)
            # Automatic multi-line wrapping for details
            if len(detail_str) > 70:
                print(f"| {field:<20} | {detail_str[:70]:<70} |")
                print(f"| {'':<20} | {detail_str[70:140]:<70} |")
                if len(detail_str) > 140:
                    print(f"| {'':<20} | {detail_str[140:210]:<70} |")
            else:
                print(f"| {field:<20} | {detail_str:<70} |")
        print("-" * 95)
        input("\nPress Enter to return to main menu...")

if __name__ == '__main__':
    upgrad_ultimate_counselor_assistant()