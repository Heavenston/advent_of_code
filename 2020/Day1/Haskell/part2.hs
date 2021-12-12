import Data.List
import Data.Function
import Data.Functor.Composition
import System.IO
import Control.Concurrent

-- subcouples p =
--    filter ((==2).length) . subsequences

subcouples 1 l = map (: []) l
subcouples p l =
    [ a:q | q <- subcouples (p-1) l,
            a <- l ]

subf p l =
    map (\m -> (sum m, m)) (subcouples p l)
day1part2 p l =
    lookup 2020 (subf p l) >>= Just . product

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    let numbers = map read (lines contents) :: [Int]
    print $ day1part2 3 numbers
