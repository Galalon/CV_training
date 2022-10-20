#Computer Vision (Classic)

- This sections teaches basic (classic) methods and algorithms in CV, before diving into learning methods.

### Course
 - In order to learn this subject comprehensively this section is based on udacity's introduction to computer vision [online course](https://www.udacity.com/course/introduction-to-computer-vision--ud810)
 - Do the following units and problem sets:
    - Unit 1 and problem set 0
    - Unit 2  and problem set 1
    - Unit 3 (without the problem set)
    - Unit 4 and problem set 4
    - Unit 6 and problem set 5
    - Unit 7 and problem set 6
    - Unit 9,section B only  
 - For your convenience, here is some useful information:
    - The course lectures are on youtube - unfortunately not in a single playlist so no link
    - The course syllabus with links to the problem sets [link](https://docs.google.com/spreadsheets/d/1ecUGIyhYOfQPi3HPXb-7NndrLgpX_zgkwsqzfqHPaus/pubhtml)
    - In the folder "course_resources" - All the required inputs for the exercises
 - After the course, do the questions in "additional_cv_exercises", use openCV functions

### Final Exercise
 - You have received intel that a terrorist organization hides messages on car tires. Your task is to:
     - Automatically recognize the car tires.
     - Crop only the tires and flatten them to rectangular images (i.e take the pixels of the tire in ring shape, and map them to a rectangle).
  - You are provided with 3 train Images (in the folder train images) to experiment on.
  - Develop an algorithm that automatically and robustly creates aligned tire Images. That will be tested on 10 test images.
  - In the development process follow these guidelines:
     - You may use every CV algorithm as long as it is not a machine learning algorithm, it is recommended to use OpenCv built in algorithms.
     - Make sure your algorithm is robust, so spend less time on parameter tuning and more on new techniques to use. Take into account that your test images might be different than the train images.
     - Be mindful about making assumptions - keep track of what your'e assuming (if at all), and make sure with your supervisor that these assumptions are legitimate.
  - When you have finished, ask for the test images from your supervisor, and test your algorithm.
  - Document your work, make sure your documentation includes:
    - Background on the problem (why did you started working on it)?
    - The goals of the document
    - technical background, explain the main tools you used in the algorithm - as a thumb rule:
      - If its common knowledge or you learned it in the training, write a short explanation, to remind the reader.
      - If its a new method, give a detailed explanation (about a page) 
    - Problem definition - a detailed explanation of the problem:
        - required inputs/outputs
        - chosen metrics
        - the dataset you worked on 
        - assumptions you made
    - A general description of the algorithm, without diving into  details
    - Algorithm, results (train and test)      
    - Conclusions, and future work 