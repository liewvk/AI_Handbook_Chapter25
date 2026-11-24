# AI Handbook — Chapter 25

A collection of Python examples for **Chapter 25** of the AI Handbook. The repository demonstrates small, self-contained examples related to multi-agent workflows and simple automated evaluation.

## Contents

- `AI_Handbook_Chapter25.py` — main project entry point
- `example_25_1.py` through `example_25_11.py` — chapter examples
- `AI_Handbook_Chapter25.pyproj` — Visual Studio Python project configuration
- `AI_Handbook_Chapter25.slnx` — Visual Studio solution file

## Requirements

- Python 3
- No third-party packages are required for the included examples

## Getting started

Clone the repository:

```bash
git clone https://github.com/liewvk/AI_Handbook_Chapter25.git
cd AI_Handbook_Chapter25
```

Run the main entry point:

```bash
python AI_Handbook_Chapter25.py
```

Run an individual example:

```bash
python example_25_11.py
```

## Example highlights

The examples use plain Python functions to illustrate concepts such as:

- Coordinating research, writing, and review stages
- Passing structured information between workflow steps
- Checking generated output against source facts
- Calculating and reporting success rates

For example, `example_25_11.py` demonstrates a small workflow that gathers facts, writes a draft, and returns an approved or rejected result:

```bash
python example_25_11.py
```

The project is configured in Visual Studio with `example_25_11.py` as its startup file.

## Running in Visual Studio

Open `AI_Handbook_Chapter25.slnx` in Visual Studio, select a Python interpreter, and run the project. You can also set any example script as the startup file.

## License

No license has been specified for this repository.
