
## Description

This LLMchat project is a Flask API that provides several endpoints for different tasks such as commenting, grading, question generation, summarizing, marking, speech feedback, and transcript correction.

## Note
The assignment / service context key and value are not compulsory so to adapt to Aireas. You can ignore the key, or add key without the value.
```json 
'assignment context': " ",
'service context' : " ",
```

## API Usage

The current LLMchat API provides the following endpoints:

### 1. `/comment`

- Method: POST
- Input: JSON with keys 'all_criteria', 'journal', 'assignment context'
- Output: JSON with key 'comment' , the comment is in HTML format

#### Input sample
```json
{
 "all_criteria" : [
    "Ability to link: Demonstrates a comprehensive understanding of how service-learning is connected to the academic content of the subject. Effectively integrates theoretical concepts with practical application in the service project.",
    "Ability to evaluate: Provides a thorough and insightful evaluation of the group's performance in the service project. Reflects a reflective analysis of strengths, weaknesses, and areas for improvement.",
    "Problem-solving: Showcases excellent problem-solving skills during the service project. Effectively identifies and resolves challenges encountered, with clear explanations of strategies used.",
    "Communication: Demonstrates exceptional communication skills with the service recipients. Effectively conveys information, actively listens, and shows sensitivity to the needs and perspectives of the recipients.",
    "Empathy: Reflects a deep and genuine empathy for the less fortunate people in society. Demonstrates a strong understanding of their struggles and needs, with insightful reflections on personal growth and transformation.",
    "Reflection: Exhibits excellent reflection on the group's role and responsibilities in society. Demonstrates deep insights into personal and social implications and offers thoughtful analysis of the impact of the service project."
 ],
 "assignment context": " ",
 "journal": "\nIntroduction\n ......  success."

}
```
#### Output sample
```json
{
    "comment": "<div>  <h3 class=\"text-lg font-semibold text-gray-700\">Feedback on Service-Learning Assignment</h3>  <h4 class=\"text-md font-semibold text-gray-700\">Strengths</h4>  <ul class=\"text-md font-base text-gray-700\">    <li>Excellent introduction that sets a clear and engaging context for the service-learning project in Cambodia.</li>    <li>Good identification of the project's mission, focusing on empowering Cambodian students through digital literacy.</li>    <li>Recognition of the importance of digital literacy in bridging the digital divide is well articulated.</li>  </ul>  <h4 class=\"text-md font-semibold text-gray-700\">Areas for Improvement</h4>  <ul class=\"text-md font-base text-gray-700\">    <li>Expand on how the academic content of the subject was linked to the service-learning project. Detailing the theoretical concepts taught and how they were applied in practice would strengthen this section.</li>    <li>Include a more thorough evaluation of the group's performance. Reflect on the strengths, weaknesses, and areas for improvement in the service project to provide a more insightful analysis.</li>    <li>Elaborate on the problem-solving strategies used during the project. Discuss specific challenges encountered and how they were resolved.</li>    <li>Enhance the section on communication by detailing how your team effectively communicated with the service recipients, including examples of active listening and sensitivity to their needs.</li>    <li>Deepen the reflection on empathy by sharing personal stories or observations that demonstrate a genuine understanding and concern for the struggles faced by the less fortunate in Cambodia.</li>    <li>Provide a more detailed reflection on the group's role and responsibilities in society, including the personal and social implications of the service project. Offer thoughtful analysis on the impact of your work.</li>  </ul></div>"
}
```

### 2. `/grade`

- Method: POST
- Input: JSON with keys 'criteria', 'journal', 'assignment context'
- Output: JSON with key 'grade'

