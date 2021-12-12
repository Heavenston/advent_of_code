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

canContainBag :: [(String, [(Int, String)])] -> String -> String -> Bool
canContainBag dict bag name =
    let contains = fromMaybe [] $ lookup name dict in
    bag `elem` map snd contains ||
    any (canContainBag dict bag . snd) contains

day7 target file =
    let dict = (map processLine . lines) file in
    length $ filter (canContainBag dict target . fst) dict

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day7 "shiny gold" contents
