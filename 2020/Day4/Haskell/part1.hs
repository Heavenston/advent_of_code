import Data.List.Extra
import Data.Function
import System.IO
import Control.Concurrent

-- myListDiff (a:l2) l1 = myListDiff l2 (delete a l1)
-- myListDiff [] l1 = l1

day4 batch requiredFields =
    -- Find list of passports              replace new lines with spaces
    let passports = splitOn "\n\n" batch & map (replace "\n" " ") in
    -- Get all fields from passports
    let fields = map (splitOn " ") passports in
    -- Extract field names of each passports
    let fieldNames = map (map $ head . splitOn ":") fields in
    -- Extract all missing fields
    let missingFields = map (foldl (flip delete) requiredFields) fieldNames in
    -- count who has zero missing
    length $ filter null missingFields

main = do
    h <- openFile "../input.txt" ReadMode
    contents <- hGetContents h
    print $ day4 contents ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
