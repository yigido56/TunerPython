# TunerPython
Guitar Tuner with Python

After run the code,There are two options which named 'Record Voice' and 'Check Tuning'.
Firstly, user need to record 6 guitar strings separately.
For this action the code asks 'which string do you want to record?'.(The answer must be: 1,2,3,4,5 or 6)
After that record starting and the file will be created which named 'gitar-akor1.wav'.(the filename will change according to the user's answer)

After recording, code will compare the frequency value with the correct frequency value for each string.
For this action the code asks 'which string do you want to compare?'.(The answer must be: 1,2,3,4,5 or 6)
after that the file will be found for example 'gitar-akor2.wav'.This voice file has an frequency value and the code calcute it.Then compare with the correct frequency value.
If it's not equal to correct frequency value the code will be instructed what you have to do.Example, turn the tuning key clockwise.

After instruction, repeat all steps until reach correct frequency value for all strings.
