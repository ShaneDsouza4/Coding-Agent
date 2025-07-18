🤖 **Terminal Based Coding Agent**  

An AI powered coding assistant that runs entirely in your terminal. Built to understand what you want to create, from scripts to components to full apps, and bring it to life through structured planning and real code generation.

Inspired by tools like Cursor and Windsurf, this agent brings a minimalist, terminal-based way to collaborate with an LLM.

---

🧰 Tools Used  
- **OpenAI API** – Drives the assistant’s reasoning, planning, and code generation.  
- **Python** – Core engine powering the control loop and tool integrations.  
- **Filesystem I/O** – Reads, writes, updates, and inspects your codebase.  
- **Terminal UI** – All interaction is handled directly through the command line.  

---

🎯 Project Focus  
This project showcases:

- How to build a terminal-based code assistant using LLMs  
- A structured prompting system (`analyse`, `plan`, `generate`, `think-on-user`)  
- Real tool integrations (`write_file`, `update_file`, `search_in_file`, etc.)  
- Reliable, JSON-formatted communication via OpenAI’s function calling  

---

🔒 Security Notes  
- Commands are executed within the workspace directory, always review what’s being run.  
- Avoid using this agent to control production systems or sensitive environments.  
- API credentials are expected via a `.env` file — **do not** expose it in public repos.  

---

📚 Usage Tips  
- **Be Clear**: The more specific your instructions, the better the results.  
- **Start Small**: Build up functionality incrementally.  
- **Inspect Outputs**: Use tools like `read_file` and `list_files` to verify changes.  
- **Work in Steps**: Break down complex builds into manageable stages.  
- **Mind the Path**: All file paths are relative to the agent’s workspace directory.  
