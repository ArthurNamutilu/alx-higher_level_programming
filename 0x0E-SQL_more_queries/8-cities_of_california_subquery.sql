-- This script checks if city and state id are the same
SELECT  id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
