CREATE TABLE zendesk_raw.messages (
    id INT64,
    conversation_id INT64,
    sender STRING,
    content TEXT,
    created_at TIMESTAMP
);
