### File 1: `theratree.json`
```json
{
  "projectName": "TheraTree",
  "tagline": "We gamified the recovery process, making a scary situation fun and easy for young children that otherwise wouldn't be able to handle it.",
  "hackathon": "Axxess Hackathon 2025",
  "likes": 3,
  "commentsCount": 1,
  "story": {
    "inspiration": "The inspiration behind TheraTree came from the need to enhance patient engagement in rehabilitation. Traditional physical therapy often lacks interactive, motivating elements that encourage continuous patient participation, especially in a home setting. We wanted to develop a solution that blends technology, personalized care, and gamification to make the rehabilitation process more engaging and effective.",
    "whatItDoes": "TheraTree is a rehabilitation device designed to assist in elbow joint recovery. It is controlled by the opposite hand and raises or lowers the forearm based on the angle between the thumb and finger of the other hand. Real-time data is recorded over 15-second intervals and displayed through an interactive game. The device helps educate patients, track their progress, and motivates them with gamified feedback, including a heat map and a progress tree that either thrives or withers based on the patient’s improvement.",
    "howWeBuiltIt": "We built TheraTree using 3D-printed parts for a lightweight and customizable design. The device is powered by an Arduino with a continuous motor, which controls the up-and-down movement of the forearm. The backend of the system runs on Python, where we leveraged Pygame for the game interface, Pandas for data analysis, and Mediapipe to train a model that collects 15-second long datasets to generate real-time feedback. The interactive data visualizations, like the heat map and progress tree, were created using Python libraries for easy understanding of the patient’s progress.",
    "challengesWeRanInto": "During the construction of the arm rehabilitation device, we encountered several challenges in both hardware selection and integration. Prototyping with different sensors proved difficult as we evaluated various options for accurate motion tracking and data allocation. Initially, we experimented with the MS61 servo motor and stepper motors, but limitations in control precision and responsiveness led us to ultimately select the Hitec HSR-1425CR continuous rotation servo for its smoother operation. Down-selecting 3D models for the arm rehab structure also posed difficulties, as we had to balance mechanical stability, weight, and ergonomic design. Additionally, integrating MediaPipe for real-time movement tracking with direct control over the arm exoskeleton was complex, requiring extensive troubleshooting to achieve seamless communication between software and hardware. Front-end and back-end development further added to the challenge, as debugging and integrating the interface with hardware components required significant effort to ensure reliable performance and user-friendly interaction.",
    "accomplishmentsWeAreProudOf": "We are incredibly proud of the real-time interactive feedback system we developed, which combines data analysis, gamification, and machine learning to create a personalized rehabilitation experience. The heat map and progress tree are unique features that visually motivate patients by tracking their improvements. Our ability to use 3D printing to design the device and keep it cost-effective while ensuring functionality has also been a significant accomplishment.",
    "whatWeLearned": "Throughout this project, we learned a great deal about hardware-software integration, machine learning, and how to apply real-time data visualization in a practical setting. We also learned the importance of patient-centric design, ensuring that the device not only provides therapeutic benefits but also keeps the patient engaged and motivated. The process also taught us the value of cross-disciplinary collaboration, especially in merging biomechanics with gaming technology.",
    "whatIsNext": "Moving forward, we plan to enhance the accuracy of the data collection model by expanding its capabilities to incorporate other joint movements beyond the elbow. We also aim to refine the game interface to make it even more engaging and rewarding for patients. TheraTree will continue to evolve with additional patient feedback and we’re exploring ways to make the device even more accessible and effective for home healthcare. Ultimately, we envision TheraTree becoming a standard tool for at-home rehabilitation, helping patients stay motivated and recover effectively."
  },
  "builtWith": [
    "3dprinting",
    "arduino",
    "csv",
    "mediapipe",
    "numpy",
    "os",
    "pandas",
    "pygame",
    "python",
    "pytz",
    "subproccess",
    "time",
    "tkinter"
  ],
  "tryItOutLinks": [
    {
      "label": "GitHub Repo",
      "url": null
    }
  ],
  "prizes": [
    "Winner Overall Prize - First Place"
  ],
  "team": [
    {
      "name": "Simar Rekhi",
      "username": null,
      "contribution": null
    },
    {
      "name": "Shashwat Singh",
      "username": null,
      "contribution": null
    },
    {
      "name": "Harsh Patel",
      "username": null,
      "contribution": null
    },
    {
      "name": "Deklen Nates",
      "username": null,
      "contribution": null
    }
  ],
  "likesBy": [
    "Aadesh Senthilkumar",
    "Shashwat Singh",
    "Simar Rekhi"
  ],
  "updates": [
    {
      "author": "Deklen Nates",
      "timestamp": "9 months ago",
      "content": "Deklen Nates started this project"
    }
  ],
  "comments": [
    {
      "author": "Aadesh Senthilkumar",
      "username": "AaduMaadu",
      "timestamp": "9 months ago",
      "content": "Amazing project! #TalkTuahTree"
    }
  ]
}
```

