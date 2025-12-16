# Advanced GUI Calculator

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

A feature-rich, modern calculator application with an intuitive graphical user interface built using Python's tkinter library. This calculator provides basic and advanced arithmetic operations with support for keyboard input, calculation history tracking, and error handling.

## Features

### Core Functionality
- ✅ **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- ✅ **Advanced Operations**: Square root (√), Sign toggle (±)
- ✅ **Decimal Support**: Handle floating-point calculations with precision
- ✅ **Keyboard Input**: Full keyboard support for faster calculations
- ✅ **Calculation History**: Track and display recent calculations
- ✅ **Error Handling**: Comprehensive error handling for division by zero and invalid inputs

### User Interface
- 🎨 **Modern Design**: Clean, Nord-themed color scheme for comfortable viewing
- 📱 **Responsive Layout**: Grid-based layout that adapts to different screen sizes
- ⌨️ **Keyboard Shortcuts**:
  - `Enter` or `=` - Calculate result
  - `Escape` or `C` - Clear display
  - `Backspace` - Delete last character
  - `0-9`, `+`, `-`, `*`, `/`, `.` - Direct input
- 📊 **Live Display**: Real-time display of current calculation and history

## Installation

### Prerequisites

```bash
python --version  # Python 3.7 or higher required
```

### Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/Jasmeen1331/Calculator.git
cd Calculator
```

2. **Run the calculator**

```bash
python calculator.py
```

*Note: Tkinter comes pre-installed with Python, so no additional dependencies are required.*

## Usage

### Running the Application

Simply execute the Python file:

```bash
python calculator.py
```

### Using the Calculator

**Mouse/Click Method:**
1. Click number buttons to input values
2. Click operator buttons (+, -, *, /) for operations
3. Click `=` to calculate the result
4. Click `C` to clear the display
5. Click `⌫` (backspace) to delete the last character

**Keyboard Method:**
1. Type numbers directly using your keyboard
2. Use operator keys: `+`, `-`, `*`, `/`
3. Press `Enter` or `=` to calculate
4. Press `Escape` to clear
5. Press `Backspace` to delete last character

### Example Calculations

```
# Basic arithmetic
15 + 27 = 42
100 - 45 = 55
8 * 9 = 72
144 / 12 = 12

# Decimal operations
3.14 * 2 = 6.28
10.5 / 2.1 = 5.0

# Advanced operations
√144 = 12.0
±25 = -25 (toggle sign)
```

## Project Structure

```
Calculator/
│
├── calculator.py           # Main application file (enhanced version)
├── PycharmProjects/        # Original project folder
│   └── pythonProject3/
│       └── calc.py         # Original calculator implementation
├── README.md               # Project documentation
└── LICENSE                 # MIT License
```

## Technical Implementation

### Architecture

The calculator is built using **Object-Oriented Programming (OOP)** principles:

```python
class Calculator:
    - __init__()           # Initialize GUI and variables
    - setup_styles()       # Configure visual theme
    - create_display()     # Build display components
    - create_buttons()     # Generate button grid
    - bind_keyboard_events() # Setup keyboard shortcuts
    - calculate()          # Perform calculations
    - append_number()      # Handle number input
    - set_operator()       # Set arithmetic operator
    - clear()              # Reset calculator
    - update_display()     # Refresh screen
```

### Key Components

1. **Display System**
   - Main display (Entry widget) for input/output
   - History display (Label widget) for showing calculation steps

2. **Button Grid**
   - 4×5 grid layout for optimal usability
   - Color-coded buttons:
     - Number buttons: Dark gray (`#4C566A`)
     - Operators: Blue (`#5E81AC`)
     - Equals: Green (`#A3BE8C`)
     - Clear: Red (`#BF616A`)

3. **Event Handling**
   - Mouse click events for button presses
   - Keyboard bindings for direct input
   - Error handling with user-friendly messages

### Color Scheme (Nord Theme)

| Component | Color Code | Purpose |
|-----------|------------|----------|
| Background | `#2E3440` | Main window background |
| Display | `#3B4252` | Calculator display area |
| Buttons | `#4C566A` | Number buttons |
| Operators | `#5E81AC` | Arithmetic operator buttons |
| Equals | `#A3BE8C` | Calculate button |
| Clear | `#BF616A` | Clear/Reset button |
| Text | `#ECEFF4` | All text elements |

## Code Quality Features

- ✅ **Comprehensive Docstrings**: Every method includes detailed documentation
- ✅ **Type Hints**: Clear parameter and return type specifications
- ✅ **Error Handling**: Try-except blocks for robust error management
- ✅ **Code Organization**: Clean separation of concerns with dedicated methods
- ✅ **PEP 8 Compliance**: Follows Python style guidelines
- ✅ **Maintainability**: Modular design for easy updates and extensions

## Future Enhancements

Potential features for future development:

- [ ] Scientific calculator mode (sin, cos, tan, log, etc.)
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] Calculation history window with save/load functionality
- [ ] Theme customization options
- [ ] Unit conversion capabilities
- [ ] Expression evaluation (e.g., "5 + 3 * 2")
- [ ] Graph plotting for functions
- [ ] Multi-language support

## Technologies Used

- **Python 3.7+**: Core programming language
- **Tkinter**: GUI framework (built-in)
- **ttk**: Themed widget set
- **Math Module**: Advanced mathematical operations

## Contributing

Contributions are welcome! If you'd like to improve this calculator:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Known Issues

Currently no known issues. If you encounter any bugs, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Jasmeen** (Student ID: 21236862)  
Final Year Computer Science Student  
University of Central Lancashire

## Acknowledgments

- Thanks to the Python community for excellent documentation
- Nord color scheme by Arctic Ice Studio
- Tkinter GUI framework by Python Software Foundation

## Contact

For questions, suggestions, or collaboration opportunities:
- GitHub: [@Jasmeen1331](https://github.com/Jasmeen1331)
- University: University of Central Lancashire

---

⭐ **Star this repository if you find it helpful for your projects or learning!**
