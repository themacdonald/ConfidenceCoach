# ConfidenceCoach

**Goal:** Create a personalized coaching tool that uses AI to help recruiters, hiring managers and junior ML engineers overcome impostor syndrome. The impostor phenomenon describes people who, despite being capable, cannot internalize their success and fear being “found out”【312862269548361†L84-L88】. Success alone often does not fix the feeling because individuals attribute positive outcomes to luck or external factors while taking full responsibility for failures【312862269548361†L104-L116】. ConfidenceCoach leverages AI to provide affirmations, self-assessment and skill-building recommendations so that users can recognize their achievements and address underlying insecurities.

## Features

- **Self‑Assessment Module:** An interactive questionnaire assesses the user’s current project context, perceived skills and emotions. It maps responses onto common impostor patterns—such as perfectionist, expert, natural genius, soloist and superperson—based on coaching research【312862269548361†L84-L88】. 
- **Data‑Driven Feedback:** A lightweight language model fine‑tuned on coaching scripts generates personalized affirmations and actionable advice. It contextualizes progress by visualizing completed milestones, code contributions or model performance to counteract “I just got lucky” narratives【312862269548361†L104-L116】.
- **Skill Gap Analysis & Learning Recommendations:** Compares the user’s self‑assessed skills against a curated competency framework (e.g. annotation, RLHF, bias analysis) and suggests targeted learning resources to close gaps.
- **Mindfulness & Reset Exercises:** Offers short cognitive exercises or “PQ reps” (e.g. breathing for ten seconds) to interrupt anxiety loops and encourage reflection. Emphasizes that this is a coaching aid, not a medical tool.
- **Privacy & Ethics:** Stores assessments locally and clearly communicates data usage. Provides a privacy policy and avoids medical claims.

## Quick Start

1. Clone this repository and install dependencies (Python ≥ 3.8).
   ```bash
   git clone https://github.com/themacdonald/ConfidenceCoach.git
   cd ConfidenceCoach
   pip install -r requirements.txt
   ```
2. Run the Streamlit interface locally:
   ```bash
   streamlit run app.py
   ```
3. Follow the on‑screen prompts to complete the self‑assessment. The app will provide affirmations, suggest resources and track your progress.

You can also run the program in Google Colab by opening the provided notebook (`colab_notebooks/confidencecoach_demo.ipynb`) for a cloud‑hosted demo.

## Implementation Plan

This project is structured as an agile two‑week sprint (~30 hours):

| Week | Tasks | Deliverables |
|---|---|---|
| **Week 1** | Design the self‑assessment questionnaire and impostor syndrome pattern classification. Build a CLI/Streamlit interface. Fine‑tune a small LLM on coaching data to generate affirmations. | Working questionnaire, initial LLM model, and basic interface. |
| **Week 2** | Implement skill gap analysis and learning recommendations. Integrate data‑driven feedback and progress visualizations. Develop mindfulness exercises and privacy features. Prepare documentation and tutorials. | Complete Streamlit app with all features, example notebook and deployment instructions. |

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch and submit a pull request. Be sure to follow the coding style and include tests where appropriate. For issues or feature requests, file an issue in the GitHub tracker.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
