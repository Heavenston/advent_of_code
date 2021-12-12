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
    readBinary (co2ScrubberRatin 0 input) * readBinary (oxygenGeneratorRatin 0 input)

    where
        getDigitHist index =
            foldl (\(zeros, ones) s -> if s !! index == '0' then (zeros + 1, ones) else (zeros, ones + 1)) (0, 0)

        oxygenGeneratorRatin i input =
            if null (tail input) then head input else
            let (z, o) = getDigitHist i input in
            let newInput = filter (\l -> if z > o then l !! i == '0' else l !! i == '1') input in

            oxygenGeneratorRatin (i+1) newInput 
        co2ScrubberRatin i input =
            if null (tail input) then head input else
            let (z, o) = getDigitHist i input in
            let newInput = filter (\l -> if z <= o then l !! i == '0' else l !! i == '1') input in

            co2ScrubberRatin (i+1) newInput

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day3 $ lines contents
