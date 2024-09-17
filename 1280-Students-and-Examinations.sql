# Write your MySQL query statement below
SELECT Students.student_id, Students.student_name, Subjects.subject_name, count(Examinations.subject_name) as attended_exams FROM Students
CROSS JOIN Subjects 
LEFT JOIN Examinations on 
Students.student_id = Examinations.student_id and Subjects.subject_name = Examinations.subject_name
group by Students.student_id, Students.student_name, Subjects.subject_name
order by Students.student_id, Subjects.subject_name


