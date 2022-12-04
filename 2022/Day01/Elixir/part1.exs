
{:ok, content} = File.read("../input.txt")
lines = String.split(content, "\n")

result =
    lines |>
    Enum.map(&String.trim/1) |>
    Enum.chunk_by(&(&1 == "")) |>
    Enum.map(fn a -> Enum.filter(a, &(String.length(&1) > 0)) end) |>
    Enum.filter(&(length(&1) > 0)) |>
    Enum.map(fn a -> Enum.map(a, fn b -> String.to_integer(b) end) end) |>
    Enum.map(&Enum.sum/1) |>
    Enum.max()

IO.puts(result)
