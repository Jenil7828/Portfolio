from django.shortcuts import render
from django.http import *
# Create your views here.
details ={
        'name': 'Jenil Girish Rathod',
        'age':21,
        'email': 'jenilrathod478@gmail.com',
        'mobile':'8983672417', 
        'skills':['Python', 'TensorFlow', 'PyTorch', 'Scikit-learn'],
        'journey':'My journey in AI started with a fascination for data-driven decision-making and automation. I love experimenting with new algorithms and optimizing models for performance and efficiency.'
}
edu = [
    {
        'degree': 'B.E. Computer Engineering',
        'university': 'Savitribai Phule Pune University',
        'year': '2022-2026',
        'cgpa': '8.5/10',
        'honours': 'Artificial Intelligence and Machine Learning',
        'link':'http:////www.unipune.ac.in//'
    },
    {
        'degree': 'HSC',
        'university': 'Central Board of Secondary Education',
        'year': '2020-2022',
        'cgpa': '91.80/100',
        'link': 'https:////www.cbse.gov.in//'
    },
    {
        'degree': 'SSC',
        'university': 'Maharashtra State Board of Secondary and Higher Secondary Education',
        'year': '2010-2020',
        'cgpa': '85.00/100',
        'link': '#'

    }
]
skill = [
    {
        'name': 'Python',
        'level': 'Expert',
        'description': 'Python is a high-level, interpreted programming language that is widely used for various applications such as web development, scientific computing, data analysis, artificial intelligence, and more.',
        'link': 'https://www.python.org//',
    },
    {
        'name': 'C++',
        'level': 'Intermediate',
        'description': 'C++ is a high-performance, compiled, general-purpose programming language that was developed as an extension of the C programming language.',
        'link': 'https://isocpp.org//',
        
    },
    {
        'name': 'Java',
        'level': 'Intermediate',
        'description': 'Java is an object-oriented programming language that is designed to have as few implementation dependencies as possible.',
        'link': 'https://www.java.com/en//',
    },
    {
        'name': 'Tkinter',
        'level': 'Intermediate',
        'description': 'Tkinter is Python\'s de-facto standard GUI (Graphical User Interface) package.',
        'link': 'https://docs.python.org/3/library/tkinter.html',
    },
    {
        'name': 'Django',
        'level': 'Beginner',
        'description': 'Django is a high-level Python web framework that encourages rapid development and clean pragmatic design.',
        'link': 'https://www.djangoproject.com//',
    },
    {
        'name': 'TensorFlow',
        'level': 'Beginner',
        'description': 'TensorFlow is an open-source software library for numerical computation, particularly well-sued for large-scale machine learning and deep learning applications.',
        'link': 'https://www.tensorflow.org//',
    },
    {
        'name': 'Pandas',
        'level': 'Expert',
        'description': 'Pandas is a powerful data analysis and manipulation library in Python.',
        'link': 'https://pandas.pydata.org//',
    },
    {
        'name': 'NumPy',
        'level': 'Expert',
        'description': 'NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.',
        'link': 'https://numpy.org//',
    },
    {
        'name': 'Mysql',
        'level': 'Intermediate',
        'description': 'MySQL is an open-source relational database management system.',
        'link': 'https://www.mysql.com//',
    },
    {
        'name': 'HTML',
        'level': 'Beginner',
        'description': 'HTML (HyperText Markup Language) is the standard markup language used to create web pages.',
        'link': 'https://www.w3schools.com/html//',
    },
    {
        'name': 'CSS',
        'level': 'Beginner',
        'description': 'CSS (Cascading Style Sheets) is a styling language used to control the layout and appearance of web pages.',
        'link': 'https://www.w3schools.com/css//',
    },
    {
        'name': 'JavaScript',
        'level': 'Beginner',
        'description': 'JavaScript is a high-level, dynamic, and interpreted programming language that is primarily used for client-side scripting on the web.',
        'link': 'https://www.javascript.com//',
    }
]

resume = {}
def main(request):
    return render(request, "app/index.html", context={'details':details})

def about(request):
    return render(request, "app/about.html", context={'details':details})

def education(request):
    return render(request, "app/education.html", context={'education':edu})

def resume(request):
    return render(request, "app/resume.html", context={'resume':resume})

def skills(request):
    return render(request, "app/skills.html", context={'skills':skill})
