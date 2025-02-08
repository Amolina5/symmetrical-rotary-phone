
--How to drp tables:
--DROP TABLE task;

-- create out table
create TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(64),
    summary VARCHAR(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (
    name,
    summary,
    description
) VALUES
(
    "walk the dog",
    "Take Fido out for a stroll",
    "Make sure you go three laps around the park"
),
(
    "wash dishes",
    "All the dishes must be washed before 10pm",
    "Makes sure use the fancy new dish soap"
),
(
    "Buy groceries",
    "Go to the supermarket and but the gtoceries",
    "we need egg, bacon and tomatoes"
);