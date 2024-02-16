#bind_cols() != JOIN

df1 = data.frame(
  id = 1:5,
  name = c("John","Marry","Anna","David","Lisa")
)

# rep = replicate
df2 = data.frame(
  city = c(rep("BKK",3),rep("LONDON",2)),
  country = c(rep("TH",3),rep("UK",2))
)

bind_cols(df1,df2)
bind_cols(df2,df1)