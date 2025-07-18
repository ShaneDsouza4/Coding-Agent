import shutil
import subprocess
import os

def run_command(input):
    """Execute a shell command and return its output."""
    command = input.get("command")
    if not isinstance(command, str) or not command.strip():
        raise ValueError("A valid 'command' string is required.")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, command, result.stderr)
    return result.stdout.strip()


def run_command_stream_output(input):
    """Execute a command and stream its output in real-time."""
    command = input.get("command")
    cwd = os.path.abspath(input.get("cwd", "."))

    if not isinstance(command, str) or not command.strip():
        raise ValueError("A valid 'command' string is required.")

    if not os.path.isdir(cwd):
        raise NotADirectoryError(f"Invalid working directory: {cwd}")

    process = subprocess.Popen(
        command, shell=True, cwd=cwd,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    output_lines = []
    for line in process.stdout:
        line = line.strip()
        if line:
            print(line)
            output_lines.append(line)

    process.wait()
    return "\n".join(output_lines)


def run_background_process(input):
    """Start a command in a new terminal window (Windows only)."""
    command = input.get("command")
    cwd = os.path.abspath(input.get("cwd", "."))

    if not isinstance(command, str) or not command.strip():
        raise ValueError("A valid 'command' string is required.")

    if not os.path.isdir(cwd):
        raise NotADirectoryError(f"Invalid working directory: {cwd}")

    try:
        subprocess.Popen(
            f'start cmd /k "{command}"',
            cwd=cwd,
            shell=True
        )
        return f"Background process started in new terminal: {command}"
    except Exception as e:
        return f"Failed to start process: {e}"


def check_command_exists(input):
    """Check if a shell command exists in PATH."""
    command = input if isinstance(input, str) else input.get("command")
    return shutil.which(command) is not None


def install_angular_cli(_input=None):
    """Install Angular CLI globally via npm."""
    return run_command({"command": "npm install -g @angular/cli"})


def create_angular_project(input):
    """Create an Angular project using Angular CLI."""
    name = input.get("name") if isinstance(input, dict) else input
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Project name must be a non-empty string.")
    return run_command_stream_output({"command": f"ng new {name} --defaults"})


def create_react_project(input):
    """Create a React project using Create React App."""
    name = input.get("name") if isinstance(input, dict) else input
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Project name must be a non-empty string.")
    if not check_command_exists("npx"):
        raise EnvironmentError("npx is not installed.")
    return run_command_stream_output({"command": f"npx create-react-app {name}"})


def generate_angular_entity(input):
    """
    Generate an Angular entity (component, service, etc.).
    Required keys: entity_type, name
    Optional keys: cwd (default '.'), options (default '')
    """
    if not isinstance(input, dict):
        raise ValueError("Input must be a dictionary.")

    entity_type = input.get("entity_type")
    name = input.get("name")
    cwd = os.path.abspath(input.get("cwd", "."))
    options = input.get("options", "")

    valid_types = [
        "component", "service", "module", "pipe",
        "directive", "guard", "interface", "class", "enum"
    ]

    if not entity_type or not name:
        raise ValueError("Both 'entity_type' and 'name' are required.")
    if entity_type not in valid_types:
        raise ValueError(f"Invalid entity_type '{entity_type}'. Must be one of: {', '.join(valid_types)}")

    command = f"ng generate {entity_type} {name} {options}".strip()
    return run_command_stream_output({"command": command, "cwd": cwd})