#### Input sample
```json
{
 "criteria" : [
    "Clarity: Uses paragraphs effectively to structure ideas, employs thesis statements, topic sentences and transition to promote clarity, connects ideas logically within and between paragraphs, and communicates clearly through accurate language",
    "Analysis: Provides relevant content to the writing topic, connects service to new learning, demonstrates critical analysis",
    "Appropriacy: Balances description and analysis",
    "Comprehension: Demonstrates a clear understanding of the material or experiences being reflected upon, including their complexities and implications.",
    "Personal Growth: Shows evidence of personal growth, learning, and development through the reflection process, indicating how experiences have impacted their perspectives or skills.",
    "Critical Thinking: Engages in critical analysis of their own assumptions, beliefs, and values in relation to the topic or experience, considering multiple viewpoints.",
    "Application: Effectively applies theoretical concepts or course material to personal experiences or practical situations, illustrating the connection between theory and practice.",
    "Reflective Insight: Provides deep, insightful reflections that demonstrate self-awareness and a high level of engagement with the reflection process.",
    "Writing Quality: Presents ideas in a well-organized, coherent manner with clarity, using appropriate style and grammar, and is free from spelling and punctuation errors."
 ],
 "journal": "Promoting digital literacy can have a significant impact on Cambodia's development in several ways ................ resource."

}
```
#### Output sample
```json
{
    "grade": {
        "Analysis": {
            "Main_Grade": "B",
            "Reason_of_Main_Grading": "Provides relevant content and demonstrates an understanding of the impact of digital literacy on Cambodia's development. However, the analysis could be deepened with more critical examination of the challenges and solutions proposed."
        },
        "Application": {
            "Main_Grade": "B+",
            "Reason_of_Main_Grading": "Effectively applies theoretical concepts to practical situations, illustrating the connection between theory and practice in the context of Cambodia. The examples provided are relevant and support the argument well."
        },
        "Appropriacy": {
            "Main_Grade": "B+",
            "Reason_of_Main_Grading": "The assignment maintains a good balance between description and analysis, effectively using personal experiences to highlight the importance of digital literacy in Cambodia."
        },
        "Clarity": {
            "Main_Grade": "B-",
            "Reason_of_Main_Grading": "The assignment demonstrates a structured approach with clear paragraphs and logical connections between ideas. However, the lack of a strong thesis statement and occasional unclear transitions between topics slightly hinder the overall clarity."
        },
        "Comprehension": {
            "Main_Grade": "B",
            "Reason_of_Main_Grading": "Shows a clear understanding of the material and the complexities involved in promoting digital literacy in Cambodia. However, a deeper exploration of the implications of these efforts could enhance comprehension."
        },
        "Critical Thinking": {
            "Main_Grade": "B-",
            "Reason_of_Main_Grading": "Engages in some level of critical analysis of assumptions and beliefs regarding digital literacy. However, the exploration of multiple viewpoints and deeper questioning of these assumptions could be improved."
        },
        "Personal Growth": {
            "Main_Grade": "A-",
            "Reason_of_Main_Grading": "The reflection on personal growth and the development of digital literacy skills in Cambodia is evident and well-articulated, indicating a significant level of learning and development."
        },
        "Reflective Insight": {
            "Main_Grade": "A",
            "Reason_of_Main_Grading": "Provides deep, insightful reflections that demonstrate a high level of self-awareness and engagement with the reflection process. The reflections on challenges and solutions are particularly strong."
        },
        "Writing Quality": {
            "Main_Grade": "B-",
            "Reason_of_Main_Grading": "The writing is generally well-organized and coherent. However, there are minor issues with style and grammar, and a few spelling and punctuation errors that detract from the overall quality."
        }
    }
}
```

### 3. `/question`

- Method: POST
- Input: JSON with keys 'journal', 'service_context', 'history', 'question'
- Output: JSON with key 'answer'

#### Input sample
```json
{
    "journal": "Here is the journal that you need to grade. Journal: Being a student for many years, I have met various teachers, some are good and some are bad. I have always thought quality teaching is easy, just reading the textbook and understanding the content before class, you can then fluently present the knowledge and 'teach' them. Little did I know, quality teaching extends much more than that, from catching students' attention to delivering the teaching kit, many preparations are required for a merely 6-session course. This service-learning course has given me a brand-new insight into what is quality teaching and how to achieve it. Quality teaching can only be achieved with students' attention. Before the detailed preparation of the teaching kit, I attended the Baptist Oi Kwan centre visit to trial out teaching lessons. Once we entered the classroom, we saw students running around the classroom",
    "service_context": "It's about education.",
    "history": [{ "question": "What is it talking about?", "answer": "The journal is discussing the student's realization that quality teaching requires more than just reading the textbook and understanding the content. It highlights the importance of catching students' attention and the preparations needed for a 6-session course. The student gained this insight through a service-learning course and a visit to the Baptist Oi Kwan center. The journal does not provide specific details about the volunteering service experiences." },
    
    {"question": "How can it write better?", "answer" : "To improve the writing, the student could provide specific details about their volunteering service experiences and how it relates to their understanding of quality teaching. Additionally, they could elaborate on the preparations needed for a 6-session course and how they applied these preparations during their teaching lessons. Adding more specific examples and reflecting on the impact of their actions would enhance the journal's clarity and depth."}],
    "question": "What is the best part of the journal"
}
```
#### Output sample
```json
{
    "answer": "The best part of the journal is the student's realization that quality teaching involves more than just understanding the content, emphasizing the importance of engaging students and the extensive preparations required for effective teaching. This insight, gained through a service-learning course and a visit to the Baptist Oi Kwan center, showcases a significant shift in the student's understanding of what constitutes quality teaching."
}
```

### 4. `/summaryNsentiment`

- Method: POST
- Input: JSON with keys 'text', 'assignment context'
- Output: JSON with the summary and sentiment analysis

#### Input sample
```json
{
    "text": "Promoting digital literacy can have a significant impact on Cambodia's development in several ways. ................lacking resource."
}
```
#### Output sample
```json
{
    "Key_Points": "Promoting digital literacy in Cambodia addresses the digital divide and supports development by improving education and entrepreneurship opportunities. Challenges include resource limitations, technological knowledge gaps, and language barriers. Solutions involve adapting teaching methods, utilizing affordable technology, and advocating for increased resources and support.",
    "Sentiment": "Positive",
    "Summary": "The reflection discusses the significant impact of promoting digital literacy in Cambodia, highlighting its potential to bridge the digital divide and foster development in education and entrepreneurship. The author shares experiences from workshops, noting challenges such as limited technological knowledge among students, language barriers, and resource constraints. To overcome these, strategies like adjusting teaching methods, using simpler concepts, and incorporating visual aids were employed. The author emphasizes the responsibility of individuals with higher digital literacy to contribute to reducing the digital divide. The reflection concludes with suggestions for improving resource availability, including government support and the use of affordable technology."
}
```

