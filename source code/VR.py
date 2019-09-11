import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(version='2016-05-20',
                                         api_key='6ba0dc9f-6af7-4d4a-bb87-42adfb2920bc:yNUpwpwXBQSw',
                                         url='https://gateway.aibril-watson.kr/visual-recognition/api')


image_path = 'photos/2098.jpg'
with open(image_path, 'rb') as image_file:
    result = visual_recognition.classify(images_file=image_file)
    print json.dumps(result, indent=2)



# api_key = {
# "username": "6ba0dc9f-6af7-4d4a-bb87-42adfb2920bc",
# "password": "yNUpwpwXBQSw"
# }

# api_key = {
# "url" : "https://gateway.aibril-watson.kr/visual-recognition/api",
# "username" : "6ba0dc9f-6af7-4d4a-bb87-42adfb2920bc",
# "password" : "yNUpwpwXBQSw"
# }

# api_key = '''{"username" : "6ba0dc9f-6af7-4d4a-bb87-42adfb2920bc","password" : "yNUpwpwXBQSw"}'''



# visual_recognition = VisualRecognitionV3(url='https://gateway.aibril-watson.kr/visual-recognition/api/v3/classify',
#                                          username='6ba0dc9f-6af7-4d4a-bb87-42adfb2920bc',
#                                          password='yNUpwpwXBQSw',
#                                          version='2016-05-20')

# visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)



# with open('api_key.json', 'rb') as json_file:
#     api_key = json.load(json_file)
#     print api_key
#     visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)
#
#     image_path = 'photos/2098.jpg'
#     with open(image_path, 'rb') as image_file:
#         result = visual_recognition.classify(images_file=image_file)
#         print json.dumps(result, indent=2)