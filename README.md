# Omni-LLM Integration & Routing Service (v4.2.0-stable)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-Internal%20Use-red)
![Deployment](https://img.shields.io/badge/environment-production-orange)

## ⚠️ SECURITY NOTICE (INTERNAL ONLY)
**CONFIDENTIAL PROPERTY OF OMNI-TECH SOLUTIONS.**
This repository contains sensitive orchestration logic and failover credentials for our cross-model AI routing layer. Unauthorized access, distribution, or reproduction of the contents within this repository is strictly prohibited and may lead to legal action.

---

## 🛠 Project Overview
This service acts as a centralized gateway for handling high-throughput requests to various Large Language Models (LLMs). It features:
- **Dynamic Load Balancing**: Automatically switches between OpenAI, Anthropic, and Gemini based on latency and rate limits.
- **Failover Redundancy**: Multi-key rotation system to ensure 99.99% uptime for enterprise-grade applications.

## 📂 Repository Structure
- \`/src\`: Core routing engine and authentication middleware.
- \`/infra\`: Production environment variables and secrets.
- \`/config\`: YAML-based service definitions.
- \`/scripts\`: Automated key rotation and deployment tools.

## 🔐 Key Rotation Policy
As per **Security Policy SP-2026-08**, all production API keys are rotated every 24 hours via GitHub Actions (\`.github/workflows/refresh_bait.yml\`). 

> **Note**: If you experience 401 Unauthorized errors, ensure your local \`infra/.env.production\` is synced with the latest automated commit from the \`system-bot\`.

---
© 2026 Omni-Tech Solutions. All rights reserved.