### File 2: `materna.json`
```json
{
  "projectName": "Materna",
  "tagline": "Materna offers AI-driven insights, symptom tracking, and expert-backed health guidance for your pregnancy. Log symptoms, get 24/7 chatbot support, and stay informed with wellness tips—all in one app!",
  "hackathon": "Axxess Hackathon 2025",
  "likes": 4,
  "commentsCount": 0,
  "story": {
    "inspiration": "Materna was inspired by the need for a comprehensive and supportive platform that helps expectant mothers track their symptoms, moods, and overall well-being. Many pregnancy apps focus on basic tracking, but we wanted to provide real-time feedback, expert-backed insights, and personalized wellness tips to empower mothers throughout their journey.",
    "whatItDoes": "Materna is an all-in-one pregnancy symptom tracker and wellness hub. It allows users to log symptoms, track moods, and receive instant feedback on whether a symptom is normal or requires medical attention. It also offers nutrition guidance, meal plans, and safe prenatal exercise recommendations to support a healthy pregnancy.",
    "howWeBuiltIt": "We developed Materna using HTML, CSS, Python, and JavaScript to ensure a seamless and interactive user experience. GitHub was used for version control and collaboration, allowing efficient team workflow. Our focus was on secure authentication, real-time symptom feedback, and an intuitive UI to make pregnancy tracking effortless and informative.",
    "challengesWeRanInto": "One of the biggest challenges was ensuring smooth navigation between different pages, especially for tracking logs and interactive recipe pages. Designing an intuitive symptom feedback system was another hurdle, as we had to ensure that medical information was clear, user-friendly, and easy to understand.",
    "accomplishmentsWeAreProudOf": "We successfully built a fully functional pregnancy wellness platform that not only tracks symptoms but also provides real-time insights and self-care solutions. The seamless UI, engaging wellness features, and interactive recipe navigation make Materna a valuable tool for expectant mothers.",
    "whatWeLearned": "Through this project, we gained a deeper understanding of UI/UX best practices, efficient symptom tracking logic, and integrating interactive elements like video-based wellness tips and nutrition guidance. We also improved our skills in authentication and data management for personalized user experiences.",
    "whatIsNext": "We aim to integrate healthcare providers for regular symptom monitoring and expert guidance. A community space will allow mothers to share experiences, seek support, and connect with others in a safe environment. Additionally, we plan to introduce transition care for new mothers, including baby growth tracking and postpartum wellness features to support them beyond pregnancy."
  },
  "builtWith": [
    "css",
    "flask",
    "html5",
    "javascript",
    "python"
  ],
  "tryItOutLinks": [
    {
      "label": "GitHub Repo",
      "url": null
    }
  ],
  "prizes": [
    "Winner Overall Prize - Second Place"
  ],
  "team": [
    {
      "name": "Kavimayil P K",
      "username": null,
      "contribution": "I developed the backend code for the chatbot that provides 24/7 support, ensuring seamless and efficient user interactions."
    },
    {
      "name": "Shriya Kalyan",
      "username": null,
      "contribution": "I worked on designing and developing 4 of the pages of our website and also backend chatbot integration as well as login/sign up."
    },
    {
      "name": "Vaishnavi Siravuri",
      "username": null,
      "contribution": "Im interested in making tangible impact in the world with the solutions I build as well empowering female coders in technology. I worked on the Front end creating webpages using HTML, CSS and Javascript and we designed various features like Mood & Symptom tracking, recipe catalogue, videos for wellness etc."
    },
    {
      "name": "Jacian Wynn",
      "username": null,
      "contribution": null
    }
  ],
  "likesBy": [
    "Vaishnavi Siravuri",
    "Shriya Kalyan",
    "Bhargavi Uttarker",
    "Kavimayil P K"
  ],
  "updates": [
    {
      "author": "Shriya Kalyan",
      "timestamp": "9 months ago",
      "content": "Shriya Kalyan started this project"
    }
  ],
  "comments": []
}
```

