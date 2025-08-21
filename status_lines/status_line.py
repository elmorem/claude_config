
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import json
import os
import sys
import subprocess
import re
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional


def log_status_line(input_data, status_line_output):
    """Log status line event to logs directory."""
    # Ensure logs directory exists
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / 'status_line.json'
    
    # Read existing log data or initialize empty list
    if log_file.exists():
        with open(log_file, 'r') as f:
            try:
                log_data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                log_data = []
    else:
        log_data = []
    
    # Create log entry with input data and generated output
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input_data": input_data,
        "status_line_output": status_line_output
    }
    
    # Append the log entry
    log_data.append(log_entry)
    
    # Write back to file with formatting
    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=2)


def get_git_branch():
    """Get current git branch if in a git repository."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def get_git_status():
    """Get git status indicators."""
    try:
        # Check if there are uncommitted changes
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            changes = result.stdout.strip()
            if changes:
                lines = changes.split('\n')
                return f"±{len(lines)}"
    except Exception:
        pass
    return ""


def get_docker_status():
    """Get Docker container status."""
    try:
        result = subprocess.run(
            ['docker', 'compose', 'ps', '--services', '--filter', 'status=running'],
            capture_output=True,
            text=True,
            timeout=3
        )
        if result.returncode == 0:
            running = result.stdout.strip().split('\n') if result.stdout.strip() else []
            if running:
                return f"🐳{len(running)}"
    except Exception:
        pass
    return ""


def get_test_status():
    """Get last test status from logs or recent commands."""
    try:
        # Check for common test result files
        test_files = [
            '.coverage',
            'coverage.xml',
            'pytest.xml',
            'test-results.xml',
            'frontend/coverage/lcov.info'
        ]
        
        latest_test = None
        for test_file in test_files:
            if os.path.exists(test_file):
                stat = os.stat(test_file)
                if not latest_test or stat.st_mtime > latest_test:
                    latest_test = stat.st_mtime
        
        if latest_test:
            # Simple indicator that tests were run recently (within last hour)
            import time
            if time.time() - latest_test < 3600:
                return "✅"
        
        return "❓"
    except Exception:
        pass
    return ""


def get_django_status():
    """Check Django application status for FowlData backend."""
    try:
        # Check if Django containers are running
        docker_result = subprocess.run(
            ['docker', 'compose', 'ps', '--format', 'json'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if docker_result.returncode == 0:
            containers = []
            for line in docker_result.stdout.strip().split('\n'):
                if line.strip():
                    try:
                        container = json.loads(line)
                        if container.get('State') == 'running':
                            containers.append(container.get('Service', ''))
                    except json.JSONDecodeError:
                        pass
            
            # Check for specific FowlData services
            fowldata_running = 'fowldata' in containers
            db_running = any('db' in svc or 'postgres' in svc for svc in containers)
            
            if fowldata_running and db_running:
                return "🦆✅"  # Duck emoji for FowlData + checkmark
            elif fowldata_running:
                return "🦆⚠️"  # Django running but DB issues
            elif containers:
                return "🐳📦"  # Some containers running
                
        return "🔴"
    except Exception:
        pass
    return ""


def get_nextjs_status():
    """Check Next.js frontend status for FowlData."""
    try:
        # Check if Next.js is running on port 3000
        result = subprocess.run(
            ['lsof', '-i', ':3000'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0 and ('node' in result.stdout.lower() or 'next' in result.stdout.lower()):
            return "⚛️✅"  # React + checkmark
        
        # Check if frontend directory exists and has package.json
        frontend_dir = Path('frontend')
        if frontend_dir.exists() and (frontend_dir / 'package.json').exists():
            return "⚛️💤"  # React + sleeping (ready but not running)
            
        return "⚛️❓"  # React + question mark
    except Exception:
        pass
    return ""


def get_fowldata_shortcuts():
    """Get FowlData-specific development shortcuts and reminders."""
    shortcuts = []
    
    # Check if in FowlData project directory
    if os.path.exists('manage.py') or os.path.exists('frontend/package.json'):
        # Check if containers need to be rebuilt (simplified check)
        if os.path.exists('docker-compose.yml'):
            shortcuts.append("💡docker up")
        
        # Check if test files exist
        if os.path.exists('testlint-quick'):
            shortcuts.append("🧪quick")
        
        if os.path.exists('testlint'):
            shortcuts.append("🔬full")
    
    return " ".join(shortcuts) if shortcuts else ""


def get_environment_indicator():
    """Get environment indicator from various sources."""
    # Check environment variables
    env_indicators = {
        'development': '🟡',
        'dev': '🟡', 
        'staging': '🟠',
        'production': '🔴',
        'prod': '🔴',
        'local': '🟢'
    }
    
    # Check common environment variables
    env_vars = ['NODE_ENV', 'DJANGO_ENV', 'ENVIRONMENT', 'ENV']
    for var in env_vars:
        env_value = os.getenv(var, '').lower()
        if env_value in env_indicators:
            return env_indicators[env_value]
    
    # Default to local development
    return '🟢'


def truncate_text(text, max_length=50):
    """Truncate text to max length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."


