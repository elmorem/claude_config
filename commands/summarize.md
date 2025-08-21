Please generate a comprehensive session summary following this structure:

  1. **Analyze This Session**: Review our conversation history and identify:
     - All tasks completed
     - Key decisions made
     - Files created/modified
     - Problems solved
     - Technical insights gained

  2. **Current State Assessment**: Determine:
     - Project current status
     - Active technology stack
     - Architecture decisions in place
     - Testing approach
     - Known issues or blockers

  3. **Context Compaction**: Distill the most important information that would
   help in future sessions:
     - Critical implementation details
     - Important patterns established
     - Performance considerations
     - Security implementations

  4. **Roadmap Update**: Based on current progress, identify:
     - Immediate next steps for next session
     - Short-term goals (1-2 weeks)
     - Medium-term objectives (1 month)
     - Dependencies and blockers

  5. **Generate File**: Create a file in TODO directory named
  `summary-YYYY-MM-DD-HHMMSS.md` with the following structure:

  ---

  # Session Summary - [Date/Time]
  *Generated: [timestamp]*

  ## 🎯 Session Objectives
  [What we set out to accomplish this session]

  ## ✅ Work Completed
  ### Major Accomplishments
  - [Key features/fixes implemented]
  - [Important decisions made]
  - [Problems solved]

  ### Technical Details
  - **Files Modified**: [list with brief descriptions]
  - **New Components**: [components created]
  - **Dependencies**: [added/updated packages]
  - **Configuration Changes**: [environment/config updates]

  ## 🧠 Key Insights & Decisions
  - [Important architectural decisions]
  - [Performance considerations]
  - [Security implementations]
  - [Design patterns used]

  ## 📋 Current Task Status
  ### Completed
  - [x] [Completed tasks from todo list]

  ### In Progress
  - [ ] [Tasks currently being worked on]

  ### Pending
  - [ ] [Queued tasks]

  ## 🗺️ Updated Roadmap
  ### Immediate Next Steps (Next Session)
  1. [Highest priority items]
  2. [Dependencies that need resolution]

  ### Short-term Goals (Next 1-2 weeks)
  - [Feature completions]
  - [Testing milestones]

  ### Medium-term Objectives (Next month)
  - [Major feature additions]
  - [Performance optimizations]

  ## 🔧 Technical Context
  ### Project Structure
  - **Tech Stack**: [current technologies]
  - **Architecture**: [key architectural decisions]
  - **Testing Strategy**: [current testing approach]

  ### Environment & Setup
  - **Development**: [dev environment details]
  - **Dependencies**: [critical dependencies]
  - **Build Process**: [current build/deploy process]

  ## 🚨 Known Issues & Blockers
  - [Current blockers requiring attention]
  - [Technical debt identified]
  - [Performance issues noted]

  ## 💡 Recommendations for Next Session
  1. [Specific actions to take immediately]
  2. [Areas needing investigation]
  3. [Optimization opportunities]

  ## 📝 Session Metadata
  - **Duration**: [estimated session length]
  - **Tools Used**: [primary tools/agents utilized]
  - **Code Quality**: [linting/testing status]
  - **Git Status**: [branch/commit information]

  ---

  Please ensure the TODO directory exists before creating the file. Use the
  current date and time for the filename in format:
  summary-YYYY-MM-DD-HHMMSS.md

  Purpose

  This command serves as a session bridge that:
  - Preserves critical context between sessions
  - Maintains project momentum
  - Provides clear next-step guidance
  - Creates searchable project history
  - Prevents loss of important decisions and insights

  Best Practices

  - Run at the end of significant work sessions
  - Use when switching between different projects
  - Generate before taking breaks from a project
  - Create after major architectural decisions
  - Run before important milestones or releases

  File Location

  Files are created in: TODO/summary-YYYY-MM-DD-HHMMSS.md

  Integration

  This command works best when combined with:
  - Regular todo list updates
  - Git commit summaries
  - Project documentation
  - Architecture decision records