### File 3: `aignosis.json`
```json
{
  "projectName": "AIgnosis",
  "tagline": "Your AI-powered health check, anytime, anywhere!",
  "hackathon": "Axxess Hackathon 2025",
  "likes": 5,
  "commentsCount": 0,
  "story": {
    "inspiration": "People in hospice and home healthcare often lack constant assistance, and some medical conditions require more extensive care than what is currently available. We understand the value of timely medical support and the importance of ensuring that patients receive the attention they need when they need it.",
    "whatItDoes": "Our healthcare web application utilizes advanced AI-driven diagnostics to assist users in identifying potential health concerns from images and biometric data. Skin Lesion Analysis – Users can upload an image of their skin to determine whether a lesion is malignant or benign using AI-powered image recognition. Diabetes Risk Assessment – The platform evaluates factors such as blood glucose fluctuations to assess the risk of developing diabetes, helping users take preventive action. Nail & Urine Analysis – By analyzing images of nails or urine samples, the system can provide preliminary diagnoses. Doctor Consultation – To ensure accuracy and reliability, all AI-driven insights are accompanied by the option to consult a medical professional.",
    "howWeBuiltIt": "We trained five specialized machine learning models, each tailored to detect and assess different health conditions, leveraging AI to provide accurate and early-stage analysis. These models empower users by offering insights into potential risks while ensuring reliable diagnostics. Our web platform features an intuitive and responsive UI built with vanilla HTML, CSS, and JavaScript, creating a seamless user experience. For secure authentication, we integrated Firebase, allowing users to access their data safely. The backend is powered by Flask, enabling smooth communication between the AI models and the front end, ensuring efficient data processing and real-time analysis.",
    "challengesWeRanInto": "Some obstacles we faced included integrating different software components and finding the perfect dataset, which was crucial for accurate predictions. We also had to augment and clean the data to improve accuracy. Additionally, working with large datasets was challenging due to the extensive training time required. After training, we rigorously tested our models to ensure they performed effectively.",
    "whatWeLearned": "Throughout this project, we gained valuable insights into the challenges and nuances of developing AI-driven healthcare solutions. We learned the importance of selecting high-quality datasets and how data augmentation and cleaning significantly impact model accuracy. Integrating multiple technologies, such as Firebase for authentication and Flask for backend communication, taught us the importance of seamless interoperability. Additionally, we recognized the trade-offs between model complexity and training time, reinforcing the need for optimization. Most importantly, we learned that AI can be a powerful tool in healthcare, but human expertise remains essential for accurate diagnosis and patient trust.",
    "whatIsNext": "We hope to improve the capabilities of AIgnosis to greater heights to meet the needs of all patients."
  },
  "builtWith": [
    "css3",
    "html5",
    "javascript",
    "numpy",
    "pandas",
    "python",
    "scikit-learn",
    "tensorflow"
  ],
  "tryItOutLinks": [
    {
      "label": "GitHub Repo",
      "url": null
    }
  ],
  "prizes": [
    "Winner Overall Prize - Third Place"
  ],
  "team": [
    {
      "name": "Syed Kabir",
      "username": null,
      "contribution": null
    },
    {
      "name": "Zainuddin A Mohammed",
      "username": null,
      "contribution": null
    },
    {
      "name": "Arvindh Kumar Kalainathan",
      "username": null,
      "contribution": null
    },
    {
      "name": "MuditUpadhyay04 Upadhyay",
      "username": null,
      "contribution": null
    }
  ],
  "likesBy": [
    "Arvindh Kumar Kalainathan",
    "MuditUpadhyay04 Upadhyay",
    "Tagan Ramsey",
    "See Pdrer",
    "Duy Pham"
  ],
  "updates": [
    {
      "author": "Syed Kabir",
      "timestamp": "9 months ago",
      "content": "Syed Kabir started this project"
    }
  ],
  "comments": []
}
```

