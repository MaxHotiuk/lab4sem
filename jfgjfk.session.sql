WITH document_counts AS (
    SELECT EXTRACT(YEAR FROM createdate) AS year, COUNT(*) AS document_count
    FROM document
    GROUP BY EXTRACT(YEAR FROM createdate)
)
SELECT year, document_count
FROM document_counts
WHERE document_count = (
    SELECT MAX(document_count) FROM document_counts
);


