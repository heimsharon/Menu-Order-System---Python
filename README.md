# Menu Order System - Python

_A simple command-line restaurant ordering system for selecting menu items and generating an itemized receipt in [Python](https://www.python.org/)._

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Python 3.x](https://img.shields.io/badge/python-3.x-blue)


---

## Table of Contents

- [Menu Order System - Python](#menu-order-system---python)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Getting Started](#getting-started)
  - [Data Structures](#data-structures)
  - [Example Output](#example-output)
  - [Notes](#notes)
  - [License](#license)
  - [Contributing, Support, and FAQ](#contributing-support-and-faq)
  - [Acknowledgments](#acknowledgments)
  - [Author](#author)

---

## Overview

**Menu Order System** is a simple command-line [Python](https://www.python.org/) application that allows users to view a categorized menu, place orders by selecting menu items and quantities, and receive an itemized receipt with the total price. The system is designed to be accessible for users with hearing and vocal impairments, requiring no verbal interaction.

---

## Features

-   Categorized menu display with item numbers and prices
-   Selection of menu items by number
-   Quantity prompt with default to 1 for invalid input
-   Clear error messages for invalid selections
-   Multiple item orders in a single session
-   Itemized receipt with total price

---

## Requirements

-   [Python](https://www.python.org/) 3.x
    > You can download the latest version of Python from the [official website](https://www.python.org/downloads/).
    > The site also provides installation instructions for Windows, macOS, and Linux.

---

## Getting Started

1. **Clone this repository:**
    ```bash
    git clone https://github.com/heimsharon/menu-order-system-python.git
    cd menu-order-system-python
    ```
2. **Run the program in your terminal:**
    ```bash
    python order_system.py
    ```
3. **Follow the on-screen prompts to place your order.**

> **Note:**
> If you are viewing this project on GitHub, you can also download the repository as a ZIP file by clicking the green "Code" button and selecting "Download ZIP."
> On GitHub, you can also browse the code online, view commit history, open issues, and submit pull requests.

---

## Data Structures

-   **Menu:** Nested dictionary (`dict`) with categories as keys and sub-dictionaries of meals and prices
-   **Order:** List of dictionaries, each containing `"Item name"`, `"Price"`, and `"Quantity"`

---

## Example Output

```
Welcome to the Generic Take Out Restaurant.
What would you like to order?
--------------------------------------------------
Item # | Item name                        | Price
-------|----------------------------------|-------
1      | Burrito - Chicken                | $4.49
...
Type menu number: 1
What quantity of Burrito - Chicken would you like?
(This will default to 1 if number is not entered)
2
Would you like to keep ordering? (N) to quit: n
Thank you for your order.
This is what we are preparing for you.

----------------------------------------------------
Item name                       | Price  | Quantity
--------------------------------|--------|----------
Burrito - Chicken               | $4.49  | 2
----------------------------------------------------
Total price: $8.98
----------------------------------------------------
```

---

## Notes

-   The starter code section at the bottom of `order_system.py` is provided for learning and should not be modified.
-   The code is heavily commented for educational purposes and future reference.
-   The GitHub repository allows you to download, fork, or contribute to the project as needed.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing, Support, and FAQ

-   **Contributions:** Pull requests are welcome! Please open an issue or submit a pull request for improvements or bug fixes.
-   **Support:** If you encounter any issues or have suggestions, please open an issue on GitHub.
-   **FAQ:**
    -   _How do I run the program?_
        See the [Getting Started](#getting-started) section above.
    -   _Can I use this for my own project?_
        Yes, this project is MIT licensed. See the [License](#license) section.

---

## Acknowledgments

Portions of this project were developed using starter code provided by [edX Boot Camps LLC](https://bootcamp.edx.org/) for educational purposes.

---

## Author

Created by Sharon Heim.
For questions or suggestions, please visit my [GitHub profile](https://github.com/heimsharon).

---

© 2025 Menu Order System Project
