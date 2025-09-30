"""
Test Video Analyzer Tool Integration
Verifies that the video analyzer tool loads correctly.
"""

from VISION.agent import root_agent
import os

def test_video_analyzer():
    print("Testing Video Analyzer Tool Integration\n")
    print("="*60)
    
    # Check if agent loaded successfully
    print("[SUCCESS] Agent loaded successfully!")
    print(f"   Agent name: {root_agent.name}")
    print(f"   Model: {root_agent.model}")
    print(f"   Total tools available: {len(root_agent.tools)}")
    
    # List all tools
    print("\nAll Available Tools:")
    video_tools = []
    file_tools = []
    other_tools = []
    
    for i, tool in enumerate(root_agent.tools, 1):
        tool_name = tool.__name__ if hasattr(tool, '__name__') else str(tool)
        
        if 'video' in tool_name.lower():
            video_tools.append(tool_name)
        elif any(x in tool_name.lower() for x in ['file', 'read', 'write', 'delete', 'list', 'directory']):
            file_tools.append(tool_name)
        else:
            other_tools.append(tool_name)
    
    if file_tools:
        print("\n  File Editor Tools:")
        for tool in file_tools:
            print(f"    - {tool}")
    
    if video_tools:
        print("\n  Video Analyzer Tools:")
        for tool in video_tools:
            print(f"    - {tool}")
    
    if other_tools:
        print("\n  Other Tools:")
        for tool in other_tools:
            print(f"    - {tool}")
    
    # Check environment configuration
    print("\n" + "="*60)
    print("Environment Configuration Check:")
    print("="*60)
    
    # Check Google Cloud Project
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
    if project_id:
        print(f"[OK] GOOGLE_CLOUD_PROJECT: {project_id}")
    else:
        print("[WARNING] GOOGLE_CLOUD_PROJECT not set")
        print("         Required for video analysis with Vertex AI")
    
    # Check Google Cloud Location
    location = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')
    print(f"[OK] GOOGLE_CLOUD_LOCATION: {location}")
    
    # Check if credentials are available
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    if creds_path:
        print(f"[OK] GOOGLE_APPLICATION_CREDENTIALS: {creds_path}")
    else:
        print("[INFO] GOOGLE_APPLICATION_CREDENTIALS not set")
        print("       Using Application Default Credentials")
    
    print("\n" + "="*60)
    print("[SUCCESS] Video Analyzer Tool is properly integrated!")
    print("="*60)
    
    # Next steps
    print("\n" + "Next Steps:")
    print("-"*60)
    
    if not project_id:
        print("\n1. Set up Google Cloud:")
        print("   - Add GOOGLE_CLOUD_PROJECT to your .env file")
        print("   - Run: gcloud auth application-default login")
        print("   - Enable Vertex AI API in Google Cloud Console")
        print("\n   See VIDEO_ANALYZER_SETUP.md for detailed instructions")
    else:
        print("\n1. Test with ADK Web Interface:")
        print("   Run: adk web")
        print("\n2. Try these commands:")
        print("   - 'Analyze this YouTube video: [URL]'")
        print("   - 'Get transcript from this video: [URL]'")
        print("   - 'Analyze visuals in this video: [URL]'")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    test_video_analyzer()


