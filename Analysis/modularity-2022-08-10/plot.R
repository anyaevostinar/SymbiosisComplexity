library(ggplot2)
library(viridis)
library(reshape2)
library(gridExtra)

#Set your working directory to the Analysis folder for your project

#Read in the data
df <- read.csv("munged_modularity.csv", h=T)

p<-ggplot(df) + geom_bar()