### File 4: `forkast.json`
```json
{
  "projectName": "Forkast",
  "tagline": "Wondering how healthy your meals are? Upload a picture of your food, and we’ll tell you exactly what nutrients are in it! See what you’ve eaten all week and understand how you can live healthier.",
  "hackathon": "Axxess Hackathon 2025",
  "likes": 1,
  "commentsCount": 1,
  "story": {
    "whyUseForkast": "Lots of apps exist that scan the barcodes of grocery store products and track your nutrition, diet habits, etc. However, there is no place to go to get accurate, quick, and easy nutrition information for home-cooked, restaurant-style, or, for students, dining-hall meals. Thats where Forkast comes in. Unlike traditional nutrition-tracking apps that rely on barcode scanning, Forkast uses AI to analyze images of food in places where nutrition information is often unavailable. Just snap a picture, and Forkast instantly identifies your meal, provides detailed nutrition insights, and tracks your eating habits over time. With an integrated chatbot, you can ask questions about macros, calories, or even meal suggestions based on your diet goals. Whether you’re a student navigating dining hall options or someone who enjoys cooking at home, Forkast ensures you get accurate, personalized nutrition data—without the guesswork.",
    "whatIsForkast": {
      "secureAuthentication": "Ensures user privacy with encrypted data flows, leveraging a serverless architecture on Amazon Web Services (AWS) for scalability and reliability.",
      "aiPoweredInsights": "NomBot, your secure, accurate, personal nutrition assistant, answers questions about meal composition, macros, and dietary trends in real time trained on 1 billion tokens through llama-3.2.",
      "instantMealRecognition": "Uses Python and open artificial intelligence models, such as llama-vision-3.2, to analyze home-cooked, restaurant-style, and dining hall meals, providing accurate nutrition breakdowns without the need for barcodes.",
      "personalizedDashboard": "Stores your meal history and nutrition data to help identify trends, set goals, and make informed dietary decisions using high detail charts."
    },
    "frameworkAndTechStack": {
      "amazonWebServices": "We use a cloud-focused and secure, serverless setup on AWS to handle authentication, data storage, and processing, ensuring scalability and security.",
      "llamaImageRecognitionAndChatBot": "Leveraging computer vision models, our app identifies meals from user-uploaded images and extracts nutritional information. Additionally, using natural language processing (NLP) and machine learning, NomBot provides real-time responses to nutrition-related queries.",
      "reactNativeAndRecharts": "Front-end developed with React Native, ensuring a smooth cross-platform experience for iOS and Android users that is scaleable for future needs, with Recharts for dynamic nutrition data visualizations.",
      "usdaFoodDataCentralAPI": "Retrieves accurate nutritional information from an extensive database of food items to enhance meal analysis.",
      "multer": "Handles image uploads efficiently, enabling secure and fast processing of user-submitted meal photos."
    },
    "challengesWeFaced": {
      "pythonBackendIntegration": "Integrating the Flask-based backend with NomBot AI presented unexpected challenges, particularly in optimizing response times and API communication.",
      "awsLambdaSetup": "Setting up AWS Lambda functions for the first time required overcoming hurdles in serverless deployment and event-driven execution.",
      "imageRecognitionModel": "Training a large, custom food recognition model proved too time-consuming for our current scope, leading us to explore alternative solutions.",
      "foodDataCentralAPI": "Sorting through USDA’s FoodData Central API to extract relevant and structured nutrition data required extensive filtering and optimization."
    },
    "biggestAccomplishments": {
      "dataEncryption": "Successfully implemented secure image processing and data processing pipeline, ensuring user privacy and protection.",
      "uiUxDesignAndDashboard": "Built an intuitive, user-friendly frontend with React Native and Recharts, providing a seamless experience for meal tracking.",
      "firstServerlessDeployment": "Successfully deployed a serverless architecture on AWS for the first time."
    },
    "whatIsNext": {
      "bloodDataIntegration": "Enable users to upload blood test data from doctors to receive personalized dietary recommendations.",
      "customDietAndHealthPreferences": "Allow users to set custom health requirements and dietary restrictions for more tailored nutrition tracking.",
      "medicalDataSharing": "Provide an option to securely share nutrient information and eating history with physicians, aiding in yearly check-ups or medical consultations.",
      "trainingOurOwnAIModel": "Develop and train a custom food recognition model, improving accuracy and expanding support for a wider variety of home-cooked meals."
    }
  },
  "builtWith": [
    "aws-api-gateway",
    "aws-dynamodb",
    "aws-lambda",
    "css",
    "flask",
    "html",
    "llamma-vision",
    "multer",
    "numpy",
    "ollama",
    "opencv",
    "python",
    "react",
    "recharts",
    "usda-fooddata-central"
  ],
  "tryItOutLinks": [
    {
      "label": "GitHub Repo",
      "url": null
    }
  ],
  "prizes": [
    "Winner Challenge Winner Prize- Streamlining Documentation and Inventory Management"
  ],
  "team": [
    {
      "name": "Allen Zheng",
      "username": null,
      "contribution": null
    },
    {
      "name": "Ishita Saran",
      "username": null,
      "contribution": null
    },
    {
      "name": "Prerita Babarjung",
      "username": null,
      "contribution": null
    },
    {
      "name": "Sai Chauhan",
      "username": null,
      "contribution": null
    }
  ],
  "likesBy": [
    "Lily"
  ],
  "updates": [
    {
      "author": "Sai Chauhan",
      "timestamp": "9 months ago",
      "content": "Sai Chauhan started this project"
    }
  ],
  "comments": [
    {
      "author": "Lily",
      "username": "so-miscellaneous-ly",
      "timestamp": "9 months ago",
      "content": "This is so well-made and useful!"
    }
  ]
}
```

