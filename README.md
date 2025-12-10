# SEO Content Analyzer

AWS serverless application that analyzes web content for SEO optimization using AI (Claude 3 via Amazon Bedrock).

## 🎯 Project Overview

This tool analyzes website content (blog posts, product descriptions, landing pages) and provides actionable SEO recommendations including keyword analysis, readability assessment, and meta tag suggestions.

**Why I built this:** As a marketing professional with SEO experience, I wanted to combine my marketing expertise with cloud technology to create an AI-powered tool that automates content analysis.

## Why Build This vs. Using Claude Directly?

**Current State (MVP):** This project demonstrates technical capability to integrate AI into marketing workflows using AWS serverless architecture.

**Future Value If Further Developed:** 
- Batch processing of multiple pages
- CMS/WordPress integration for automated audits
- Historical tracking and trend analysis
- Team collaboration and standardized analysis
- Custom brand voice training
- Cost optimization through caching and smart routing

**Portfolio Purpose:** Showcases ability to architect AI-powered marketing solutions and bridge the gap between marketing strategy and technical implementation.

## 🏗️ Architecture

- **AWS Lambda** (Python 3.12): Core processing logic
- **Amazon Bedrock** (Claude 3 Haiku): AI-powered content analysis
- **API Gateway (REST API): Public endpoint with rate limiting and throttling**
- **IAM**: Secure permissions management
- **CloudWatch**: Monitoring,logging, billing alarms

## ✨ Features

- Analyzes text content for SEO optimization
- Identifies primary keywords and keyword density
- Assesses readability
- Suggests optimized title tags and meta descriptions
- Provides 5+ actionable recommendations
- Handles content up to 5,000 characters
- Returns structured JSON responses

## 🚀 How It Works

1. User submits content via Lambda test console or API Gateway
2. Lambda function receives and validates content
3. Formats prompt and calls Bedrock API (Claude 3 Haiku)
4. Claude analyzes content and returns SEO recommendations
5. Lambda returns structured JSON response with analysis


## 🧪 Testing


**Example test event:**
```json
{
  "content": "Your webpage or blog content here..."
}
```

**Example response:**
```json
{
  "analysis": {
    "keyword_analysis": {...},
    "readability": {...},
    "title_tag": {...},
    "meta_description": {...},
    "top_recommendations": [...]
  },
  "metadata": {
    "content_length": 373,
    "model": "claude-3-haiku"
  }
}
```

## 🎓 What I Learned

- AWS Lambda function development and deployment
- Amazon Bedrock integration and AI prompt engineering
- IAM role and policy configuration
- Serverless architecture patterns
- Cost optimization strategies
- JSON data structure handling in Python

## 🔮 Future Enhancements

### Phase 3: Frontend Interface
- [ ] Build simple HTML/JS interface
- [ ] Host on S3 + CloudFront
- [ ] Form for content submission
- [ ] Formatted display of results

### Phase 4: Advanced Features
- [ ] DynamoDB caching for repeated analyses
- [ ] URL fetching (analyze any webpage directly)
- [ ] Competitor comparison mode
- [ ] Historical tracking of content improvements
- [ ] Export results as PDF report

### Phase 5: Cost Optimization
- [ ] Implement result caching in DynamoDB
- [ ] Add request throttling
- [ ] CloudWatch cost monitoring dashboard
- [ ] Billing alerts
