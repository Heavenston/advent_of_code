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

day3 board (right, down) =
    inner 0 board
    where
        inner _ []     = 0
        inner x (line:b) = aux x line line
                         + inner (x + right) (drop down (line:b)) 

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    let result = product $ map (day3 $ lines contents) slopes
    print result
