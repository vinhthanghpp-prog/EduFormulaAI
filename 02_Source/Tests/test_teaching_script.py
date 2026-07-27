from pprint import pprint

from Modules.Teaching import TeachingScript

script = TeachingScript()

script.explanation = "Muốn xác định chiều đồ thị, hãy tìm hệ số a."

script.question = "Hệ số a bằng bao nhiêu?"

script.answer = "2"

script.feedback = "Chính xác."

script.hint = "Nhìn số đứng trước x."

script.transition = "Chúng ta sang bước tiếp."

pprint(script.to_dict())