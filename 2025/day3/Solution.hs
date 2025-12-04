module Main where

import Data.Array
import Data.Char

solve :: Int -> Array Int Int -> Int
solve n ds = arr ! (n, lb)
  where
    (lb, ub) = bounds ds

    arr :: Array (Int, Int) Int
    arr = array ((1, lb), (n, ub))
      [((nd, si), todo nd si) | nd <- [1..n], si <- indices ds]

    todo nd si =
      let l' = rangeSize (si, ub)
      in if nd == 1 then maximum $ ixmap (si, snd (bounds ds)) id ds
         else let v = if nd + 1 <= l' then arr ! (nd, si + 1) else -1
                  w = arr ! (nd - 1, si + 1)
              in max v $ w + (ds ! si) * 10 ^ (nd-1)

getInput :: String -> IO [Array Int Int]
getInput fname = do
  s <- readFile fname
  pure $ map (\l -> listArray (1, length l) $ map digitToInt l) $ lines s

main :: IO ()
main = do
  s <- getInput "input"
  print $ sum $ solve 12 <$> s
  pure ()
