import json
import boto3
import hashlib
from datetime import datetime

# Initialize Bedrock client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    """
    Main Lambda function that analyzes content for SEO
    """
    
    try:
        # Get content from the request
        # When testing in console, you'll pass this in the test event
        if 'body' in event:
            body = json.loads(event['body'])
        else:
            body = event
            
        content = body.get('content', '')
        
        # Validate we have content
        if not content or len(content.strip()) == 0:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No content provided'})
            }
        
        # Truncate if content is too long (to manage costs)
        if len(content) > 5000:
            content = content[:5000]
            truncated = True
        else:
            truncated = False
        
        # Create the prompt for Claude
        prompt = f"""Analyze the following content for SEO optimization and provide actionable recommendations.

Content to analyze:
{content}

Please provide a comprehensive SEO analysis in the following JSON format:
{{
  "keyword_analysis": {{
    "primary_keywords": ["list of 3-5 main keywords/phrases found"],
    "keyword_density_issues": "brief assessment of keyword usage"
  }},
  "readability": {{
    "score": "simple assessment like 'Good', 'Needs Improvement', or 'Excellent'",
    "issues": ["list of readability problems if any"]
  }},
  "title_tag": {{
    "current": "extract if present, otherwise 'Not found'",
    "suggestion": "improved title under 60 characters"
  }},
  "meta_description": {{
    "current": "extract if present, otherwise 'Not found'",
    "suggestion": "improved meta description under 155 characters"
  }},
  "content_structure": {{
    "headings_assessment": "brief comment on heading structure",
    "paragraph_assessment": "brief comment on paragraph length"
  }},
  "top_recommendations": [
    "specific actionable recommendation 1",
    "specific actionable recommendation 2",
    "specific actionable recommendation 3",
    "specific actionable recommendation 4",
    "specific actionable recommendation 5"
  ]
}}

Provide ONLY the JSON object, no additional text."""

        # Call Bedrock with Claude
        response = bedrock.invoke_model(
            modelId='anthropic.claude-3-haiku-20240307-v1:0',
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                'anthropic_version': 'bedrock-2023-05-31',
                'max_tokens': 2000,
                'messages': [
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            })
        )
        
        # Parse the response
        response_body = json.loads(response['body'].read())
        claude_response = response_body['content'][0]['text']
        
        # Try to parse Claude's JSON response
        try:
            analysis = json.loads(claude_response)
        except json.JSONDecodeError:
            # If Claude didn't return pure JSON, wrap the text response
            analysis = {
                'raw_analysis': claude_response,
                'note': 'Response was not in JSON format'
            }
        
        # Add metadata
        result = {
            'analysis': analysis,
            'metadata': {
                'content_length': len(content),
                'truncated': truncated,
                'timestamp': datetime.utcnow().isoformat(),
                'model': 'claude-3-haiku'
            }
        }
        
        # Return success
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # For CORS if you add a frontend later
            },
            'body': json.dumps(result, indent=2)
        }
        
    except Exception as e:
        # Handle any errors
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }
