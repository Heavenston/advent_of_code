import Data.List;
import Data.Function;
import Data.Functor.Composition;
import System.IO

day1 l = length $ filter (uncurry (>)) $ zip (tail l) l
 
-- 'Point free' version ^^'
-- day1 = length . filter (uncurry (>)) . dupe (flip zip . tail)
--     where dupe f a = f a a


main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    let numbers = map read (lines contents) :: [Int]
    print $ day1 numbers
