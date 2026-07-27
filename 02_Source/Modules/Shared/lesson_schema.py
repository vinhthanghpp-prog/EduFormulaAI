"""
EduFormula AI

Lesson Schema v3
"""


def create_empty_lesson():

    return {

        "metadata":{

            "id":"",

            "subject":"",

            "grade":"",

            "chapter":"",

            "lesson":"",

            "title":"",

            "version":"1.0"

        },

        "objectives":[],

        "motivation":"",

        "concept":{

            "content":""

        },

        "formula":{

            "expression":"",

            "latex":"",

            "description":""

        },

        "variables":[],

        "visualization":{

            "graph":None,

            "animation":None,

            "interactive":False

        },

        "examples":[],

        "practice":[],

        "common_mistakes":[],

        "summary":"",

        "tips":[]

    }