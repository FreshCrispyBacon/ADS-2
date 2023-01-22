# David's Portfolio - Group 2 of ADS
### Student: David Kaldor - 20141211


# <a id="table-of-contents"></a>Table of Contents <!-- omit in toc -->
- [Obligatory Criteria](#obligatory-criteria)
  - [Datacamp assignments](#datacamp-assignments)
- [1. The Project](#the-project)
  - [Foodboost](#the-project-foodboost)
  - [Vision](#the-project-vision)
- [2. Predictive Models](#predictive-models)
  - [Foodboost (Decision Tree Classifier)](#predictive-models-foodboost)
  - [Vision (YOLOv5)](#predictive-models-vision)
- [3. Domain Knowledge](#domain-knowledge)
  - [Foodboost](#domain-foodboost) 
  - [Literature](#domain-knowledge-literature-foodboost)
  - [Terminology](#domain-knowledge-terminology-foodboost)
  - [Vision](#domain-vision) 
  - [Literature](#domain-knowledge-literature-vision)
  - [Terminology](#domain-knowledge-terminology-vision)
- [4. Data Preprocessing](#data-preprocessing)
  - [Foodboost](#data-preprocessing-foodboost)
  - [Vision](#data-preprocessing-vision)
- [5. Communication](#communication)
  - [Presentations](#presentations)
  - [Paper](#paper)

---

# <a id="obligatory-criteria"></a>Obligatory Criteria
## <a id="datacamp-assignments"></a>Datacamp assignments

- 21 / 01 / 2023 Datacamp progress

  <details><summary>Datacamp progress</summary><img src="Screenshot_20230121_090154.png"></details>
  
  [Back to Table of Contents](#table-of-contents)

# <a id="the-project"></a>1. The Project
There were two projects we worked on. The first project is Foodboost, and the second project is Vision (IV-Infra). I will cover both of them seperately here.

##  <a id="the-project-foodboost"></a>Foodboost
The goal of Project Foodboost was to develop a recommendation system that helps users adopt healthier eating habits. Since the concept of "healthy" can be subjective, our approach was to gradually introduce more nutritious options over an extended period of time, recognizing that eating well is a long-term lifestyle change, not a temporary trend.

For this goal, we set the following research questions:
1. How can we predict a healthier diet for someone based on their previous recipes?
2. How can we define "healthier"?
3. What is the effectiveness of the Nutri-Score system in guiding users towards healthier food choices within the Foodboost recommendation system?

### Future Work
The main setback I felt we had was the lack of real user data, more specifically, user input data. User input data is considered data we can use where a user has rated a considerable amount of tried recipes. Lacking user data is important for a machine learning model that aims to recommend healthier food options because the model relies on this data to learn about the user's preferences, dietary restrictions, and current eating habits. Without this information, the model would not be able to make personalized or accurate recommendations. Additionally, the model would not be able to track the user's progress and adjust its recommendations accordingly. Without data, the model would not be able to learn from user interactions and feedback, which is crucial for improving the model's performance over time.

### Conclusions

#### 1. How can we predict a healthier diet for someone based on their previous recipes?

One way to predict a healthier diet for someone based on their previous recipes is to analyze the nutrient content of the recipes and make recommendations for substitutions or additions of healthier ingredients. For example, if a person frequently uses high-calorie, high-fat ingredients, suggestions could be made to use leaner protein sources and more vegetables. Additionally, a dietary analysis could be done to identify any nutrient deficiencies and make recommendations to address those deficiencies through food choices. Machine learning algorithms can also be used to analyze the person's previous recipes and suggest new, healthier recipes based on their dietary patterns.

#### 2. How can we define "healthier"?

The Nutri-Score is a nutrition label that can be used to define "healthier" food options. The Nutri-Score uses a five-color scale (from dark green to red) to classify foods based on their nutritional quality. The score takes into account the amount of energy (calories), sugar, saturated fat, sodium, and the presence of fruits, vegetables, nuts, fiber, and protein. Foods with a higher Nutri-Score are considered healthier than those with a lower score. Food items are scored based on these criteria and assigned a letter grade (A, B, C, D, or E) with A being the healthiest and E being the least healthy. This scoring system is a simple and effective way to help consumers make informed choices about the nutritional quality of the food they buy.

#### 3. What is the effectiveness of the Nutri-Score system in guiding users towards healthier food choices within the Foodboost recommendation system?

To determine the effectiveness of the Nutri-Score system in guiding users towards healthier food choices within the Foodboost recommendation system, a study should be conducted where participants are asked to use the Foodboost recommendation system for a certain period of time, for example, 6 months. The study should also include a control group which does not use the Foodboost recommendation system.

The study should measure the proportion of food choices made by the participants that have a higher Nutri-Score rating. Additionally, the study should measure the nutrient content of the food choices made by the participants, and compare the nutrient content of the food choices made by the participants in the experimental group to those made by the control group.

It's also important to have a measure of participant's satisfaction with the system, and their perception of the Nutri-Score system in terms of its usefulness and ease of use.

The results of such a study would provide an indication of the effectiveness of the Nutri-Score system in guiding users towards healthier food choices within the Foodboost recommendation system.

### Planning
Initially, we had intended to utilize Trello as a means of keeping each other informed about progress made on the project. However, as we progressed, we found ourselves neglecting Trello in favor of prioritizing the completion of tasks.

## <a id="the-project-vision"></a>Vision
In this research project, the context was to develop a data science solution for checking the status of road signs for IV-Infra. The problem being addressed was the need to efficiently and accurately map and check the status of road signs, such as determining if a sign is in the correct location, if it is rotated too much, or if it is expired. 

For this goal, we set the following research questions:
1. "How can road signs be recognized and mapped using a series of photos?" 
2. To what extent has research been done into recognizing traffic signs by means of Machine Learning and/or Neural Networks?
3. What drives traffic sign mapping?
4. Which data from the NDW will be integrated into the Neural Network?
5. How accurately can a traffic sign be recognized using LiDAR data?

### Future Work

Based on the research conducted, there are several steps that can be taken to improve the model. One of the most beneficial steps is to increase the amount of data used to train the model. This can be achieved by having IV-infra collect data from various locations and in different weather conditions.

In the future, the model can also be useful for municipalities in maintaining traffic signs. If the model does not detect a sign that is supposed to be present according to NDW, the municipality can check if the sign is damaged or stolen. Conversely, if the model detects a sign that is not in the NDW dataset, it is likely a temporary sign and the municipality can determine the duration of its placement and if it needs to be removed.

Additionally, the model can be utilized to trigger actions based on the recognition of specific traffic signs. For example, the model can be used to prompt self-driving cars to reduce speed at speed signs, speed cameras, and dangerous intersections. This way the model can contribute to the safety of self-driving cars.

### Conclusions

#### 1. "How can road signs be recognized and mapped using a series of photos?" 

To address this question, we used YOLOv5 as the object detection model and trigonometric calculations to map the detected road signs. We also used a dataset provided by IV-Infra and compared the results to the road sign records held by NDW. Overall, the context and research question were clearly defined and were reasonable given the need for an efficient and accurate solution for monitoring road signs.

#### 2. To what extent has research been done into recognizing traffic signs by means of Machine Learning and/or Neural Networks?

There has been a significant amount of research done in the field of recognizing traffic signs using Machine Learning and Neural Networks. The task of traffic sign recognition (TSR) is a well-established computer vision task that has been studied extensively in the literature.

Many studies have been conducted using various Machine Learning and Neural Network algorithms such as Support Vector Machines (SVMs), Random Forest, k-Nearest Neighbors (k-NN), Convolutional Neural Networks (CNNs), and Recurrent Neural Networks (RNNs) to name a few.

Convolutional Neural Networks (CNNs) have been particularly effective in TSR, especially deep CNNs. These methods have shown to achieve high accuracy rates on various benchmark datasets such as the German Traffic Sign Recognition Benchmark (GTSRB).

Additionally, researchers have been also working on improving the robustness of TSR systems by incorporating techniques such as data augmentation, transfer learning, and Adversarial machine learning to handle different variations in traffic sign appearances, such as different lighting conditions, weather, and camera perspectives.

In recent years, researchers have also been working on developing real-time TSR systems that can be deployed on vehicles and embedded systems, to enhance the safety of autonomous vehicles.

Overall, the field of TSR using Machine Learning and Neural Networks is a very active area of research with a great deal of progress being made in recent years, and it is expected to continue to evolve as technology improves.

#### 3. How is traffic sign mapping accomplished?

The research question can be approached by using a combination of image processing techniques, machine learning, and data visualization tools.

One way to accomplish traffic sign mapping is to first use image processing techniques such as YOLOv5 to detect and identify traffic signs in images captured by cameras mounted on a vehicle. The output of YOLOv5 detection will give type of detected traffic signs in the images.

Then, trigononmetric calculations are performed on a pair of YOLOv5 output images to retrieve new coordinates signifying the detected road sign's location.

Next, these coordinates can be verified against the National Data Warehouse (NDW) database, which contains information on traffic signs in the Netherlands, including their location and attributes. By cross-referencing the coordinates with the NDW database, it can be verified that the traffic signs have been placed in the correct location and that they conform to national and international standards.

Once the coordinates have been verified, they can be plotted on a map using a Python library such as Plotly Express. This allows for the visualization of the locations of the traffic signs and can be used to identify patterns and trends in the data.

In this way, traffic sign mapping is accomplished by using image processing techniques to detect and identify traffic signs, and then using machine learning and data visualization tools to verify the location of the traffic signs and map them on a map.

#### 4. Which data from the NDW will be integrated into the Neural Network?



#### 5. How accurately can a traffic sign be recognized using LiDAR data?

In this research, the use of computer vision techniques and the YOLOv5 object detection algorithm was chosen as the primary approach for detecting and mapping road signs in a series of photos. YOLOv5, known for its high accuracy and real-time performance, was trained on the dataset provided by IV-Infra and was able to detect road signs with high accuracy. This approach was found to be highly effective in detecting and mapping road signs in a variety of environments. In contrast, LiDAR technology, while widely used in tasks such as object detection, mapping, and navigation, proved to be less suitable for this specific task. LiDAR technology is relatively slow, unreliable and requires a clear line of sight to the object, which makes it hard to detect objects that are obscured or behind other objects. Furthermore, while LiDAR is mainly used to detect objects in 3D space, the detection of road signs is mainly a 2D task, which can be achieved with high accuracy using computer vision techniques and YOLOv5 object detection algorithm. This approach, therefore, proved to be more efficient and reliable for this study.

### Planning
In this project, we initially planned to use Trello as our task management tool but ended up not utilizing it. Despite this, we were still able to effectively communicate and keep track of our tasks and progress.
<details><summary>Planning Vision</summary><img src="Screenshot_20230121_103116.png"></details>

[Back to Table of Contents](#table-of-contents)
# <a id="predictive-models"></a>2. Predictive Models

I have created multiple predictive models, which I will present and discuss separately for each project.
## <a id="predictive-models-foodboost"></a>Project Foodboost

Project foodboost was mainly based around basic machine learning models.

content here

## <a id="predictive-models-vision"></a>Project Vision

Project vision ...

content here

[Back to Table of Contents](#table-of-contents)
# <a id="domain-knowledge"></a>3. Domain Knowledge
# <a id="domain-foodboost"></a>Foodboost
The field of healthy food and nutrition is a complex and ever-evolving one, making it essential for the success of Project Foodboost to have a deep understanding of how healthy diets are constructed. As someone who has been following a healthy diet for the past 9 years, both for personal fitness goals and due to dietary needs stemming from personal health issues, I was well-suited to take on this project.

The goal of Project Foodboost was to develop a recommendation system that helps users adopt healthier eating habits. Given that the concept of "healthy" can be subjective, our approach was to gradually introduce more nutritious options over an extended period of time. By recognizing that eating well is a long-term lifestyle change, and not a temporary trend, we were able to develop a system that takes into account the unique needs and preferences of each individual user.

Through this project, I was able to apply my knowledge and experience in healthy eating to try and create a tool that can assist others in making positive changes to their diets. I am excited to see the impact that this project will have in the future on helping individuals improve their health and well-being through healthier food choices.

## <a id="#domain-knowledge-literature-foodboost"></a>Literature
During this project, which spanned over the first six weeks of the minor kick-off. My main source of knowledge origins from the DataCamp courses. Furthermore I educated myself on the types of recommender systems and how to apply those techniques for promoting a long-term lifestyle change.

* [Introduction to Recommender System](https://towardsdatascience.com/intro-to-recommender-system-collaborative-filtering-64a238194a26)
* [A Complete Guide To Recommender Systems](https://towardsdatascience.com/a-complete-guide-to-recommender-system-tutorial-with-sklearn-surprise-keras-recommender-5e52e8ceace1)

## <a id="#domain-knowledge-terminology-foodboost"></a>Terminology

# <a id="domain-vision"></a>Vision

## <a id="#domain-knowledge-literature-vision"></a>Literature
## <a id="#domain-knowledge-terminology-vision"></a>Terminology

