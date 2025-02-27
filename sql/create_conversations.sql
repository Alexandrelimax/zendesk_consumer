CREATE TABLE zendesk_raw.conversations (
    id INT64,
    ticket_id INT64,
    sender STRING,
    message TEXT,
    created_at TIMESTAMP
);