def get_prompt_info(input_data):
    """Extract current and previous prompt information."""
    current_prompt = ""
    previous_prompt = ""
    
    try:
        # Get current prompt from input_data
        messages = input_data.get('messages', [])
        if messages:
            # Find the last user message
            for msg in reversed(messages):
                if msg.get('role') == 'user':
                    content = msg.get('content', '')
                    if isinstance(content, str):
                        current_prompt = content
                    elif isinstance(content, list):
                        # Handle list of content parts
                        text_parts = [part.get('text', '') for part in content if part.get('type') == 'text']
                        current_prompt = ' '.join(text_parts)
                    break
            
            # Find the second-to-last user message for previous
            user_messages = [msg for msg in messages if msg.get('role') == 'user']
            if len(user_messages) > 1:
                prev_msg = user_messages[-2]
                content = prev_msg.get('content', '')
                if isinstance(content, str):
                    previous_prompt = content
                elif isinstance(content, list):
                    text_parts = [part.get('text', '') for part in content if part.get('type') == 'text']
                    previous_prompt = ' '.join(text_parts)
    except Exception:
        pass
    
    return current_prompt, previous_prompt


def generate_status_line(input_data):
    """Generate the FowlData-specific status line based on input data."""
    parts = []
    
    # Model display name
    model_info = input_data.get('model', {})
    model_name = model_info.get('display_name', 'Claude')
    parts.append(f"\033[36m[{model_name}]\033[0m")  # Cyan color
    
    # Project name indicator for FowlData
    workspace = input_data.get('workspace', {})
    current_dir = workspace.get('current_dir', '')
    if current_dir:
        dir_name = os.path.basename(current_dir)
        if 'fowldata' in dir_name.lower():
            parts.append(f"\033[34m🦆 FowlData\033[0m")  # Blue with duck emoji
        else:
            parts.append(f"\033[34m📁 {dir_name}\033[0m")  # Blue color
    
    # Git branch and status
    git_branch = get_git_branch()
    if git_branch:
        git_status = get_git_status()
        git_info = f"🌿 {git_branch}"
        if git_status:
            git_info += f" {git_status}"
        parts.append(f"\033[32m{git_info}\033[0m")  # Green color
    
    # Django backend status
    django_status = get_django_status()
    if django_status:
        parts.append(f"\033[91m{django_status}\033[0m")  # Light red
    
    # Next.js frontend status
    nextjs_status = get_nextjs_status()
    if nextjs_status:
        parts.append(f"\033[94m{nextjs_status}\033[0m")  # Light blue
    
    # Docker status (general container count)
    docker_status = get_docker_status()
    if docker_status:
        parts.append(f"\033[96m{docker_status}\033[0m")  # Light cyan
    
    # Test status
    test_status = get_test_status()
    if test_status:
        parts.append(f"\033[92m{test_status}\033[0m")  # Light green
    
    # FowlData development shortcuts
    shortcuts = get_fowldata_shortcuts()
    if shortcuts:
        parts.append(f"\033[93m{shortcuts}\033[0m")  # Yellow
    
    # Environment indicator
    env_indicator = get_environment_indicator()
    parts.append(f"\033[93m{env_indicator}\033[0m")  # Yellow color
    
    # Current and previous prompts (shorter for more compact display)
    current_prompt, previous_prompt = get_prompt_info(input_data)
    if current_prompt:
        truncated_current = truncate_text(current_prompt, 25)
        parts.append(f"\033[95m💬 {truncated_current}\033[0m")  # Magenta
    
    # Version info (optional, smaller)
    version = input_data.get('version', '')
    if version:
        parts.append(f"\033[90mv{version}\033[0m")  # Gray color
    
    return " | ".join(parts)


def main():
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())
        
        # Generate status line
        status_line = generate_status_line(input_data)
        
        # Log the status line event
        log_status_line(input_data, status_line)
        
        # Output the status line (first line of stdout becomes the status line)
        print(status_line)
        
        # Success
        sys.exit(0)
        
    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully - output basic status
        print("\033[31m[Claude] 📁 Unknown\033[0m")
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully - output basic status
        print("\033[31m[Claude] 📁 Error\033[0m")
        sys.exit(0)


if __name__ == '__main__':
    main()
