-- Stuart Harley
-- Assignment 2

-- Problem 1
superpow num = num ^ num ^ num

-- Problem 2
firstAndLast list = [head(list), last(list)]

-- Problem 3
evenSum :: [Integer] -> Integer

evenSum list = accumSum 0 list

accumSum n list = if list == []
                  then n
                  else let x = head list
                           xs = tail list
                       in if even x
                          then accumSum (n+x) xs
                          else accumSum n xs

-- Problem 4
isCodeWithComments :: String -> Bool

isCodeWithComments str = if str == []
                         then True
                         else code str

code str = if str == []
           then True
           else if head str == 'a' || head str == ' ' || head str == '*'
                then code (tail str)
           else if head str == '/'
                then slash (tail str)
           else False

slash str = if str == []
            then True
            else if head str == '/'
                 then slash (tail str)
            else if head str == 'a' || head str == ' '
                 then code (tail str)
            else if head str == '*'
                 then comment (tail str)
            else False

comment str = if str == []
              then False
              else if head str == 'a' || head str == ' ' || head str == '/'
                   then comment (tail str)
              else if head str == '*'
                   then endComment (tail str)
              else False

endComment str = if str == []
                 then False
                 else if head str == 'a' || head str == ' '
                      then comment (tail str)
                 else if head str == '*'
                      then endComment (tail str)
                 else if head str == '/'
                      then code (tail str)
                 else False
