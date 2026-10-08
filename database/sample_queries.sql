-- Verify recent metadata records
SELECT id, file_name, processed_at, status, source
FROM metadata
ORDER BY id DESC
LIMIT 10;