### File 5: `ai_home_healthcare_assistant.json`
```json
{
  "projectName": "AI-powered Home Healthcare Assistant",
  "tagline": "AI-powered home healthcare: Interpret, Monitor, Alert—Because every second counts.",
  "hackathon": "Axxess Hackathon 2025",
  "likes": 0,
  "commentsCount": 0,
  "story": {
    "inspiration": "Millions of homebound patients, like John, receive lab reports but struggle to interpret them without immediate access to a doctor. Many also rely on wearable devices for health tracking but lack a system to analyze trends, generate actionable insights, and send alerts in case of emergencies. Our goal was to bridge this gap with an AI-powered home healthcare assistant that provides structured health guidance and real-time monitoring, ensuring proactive and accessible care.",
    "whatItDoes": "Our AI-powered home healthcare assistant helps patients understand their lab reports, monitor their vitals in real-time, and receive emergency alerts when necessary. The system: Accepts patient lab report inputs and generates a structured six-section healthcare plan with personalized recommendations. Uses a machine learning model to classify cardiovascular risk and refine health recommendations accordingly. Connects with wearable devices to track vitals like heart rate and oxygen levels, storing this data in AWS and visualizing it through Grafana. Triggers automatic alerts to emergency contacts and healthcare providers when critical health thresholds are breached.",
    "howWeBuiltIt": {
      "machineLearningModel": "Trained to classify cardiovascular risk based on patient data.",
      "streamlitFrontend": "Developed an interactive and user-friendly interface for patients to input their lab report details.",
      "awsAndGrafana": "Built a backend system to store and visualize wearable health data, allowing real-time monitoring.",
      "automatedAlertSystem": "Implemented a mechanism that notifies emergency contacts and healthcare providers when vital signs exceed safe thresholds."
    },
    "challengesWeRanInto": {
      "dataAccessibility": "Finding publicly available datasets that accurately reflect real-world patient conditions was challenging.",
      "wearableDeviceIntegration": "Ensuring seamless synchronization between wearable devices and our backend system required significant optimization.",
      "thresholdSensitivity": "Balancing the alert system to avoid false positives while ensuring critical issues are detected reliably."
    },
    "accomplishmentsWeAreProudOf": {
      "proactiveAndReactiveSupport": "Successfully built a machine learning-powered healthcare assistant that provides both proactive and reactive healthcare support.",
      "realTimeMonitoring": "Integrated real-time health monitoring with AWS and Grafana for continuous patient tracking.",
      "userFriendlyApplication": "Developed a user-friendly Streamlit application designed for accessibility, even for non-technical users.",
      "emergencyAlertSystem": "Implemented a fully functional emergency alert system to notify caregivers and healthcare providers in case of medical emergencies."
    },
    "whatWeLearned": {
      "healthcareAIApplications": "Gained deeper insights into how AI can be used to enhance home healthcare and bridge gaps in medical accessibility.",
      "cloudBasedHealthMonitoring": "Learned to build scalable and real-time data processing systems using AWS and Grafana.",
      "userExperienceInHealthcare": "Understood the importance of designing an intuitive, easy-to-use interface for patients and caregivers."
    },
    "whatIsNext": {
      "expandingMLCapabilities": "Improve the predictive model to assess risks for a broader range of diseases.",
      "wearableDeviceIntegration": "Expand compatibility to include more health-tracking devices.",
      "multilingualSupport": "Develop support for multiple languages to enhance accessibility for diverse communities.",
      "doctorAndCaregiverPortal": "Introduce a dedicated portal for doctors and caregivers to monitor patient data and intervene when necessary."
    }
  },
  "builtWith": [
    "amazon-web-services",
    "grafana",
    "python",
    "streamlit"
  ],
  "tryItOutLinks": [
    {
      "label": "GitHub Repo",
      "url": null
    }
  ],
  "prizes": [
    "Winner Challenge Winner Prize- AI ML in Home Healthcare"
  ],
  "team": [
    {
      "name": "Swapnil Banduke",
      "username": null,
      "contribution": null
    },
    {
      "name": "Mihir Hirave",
      "username": null,
      "contribution": null
    }
  ],
  "likesBy": [],
  "updates": [
    {
      "author": "Swapnil Banduke",
      "timestamp": "9 months ago",
      "content": "Swapnil Banduke started this project"
    }
  ],
  "comments": []
}
```

