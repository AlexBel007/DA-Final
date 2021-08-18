List.Average(
    Table.SelectRows(#"Inserted Parsed Date",
(rec) => ((rec[Index] >= [Index] - 7) and (rec[Index] < [Index]))  )[NewInfections]
))