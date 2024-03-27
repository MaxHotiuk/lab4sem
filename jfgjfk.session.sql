SELECT document.name, document.createdate, history.changedate
FROM document
JOIN history ON document.historyid = history.id
WHERE history.id >= 3
ORDER BY document.name DESC
LIMIT 2;
