-- 1. Latest NAV of Axis Bluechip
SELECT * FROM axis_bluechip
ORDER BY date DESC
LIMIT 1;

-- 2. Latest NAV of HDFC Top100
SELECT * FROM hdfc_top100
ORDER BY date DESC
LIMIT 1;

-- 3. Average NAV of Axis Bluechip
SELECT AVG(nav)
FROM axis_bluechip;

-- 4. Maximum NAV of HDFC Top100
SELECT MAX(nav)
FROM hdfc_top100;

-- 5. Minimum NAV of HDFC Top100
SELECT MIN(nav)
FROM hdfc_top100;

-- 6. Total records in SBI Bluechip
SELECT COUNT(*)
FROM sbi_bluechip;

-- 7. Average NAV of ICICI Bluechip
SELECT AVG(nav)
FROM icici_bluechip;

-- 8. Highest NAV among Kotak Bluechip
SELECT MAX(nav)
FROM kotak_bluechip;

-- 9. Latest NAV of Nippon LargeCap
SELECT *
FROM nippon_largecap
ORDER BY date DESC
LIMIT 1;

-- 10. Average NAV of all funds
SELECT
(
    (SELECT AVG(nav) FROM axis_bluechip) +
    (SELECT AVG(nav) FROM hdfc_top100) +
    (SELECT AVG(nav) FROM icici_bluechip) +
    (SELECT AVG(nav) FROM kotak_bluechip) +
    (SELECT AVG(nav) FROM nippon_largecap) +
    (SELECT AVG(nav) FROM sbi_bluechip)
) / 6;