library(ggplot2)
library(viridis)
library(reshape2)
library(gridExtra)

#Set your working directory to the Analysis folder for your project

#Read in the data
initial_data <- read.csv("munged_tasks.csv", h=T)
final_update <- subset(initial_data, update == "10000")
final_update[final_update$vert == "No symbiont", c("vert", "partner")] <- list("", "nosym")

b <- ggplot(data=subset(final_update, partner=="symbiont"), aes(x=factor(as.character(vert), levels=unique(vert)), y=donate_calls)) +
	geom_boxplot(alpha=0.5, outlier.size=0.5) +
    ylab("Total times symbionts ran the donate instruction") +
	xlab("Vertical transmission rate") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none")# +
c <- ggplot(data=subset(final_update, partner=="symbiont"), aes(x=factor(as.character(vert), levels=unique(vert)), y=mutualism)) +
	geom_boxplot(alpha=0.5, outlier.size=0.5) +
    ylab("Average mutualism") +
    ylim(-1, 1) +
	xlab("Vertical transmission rate") +
	theme(panel.background = element_rect(fill='white', colour='black')) +
	theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(), legend.position='top') +
	guides(fill="none")# +
	#scale_color_manual(name="", values=viridis(2), guide=guide_legend(direction='horizontal'), breaks=c("earned", "donated"), labels=c("Symbiont earned resources", "Symbiont donated resources"))
	
grid.arrange(arrangeGrob(b, c, ncol=2), nrow=2)
