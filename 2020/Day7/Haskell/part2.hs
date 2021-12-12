import Data.List.Extra
import Data.Function
import Data.Bifunctor
import Data.Maybe
import System.IO
import Control.Concurrent
import Text.Read

breakOmit s =
    second (drop $ length s) .
    breakOn s

processLine :: String -> (String, [(Int, String)])
processLine =
    second processContains .
    breakOmit " bags contain "
    where
        processContains =
            map (
                bimap
                    (fromMaybe 0 . readMaybe . trim :: String -> Int)
                    (trim . dropSuffix "bag" . dropSuffix "bags" . dropSuffix ".") .
                breakOmit " "
            ) .
            splitOn ", "

countContainingBags:: [(String, [(Int, String)])] -> String -> Int
countContainingBags dict name =
    let contains = fromMaybe [] $ lookup name dict in
    sum (map (uncurry (*) . second ((+1) . countContainingBags dict)) contains)

day7 target file =
    let dict = (map processLine . lines) file in
    countContainingBags dict "shiny gold"

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day7 "shiny gold" contents
