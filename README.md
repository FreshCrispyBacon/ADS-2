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
  - [Vision](#domain-vision) 
- [4. Data Preprocessing](#data-preprocessing)
  - [Foodboost](#data-preprocessing-foodboost)
  - [Vision](#data-preprocessing-vision)
- [5. Communication](#communication)
  - [Presentations](#presentations)
  - [Paper](#paper)
- [6. Codesnippets](#codesnippets)
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
During this project, which spanned over the first six weeks of the minor kick-off, my main source of knowledge originates from the DataCamp courses. Furthermore I educated myself on the types of recommender systems and how to apply those techniques for promoting a long-term lifestyle change, in addition to understanding the Nutri-Score and Nutri-Label algorithm.

* [Update of the Nutri-Score Algorithm](https://open.overheid.nl/repository/ronl-34c6383f5747298a4d0a93c2ac884f150557f51e/1/pdf/2022-main-algorithm-report-update.pdf)
* [Introduction to Recommender System](https://towardsdatascience.com/intro-to-recommender-system-collaborative-filtering-64a238194a26)
* [A Complete Guide To Recommender Systems](https://towardsdatascience.com/a-complete-guide-to-recommender-system-tutorial-with-sklearn-surprise-keras-recommender-5e52e8ceace1)

## <a id="#domain-knowledge-terminology-foodboost"></a>Terminology
<details>
<summary>
Below are some terms and jargon that are explained in further detail
</summary>

- Nutri-Score
  
  The Nutri-Score is a nutrition label that uses a five-color scale (from dark green to red) to classify foods based on their nutritional quality. It takes into account the amount of energy (calories), sugar, saturated fat, sodium, and the presence of fruits, vegetables, nuts, fiber, and protein. Foods with a higher Nutri-Score are considered healthier than those with a lower score. The Nutri-Score label is an easy way for consumers to identify healthier food options at a glance.
  
- Nutri-Label
  
  Nutri-label is a similar concept, it is a nutrition label that is used to display the nutritional value of a product. Nutri-label usually contains information such as the energy value, the amounts of fat, saturated fat, carbohydrates, sugars, protein and salt per 100g or per serving. It also includes a reference intake (RI) for an average adult. Nutri-label aims to make it easier for consumers to make informed choices about the food they buy and to help them to achieve a balanced diet.
  
- Recommender System
  
  A recommender system is a type of algorithm that is used to suggest items to users based on their preferences and behavior. These systems are commonly used in online platforms such as e-commerce websites, streaming services, and social media. They help users discover new products, movies, music, articles and more that they may be interested in.

  There are several types of recommender systems, the most common are:

  Content-based filtering: This type of system uses the characteristics of the items a user has previously interacted with to suggest similar items. For example, a music streaming service may recommend songs that are similar to ones a user has previously listened to.

  Collaborative filtering: This type of system uses the behavior of other users to make recommendations. For example, if many users who have similar tastes to a user have liked a particular recipe, the system may recommend that recipe to the user.

  Hybrid systems: This type of systems combine the previous two types of recommendation, using both the content of the items and the behavior of other users to make recommendations.

  Recommender systems can use various techniques to make recommendations such as matrix factorization, cosine similarity, and neural networks. These systems are constantly learning and adapting to the user's behavior, making their recommendations more accurate over time.

</details>

[Back to Table of Contents](#table-of-contents)

# <a id="domain-vision"></a>Vision
In this project, entitled "Vision", I delved into the field of computer vision and object detection. Having taken a course on computer vision the prior year, I was already familiar with the principles of this area of study. However, I had always been particularly interested in the application of object detection, and this project provided me with the opportunity to work with it firsthand.

The context of this research project was to develop a data science solution for checking the status of road signs for IV-Infra. The problem being addressed was the need to efficiently and accurately map and check the status of road signs, such as determining if a sign is in the correct location, if it is rotated too much, or if it is expired. The research question being addressed was, "How can road signs be recognized and mapped using a series of photos?"

I was primarily focused on researching and implementing the YOLOv5 object detection model. This involved deep diving into the inner workings of the model, as well as experimenting with various configurations to ensure it was optimally suited for our project. I also spent a significant amount of time researching and implementing various preprocessing techniques for the dataset before it was fed into the model. This allowed me to ensure the best possible results and accuracy of the model. 

Lastly, my colleague Bram and I wrote a python script from scratch to bring all the components of the project together. This script utilized the YOLOv5 object detection model and trigonometric calculations to effectively map the road signs detected by the model. This script was crucial to achieving the final goal of the project, which was to accurately map and check the status of road signs. The process of writing this script required a deep understanding of the YOLOv5 model, trigonometry, and programming skills. It was a challenging but rewarding experience to work on this script and bring the project to fruition

## <a id="#domain-knowledge-literature-vision"></a>Literature
In this second project, I leveraged the knowledge and skills I had gained from my previous experiences, particularly in the field of Python programming. I had completed several courses on DataCamp and was well-versed in the language. This allowed me to focus more on understanding the inner workings of the YOLOv5 object detection model and researching ways to optimize its deployment for our specific project. I spent a significant amount of time studying the model and experimenting with different configurations to ensure that it was properly tailored to our needs. Finally, I implemented the model and integrated it into the project. The knowledge and experience I had gained from my prior training in Python programming enabled me to approach this project with confidence and make meaningful contributions to the project's success.

* [Traffic Sign Recognition Application Using Yolov5 Architecture](https://ieeexplore.ieee.org/abstract/document/9537355)
* [Improved YOLOv5 network for real-time multi-scale traffic sign detection](https://link.springer.com/article/10.1007/s00521-022-08077-5)
* [A Novel Neural Network Model for Traffic Sign Detection and Recognition under Extreme Conditions](https://www.hindawi.com/journals/js/2021/9984787/)
* [Detecting objects with YOLOv5, OpenCV, Python and C++](https://medium.com/mlearning-ai/detecting-objects-with-yolov5-opencv-python-and-c-c7cf13d1483c)
* [Training YOLOv5 custom dataset](https://medium.com/mlearning-ai/training-yolov5-custom-dataset-with-ease-e4f6272148ad)
* [What is YOLO algorithm? | Deep Learning (Tensorflow, Keras & Python)](https://www.youtube.com/watch?v=ag3DLKsl2vk)

## <a id="#domain-knowledge-terminology-vision"></a>Terminology

LiDAR
mAP
Confidence
Ground Truth


[Back to Table of Contents](#table-of-contents)
# <a id="data-preprocessing"></a>4. Data Preprocessing
The "Data Preprocessing" section of this portfolio showcases my skills and experience in preparing and cleaning data for analysis. This includes tasks such as data cleaning, data transformation, feature selection, data annotation, data normalization and data visualization. 

## <a id="data-preprocessing-foodboost"></a>Project Foodboost

intro here

### Dataset *Allerhande

info
text

### Dataset *Food.com

info
text

## <a id="data-preprocessing-vision"></a>Project Vision

intro here

### Dataset *IV-Infra

info
text

#### Images, LiDAR and Coordinates

info
text

#### The 6 Steps Bram and I Followed to Preprocess Data in Object Detection
<details><summary>Data acquisition:</summary> The first step is to acquire the data that will be used to train and test the YOLOv5 model. This was done by by navigating Jupyter Notebook's server files with the terminal feature to acquire the data provided by IV-Infra objects that need to be detected.</details>
<details><summary>Data Rescaling:</summary>The first thing we did with the data was to reduce the overall size of it. Every image was reduced to the resolution of 640x640 from 5120x5120. This effectively reduced the size of all the pictures to 640x640 from 5120x5120. The reason for this was to manageable, the total file size was roughly divided by 64. Additionally, 640x640 is optimal for the YOLOv5m weights; more on this later.</details>
<details><summary>Data cleaning:</summary> The next step was to clean the data by removing any irrelevant or duplicate data, and ensuring that the data is of high quality. This step is important to ensure that the model is only trained on relevant and accurate data. In our case this was the removal of many images lacking any clearly visible traffic signs.</details>
<details><summary>Data annotation:</summary> Once the data was cleaned, it needs to be annotated in order to indicate the location of the traffic signs that need to be detected. This step is usually done using annotation tools such as LabelImg, RectLabel, or Roboflow. After testing these 3 popular options, Roboflow was clearly superior. Due its large amount of features, most importantly, we were able to divide our dataset into five equal parts for each member to annotate. Additionally, every object class created by any member was visible to all member, all in real-time.</details>
<details><summary>Data splitting:</summary> After the data is annotated, it needed to be split into training, testing, and validation sets. This is important to ensure that the model is tested on unseen data and to prevent overfitting. The split chosen was a standard 70/20/10 split.</details>
<details><summary>Data normalization:</summary> This step was already executed in step 2 for convinience and resource-efficiency. Data Normaization can be done by rescaling the images to a uniform size and converting them to a format that is compatible with the YOLOv5 model.</details>
<details><summary>Data augmentation:</summary> To increase the diversity of the data and to make the model more robust to different variations in the data, data augmentation can be applied to the training data. The augmentation techniques used were as follows:<br>
	* Rotation: Between -5° and +5°<br>
	* Hue: Between -30° and +30°<br>
	* Saturation: Between -70 and +70<br>
	* Brightness: Between 0% and +80%<br>
	* Bounding Box: Shear: ±12° Horizontal, ±4° Vertical<br>
Do note these values are final values after several tweaks according to model performance.</details>

#### The Annotation process

info
text

#### Data Augmantation

info
text

### Dataset *NDW

info
text


[Back to Table of Contents](#table-of-contents)
# 5. <a id="communication"></a>Communication

## Presentations

During this minor I have presented x presentations.

Foodboost
  - 
  - 

Vision
  -
  -

## Paper

The paper my group delivered at the end of the ADS Minor targeted the Vision project, as it was the longest project in the minor.
For the paper I contributed in 7 specific sections, aside from giving feedback on the remaining sections and my teammates' work.

<details><summary>Abstract</summary> Deze onderzoekspaper presenteert een methode om verkeersborden te herkennen en in kaart te brengen aan de hand van een reeks foto's. Het objectdetectiemodel dat in dit onderzoek wordt gebruikt, is YOLOv5. Dit model staat bekend om zijn hoge nauwkeurigheid, efficiëntie en real-time prestaties. De dataset die in dit onderzoek is gebruikt, is aangeleverd door IV-Infra en is gebruikt om het model te trainen. De goniometrische berekeningen zijn vervolgens ingezet om de gedetecteerde verkeersborden in kaart te brengen. Hierna is het NDW-dataset gebruikt ter controle. De resultaten van deze studie tonen de effectiviteit aan van het gebruik van YOLOv5 voor het herkennen en in kaart brengen van verkeersborden. Ook toont dit het potentieel van deze methode voor gebruik in real-world toepassingen, zoals autonome voertuigen en intelligente transportsystemen.</details>

<details><summary>3.2 Traffic Signs in Machine Learning and/or Neural Networks</summary>
  Er is veel onderzoek gedaan op het gebied van het herkennen van verkeersborden met behulp van Machine Learning en Neural Networks. Verschillende algoritmen zoals Support Vector Machines (SVM's), Random Forest, k-Nearest Neighbours (k-NN), Convolutional Neural Networks (CNN's) en Recurrent Neural Networks (RNN's) zijn in deze onderzoeken gebruikt om hoge nauwkeurigheidspercentages te bereiken. Diepe CNN's zijn bijzonder effectief geweest bij het herkennen van verkeersborden en zijn gebruikt om hoge nauwkeurigheidspercentages te bereiken op verschillende benchmarkdatasets, zoals de Duitse Traffic Sign Recognition Benchmark (GTSRB). Onderzoekers hebben gewerkt aan het verbeteren van de robuustheid van de systemen door technieken toe te voegen zoals data-augmentatie, transfer learning en Adversarial machine learning. Bovendien heeft recent onderzoek zich gericht op de ontwikkeling van real-time TSR-systemen die kunnen worden ingezet op voertuigen en ingebedde systemen om de veiligheid van autonome voertuigen te verbeteren. Het gebied van TSR met behulp van machine learning en neurale netwerken is een zeer actief onderzoeksgebied en zal naar verwachting blijven evolueren naarmate de technologie verbetert.
 </details>

<details><summary>3.3.1 YOLOv5</summary>Here I wrote most of the text for a teammate, thereafter they changed it to their liking.<br><br> 
  Het YOLOv5-objectdetectiealgoritme werd gebruikt om ons model te trainen. De YOLOv5m-gewichten werden gebruikt als de eerste parameters voor het trainingsproces. De training duurde in totaal 50 epochs, met een batchgrootte van 16. De trainingsgegevens bestonden uit afbeeldingen verkregen van IV-Infra, die vooraf waren verwerkt door hun resolutie te verlagen van 5120x5120 pixels naar 640x640 pixels. Dit is gedaan om de data beter beheersbaar te maken en tegelijkertijd het verlies van informatie te minimaliseren door de afbeelding geleidelijk te verkleinen in plaats van deze bij te snijden. Door het gebruik van YOLOv5, getraind op YOLOv5m-gewichten en de specifieke trainingsconfiguratie (50 tijdperken, batchgrootte van 16) konden we een hoge mate van nauwkeurigheid en efficiëntie bereiken bij het detecteren van objecten in de afbeeldingen.
</details>

<details><summary>3.3.2 Annotating Images</summary>Here I wrote most of the text for a teammate, thereafter they changed it to their liking.<br><br>
  Het Roboflow-platform werd gebruikt voor het annoteren en uitbreiden van de dataset voor het trainen van het objectdetectiemodel. Het platform bood een efficiënte manier van annotatie via de gebruiksvriendelijke interface voor annotatie van bounding boxes en aanpasbare annotatiepijplijn. Er werd een breed scala aan technieken voor gegevensvergroting toegepast, waaronder het omdraaien van afbeeldingen, roteren en schalen, om de robuustheid van het model voor variaties in de data te verbeteren. Daarnaast werden beeldsynthesetechnieken zoals uitsnijding, kleurtrillingen en onscherpte gebruikt om een gevarieerde set trainingsbeelden te genereren. Het gebruik van Roboflow voor annotatie en gegevensvergroting hielp om de prestaties en generalisatiemogelijkheden van het model te verbeteren.
</details>

<details><summary>3.4.1 LiDAR</summary> In dit onderzoek is gekozen voor het gebruik van computer vision-technieken en het YOLOv5-objectdetectiealgoritme als primaire benadering voor het detecteren en in kaart brengen van verkeersborden in een reeks foto's. YOLOv5, bekend om zijn hoge nauwkeurigheid en real-time prestaties, werd getraind op de dataset van IV-Infra en was in staat verkeersborden met hoge nauwkeurigheid te detecteren. Deze aanpak bleek zeer effectief te zijn bij het detecteren en in kaart brengen van verkeersborden in verschillende omgevingen. Daarentegen bleek de LiDAR-technologie, die veel wordt gebruikt bij taken als objectdetectie, mapping en navigatie, minder geschikt te zijn voor deze specifieke taak. LiDAR-technologie is relatief traag, onbetrouwbaar en vereist een duidelijke zichtlijn naar het object, waardoor het moeilijk is om objecten te detecteren die aan het zicht onttrokken zijn of zich achter andere objecten bevinden. Bovendien, terwijl LiDAR voornamelijk wordt gebruikt om objecten in de 3D-ruimte te detecteren, is de detectie van verkeersborden voornamelijk een 2D-taak, met behulp van 2D-beelden en 2D-begrenzingskaders, wat met hoge nauwkeurigheid kan worden bereikt met behulp van computervisietechnieken en het YOLOv5-objectdetectiealgoritme. Deze aanpak bleek daarom efficiënter en betrouwbaarder voor dit onderzoek. Bovendien kunnen computervisietechnieken worden verbeterd door deep learning-modellen die de prestaties en robuustheid van het systeem kunnen verbeteren.
 </details>

<details><summary>4.2 Image of Created Mapping </summary> </details>

<details><summary>Conclusion</summary>Here I wrote most of the text for a teammate, thereafter they changed it to their liking.<br><br> 
  Dit onderzoekspaper presenteert een methode voor het herkennen en in kaart brengen van verkeersborden met behulp van een reeks afbeeldingen en een geavanceerd objectdetectiemodel, YOLOv5. De resultaten van dit onderzoek tonen de effectiviteit aan van het gebruik van YOLOv5 voor het herkennen en in kaart brengen van verkeersborden met hoge nauwkeurigheid en real-time prestaties. Dit onderzoek sluit aan bij de eerdere onderzoeken die zijn gedaan op het gebied van het herkennen van verkeersborden door middel van Machine Learning en Neural Networks.
Verder onderzocht het onderzoek ook het gebruik van LIDAR-technologie als een geschikt alternatief voor verkeersborddetectie. Het is eerder bewezen dat LIDAR-technologie een effectieve manier is om verkeersborden te detecteren en in kaart te brengen. Nader onderzoek wijst echter uit dat de prestaties en betrouwbaarheid onder verschillende licht- en weersomstandigheden drastisch afnemen.
Met behulp van trigonometrische berekeningen kon het onderzoek de gedetecteerde verkeersborden in kaart brengen en met behulp van de NDW-database werden de berekende coördinaten geverifieerd. Deze aanpak kan worden gebruikt als referentie voor het in kaart brengen van verkeersborden in de toekomst.
Al met al biedt deze onderzoek waardevolle inzichten in de mogelijkheden van YOLOv5 en zijn potentieel als hulpmiddel voor het in kaart brengen van verkeersborden, en het onderzoek zou kunnen worden uitgebreid om de robuustheid en nauwkeurigheid van YOLOv5 in verschillende scenario's te onderzoeken, zoals verschillende weersomstandigheden, verlichting en weg kwaliteit. De in deze onderzoek voorgestelde methoden kunnen als referentie dienen voor toekomstig onderzoek en ontwikkeling op het gebied van verkeersbordherkenning en -kartering. Het gebruik van Machine Learning en Neural Networks, en tools voor datavisualisatie hebben bewezen effectief te zijn voor het herkennen en in kaart brengen van verkeersborden, en voor het waarborgen van de veiligheid en efficiëntie van transportsystemen. Dit onderzoek draagt bij aan de voortdurende inspanningen om de veiligheid en efficiëntie van transportsystemen te verbeteren en kan worden toegepast in real-world toepassingen zoals autonome voertuigen en intelligente transportsystemen.</details>

# <a id="codesnippets"></a>Code snippets for contributions 
## FoodBoost

```py
python code here
```

## Vision

```py
python code here
```

### <a id="resize"></a>Resize images in a folder to 640x640 retaining the original name in new path

```py
import cv2
from datetime import datetime

counter = 0
now = datetime.now()
print('Starting time: ', datetime.now())

for filename in glob.glob('alles/20221005_selectie_360_5/*'):
    
    # read image
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    #print('Original Dimensions of image number ', counter, ' is: ',img.shape)
 
    # new dimensions
    width = 640
    height = 640
    dim = (width, height)
 
    # resize image
    resized = cv2.resize(img, dim)
 
    #print('Resized Dimensions : ',resized.shape)
    
    # save new image
    if filename[-5:-4] == '1':
        cv2.imwrite('resizedfinal/'+filename[-28:] ,resized)
        print(filename[-28:])
        print('Image number: ', counter)
    
        counter += 1

print('Finished time: ', datetime.now())
print('Total time: ', datetime.now()-now)
```

