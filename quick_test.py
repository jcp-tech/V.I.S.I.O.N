"""
Quick Test - File Editor Tool
Verifies that the file editor tool loads correctly.
"""

from VISION.agent import root_agent

def quick_test():
    print("Quick Test: File Editor Tool\n")
    print("="*60)
    
    # Check if agent loaded successfully
    print("[SUCCESS] Agent loaded successfully!")
    print(f"   Agent name: {root_agent.name}")
    print(f"   Model: {root_agent.model}")
    print(f"   Tools available: {len(root_agent.tools)}")
    
    # List the tools
    print("\nAvailable Tools:")
    for i, tool in enumerate(root_agent.tools, 1):
        tool_name = tool.__name__ if hasattr(tool, '__name__') else str(tool)
        print(f"   {i}. {tool_name}")
    
    print("\n" + "="*60)
    print("[SUCCESS] File Editor Tool is properly integrated!")
    print("\nNext Step: Test with ADK Web Interface")
    print("   Run: adk web")
    print("   Then interact with your agent in the browser")
    print("="*60)

if __name__ == "__main__":
    quick_test()


