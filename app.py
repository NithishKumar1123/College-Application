import csv
import sys
from jinja2 import Template
import matplotlib.pyplot as plt

def table_definition():
  table = []
  with open("data.csv", 'r') as file_object:
      data = csv.reader(file_object)
      for row in data:
          table.append(row)
      file_object.close()
  for i in range(1, len(table)):
      for j in range(len(table[i])):
          table[i][j] = int(table[i][j])
  return table[1:]

HTML1 = """
<!DOCTYPE html>
<html>
  <body>
    <h1>Student Details</h1>
    <table border = "2">
      <tr>
        <th>Student id</th>
        <th>Course id</th>
        <th>Marks</th>
      </tr>
      {% for row in result %}
      <tr>
        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
      </tr>
      {% endfor %}  
      <tr>
        <td colspan = '2' style = "text-align: center">Total Marks</td>
        <td>{{total}}</td>
      </tr>
    </table>
  </body>
</html>
"""
HTML2 = """
<!DOCTYPE html>
<html>
  <body>
    <h1>Course Details</h1>
    <table border = "2">
      <tr>
        <th>Average Marks</th>
        <th>Maximum Marks</th>
      </tr>
      <tr>
        <td>{{result}}</td>
        <td>{{total}}</td>
      </tr>
    </table>
    <img src = "img.jpg"/>
  </body>
</html>
"""
HTML3 = """
<!DOCTYPE html>
<html>
  <body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
  </body>
</html>
"""

def student(student_id, table):
  result = []
  total = 0
  flag = True
  for row in table:
    if(row[0] == student_id):
      flag = False
      result.append(row)
      total += row[2]
  if(flag):
    return (None, None)
  return (result, total)

def course(course_id, table):
  max = 0
  total = 0
  count = 0
  flag = True
  mark_list = []
  for row in table:
    if(row[1] == course_id):
      flag = False
      mark_list.append(row[2])
      total += row[2]
      count += 1
      if(max < row[2]):
        max = row[2]
  if(flag):
    return (None, None, None)
  avg = total / count
  return (avg, max, mark_list)

def get_HTML(result, total, HTML):
  temp = Template(HTML)
  html_code = temp.render(result = result, total = total)
  file = open("output.html", 'w')
  file.write(html_code)
  file.close

def main():
  flag = False
  table = table_definition()
  if(sys.argv[1] == '-s'):
    student_id = int(sys.argv[2])
    (result, total) = student(student_id, table)
    if(result == None):
      flag = True
    else:
      get_HTML(result, total, HTML1)
  elif(sys.argv[1] == '-c'):
    course_id = int(sys.argv[2])
    (avg, max, mark_list) = course(course_id, table)
    if(avg == None):
      flag = True
    else:
      plt.hist(mark_list, bins = 10)
      plt.xlabel('Marks')
      plt.ylabel('Frequency')
      plt.savefig('img.jpg')
      get_HTML(avg, max, HTML2)
      print(mark_list)
  if(flag):
    temp = Template(HTML3)
    html_code = temp.render()
    file = open("output.html", 'w')
    file.write(html_code)
    file.close

if __name__ == '__main__':
  main()