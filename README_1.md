	

# Python Questions

**i. Is Python a compiled language or an interpreted language?  Is Python statically typed or dynamically typed?**

	Answer: Python is an interpreted language, where the source code of a Python program is converted into bytecode that is then executed by the Python Virtual Machine. Python is dynamically typed.

**ii. Unlike the Java project we didn't create a Matrix class. What class did we use to represent our Matrix in the Python project?  Why is this potentially better than creating our own Matrix class?**

	Answer: We used the matmpy.py class to represent our Matrix in the Python project. In this class, we defined a function (mat_mpy()) that takes in a Pandas Dataframe for matrix A and matrix B, which specifies with a function annotation that the result return type will also be a Pandas Dataframe. This is potentially better because the application user can call on the Pandas' extensive library of features instead of writing extra code for error handling.

**iii. In our mat_mpy function definition, what does the -> symbol mean?  Is it required for our function to operate correctly? What is the advantage of using this syntax?**

	Answer: The -> symbol is a function annotation. It serves as a way to associate arbitrary Python expressions with various parts of a function at compile-time. In this case, it annotates the type of a function's return value. Since it dictates the result's return type, I think that it is required for the function to operate correctly. The advantage of using function annotation is that it ensures the result of the function can also use Pandas functionality.

