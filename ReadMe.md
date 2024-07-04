# Practice setup

This is the setup for running Java classes in different folders / packages by simply using bash. Running this requires Java and Python (3.6+) installed on system.

Just create any java file. Then to run its main method, use the command `python run.py <java_class_name>`.

> NOTE: Just specify the class name. Omit the `.java` extension. Also, only the class name is required, subfolder or path is to be omitted as well.

### Input files

Input files are the files where you can store the user input for the program.
Input files should be in same folder as the java file and should start with the same name as the corresponding java file (class) and should end with `.txt`.

Input files are automatically included and the input is passed to the java files.

If there are multiple input files, then the java class is run multiple times, passing each file individually and printing the output each time.

### Example

File `./setuptest/setuptesting/TestingJavaSetup.java` in a package was created for the example.
To run this file, run the command `python run.py TestingJavaSetup`.

The file TestingJavaSetup.java also as 3 input files:-

1. TestingJavaSetup.txt
2. TestingJavaSetup copy.txt
3. TestingJavaSetup copy 2.txt

Running the command automatically picks up each of the 3 files, runs the class three times with each input file and also prints the output for each input.

The output of running the TestingJavaSetup.java file is shown in sampleOutput.txt file.
