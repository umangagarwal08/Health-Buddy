# Health Buddy

**Health Buddy** is an intelligent health and wellness advisor application that provides users with personalized health recommendations. It leverages the power of Google Generative AI (Gemini 1.5 Flash) to deliver customized plans, including dietary suggestions, yoga routines, exercise schedules, natural remedies, and lifestyle tips tailored to the user's health profile.

---

## Features

1. **Personalized Wellness Plans**
   - Diet plans with culturally appropriate and traditional Indian meals.
   - Yoga routines tailored to individual needs.
   - Exercise schedules for all fitness levels.
   - Natural remedies and Ayurvedic suggestions.
   - Practical lifestyle tips for long-term health.

2. **User Inputs**
   - Age
   - Height
   - Weight
   - Lifestyle (Sedentary, Active, Moderately Active)
   - Blood Pressure status
   - Diabetes type
   - Dietary preferences (Vegetarian, Non-vegetarian)
   - Gender

3. **AI-Powered Responses**
   - Backed by Google Generative AI to ensure accuracy and relevance.
   - Provides detailed, easy-to-follow recommendations.

4. **Streamlit Frontend**
   - Interactive and user-friendly interface.
   - Supports responsive design for seamless user experience.

---

## Prerequisites

- **Python 3.8+**
- **Streamlit** for building the frontend interface.
- **Google Generative AI SDK** for generating intelligent health recommendations.
- **dotenv** for managing environment variables securely.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/health-buddy.git
   cd health-buddy
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**
   - Obtain an API key for Google Generative AI.
   - Create a `.env` file in the root directory with the following content:
     ```env
     GOOGLE-API-KEY=your-google-api-key
     ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Launch the application using the command above.
2. Enter your health profile details in the input fields.
3. Ask a health-related question in the text box (e.g., "What diet should I follow?").
4. Click the **Submit** button to receive a detailed health plan.

---

## File Structure

```plaintext
health-buddy/
|-- app.py                     # Main Streamlit app
|-- propmpt.py                 # Contains the AI prompt and response logic
|-- requirements.txt           # Python dependencies
|-- .env                       # Environment variables (not included in repo)
|-- logo.png                   # Logo for the application
```

---

## Technologies Used

- **Streamlit**: Interactive web application framework.
- **Google Generative AI**: For generating intelligent health recommendations.
- **Python**: Core programming language.
- **dotenv**: Secure management of environment variables.

---

## Disclaimer

1. This application is an advisor providing general guidance and should not be construed as professional medical advice.
2. Before taking any action based on the recommendations, consult with a qualified healthcare professional.

---

## Author

This project was developed as a part of an effort to combine AI with healthcare to improve accessibility and personalization in wellness planning. Reach out for queries or collaborations!

---

## Future Enhancements

- **Integration with Wearable Devices**
  - Sync data from devices like Fitbit or Apple Watch for more accurate recommendations.
- **Multilingual Support**
  - Provide health plans in regional Indian languages.
- **Expanded Dietary Options**
  - Include Jain, Vegan, and Keto diet plans.
- **Progress Tracking**
  - Allow users to log and track their progress over time.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests for new features or improvements.

