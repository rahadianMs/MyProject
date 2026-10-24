## 💼 Portfolio Projects

Welcome to my project gallery! 🚀
I am a **Smart Tourism Product Engineer at Wise Steps Consulting** (formal title Smart Tourism Data Analyst). This page collects the products I build at work, my freelance delivery, my data-analysis work and my earlier AI and data projects.

Most product source code is private (internal or client systems), so those entries link to the live product where one exists. The data and AI projects further down include their code in this repository.

---

## 🏢 Wise Steps Consulting products (Nov 2025 to now)

Role on every project: **Product Engineer**, from the brief to the database, the screens and the deploy, with AI agents as the build team and every change reviewed by me. Since Jan 2026 I build the division's products end to end with one intern, whom I supervise.

### 1. IMS WSC: the ERP that runs the firm · [Live](https://ims.wisestepsconsulting.id/)
> One system for HR, attendance, KPI, CRM, projects, budget, finance, procurement and sustainability, used by all 13 people at the firm, from the CEO to the interns.
- Helped Wise Steps Consulting get **ISO 9001:2015 certified** (Control Union, Aug 2026): the auditor reviewed workflows run inside the system and documents kept under version control in it.
- 14 releases (v1.0 to v4.4, Jan to Sep 2026); Row Level Security across 95 Postgres tables; 1,586 unit tests and 26 Playwright scenarios in CI; Website Carbon A.

📌 *Stack:* Next.js 16, React 19, TypeScript, Supabase, Tailwind v4, shadcn/ui, Resend, Playwright

### 2. ESG Wise Impact: the firm's first sell-ready SaaS · [Live, pilot use](https://www.esg-wsc.id/)
> Multi-tenant ESG disclosure SaaS for Indonesian tourism and hospitality businesses: 195 metrics mapped to 8 frameworks, PDF, Word and Excel reports.
- **DOKU payment gateway live in production** since Jul 2026, tested end to end: verified webhooks, one idempotent fulfillment function and a reconciliation sweep.
- A complete product in pilot use (no paying client yet); Website Carbon A+ (0.03 g CO2 per visit, cleaner than 93% of pages, Oct 2026).

📌 *Stack:* Next.js 16, TypeScript, Supabase, DOKU

### 3. GSTC Certification Assistant · [Live](https://gstc.wisestepsconsulting.id/)
> Guided GSTC self-assessment and evidence review for destinations and accommodations, bilingual ID and EN.
- Used to run the firm's offline **GSTC training in Bandung** (22 to 23 Sep 2026) for 15 participants, including hotel general managers, managers and lecturers.
- Its first version served **ITDC Nusa Dua (InJourney Group)** from Oct 2025 to Feb 2026; the client's data moved into this platform in Oct 2026. Since Oct 2026 I supervise the intern on the GSTC v4.0 hotel update.

📌 *Stack:* Next.js 16, Supabase, Playwright, Vercel

### 4. Indonesia Tourism Stakeholder Platform (ITSP) · [sustainabletourism.id](https://www.sustainabletourism.id/)
> A national sustainable-tourism platform plus a community forum, one login across both, with Wise Steps Consulting and Wonderful Indonesia.
- Built the forum in about 4 weeks (Aug 2026, 55 merged PRs) as the main contributor, working with one intern.
- Website Carbon A (0.04 g CO2 per visit, cleaner than 91% of pages). Live; the next phase waits on funding.

📌 *Stack:* Next.js, Vite, React, TypeScript, Supabase

### 5. IMS LMFE Padjadjaran · handed over Jun 2026
> Internal management system for a research center at FEB Universitas Padjadjaran, an external client of the firm: workload capacity, KPI, projects and reporting, set up for about 32 staff.
- Delivered in about a month (May to Jun 2026), helped by an intern.

📌 *Stack:* Next.js 16, Supabase, Resend

### 6. Client ERP modules · go-live planned Dec 2026
> 13 modules in a client's ERP, go-live planned Dec 2026, delivered as Product Engineer (lead project).

📌 *Stack:* Laravel, PostgreSQL, Nuxt

### 🗄️ Archived and superseded

