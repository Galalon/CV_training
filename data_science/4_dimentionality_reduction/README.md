### Dimentionality reduction

#### Theory
 - Read pages 559-570 about PCA in Bishop book – first part on PCA, and more in the internet of course :)
 - Read about kernels in Bishop Chapter 6 up to 6.1 (pages 292-294).
 - Solve exercise 6.3 in the end of the chapter (page 320)
 - Read about KPCA in Bishop 586-590 
 - Some intuition about kernels [here](https://sebastianraschka.com/Articles/2014_kernel_pca.html), [and here](https://arxiv.org/pdf/1207.3538.pdf)
 - Read about t-SNE a useful algorithm for visualization. Find information [here](https://medium.com/swlh/t-sne-explained-math-and-intuition-94599ab164cf). 
  
### Exercise
 - In this exercise you will implement PCA on a given faces images dataset.
 - Only numpy,cv2 libraries are allowed. Matplotlib only to visualize results.
 - use np.linalg – to calculate distances, eigenvalues and eigenvectors.
 - Do the following:
    - Present the average face.
    - Present 5 most dominant eigenfaces spreading the data (“ghost images”).
    - Decompose an image\images using PCA and reconstrucut the faces using a small number of eigen faces (2,5,10,50,100...), what is the difference between the different  reconstructions, why is that?
    - Define metric between two images (use your own), It should have a defined rule for success or failure.
    - Use it to detect What is the minimum number of eigenfaces needed to reach 60% precision on the given 10 test image pairs? Choose your metric wisely.


