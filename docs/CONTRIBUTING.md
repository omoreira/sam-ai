# Contributing to Sam AI

First off, thank you for considering contributing to Sam AI! It's people like you that will make this a truly valuable tool for everyone.

This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please be kind, respectful, and helpful to everyone.

## How Can I Contribute?

### Reporting Bugs
Bugs are tracked as [GitHub issues](https://github.com/your-username/sam-ai/issues).

**Before submitting a bug report:**
*   **Check existing issues** to see if the problem has already been reported.
*   **Check the documentation** (`SETUP.md`, `ARCHITECTURE.md`) to see if you can solve it yourself.

**Submitting a good bug report:**
*   Use a clear and descriptive title.
*   Describe the exact steps to reproduce the problem.
*   Describe the behavior you observed and what you expected to see instead.
*   Include details about your environment: OS, Python version, Ollama version, etc.
*   If possible, include relevant logs or error messages.

### Suggesting Enhancements
We welcome suggestions for new features or improvements! Please create an issue and:
*   Use a clear and descriptive title.
*   Provide a detailed description of the proposed feature.
*   Explain why this enhancement would be useful to most Sam AI users.

### Pull Requests (Code Contributions)
We love pull requests. Here's a quick guide:

1.  **Fork the repo** and create your branch from `main`. Use a descriptive branch name (e.g., `fix/ollama-connection-error`, `feat/add-anthropic-provider`).
2.  **Set up your development environment** as described in `SETUP.md`.
3.  **Make your changes.**
    *   Follow the existing code style (we use **Black** for formatting).
    *   **Write tests** for any new functionality in the `tests/` directory.
    *   **Update the documentation** if you change how something works.
4.  **Test your changes:** Ensure all existing and new tests pass.
5.  **Push to your fork** and [submit a pull request](https://github.com/your-username/sam-ai/compare) to our `main` branch.
6.  **Discuss and review:** We may ask you to make changes. This is a normal part of the process.

### Development Setup
Please see the detailed instructions in [`SETUP.md`](./SETUP.md).

## Project Philosophy & Priorities
*   **Privacy-First:** Default to local, on-device operation. Cloud API integration must be an explicit, user-enabled choice.
*   **User Sovereignty:** The user owns their data and their experience.
*   **Modularity:** Build with clear, decoupled components. This applies to AI Providers, Tools, and the UI.
*   **Clarity over Cleverness:** Readable, maintainable code is more important than clever but opaque solutions.

## Styleguides

### Git Commit Messages
*   Use the present tense ("Add feature" not "Added feature").
*   Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
*   Keep the first line under 50 characters.
*   Reference issues and pull requests liberally after the first line.

### Python Styleguide
*   We enforce formatting with **Black**. Please run `black .` before committing.
*   We recommend sorting imports with **isort** (`isort .`).
*   Strive for clear, descriptive variable and function names.
*   Use type hints where practical to improve code clarity.

© 2025 Olga Moreira, PhD. All rights reserved.


### Documentation Styleguide
*   Use Markdown.
*   Keep lines at a reasonable length (~80-100 characters).
*   Update documentation alongside code changes.

Thank you again for your interest in making Sam AI better!
