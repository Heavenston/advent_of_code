import Data.List
import Data.List.Split
import Data.Function
import System.IO
import Control.Concurrent

day2 =
    length.filter
    (\w ->
        let splits = splitOneOf " :-" w in
        let min = read (head splits) in
        let max = read (splits !! 1) in
        let char = head $ splits!!2 in
        let n = (length.filter (==char)) (splits!!4) in
            n >= min && n <= max
    )

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day2 (lines contents)