### File 6: `alignify.json`
```json
{
  "projectName": "Alignify",
  "tagline": "Flow with ease, bend with care, Alignify's guidance gets you there.",
  "hackathon": "Axxess Hackathon 2025",
  "likes": 1,
  "commentsCount": 0,
  "story": {
    "inspiration": "Alignify was inspired by a desire to bring the healing and balance of yoga into the homes of everyone—especially our elderly and homecare patients. We recognized that many seniors face challenges in maintaining mobility and overall well-being due to limited access to physical therapy and group classes. Alignify combines cutting-edge AI-driven pose detection with personalized guidance to create a yoga experience that is both safe and engaging. By focusing on homecare, we aim to empower users to practice yoga confidently, knowing they have a virtual coach guiding them every step of the way.",
    "whatItDoes": "Alignify is an immersive and interactive yoga application that leverages your device’s camera to monitor and assess your yoga poses in real time. Using AI-powered feedback, the app provides personalized guidance by comparing your movements to a set of pre-calibrated reference poses, helping you adjust your form for better alignment. With both voice and visual cues, Alignify ensures you maintain proper balance through spoken instructions and on-screen overlays. Before starting a session, users can calibrate the app by capturing three standard poses, which serve as personalized benchmarks tailored to their body and ability. Designed with a homecare focus, particularly for the elderly, Alignify emphasizes gentle movements and safety, allowing users to experience the benefits of yoga without the need for strenuous exercise.",
    "howWeBuiltIt": {
      "description": "Alignify is a full-stack application built with a blend of innovative technologies:",
      "frontend": "Developed using Pyqt5, our user interface is intuitive and accessible. The calibration page allows users to capture reference images easily, while the live pose feed uses the device’s camera to provide real-time feedback.",
      "backend": "The server is powered by Flask and integrates MediaPipe for pose detection and analysis. This backend processes images, compares user poses to the reference benchmarks, and returns actionable feedback.",
      "augmentedRealityAndAI": "By leveraging MediaPipe and custom algorithms, we overlay reference landmarks on the user’s video feed, ensuring accurate and immediate pose correction.",
      "voiceIntegration": "Originally, we explored third-party TTS APIs, but eventually integrated a built‑in voice feedback system using pyttsx3 for a reliable and offline experience—perfect for homecare scenarios."
    },
    "challengesWeRanInto": "Throughout the development of Alignify, we encountered several challenges that required careful problem-solving and optimization. One major hurdle was hardware variability, as ensuring consistent performance across different devices and varying camera qualities proved difficult. To address this, we optimized our image processing pipeline to accommodate a wide range of hardware capabilities. Delivering real-time feedback was another challenge, particularly for users with limited mobility. Fine-tuning the AI model and adjusting movement detection thresholds were necessary to provide accurate and timely guidance. Additionally, designing a user-friendly interface for elderly users required a focus on accessibility, incorporating simplicity, large buttons, and clear instructions to enhance navigation. Finally, integrating a reliable calibration phase that could adapt to individual differences was complex but essential for personalizing the yoga experience, ensuring each user received tailored feedback based on their unique movements and abilities.",
    "accomplishmentsWeAreProudOf": {
      "realTimePoseCorrection": "The integration of MediaPipe and custom algorithms has resulted in a robust real-time pose correction system that empowers users to improve their form safely at home.",
      "accessibility": "We’ve created an intuitive and user-friendly interface specifically designed for elderly users and those in homecare, making yoga accessible to a wider audience.",
      "offlineFunctionality": "By relying on local processing and offline TTS, Alignify can operate without constant internet connectivity, ensuring a smooth and uninterrupted experience."
    },
    "whatWeLearned": "Balancing AI with a human touch was one of the key challenges in developing Alignify. Ensuring that technology complemented rather than overwhelmed the user experience required careful design, and through this process, we gained valuable insights into how AI can support health and wellness in a meaningful way. The iterative nature of development played a crucial role, as continuous calibration, testing, and refinement highlighted the importance of user feedback, particularly for homecare applications. Additionally, integrating multiple technologies—augmented reality, AI, voice synthesis, and real-time video processing—deepened our understanding of how to create a seamless and effective solution that enhances the yoga experience without feeling intrusive or overly complex.",
    "whatIsNext": "Looking ahead, we have several plans to enhance Alignify and make it even more effective for users of all abilities. One key improvement is expanding the pose library to include more yoga poses and personalized workout routines, allowing us to cater to a broader range of fitness levels. Additionally, integrating remote monitoring and telehealth features could enable healthcare professionals to track user progress and adjust routines as needed, making Alignify a valuable tool for therapists and rehabilitation programs. To foster engagement and motivation, we aim to introduce community features that let users share their progress, join virtual classes, and connect with others. We’re also exploring advanced machine learning models to refine our feedback loop, providing not just real-time corrections but also personalized modifications for users with specific mobility challenges."
  },
  "builtWith": [
    "flask",
    "javascript",
    "mediapipe",
    "opencv",
    "python"
  ],
  "tryItOutLinks": [
    {
      "label": "GitHub Repo",
      "url": "https://github.com/jxv210016/Alignify"
    }
  ],
  "prizes": [
    "Winner Challenge Winner Prize- Patient Engagement"
  ],
  "team": [
    {
      "name": "Renjit Joseph",
      "username": null,
      "contribution": null
    },
    {
      "name": "Aditya Bapanapalli",
      "username": null,
      "contribution": null
    },
    {
      "name": "Harsha Sirigina",
      "username": null,
      "contribution": null
    },
    {
      "name": "Jay Vanam",
      "username": null,
      "contribution": null
    }
  ],
  "likesBy": [
    "Anuradha Sirigina"
  ],
  "updates": [
    {
      "author": "Aditya Bapanapalli",
      "timestamp": "9 months ago",
      "content": "Aditya Bapanapalli started this project"
    }
  ],
  "comments": []
}
```