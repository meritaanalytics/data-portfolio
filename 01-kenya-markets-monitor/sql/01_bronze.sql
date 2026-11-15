CREATE TABLE IF NOT EXISTS bronze_fx_raw (
    rate_date  DATE PRIMARY KEY,
    payload    JSONB NOT NULL,
    loaded_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