| Project | What it was | Status |
|---|---|---|
| **GSTC Nusa Dua Portal** | First version of the GSTC platform for ITDC Nusa Dua (Oct 2025 to Feb 2026) | Superseded by the GSTC Certification Assistant |
| **WIDI Hub** | National tourism carbon portal MVP for the Ministry of Tourism RI (Scope 1, 2 and waste Scope 3, GIS maps); prototype and concept for an emission calculator | Archived |
| **ITDC Nusa Dua ERMC** | Carbon and water MRV MVP for The Nusa Dua estate (GHG scopes, GRI 303) | Archived |
| **Tourism Events Impact Tracker** | Pre-sales mockup: Triple Bottom Line event-impact dashboard with illustrative mock data | [Archived mockup](https://dampakevent.wisestepsconsulting.web.id/) |
| **CEM, Voice of Customer** | Pre-sales mockup built in 5 days: survey to insight dashboard for hotels, malls and restaurants | [Archived mockup](https://cem-wsc.vercel.app/) |

---

## 🧑‍💼 Freelance

### Imperial Living booking and operations app · [imperialliving.id](https://imperialliving.id/)
> Booking, check-in, cleaning queue, payments and owner reports for an hourly apartment rental in Bandung (40 units, 4 unit owners).
- From brief to daily use in **about two weeks**; live since Oct 2026 and used by 15 people. Bookings moved from WhatsApp chats and Excel recaps into one app.
- Double booking blocked by the database, prices locked by a trigger, payments append-only; Website Carbon A+ (0.03 g CO2 per visit).

📌 *Stack:* Next.js 16, Supabase, Vercel

---

## 📊 Data analysis

### 🌏 7. [Evaneos "Indonesia 360": Booking Data Analysis](Evaneos_INDO360_Data_Analysis/)
> Data analyst work for an international client, Evaneos (Paris), within a Wise Steps Consulting sustainable-tourism study on overtourism and carbon emissions (2025, internship).
- Cleaned **about 29,000 raw booking records into 16,000+ analysis-ready rows (about 1,200 trips)** and built a keyword-based destination classifier over multilingual itinerary text.
- The published notebook is code only, with no client data or results, and runs on a fictional sample.

📌 *Tools:* Python, pandas, regex text classification, Excel

---

## 🧠 AI and data projects (code in this repository)

### 🧠 8. [Equifit: An AI-Powered Fitness Companion for Combating Obesity](https://github.com/CH2-PS090/machine-learning)
> Bangkit capstone: estimates body-fat percentage from a smartphone camera and gives personalized recommendations.
📌 *Tools:* Python, TensorFlow, Scikit-learn

### 🕌 9. [Sentiment Analysis of Halal Tourism Policy using Gemini LLM](Sentiment%20Analysis%20of%20Halal%20Tourism%20Policy%20using%20Gemini%20LLM/)
> Thesis project: Gemini 1.0 Pro evaluates public sentiment toward halal tourism policy in Bandung Regency (245 survey respondents, 95.93% accuracy).
📌 *Tools:* Google Gemini LLM, Prompt Engineering, Policy Research

### 💬 10. [Sentiment Analysis of Grab App Reviews](Grab_Sentimen_Analysis/)
> NLP pipeline over 112,501 Google Play reviews: scraping, slang normalization, TF-IDF and Word2Vec, then BiLSTM, Random Forest and Logistic Regression (90% test accuracy).
📌 *Tools:* Python, NLTK, Sastrawi, Gensim, scikit-learn, TensorFlow

### 🥕 11. [Vegetable Image Classification with CNNs](Vegetable_Image_Classification_with_CNNs/)
> CNN image classifier with 95% validation accuracy, exported to H5, SavedModel, TFLite and TensorFlow.js.
📌 *Tools:* TensorFlow, Keras, Computer Vision

### 🎓 12. [Student Dropout Prediction: Jaya Jaya Institute](FinalSubmit/)
> Applied data science final project: analysis of student data, a dropout prediction model, a Streamlit prototype and a business dashboard.
📌 *Tools:* Python, scikit-learn, Streamlit, dashboard

### 🧭 13. [Consulting Service Recommender Prototype](wsc/)
> Internship prototype at Wise Steps Consulting (Jul 2025): a Streamlit questionnaire that recommends the firm's consulting services, with a model trained on a synthetic dataset.
📌 *Tools:* Python, Streamlit, scikit-learn

### 🧮 14. [Accenture Data Analytics and Visualization Job Simulation](Accenture%20Data%20Analytics%20and%20Visualization%20Job%20Simulation/)
> Forage virtual internship: cleaned, modelled and analysed 7 datasets to advise a social-media client, with a final presentation.
📌 *Tools:* Excel, Data Visualization, Analytical Thinking

### 📈 15. [Jiwa Sehati: Digital Marketing Final Project](https://www.canva.com/design/DAGUjSf_yPY/ylTEmGD8cHmivt0Q4dWyYQ/edit?utm_content=DAGUjSf_yPY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
> A digital marketing campaign to boost brand awareness through social media strategy, SEO and creative content.
📌 *Tools:* Canva, Meta Ads, Copywriting, SEO

---

More about me: [rahadian.ai.id](https://www.rahadian.ai.id/) · [LinkedIn](https://www.linkedin.com/in/rahadianms/) · [Certificates](https://github.com/rahadianMs/MyCertificates).
If you would like to collaborate or discuss any of these projects, [reach out to me](mailto:rahadianms.work@gmail.com) or leave a ⭐ on your favorite repository!
