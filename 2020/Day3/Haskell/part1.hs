import Data.List
import Data.List.Split
import Data.Function
import System.IO
import Control.Concurrent

aux 0 l (a:q)
  | a == '#'  = 1
  | otherwise = 0
aux x l [] = aux x l l
aux x l (_:q) = aux (x-1) l q

day3 b =
    inner 0 b
    where
        inner _ []     = 0
        inner x (l:b) = aux x l l + inner (x+3) b

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day3 (lines contents)
