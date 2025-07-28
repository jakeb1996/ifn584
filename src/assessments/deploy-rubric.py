# Adapted from the `canvastools/canvas_rubric` tool: 
#    https://github.com/mckaguem/canvastools/tree/281561c7b1d494b21feda943593d0b77f8528cd8/canvas_rubric


from canvasapi import Canvas
import configparser
import logging, sys
from pathlib import Path
import yaml
from pprint import pprint
import pathlib

def enableDebug():
    logger = logging.getLogger("canvasapi")
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


def readConfiguration(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    url = config.get('Credentials', 'url')
    access_token = config.get('Credentials', 'access_token')

    return url, access_token


def connectToCanvasCourse(url, access_token, courseNum):
    return Canvas(url, access_token).get_course(courseNum)


def createRubric(course, assign, rubric):
    r = course.create_rubric(rubric=rubric)
    rubric = r['rubric']
    course.create_rubric_association(
        rubric_association={
            'rubric_id': rubric.id,
            'association_type': 'Assignment',
            'association_id': assign,
            'purpose': 'grading',
        }
    )


def readRubricFromFile(fileName):
    with Path(fileName).open() as theFile:
        rubricYaml = yaml.safe_load(theFile)
    
    rubric = dict(rubricYaml)
    criteria = rubricYaml.get('criteria', list())
    criteriaDict = dict()
    for j, criterionYaml in enumerate(criteria):
        criterionDict = dict(criterionYaml)
        ratingsYaml = criterionYaml.get('ratings', list())
        ratingsDict = dict()
        for k, rating in enumerate(ratingsYaml):
            ratingsDict[k] = rating
        
        criterionDict['ratings'] = ratingsDict
        criteriaDict[j] = criterionDict

    rubric['criteria'] = criteriaDict

    return rubric


def find_canvas_credentials():
    home_dir = pathlib.Path.home()  # Cross-platform way to get home directory
    canvas_dir = home_dir / ".canvas"
    credentials_file = canvas_dir / "credentials.ini"
    
    if not credentials_file.exists():
        print(f"Cannot find: {credentials_file}")
        
    return credentials_file

if __name__ == '__main__':
    # enableDebug()
    
    filename = sys.argv[1]
    
    courseNum = sys.argv[2]

    assign = sys.argv[3]

    rubric = (readRubricFromFile(filename))

    #course = connectToCanvasCourse(*readConfiguration(find_canvas_credentials()), courseNum)

    course = connectToCanvasCourse(*readConfiguration('/mnt/c/Users/bradfoj3/.canvas/credentials.ini'), courseNum)

    createRubric(course, int(assign), rubric)
    

