# Read Summary Command

  ## Command Name: `/read-summary`

  ### Description
  Reads and processes session summary files to restore project context,
  understand previous work, and establish continuity from past sessions. This
  command helps Claude quickly understand project state, decisions made, and
  next steps when starting a new session.

  ### Usage
  ```bash
  /read-summary [filename]
  /read-summary [latest]
  /read-summary [date-pattern]

  Examples:
  - /read-summary - Reads the most recent summary file
  - /read-summary latest - Same as above
  - /read-summary summary-2025-01-15-143022.md - Reads specific file
  - /read-summary 2025-01-15 - Reads latest summary from that date

  Implementation

  Prompt for Claude:

  Please read and process the session summary file following this protocol:

  1. **File Location & Selection**:
     - Look in the TODO directory for summary files
     - If no filename specified, find the most recent summary-*.md file
     - If date pattern provided, find the latest file matching that date
     - If specific filename provided, read that exact file

  2. **Parse Summary Structure**:
     - Extract session objectives and what was accomplished
     - Identify current project state and technical context
     - Note completed, in-progress, and pending tasks
     - Understand key architectural decisions and patterns
     - Review known issues and blockers

  3. **Context Integration**:
     - Absorb the technical context (tech stack, architecture, testing)
     - Understand the development environment and setup
     - Note critical dependencies and build processes
     - Identify important patterns and design decisions

  4. **Roadmap Analysis**:
     - Review immediate next steps identified in previous session
     - Understand short-term and medium-term goals
     - Identify any dependencies or blockers that need attention
     - Note recommendations from previous session

  5. **Current State Assessment**:
     - Determine where the project stands now vs. when summary was created
     - Check if any immediate next steps have been completed
     - Identify if any blockers have been resolved
     - Assess if roadmap needs updating

  6. **Provide Contextualized Response**:
     After reading the summary, provide a response in this format:

     ## 📖 Summary Loaded: [filename]
     *From session: [date/time]*

     ### 🎯 Previous Session Recap
     [Brief summary of what was accomplished]

     ### 🔧 Current Technical Context
     - **Tech Stack**: [technologies in use]
     - **Architecture**: [key architectural decisions]
     - **Last Known State**: [project status when summary was created]

     ### 📋 Task Continuity
     #### From Previous Session:
     - **Completed**: [tasks that were done]
     - **In Progress**: [tasks that were being worked on]
     - **Planned Next Steps**: [what was planned for next session]

     ### 🗺️ Recommended Actions
     Based on the summary, here's what I recommend for this session:
     1. [Immediate priority items]
     2. [Items to verify/check]
     3. [Next logical development steps]

     ### ❓ Context Questions
     To ensure I have complete context:
     - [Questions about current state vs. summary]
     - [Clarifications needed about recent changes]
     - [Verification of assumptions from summary]

     ### 🚀 Ready to Proceed
     I'm now contextualized with your project state. What would you like to 
  work on?

  7. **Error Handling**:
     - If no summary files found, explain how to create one
     - If file is corrupted or unreadable, suggest alternatives
     - If multiple files match pattern, list options for user to choose

  8. **Integration with Current Session**:
     - Immediately update any todo lists based on summary roadmap
     - Prepare to continue from where previous session left off
     - Be ready to verify current state against summary expectations

  Purpose

  This command serves as a session bridge that:
  - Restores context from previous work sessions
  - Eliminates need to re-explain project details
  - Maintains development momentum across time gaps
  - Provides immediate actionable next steps
  - Ensures continuity of architectural decisions

  File Discovery Logic

  1. Default behavior: Find most recent summary-*.md in TODO directory
  2. Specific file: Read exact filename if provided
  3. Date pattern: Match partial dates (e.g., "2025-01-15" finds latest from
  that day)
  4. Latest keyword: Explicitly request most recent file

  Integration Benefits

  This command works optimally when:
  - Used at the start of new development sessions
  - Combined with current codebase analysis
  - Followed by verification of current project state
  - Integrated with existing todo lists and task management

  Best Practices

  - Always run first when resuming work on a project
  - Verify assumptions from summary against current codebase
  - Update roadmaps if project state has changed
  - Ask clarifying questions if summary seems outdated
  - Cross-reference with git history and recent commits

  Error Recovery

  If summary files are missing or corrupted:
  1. Suggest creating a new baseline summary
  2. Analyze current codebase to establish context
  3. Work with user to reconstruct recent project history
  4. Create fresh roadmap based on current state

  Output Format

  The command should always provide:
  - Clear indication of which summary was loaded
  - Structured recap of previous session
  - Current technical context understanding
  - Actionable next steps
  - Questions to verify current state
