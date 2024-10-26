# Code Generator
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B&labelColor=3A3F44)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=orange&labelColor=3A3F44)
![PyTorch](https://img.shields.io/badge/PyTorch-1.x-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=red&labelColor=3A3F44)
![GitHub](https://img.shields.io/badge/GitHub-1.0-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=3A3F44)
![Transformers](https://img.shields.io/badge/Transformers-4.x-6F1D99?style=for-the-badge&logo=transformers&logoColor=white&labelColor=3A3F44)


The **Code Generator** is a **Python**-based project designed to generate code snippets using a fine-tuned machine learning model. It leverages advanced libraries such as **TensorFlow** and **PyTorch** for model training and inference, enabling efficient and powerful code generation.


## 📁 Folder Structure
```
Code Generator/
    ├── data/                       # Contains datasets used for training and testing the model
    ├── img/                        # Stores output images
    │   └── output.png             # Example of generated code output
    ├── logs/                       # Log files generated during execution
    ├── results/                    # Stores results of the model evaluations
    ├── main.py                     # Main script to run the code generation
    └── python_code_snippet_collector.py  # Utility script for collecting code snippets
```

## 🚀 Usage
1. **Installation**: Ensure you have Python 3.8 or higher installed along with the required libraries. Install the necessary libraries using pip:

   ```bash
   pip install -U PyGithub datasets transformers torch tensorflow tf-keras==0.26.0
   ```

2. **Running the Code Generator**: 
   - Execute the main script to start generating code snippets:

   ```bash
   python main.py
   ```

   - **Modify and Run Code Snippets**: You can customize your code generation by editing the `python_code_snippet_collector.py` file with different datasets or prompts. Run this file to generate various outputs based on your changes.

## 📥 Output
The generated output will be saved in the `results/` folder. Below is a sample of the generated code:

![Generated Code Output](img/output.png)

## 📝 Logs
For debugging and tracking purposes, logs of the execution can be found in the `logs/` folder.

## 🤝 Contributing
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are welcome!

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

