SELECT
    E.EMP_NO,
    E.EMP_NAME,
    IF(G.SCO >= 96, 'S', 
       IF(G.SCO >= 90, 'A',
          IF(G.SCO >= 80, 'B', 'C'
        ))) AS GRADE,
    IF(G.SCO >= 96, E.SAL * 0.2,
       IF(G.SCO >= 90, E.SAL * 0.15,
          IF(G.SCO >= 80, E.SAL * 0.1, 0
        ))) AS BONUS
FROM HR_EMPLOYEES E
JOIN (
    SELECT
        EMP_NO,
        AVG(SCORE) AS SCO
    FROM HR_GRADE
    GROUP BY EMP_NO
) G ON E.EMP_NO = G.EMP_NO
ORDER BY E.EMP_NO;