# Write your MySQL query statement below
# Department.id is not null
# for each departments, find the highest salary
# in any order

-- select b.name as Department, a.name as Employee, a.salary as Salary
-- from Employee as a
-- join Department as b
-- on a.departmentId = b.id
-- group by a.departmentId
-- having a.salary = max(a.salary)

SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM Employee e
JOIN Department d
  ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);