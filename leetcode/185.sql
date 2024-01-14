# Write your MySQL query statement below
WITH EMPLOYEE_RANK AS (
    SELECT id,
           name AS employee,
           salary,
           departmentId,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary desc) AS salaryRank
    FROM EMPLOYEE
)
SELECT name AS Department,
       employee AS Employee,
       salary AS Salary 
FROM EMPLOYEE_RANK
    INNER JOIN DEPARTMENT
    ON (EMPLOYEE_RANK.departmentId = DEPARTMENT.id)
WHERE salaryRank <= 3
