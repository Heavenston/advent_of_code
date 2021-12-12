import Data.List;
import Data.Function;
import Data.Functor.Composition;
import System.IO

slidingChunk :: [Int] -> Int -> [[Int]]
slidingChunk [] p = []
slidingChunk (a:q) p =
    take p (a:q) : slidingChunk q p

part1 :: [Int] -> Int
part1 l = length $ filter (uncurry (>)) $ zip (tail l) l

-- day1 :: [Int] -> Int
-- day1 l =
--     let windows = filter ((==3) . length) (slidingChunk l 3) in
--     part1 (map sum windows)

day1 l = part1 $ zipWith3 (\a b c -> a + b + c) l (tail l) (tail $ tail l)

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    let numbers = map read (lines contents) :: [Int]
    print $ day1 numbers
