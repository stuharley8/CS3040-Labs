-- Stuart Harley
-- Exercise 2

-- Problem 1
countPositive [] = 0
countPositive (x:rest) = if x > 0
                         then x + (countPositive rest)
                         else countPositive rest

-- Problem 2
countPositive2 list = (sum (map (\x -> if x < 0 then 0 else x) list))

-- Problem 3
data Vehicle = Car | Bicycle | Bus Integer
capacity Car = 5
capacity Bicycle = 1
capacity (Bus n) = if n > 0 then n else 0

totalCapacity list = sum (map capacity list)

-- Problem 4
foot [] = error "foot: empty list"
foot (x:[]) = x
foot (x:rest) = foot rest