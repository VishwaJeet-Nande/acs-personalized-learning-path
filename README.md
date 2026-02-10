# ACS 2.0 – Intelligent Academic Communication System

ACS 2.0 is a smart academic intervention system designed to analyze student attendance data, identify academic risk levels, generate personalized learning paths, and automatically communicate with students and parents using real-time email notifications.

This system helps educational institutions move from **manual attendance tracking** to **intelligent academic decision-making**.

---

## 🚀 Features

- 📊 Attendance analysis (subject-wise & week-wise)
- 📈 Trend detection (Improving / Declining performance)
- ⚠️ Risk classification (Low / Medium / High)
- 🧠 Personalized learning path generation
- ✅ Academic committee approval workflow
- 📧 Live email communication to students & parents
- 🗂 Communication audit logs
- 🎨 Modern dashboard UI with dark theme

---

## 🏗 System Workflow

1. **Upload Attendance File**
   - Teacher uploads Excel / CSV attendance data
2. **Data Processing**
   - Attendance is analyzed subject-wise
   - Average attendance & trends are calculated
3. **Risk Evaluation**
   - Students are classified using rule-based logic
4. **Approval Stage**
   - Academic committee reviews & approves communication
5. **Communication**
   - Personalized emails sent to students & parents
6. **Logs**
   - All communications are logged for audit

---

## 📁 Attendance File Format

The uploaded Excel / CSV file must contain the following columns:

| Column Name      | Description                          |
|------------------|--------------------------------------|
| name             | Student name                         |
| student_email    | Student email address                |
| parent_email     | Parent email address                 |
| subject          | Subject name                         |
| week             | Week number                          |
| attendance       | Attendance percentage (0–100)        |

---

## 🧠 Risk Logic (Example)

- **Low Risk**: Average attendance ≥ 75%
- **Medium Risk**: Average attendance between 60–74%
- **High Risk**: Average attendance < 60%

Learning paths are enhanced with:
- Weak subject identification
- Performance improvement trends

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS (Custom UI)
- **Backend**: Python (Flask)
- **Data Processing**: Pandas
- **Email**: SMTP (Gmail)
- **Storage**: CSV / Excel
- **Session Handling**: Flask Sessions

---

## 🔐 Email Configuration

Emails are sent using Gmail SMTP.

Create a `.env` file (not committed to Git):

```env
EMAIL_ADDRESS=jeetworkspace1@gmail.com
EMAIL_PASSWORD=oxlxzhoxbzzfgmgn
