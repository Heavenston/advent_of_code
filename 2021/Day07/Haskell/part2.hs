import Data.List.Extra;
import Data.Function;
import Data.Functor.Composition;
import Data.Bifunctor
import System.IO

breakOmit s =
    second (drop $ length s) .
    breakOn s
readBinary :: String -> Int
readBinary = foldl (\acc a -> acc * 2 + (if a == '0' then 0 else 1)) 0

day7 input =
    let numbers = map (read . trim :: String -> Int) . splitOn "," $ input in
    minimum $ map (\i -> sum $ map (addExp . abs . (i-)) numbers) [0..1000]
        where
            addExp n = (n*(n+1)) `quot` 2

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day7 contents
    
