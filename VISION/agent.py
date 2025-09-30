from google.adk.agents import BaseAgent, Agent, LlmAgent, SequentialAgent, LoopAgent, ParallelAgent
from google.adk.tools.mcp_tool.mcp_toolset import (
    MCPToolset,
    # StdioConnectionParams,
    StdioServerParameters
)
from .custom_utils.enviroment_interaction import load_instruction_from_file
from .tools.fileEditor import (
    read_file,
    write_file,
    delete_file,
    list_directory,
    create_directory,
    get_file_info
)
from .tools.videoAnalyzer import (
    analyze_video,
    analyze_video_transcript_only,
    analyze_video_visuals_only,
    analyze_video_with_custom_prompt
)
from dotenv import load_dotenv
# import asyncio
import os

load_dotenv()

MODEL = os.getenv('GOOGLE_GENAI_MODEL', 'gemini-2.0-flash')

GITHUB_PAT = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')

# Only create GitHub MCP toolset if token is available
copilot_toolset = None
if GITHUB_PAT:
    copilot_toolset = MCPToolset(
        connection_params=StdioServerParameters(
            command="docker",
            args=[
                "run",
                "-i",
                "--rm",
                "-e",
                "GITHUB_PERSONAL_ACCESS_TOKEN",
                "ghcr.io/github/github-mcp-server"
            ],
            env={
                "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_PAT
            },
        ),
        # tool_filter=[] # Optional: ensure only specific tools are loaded
    )

root_agent = LlmAgent(
    model=MODEL,
    name='root_agent',
    # description='A helpful assistant for user questions.',
    # instruction='Answer user questions to the best of your knowledge',
    instruction=load_instruction_from_file("code_mcp.prompt", subs={}),
    tools=[
        # File Editor Tools
        read_file,
        write_file,
        delete_file,
        list_directory,
        create_directory,
        get_file_info,
        # Video Analyzer Tools
        analyze_video,
        analyze_video_transcript_only,
        analyze_video_visuals_only,
        analyze_video_with_custom_prompt
    ]
)
