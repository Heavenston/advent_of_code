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

boardSize = 5

day4 input =
    let parts = splitOn "\n\n" input in

    let numbers = head parts in
    let numbersL = splitOn "," numbers in
    let numbersP = map (read . trim :: String -> Int) numbersL in

    let boards = tail parts in
    let boardsL = map (map trim . splitOn "\n" . dropSuffix "\n") boards in
    let boardsL2 = map (map $ splitOn " " . replace "  " " ") boardsL in
    let boardsP = map (map $ map (read :: String -> Int)) boardsL2 in

    run [] numbersP boardsP (map (map $ map $ const 0) boardsP)

        where
            apply a board mask = zipWith (\l ml ->
                    zipWith (\n nl -> if n == a || nl == 1 then 1 else 0) l ml
                ) board mask
            hasWon mask = any (all (==1)) mask || any (\i -> all ((==1).(!!(i-1))) mask) [1..boardSize]
            getScore board mask = sum $ zipWith (\l ml ->
                    sum $ zipWith (\n nl -> if nl == 0 then n else 0) l ml
                ) board mask
            
            dd board mask = zipWith (\l ml ->
                    zipWith (\n nl -> if nl == 0 then n else 0) l ml
                ) board mask

            run wins [] b m = wins
            run wins (n:numbers) boards masks =
                let next = zipWith (\a b -> (a, apply n a b)) boards masks in
                case find (\(a, b) -> hasWon b) next of
                  Just (wBoard, wMask) -> 
                      (uncurry $ run ((length boards, n, dd wBoard wMask, n * getScore wBoard wMask):wins) numbers)
                      (unzip $ filter (\(a, b) -> a /= wBoard || b /= wMask) next)
                  -- Just (wBoard, wMask) -> run (Just $ n * getScore wBoard wMask) numbers (delete wBoard boards) (delete wMask newMasks)
                  Nothing     -> run wins numbers (map fst next) (map snd next)


main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day4 $ contents
