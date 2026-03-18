\# System Design



\## Architecture

ESP32 → Edge Processing → Backend API → Database → Dashboard



\## Components

\- Temperature (Potentiometer)

\- Light (LDR)

\- Motion (PIR)

\- Output: LED + Buzzer



\## Edge Logic

\- High temperature

\- Low light

\- No motion → Stress HIGH



\## GPIO Mapping

\- GPIO34 → Temperature

\- GPIO35 → Light

\- GPIO32 → Motion

\- GPIO25 → LED

\- GPIO26 → Buzzer

