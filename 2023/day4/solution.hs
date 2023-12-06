import qualified Data.Set as S

main :: IO ()
main = do
  inp <- map (
    both (S.fromList . map (read :: String -> Int) . words . tail)
    . span (/= '|')
    . dropWhile (/= ':')
    ) . lines <$> readFile "input"

  let ns = map (S.size . uncurry S.intersection) inp

  putStr "Part 1: "
  print $ sum $ map (\i -> if i == 0 then 0 else 2 ^ (i-1)) ns

  putStr "Part 2: "
  print $ solvePart2 ns (1 <$ ns)

  where
    both f (x, y) = (f x, f y)

solvePart2 :: [Int] -> [Int] -> Int
solvePart2 [] [] = 0
solvePart2 (x : xs) (v : vs) = v + solvePart2 xs newVs
  where
    newVs = map (+v) (take x vs) ++ drop x vs

