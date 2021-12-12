import Data.List;
import Data.Function;
import Data.Functor.Composition;
import System.IO

subcouples =
    filter ((==2).length) . subsequences
subf l =
    map (\[a,b] -> (a+b, (a, b))) (subcouples l)
day1 l =
    lookup 2020 (subf l) >>= (\(a, b) -> Just $ a * b)

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    let numbers = map read (lines contents) :: [Int]
    print $ day1 numbers