### 5. `/marking`

- Method: POST
- Input: JSON with keys 'assignment context', 'question', 'sample solution', 'total marks', 'student solution'
- Output: JSON with the marking result

#### Input sample
```json
{
    "assignment context" : [
        "subject: Computer Science",
        "topic: Search algorithm",
        "difficulty: Intermediate",
        "type: Open-ended"
    ],
    "question" : [
        "What is the difference between breadth-first search (BFS) and depth-first search(DFS) in terms of their exploration strategy?"
    ],
    "sample solution" : [
        "BFS explores the search space level by level, visiting all neighbors of a node beforemoving on to the next level(1.5 marks). DFS, on the other hand, explores as far as possible alongeach branch before backtracking(1.5 marks)."
    ],
    "total marks" :[
        "3"
    ],
    "student solution" :[
        "BFS use FIFS and DFS use LIFO. "
    ]
}
```
#### Output sample

```json
[
    {
        "explanation": "The student's response correctly identifies the underlying data structures used by BFS and DFS, which are indeed crucial to their exploration strategies. BFS uses a queue (FIFO - First In First Out) approach to explore level by level, while DFS uses a stack (LIFO - Last In First Out) to explore as far as possible along each branch before backtracking. However, the response lacks detail on how these strategies impact the exploration process itself, such as visiting all neighbors of a node before moving on to the next level for BFS, and exploring as far as possible along each branch before backtracking for DFS. Therefore, the student receives half of the total marks for correctly identifying the data structures but not fully explaining their impact on the exploration strategies.",
        "marking": "1.5"
    }
]
```

### 6. `/speech_feedback` (Under development)

- Method: POST
- Input: JSON with keys 'assignment context', 'gaze', 'clear_view', 'filler_word', 'pronunciation_error', 'transcript_count', 'transcript'
- Output: JSON with key 'speech feedback'

#### Input sample
```json
{
    "assignment context":"",
    "gaze":[{"gaze":0.8}],
    "clear_view":[{"clear_view":0.9}],
    "filler_word":[{
	"total_count": 43,
	"filler_words": {
		"um": 4,
		"uh": 2,
		"oh": 3,
		"er": 6,
		"ah": 5,
		"you know": 7,
		"well": 3,
		"so": 4,
		"i mean": 5,
		"just": 4
	}
    }],
    "pronunciation_error":"",
    "transcript_count":"",
    "transcript":""
}
```
#### Output sample
```json
No output sample yet
```

### 7. `/transcript_correction` (Under development)

- Method: POST
- Input: JSON with keys 'assignment context', 'transcript'
- Output: JSON with the corrected transcript

#### Input sample
```json
{
    "assignment context":"",
    "transcript":""
}
```
#### Output sample
```json
No output sample yet
```

### 8. `/question_generation`

- Method: POST
- Input file format: pdf, pptx, docx. 
- Input keys: Form data with file key 'subject_context', and text keys: 'difficulty', 'question_type', 'num_questions', 'num_choices', 'requirement'.
- Output Json: JSON with the generated questions, with keys of 'Question', 'Answers', 'Correct_answer', 'Explanation'.
- Output file: Two question documents in docx format: one for the teacher and one for the student.
- Storage: The uploaded file is stored in the 'uploads' folder, The generated question documents are stored in the 'output' folder.

#### Input sample
```json
form-data
{
    
    "subject_context": the course file,
    "difficulty": "Intermediate",
    "question_type": "multiple choice",
    "num_questions": "2",
    "num_choices": "4",
    "requirement": "You may come up with coding, memorize knowledge questions, noted that the generated quesition cannot exceed the subject_context range."
}
```
#### Output sample
```json
[
    {
        "Answers": {
            "A": "Strings are mutable.",
            "B": "Strings can be created using the 'new' keyword only.",
            "C": "String objects are immutable.",
            "D": "StringBuffer is faster than StringBuilder because it is not synchronized."
        },
        "Correct_answer": "C",
        "Explanation": "String objects in Java are immutable, meaning once created, their values cannot be changed.",
        "Question": "Which of the following statements is true about strings in Java?"
    },
    {
        "Answers": {
            "A": "It ensures that all strings are mutable.",
            "B": "It creates a new object for each string literal.",
            "C": "It improves efficiency by reusing instances for strings with the same character sequence.",
            "D": "It automatically encrypts string literals."
        },
        "Correct_answer": "C",
        "Explanation": "Interning of strings in Java improves efficiency and saves memory by reusing instances for strings with the same character sequence.",
        "Question": "What does the 'interning' of strings in Java help with?"
    }
]
```