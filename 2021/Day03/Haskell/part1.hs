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

day3 input =
    let initHist = map (const (0, 0)) [length (head input)..] in
    let hist = foldl registerToHist initHist input in
    let gammaRate = readBinary $ map (\(z, o) -> if z > o then '0' else '1') hist in
    let other = readBinary $ map (\(z, o) -> if z < o then '0' else '1') hist in

    gammaRate * other

    where
        registerToHist =
            zipWith (\(zeros, ones) v -> if v == '0' then (zeros + 1, ones) else (zeros, ones + 1))

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day3 $ lines contents
