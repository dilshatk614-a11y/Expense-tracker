books=[
{"title":"Python Mastery","tags":["python","programming","beginner"],"rating":4.7},
{"title":"Data Science Essentials","tags":["python","data science"],"rating":4.9},
{"title":"AI Fundamentals","tags":["python","ai","data science"],"rating":4.9},
{"title":"Web Development","tags":["html","css","javascript"],"rating":4.5}
]
required_tags=["python","data science"]
minimum_rating=4.8
r=[]
for i in books:
    if all(tag in i["tags"] for tag in required_tags) and i["rating"]>minimum_rating:
        r.append(i["title"])
r.sort()        
print(r)		  