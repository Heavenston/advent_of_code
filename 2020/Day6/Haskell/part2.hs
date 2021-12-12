import Data.List.Extra
import Data.Function
import Data.Bifunctor
import Data.Maybe
import System.IO
import Control.Concurrent

day5 :: String -> Int
day5 =
    sum .
    map ( -- Append all answers of all groups, remove dulicate and count
        length .
        foldr1 intersect .
        filter (not . null) .
        splitOn "\n"
    ) .
    splitOn "\n\n" -- Split all different groups
    

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day5 contents
